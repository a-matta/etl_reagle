import pathlib
import subprocess
from importlib.metadata import version

from invoke import task

ROOT = pathlib.Path(__file__).parent.resolve().as_posix()
VERSION = version("etl_reagle")


@task
def clean(context):
    """Clean the root folder. Remove all generated files/directories"""
    cmd = [
        "rm",
        "-rf",
        f"{ROOT}/.pytest_cache",
        f"{ROOT}/pytest.log",
        f"{ROOT}/report",
        f"{ROOT}/test-results",
        f"{ROOT}/allure-results",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=False)


@task(pre=[clean])
def tests(context, mark=""):
    """Run the tests in 'tests' directory.

    Args:
        mark: Mark to select/deselect tests to be executed.
    """
    cmd = [
        "pytest",
        "--alluredir",
        "allure-results",
        f'-m "{mark}"' if mark else "",
        f"{ROOT}/tests",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=True)
