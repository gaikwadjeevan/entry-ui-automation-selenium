from selenium import webdriver
import os
import pytest

current_dir = os.getcwd()
project_root = os.path.abspath(os.path.join(current_dir, ".."))


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("*** Launching Google Chrome Browser ***")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("*** Launching Mozzila Firefox Browser ***")
    else:
        driver = webdriver.Ie()
        print("*** Launching IE Browser ***")
    return driver


def pytest_addoption(parser):  # This will get the values from the CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(pytestconfig):  # This will return the browser value to setup method
    return pytestconfig.getoption("--browser")


def pytest_configure(config):
    config._metadata = {
            " Project Name ": "Sample Project"
    }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
