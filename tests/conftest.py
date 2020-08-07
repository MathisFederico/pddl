# -*- coding: utf-8 -*-
"""This module contains the configurations for the tests."""
import inspect
import os
from pathlib import Path

import pytest

from pddl.parser.domain import DomainParser
from pddl.parser.problem import ProblemParser

CUR_PATH = Path(os.path.dirname(inspect.getfile(inspect.currentframe())))  # type: ignore
ROOT_DIR = Path(CUR_PATH, "..").resolve()  # type: ignore

FIXTURES_DIR = CUR_PATH / "fixtures"


@pytest.fixture(scope="session")
def domain_parser():
    """Get the PDDL domain parser."""
    return DomainParser()


@pytest.fixture(scope="session")
def problem_parser():
    """Get the PDDL problem parser."""
    return ProblemParser()


#################################################
# Import PDDL fixtures
from tests.fixtures.code_objects.blocksworld_ipc08 import (  # noqa: E402, F401
    blocksworld_ipc08_domain,
    blocksworld_ipc08_problem_01,
)

#################################################
