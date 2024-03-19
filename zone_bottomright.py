from uagents import Context
from environment import Guys
from environment import NeedHelp
from environment import StopSearching
from environment import matrix
from environment import police_agent
from environment import radar_upleft
from environment import radar_upright
from environment import radar_bottomleft
from environment import radar_bottomright

@radar_bottomright.on_interval(period=0.1)
async def scan_area(ctx: Context):
    i = ctx.storage.get("i")
    j = ctx.storage.get("j")
    if matrix[i][j] == Guys.BAD_GUY:
        ctx.logger.info("bad guy found! calling for HELP: ({}, {})".format(i, j))
        ctx.storage.set("moving", False)
        await ctx.send(police_agent.address, NeedHelp(coordinates=(i, j)))
        await ctx.send(radar_upleft.address, StopSearching())
        await ctx.send(radar_upright.address, StopSearching())
        await ctx.send(radar_bottomleft.address, StopSearching())
    else:
        ctx.logger.info("not bad guy at: ({}, {})".format(i, j))
    
    moving = ctx.storage.get("moving")
    if moving:
        # go to next area
        if j + 1 < ctx.storage.get("j_end"):
            ctx.storage.set("j", j + 1)
        else:
            if i + 1 < ctx.storage.get("i_end"):
                ctx.storage.set("i", i + 1)
                ctx.storage.set("j", ctx.storage.get("j_start"))
            else:
                ctx.storage.set("i", ctx.storage.get("i_start"))
                ctx.storage.set("j", ctx.storage.get("j_start"))

@radar_bottomright.on_message(model=StopSearching, replies=set())
async def give_help(ctx: Context, sender: str, msg: StopSearching):
    ctx.storage.set("moving", False)
    ctx.logger.info("radar bottom right stopped-----------------------------")