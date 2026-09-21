import mujoco
from mujoco import viewer

from ariel.simulation.environments import SimpleFlatWorld
from ariel.body_phenotypes.custom_robots_miranda.insect_small7 import insect_small

# 1. Create a world (a flat terrain)
world = SimpleFlatWorld()

# 2. Build a modular robot body and spawn it into the world
robot = insect_small()                       # returns a CoreModule
world.spawn(robot.spec, position=[0, 0, 0.1])

# 3. Compile to a MuJoCo model + data
model = world.spec.compile()
data = mujoco.MjData(model)

# 4. Watch it in the interactive viewer
viewer.launch(model, data)