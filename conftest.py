import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--env_file", action="store", default=".demo.env"
    )


def pytest_configure(config):
    env_file_name = config.getoption("--env_file")
    os.environ["env_file_name"] = env_file_name


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
