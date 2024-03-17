from uagents import Agent, Context, Bureau, Model
from enum import Enum
import random
import time
import environment
import police

radar_upright = Agent(name="radar_upright", seed="radar_upright recovery phrase")

@radar_upright.on_interval(period=0.1)
async def scan_area(ctx: Context):
    # if not ctx.storage.has("i"):
    #     ctx.storage.set("i", 0)
    # if not ctx.storage.has("j"):
    #     ctx.storage.set("j", 5)
    # if not ctx.storage.has("i_limit"):
    #     ctx.storage.set("i_limit", 10)
    # if not ctx.storage.has("j_limit"):
    #     ctx.storage.set("j_limit", 10)
    
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
            ctx.storage.set("j", 5)
        else:
            ctx.storage.set("i", 0)
            ctx.storage.set("j", 5)

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







# from uagents import Agent, Context, Bureau

# import random

# radar_upright = Agent(name="radar_upright", seed="radar_upright recovery phrase")
# police = Agent(name="police", seed="police")
# bad_guy = Agent(name="bad", seed="baaaad")


# @radar_upleft.on_interval(period=3.0)
# async def scan_area(ctx: Context):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     found = False
#     #upleft
#     # for i in range(rows // 2):
#     #     for j in range(cols // 2):

#     #upright
#     # for i in range(rows):
#     #     for j in range(cols // 2, cols):
#     #         if i < rows // 2 and j >= cols // 2:

#     #bottomleft
#     # for i in range(rows // 2, rows):
#     #     for j in range(cols // 2):
#     #         if i >= rows // 2 and j < cols // 2:
    
#     #bottomright
#     # for i in range(rows // 2, rows):
#     #     for j in range(cols // 2, cols):
#     #         if i >= rows // 2 and j >= cols // 2:

#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == Guys.BAD_GUY:
#                 ctx.logger.info("bad guy found! calling for HELP")
#                 found = True
#                 await ctx.send(police.address, NeedHelp(coordinates=(i, j)))
    
#     if not found:
#         ctx.logger.info("no bad guys in zone 1...")

# @police.on_message(model=NeedHelp, replies=set())
# async def give_help(ctx: Context, sender: str, msg: NeedHelp):
#     coord = msg.coordinates
#     matrix[coord[0]][coord[1]] = Guys.EMPTY_SPACE
    
#     ctx.logger.info("police done for looking for bad guys")

# @bad_guy.on_interval(period=5.0)
# async def spawn_random(ctx: Context):
#     rows = len(matrix)
#     cols = len(matrix[0])

#     random_coords = (random.randint(0, rows-1), random.randint(0, cols-1))
#     matrix[random_coords[0]][random_coords[1]] = Guys.BAD_GUY
#     ctx.logger.info("BAD GUY SPAWNED!")

# bureau = Bureau()
# bureau.add(radar_upleft)
# bureau.add(police)
# bureau.add(bad_guy)

# if __name__ == "__main__":
#     bureau.run()