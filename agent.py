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
    random_coords = (random.randint(0, rows-1), random.randint(0, cols-1))

    environment.matrix[random_coords[0]][random_coords[1]] = environment.Guys.BAD_GUY
    ctx.logger.info("BAD GUY SPAWNED at {}". format(random_coords))

def init_all():
    zone_upleft.radar_upleft._storage.set("i", 0)
    zone_upleft.radar_upleft._storage.set("j", 0)
    zone_upleft.radar_upleft._storage.set("i_limit", 5)
    zone_upleft.radar_upleft._storage.set("j_limit", 5)

    zone_upright.radar_upright._storage.set("i", 5)
    zone_upright.radar_upright._storage.set("j", 5)
    zone_upright.radar_upright._storage.set("i_limit", 10)
    zone_upright.radar_upright._storage.set("j_limit", 10)

    zone_bottomleft.radar_bottomleft._storage.set("i", 5)
    zone_bottomleft.radar_bottomleft._storage.set("j", 0)
    zone_bottomleft.radar_bottomleft._storage.set("i_limit", 10)
    zone_bottomleft.radar_bottomleft._storage.set("j_limit", 5)

    zone_bottomright.radar_bottomright._storage.set("i", 5)
    zone_bottomright.radar_bottomright._storage.set("j", 5)
    zone_bottomright.radar_bottomright._storage.set("i_limit", 10)
    zone_bottomright.radar_bottomright._storage.set("j_limit", 10)

bureau = Bureau()
bureau.add(zone_upleft.radar_upleft)
bureau.add(zone_upright.radar_upright)
bureau.add(zone_bottomleft.radar_bottomleft)
bureau.add(zone_bottomright.radar_bottomright)
bureau.add(police.police_agent)
bureau.add(bad_guy)

if __name__ == "__main__":
    init_all()
    bureau.run()
