import os

import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("headless")
    return chrome_options


@pytest.fixture
def prepare_test_baseurl():
    # TODO: find a way fo use container vars oder given url
    if "SELENIUM_BASE_URL" in os.environ:
        url = os.environ["SELENIUM_BASE_URL"]
    else:
        url = "http://{host}:{port}/".format(host="localhost", port=os.environ["NGINX_80_TCP"])
    return url


def test_example(selenium, prepare_test_baseurl):
    selenium.get(prepare_test_baseurl)
    # selenium.save_screenshot('/tmp/screenshot/sample_screenshot_1.png');
    assert (
        "Cookiecutter Template for circleci BuildJobs — Cookiecutter CircleCI Pipeline documentation" in selenium.title
    )
