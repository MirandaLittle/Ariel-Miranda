from ariel.body_phenotypes.robogen_lite.config import ModuleFaces
from ariel.body_phenotypes.robogen_lite.modules.brick import BrickModule
from ariel.body_phenotypes.robogen_lite.modules.core import CoreModule
from ariel.body_phenotypes.robogen_lite.modules.hinge import HingeModule


def insect_small() -> CoreModule:
    """Custom robot body built with the 3D editor."""
    core = CoreModule(index=0)
    hinge_0 = HingeModule(index=1)
    core.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_0.body,
        prefix="hinge_0",
    )
    brick_0 = BrickModule(index=4)
    hinge_0.sites[ModuleFaces.FRONT].attach_body(
        body=brick_0.body,
        prefix="brick_0",
    )
    hinge_1 = HingeModule(index=9)
    brick_0.sites[ModuleFaces.FRONT].attach_body(
        body=hinge_1.body,
        prefix="hinge_1",
    )
    brick_1 = BrickModule(index=10)
    hinge_1.sites[ModuleFaces.FRONT].attach_body(
        body=brick_1.body,
        prefix="brick_1",
    )
    hinge_2 = HingeModule(index=23)
    hinge_2.rotate(90)
    brick_1.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_2.body,
        prefix="hinge_2",
    )
    brick_2 = BrickModule(index=24)
    hinge_2.sites[ModuleFaces.FRONT].attach_body(
        body=brick_2.body,
        prefix="brick_2",
    )
    hinge_3 = HingeModule(index=25)
    hinge_3.rotate(-90)
    brick_1.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_3.body,
        prefix="hinge_3",
    )
    brick_3 = BrickModule(index=26)
    hinge_3.sites[ModuleFaces.FRONT].attach_body(
        body=brick_3.body,
        prefix="brick_3",
    )
    hinge_4 = HingeModule(index=21)
    hinge_4.rotate(90)
    brick_0.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_4.body,
        prefix="hinge_4",
    )
    brick_4 = BrickModule(index=22)
    hinge_4.sites[ModuleFaces.FRONT].attach_body(
        body=brick_4.body,
        prefix="brick_4",
    )
    hinge_5 = HingeModule(index=27)
    hinge_5.rotate(-90)
    brick_0.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_5.body,
        prefix="hinge_5",
    )
    brick_5 = BrickModule(index=28)
    hinge_5.sites[ModuleFaces.FRONT].attach_body(
        body=brick_5.body,
        prefix="brick_5",
    )
    hinge_6 = HingeModule(index=17)
    hinge_6.rotate(90)
    core.sites[ModuleFaces.RIGHT].attach_body(
        body=hinge_6.body,
        prefix="hinge_6",
    )
    brick_6 = BrickModule(index=18)
    hinge_6.sites[ModuleFaces.FRONT].attach_body(
        body=brick_6.body,
        prefix="brick_6",
    )
    hinge_7 = HingeModule(index=19)
    hinge_7.rotate(-90)
    core.sites[ModuleFaces.LEFT].attach_body(
        body=hinge_7.body,
        prefix="hinge_7",
    )
    brick_7 = BrickModule(index=20)
    hinge_7.sites[ModuleFaces.FRONT].attach_body(
        body=brick_7.body,
        prefix="brick_7",
    )
    return core
