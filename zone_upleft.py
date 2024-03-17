from uagents import Agent, Context, Bureau, Model
from enum import Enum
import random
import time
import environment
import police

radar_upleft = Agent(name="radar_upleft", seed="radar_upleft recovery phrase")

@radar_upleft.on_message(model=environment.Initialization, replies=set())
async def init(ctx: Context):
    ctx.storage.set("i", 0)
    ctx.storage.set("j", 0)
    ctx.storage.set("i_limit", 3)
    ctx.storage.set("j_limit", 3)

# @radar_upleft._on_startup()
# async def initialization(ctx: Context):
#     ctx.storage.set("i", 0)
#     ctx.storage.set("j", 0)
#     ctx.storage.set("i_limit", 3)
#     ctx.storage.set("j_limit", 3)

@radar_upleft.on_interval(period=0.1)
async def scan_area(ctx: Context):
    # if not ctx.storage.has("i"):
    #     ctx.storage.set("i", 0)
    # if not ctx.storage.has("j"):
    #     ctx.storage.set("j", 0)
    # if not ctx.storage.has("i_limit"):
    #     ctx.storage.set("i_limit", 10)
    # if not ctx.storage.has("j_limit"):
    #     ctx.storage.set("j_limit", 5)
    
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
            ctx.storage.set("i", 0)
            ctx.storage.set("j", 0)

    # rows = len(matrix)
    # cols = len(matrix[0])
    # found = False
    # #upleft
    # for i in range(rows // 2):
    #     for j in range(cols // 2):
    #         ctx.logger.info("bad guy found! calling for HELP")
    #         found = True
    #         await ctx.send(police.address, NeedHelp(coordinates=(i, j)))
    
    # if not found:
    #     ctx.logger.info("no bad guys in zone 1...")

# @radar_upleft.on_interval(period=3.0)
# async def scan_area(ctx: Context):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     found = False
#     #upleft
#     for i in range(rows // 2):
#         for j in range(cols // 2):
#             ctx.logger.info("bad guy found! calling for HELP")
#             found = True
#             await ctx.send(police.address, NeedHelp(coordinates=(i, j)))
    
#     if not found:
#         ctx.logger.info("no bad guys in zone 1...")
