from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


def insect_long_legs() -> CoreModule:
    """Custom robot body built with the 3D editor."""
    core = CoreModule(index=0)
    hinge_0 = HingeModule(index=40)
    hinge_0.rotate(90)
    core.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_0.body,
        prefix="hinge_0",
    )
    hinge_1 = HingeModule(index=122)
    hinge_0.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_1.body,
        prefix="hinge_1",
    )
    brick_0 = BrickModule(index=125)
    hinge_1.sites[ModuleFaces.FRONT].attach_body(
        body=brick_0.body,
        prefix="brick_0",
    )
    hinge_2 = HingeModule(index=127)
    core.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_2.body,
        prefix="hinge_2",
    )
    hinge_3 = HingeModule(index=128)
    hinge_2.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_3.body,
        prefix="hinge_3",
    )
    brick_1 = BrickModule(index=129)
    hinge_3.sites[ModuleFaces.FRONT].attach_body(
        body=brick_1.body,
        prefix="brick_1",
    )
    hinge_4 = HingeModule(index=136)
    hinge_4.rotate(-90)
    brick_1.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_4.body,
        prefix="hinge_4",
    )
    hinge_5 = HingeModule(index=138)
    hinge_4.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_5.body,
        prefix="hinge_5",
    )
    brick_2 = BrickModule(index=139)
    hinge_5.sites[ModuleFaces.FRONT].attach_body(
        body=brick_2.body,
        prefix="brick_2",
    )
    hinge_6 = HingeModule(index=140)
    brick_1.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_6.body,
        prefix="hinge_6",
    )
    hinge_7 = HingeModule(index=141)
    hinge_6.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_7.body,
        prefix="hinge_7",
    )
    brick_3 = BrickModule(index=142)
    hinge_7.sites[ModuleFaces.FRONT].attach_body(
        body=brick_3.body,
        prefix="brick_3",
    )
    hinge_8 = HingeModule(index=149)
    hinge_8.rotate(90)
    brick_3.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_8.body,
        prefix="hinge_8",
    )
    hinge_9 = HingeModule(index=150)
    hinge_8.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_9.body,
        prefix="hinge_9",
    )
    brick_4 = BrickModule(index=151)
    hinge_9.sites[ModuleFaces.FRONT].attach_body(
        body=brick_4.body,
        prefix="brick_4",
    )
    hinge_10 = HingeModule(index=168)
    hinge_10.rotate(-90)
    brick_3.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_10.body,
        prefix="hinge_10",
    )
    hinge_11 = HingeModule(index=169)
    hinge_10.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_11.body,
        prefix="hinge_11",
    )
    brick_5 = BrickModule(index=170)
    hinge_11.sites[ModuleFaces.FRONT].attach_body(
        body=brick_5.body,
        prefix="brick_5",
    )
    hinge_12 = HingeModule(index=165)
    hinge_12.rotate(90)
    brick_1.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_12.body,
        prefix="hinge_12",
    )
    hinge_13 = HingeModule(index=166)
    hinge_12.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_13.body,
        prefix="hinge_13",
    )
    brick_6 = BrickModule(index=167)
    hinge_13.sites[ModuleFaces.FRONT].attach_body(
        body=brick_6.body,
        prefix="brick_6",
    )
    hinge_14 = HingeModule(index=162)
    hinge_14.rotate(-90)
    core.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_14.body,
        prefix="hinge_14",
    )
    hinge_15 = HingeModule(index=163)
    hinge_14.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_15.body,
        prefix="hinge_15",
    )
    brick_7 = BrickModule(index=164)
    hinge_15.sites[ModuleFaces.FRONT].attach_body(
        body=brick_7.body,
        prefix="brick_7",
    )
    return core
