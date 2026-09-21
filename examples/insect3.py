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
    hinge_1 = HingeModule(index=52)
    hinge_0.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_1.body,
        prefix="hinge_1",
    )
    brick_0 = BrickModule(index=54)
    hinge_1.sites[ModuleFaces.FRONT].attach_body(
        body=brick_0.body,
        prefix="brick_0",
    )
    hinge_2 = HingeModule(index=2)
    core.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_2.body,
        prefix="hinge_2",
    )
    hinge_3 = HingeModule(index=51)
    hinge_2.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_3.body,
        prefix="hinge_3",
    )
    brick_1 = BrickModule(index=53)
    hinge_3.sites[ModuleFaces.FRONT].attach_body(
        body=brick_1.body,
        prefix="brick_1",
    )
    brick_2 = BrickModule(index=55)
    core.sites[ModuleFaces.RIGHT].attach_body(
        body=brick_2.body,
        prefix="brick_2",
    )
    brick_3 = BrickModule(index=56)
    brick_2.sites[ModuleFaces.FRONT].attach_body(
        body=brick_3.body,
        prefix="brick_3",
    )
    brick_4 = BrickModule(index=57)
    brick_3.sites[ModuleFaces.FRONT].attach_body(
        body=brick_4.body,
        prefix="brick_4",
    )
    brick_5 = BrickModule(index=66)
    brick_4.sites[ModuleFaces.FRONT].attach_body(
        body=brick_5.body,
        prefix="brick_5",
    )
    hinge_4 = HingeModule(index=67)
    brick_5.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_4.body,
        prefix="hinge_4",
    )
    hinge_5 = HingeModule(index=68)
    hinge_4.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_5.body,
        prefix="hinge_5",
    )
    brick_6 = BrickModule(index=72)
    hinge_5.sites[ModuleFaces.FRONT].attach_body(
        body=brick_6.body,
        prefix="brick_6",
    )
    hinge_6 = HingeModule(index=69)
    brick_5.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_6.body,
        prefix="hinge_6",
    )
    hinge_7 = HingeModule(index=70)
    hinge_6.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_7.body,
        prefix="hinge_7",
    )
    brick_7 = BrickModule(index=74)
    hinge_7.sites[ModuleFaces.FRONT].attach_body(
        body=brick_7.body,
        prefix="brick_7",
    )
    hinge_8 = HingeModule(index=62)
    brick_3.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_8.body,
        prefix="hinge_8",
    )
    hinge_9 = HingeModule(index=63)
    hinge_8.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_9.body,
        prefix="hinge_9",
    )
    brick_8 = BrickModule(index=71)
    hinge_9.sites[ModuleFaces.FRONT].attach_body(
        body=brick_8.body,
        prefix="brick_8",
    )
    hinge_10 = HingeModule(index=64)
    brick_3.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_10.body,
        prefix="hinge_10",
    )
    hinge_11 = HingeModule(index=65)
    hinge_10.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_11.body,
        prefix="hinge_11",
    )
    brick_9 = BrickModule(index=73)
    hinge_11.sites[ModuleFaces.FRONT].attach_body(
        body=brick_9.body,
        prefix="brick_9",
    )
    return core