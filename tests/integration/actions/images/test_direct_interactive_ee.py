""" direct from cli interactive w/ ee
"""
import pytest

from .base import base_steps
from .base import BaseClass
from .base import IMAGE_SHORT

from ..._interactions import add_indicies
from ..._interactions import Command
from ..._interactions import Step
from ..._interactions import step_id


CLI = Command(subcommand="images", execution_environment=True).join()

initial_steps = (
    Step(user_input=CLI, comment="ansible-navigator images top window", look_fors=[IMAGE_SHORT]),
)

steps = add_indicies(initial_steps + base_steps)


@pytest.mark.parametrize("step", steps, ids=step_id)
class Test(BaseClass):
    """run the tests"""

    UPDATE_FIXTURES = False
