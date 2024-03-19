from uagents import Agent, Context, Bureau
import zone_upleft
import zone_upright
import zone_bottomleft
import zone_bottomright
import police
import environment
import random

bad_guy = Agent(name="bad", seed="baaaad")

@bad_guy.on_interval(period=0.5)
async def spawn_random(ctx: Context):
    rows = len(environment.matrix)
    cols = len(environment.matrix[0])

    rows = 9
    cols = 9
    random_coords = (random.randint(0, rows-1), random.randint(0, cols-1))

    environment.matrix[random_coords[0]][random_coords[1]] = environment.Guys.BAD_GUY
    ctx.logger.info("BAD GUY SPAWNED at {}". format(random_coords))

if __name__ == "__main__":
    bureau = Bureau()
    bureau.add(zone_upleft.radar_upleft)
    bureau.add(zone_upright.radar_upright)
    bureau.add(zone_bottomleft.radar_bottomleft)
    bureau.add(zone_bottomright.radar_bottomright)
    bureau.add(police.police_agent)
    bureau.add(bad_guy)
    environment.init_all()
    bureau.run()
