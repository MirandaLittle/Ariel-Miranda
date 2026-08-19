# Standard library
from pathlib import Path

# Third-party libraries
import matplotlib.pyplot as plt
import mujoco
import numpy as np
from mujoco import viewer

# ARIEL — module primitives (for manual assembly)
from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.constructor import (
    construct_mjspec_from_graph,
)
from ariel.body_phenotypes.robogen_lite.decoders.hi_prob_decoding import (
    HighProbabilityDecoder,
)
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule

# ARIEL — prebuilt robot bodies
from ariel.body_phenotypes.robogen_lite.prebuilt_robots.gecko import gecko

# ARIEL — genotype-to-phenotype pipeline
from ariel.ec.genotypes.nde import NeuralDevelopmentalEncoding

# ARIEL — controller
from ariel.simulation.controllers.controller import Controller
from ariel.simulation.controllers.na_cpg import (
    NaCPG,
    create_fully_connected_adjacency,
)

# ARIEL — simulation environments
from ariel.simulation.environments import SimpleFlatWorld

# ARIEL — utilities
from ariel.utils.runners import simple_runner
from ariel.utils.tracker import Tracker

# Custom robot made in robot builder

from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


def custom_robot() -> CoreModule:
    """Custom robot body built with the 3D editor."""
    core = CoreModule(index=0)
    hinge_0 = HingeModule(index=1)
    core.sites[ModuleFaces.BACK].attach_body(
        body=hinge_0.body,
        prefix="hinge_0",
    )
    brick_0 = BrickModule(index=3)
    hinge_0.sites[ModuleFaces.FRONT].attach_body(
        body=brick_0.body,
        prefix="brick_0",
    )
    hinge_1 = HingeModule(index=2)
    core.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_1.body,
        prefix="hinge_1",
    )
    brick_1 = BrickModule(index=4)
    hinge_1.sites[ModuleFaces.FRONT].attach_body(
        body=brick_1.body,
        prefix="brick_1",
    )
    hinge_2 = HingeModule(index=9)
    core.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_2.body,
        prefix="hinge_2",
    )
    brick_2 = BrickModule(index=34)
    hinge_2.sites[ModuleFaces.FRONT].attach_body(
        body=brick_2.body,
        prefix="brick_2",
    )
    hinge_3 = HingeModule(index=35)
    brick_2.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_3.body,
        prefix="hinge_3",
    )
    brick_3 = BrickModule(index=38)
    hinge_3.sites[ModuleFaces.FRONT].attach_body(
        body=brick_3.body,
        prefix="brick_3",
    )
    hinge_4 = HingeModule(index=36)
    brick_2.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_4.body,
        prefix="hinge_4",
    )
    brick_4 = BrickModule(index=39)
    hinge_4.sites[ModuleFaces.FRONT].attach_body(
        body=brick_4.body,
        prefix="brick_4",
    )
    hinge_5 = HingeModule(index=37)
    brick_2.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_5.body,
        prefix="hinge_5",
    )
    brick_5 = BrickModule(index=40)
    hinge_5.sites[ModuleFaces.FRONT].attach_body(
        body=brick_5.body,
        prefix="brick_5",
    )
    hinge_6 = HingeModule(index=41)
    brick_5.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_6.body,
        prefix="hinge_6",
    )
    brick_6 = BrickModule(index=43)
    hinge_6.sites[ModuleFaces.FRONT].attach_body(
        body=brick_6.body,
        prefix="brick_6",
    )
    hinge_7 = HingeModule(index=42)
    brick_5.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_7.body,
        prefix="hinge_7",
    )
    brick_7 = BrickModule(index=44)
    hinge_7.sites[ModuleFaces.FRONT].attach_body(
        body=brick_7.body,
        prefix="brick_7",
    )
    return core

# Always reset the control callback before building a new simulation.
mujoco.set_mjcb_control(None)

# Create the world
world = SimpleFlatWorld()

# Create the robot body
robot = custom_robot()

# Spawn the robot at the origin
world.spawn(robot.spec, position=[0, 0, 0])

# Compile into a MuJoCo model and initialise data
model = world.spec.compile()
data = mujoco.MjData(model)

print(f"Number of actuators (joints): {model.nu}")
print(f"Number of degrees of freedom: {model.nv}")

# Build the CPG — one node per actuator, fully connected.
adj_dict = create_fully_connected_adjacency(model.nu)
cpg = NaCPG(
    adjacency_dict=adj_dict,
    hard_bounds=(-np.pi / 2, np.pi / 2),  # keep angles within hinge limits
)

print(f"CPG nodes (= actuators): {cpg.n}")
print(f"Total learnable parameters: {cpg.num_of_parameters}")


# Set up the tracker — Controller will call tracker.update() automatically.
tracker = Tracker(
    mujoco_obj_to_find=mujoco.mjtObj.mjOBJ_GEOM,
    name_to_bind="core",
    observable_attributes=["xpos"],
)
tracker.setup(world.spec, data)

# Wrap the CPG: the callback receives (model, data) and returns joint angles.
def cpg_callback(model: mujoco.MjModel, data: mujoco.MjData):
    return cpg.forward(time=data.time)

# Create the Controller.
controller = Controller(
    controller_callback_function=cpg_callback,
    time_steps_per_ctrl_step=50,   # call CPG every 50 physics steps
    time_steps_per_save=500,        # record tracker data every 500 steps
    alpha=0.5,                      # smoothing: 0 = never update, 1 = immediate update
    tracker=tracker,
)

# Register with MuJoCo — controller.set_control IS the callback.
mujoco.set_mjcb_control(controller.set_control)

print("Controller registered.")

# Uncomment to open the interactive viewer
mujoco.set_mjcb_control(controller.set_control)
viewer.launch(model=model, data=data)

# Plot trajectory

def plot_trajectory(history: list) -> None:
    """Plot the XY trajectory of the robot's core module."""
    pos = np.array(history)  # shape: (T, 3)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot(pos[:, 0], pos[:, 1], "b-", linewidth=1.5, label="Path")
    ax.plot(pos[0, 0], pos[0, 1], "go", markersize=10, label="Start")
    ax.plot(pos[-1, 0], pos[-1, 1], "ro", markersize=10, label="End")

    ax.set_xlabel("X position (m)")
    ax.set_ylabel("Y position (m)")
    ax.set_title("Robot trajectory (XY plane)")
    ax.legend()
    ax.set_aspect("equal")
    ax.grid(True)

    # Centre the view
    margin = max(np.abs(pos[:, :2]).max(), 0.3)
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)

    plt.tight_layout()
    plt.show()


plot_trajectory(tracker.history["xpos"][0])

# Define a fitness function

#def displacement_fitness(history: list) -> float:
#    """Return the 2-D Euclidean distance from start to end position."""
#    pos = np.array(history)
#    x0, y0 = pos[0, :2]
#    xf, yf = pos[-1, :2]
#    return float(np.sqrt((xf - x0) ** 2 + (yf - y0) ** 2))


#fitness = displacement_fitness(tracker.history["xpos"][0])
#print(f"Fitness (displacement): {fitness:.4f} m")

# Task gait learning
"""Gait learning."""

def xy_displacement(
    xy1: tuple[float, float],
    xy2: tuple[float, float],
) -> float:
    """
    Calculate the displacement between two points in 2D space.

    Parameters
    ----------
    xy1
        Coordinates of the first point (x1, y1).
    xy2
        Coordinates of the second point (x2, y2).

    Returns
    -------
    float
        The Euclidean distance between the two points.
    """
    return ((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2) ** 0.5


def x_speed(
    xy1: tuple[float, float],
    xy2: tuple[float, float],
    dt: float,
) -> float:
    """
    Calculate the speed in the x direction between two points.

    Parameters
    ----------
    xy1
        Coordinates of the first point (x1, y1).
    xy2
        Coordinates of the second point (x2, y2).
    dt
        Time difference between the two points.

    Returns
    -------
    float
        The speed in the x direction.
    """
    return abs(xy2[0] - xy1[0]) / dt if dt > 0 else 0.0


def y_speed(
    xy1: tuple[float, float],
    xy2: tuple[float, float],
    dt: float,
) -> float:
    """
    Calculate the speed in the y direction between two points.

    Parameters
    ----------
    xy1
        Coordinates of the first point (x1, y1).
    xy2
        Coordinates of the second point (x2, y2).
    dt
        Time difference between the two points.

    Returns
    -------
    float
        The speed in the y direction.
    """
    return abs(xy2[1] - xy1[1]) / dt if dt > 0 else 0.0



# Evaluate

def evaluate(
    cpg: NaCPG,
    *,
    duration: float = 15.0,
) -> float:
    """Evaluate a CPG controller on the gecko robot and return displacement fitness.

    Parameters
    ----------
    cpg:
        A configured NaCPG instance whose parameters define the controller.
    duration:
        How many simulated seconds to run.

    Returns
    -------
    float
        2-D displacement from start to end (metres).
    """
    # --- Build world + robot ---
    mujoco.set_mjcb_control(None)
    world = SimpleFlatWorld()
    robot = custom_robot()
    world.spawn(robot.spec, position=[0, 0, 0])
    model = world.spec.compile()
    data = mujoco.MjData(model)

    # --- Tracker + Controller ---
    tracker = Tracker(
        mujoco_obj_to_find=mujoco.mjtObj.mjOBJ_GEOM,
        name_to_bind="core",
        observable_attributes=["xpos"],
    )
    tracker.setup(world.spec, data)

    controller = Controller(
        controller_callback_function=lambda m, d: cpg.forward(time=d.time),
        tracker=tracker,
    )
    mujoco.set_mjcb_control(controller.set_control)

    # --- Run ---
    simple_runner(model, data, duration=duration)

    # --- Score ---
    return xy_displacement(tracker.history["xpos"][0])


# Create a CPG with random parameters and evaluate it
mujoco.set_mjcb_control(None)
world_tmp = SimpleFlatWorld()
robot_tmp = custom_robot()
world_tmp.spawn(robot_tmp.spec, position=[0, 0, 0])
model_tmp = world_tmp.spec.compile()

cpg_to_eval = NaCPG(
    adjacency_dict=create_fully_connected_adjacency(model_tmp.nu),
    hard_bounds=(-np.pi / 2, np.pi / 2),
)

score = evaluate(cpg_to_eval, duration=15)
print(f"Displacement: {score:.4f} m")