from uagents import Agent, Context
import environment

police_agent = Agent(name="police", seed="police")

@police_agent.on_message(model=environment.NeedHelp, replies=set())
async def give_help(ctx: Context, sender: str, msg: environment.NeedHelp):
    index = 0
    for i in range(100000000):
        index = index + 1

    coord = msg.coordinates
    environment.matrix[coord[0]][coord[1]] = environment.Guys.EMPTY_SPACE
    
    ctx.logger.info("police done for looking for bad guys")