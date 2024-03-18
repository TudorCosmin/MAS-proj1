from uagents import Agent, Context, Bureau, Model
from enum import Enum
import random
import time
import environment
import police

radar_bottomleft = Agent(name="radar_bottomleft", seed="radar_bottomleft recovery phrase")

@radar_bottomleft.on_interval(period=0.1)
async def scan_area(ctx: Context):
    i = ctx.storage.get("i")
    j = ctx.storage.get("j")
    if environment.matrix[i][j] == environment.Guys.BAD_GUY:
        ctx.logger.info("bad guy found! calling for HELP: ({}, {})".format(i, j))
        await ctx.send(police.police_agent.address, environment.NeedHelp(coordinates=(i, j)))
    else:
        ctx.logger.info("not bad guy at: ({}, {})".format(i, j))
    
    # go to next area
    if j + 1 < ctx.storage.get("j_limit"):
        ctx.storage.set("j", j + 1)
        # print(j)
    else:
        if i + 1 < ctx.storage.get("i_limit"):
            ctx.storage.set("i", i + 1)
            ctx.storage.set("j", 0)
        else:
            ctx.storage.set("i", 5)
            ctx.storage.set("j", 0)
