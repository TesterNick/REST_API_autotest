import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import get, parse_json


@pytest.fixture(scope="class", autouse=True)
def set_up(request):
    link = "http://dummy.restapiexample.com/api/v1/employee/1/employee_name"
    request.cls.full_response = get(link)
    request.cls.response_data = parse_json(request.cls.full_response)


@pytest.mark.GET
@pytest.mark.negative
class TestGetNegative(BaseTest):

    @pytest.mark.xfail(reason=("Server returns html page, but Content-Type "
                               "header contains application/json"))
    def test_get_content_type_on_not_found(self):
        self.check_content_type("text/html; charset=UTF-8")

    def test_get_cookies_on_not_found(self):
        self.check_cookies()

    def test_get_returns_not_found(self):
        self.check_http_status(404)

    def test_get_time_on_not_found_is_small(self):
        # Time of response is subject to adjust to conform to
        # performance requirements.
        assert self.full_response.elapsed < datetime.timedelta(seconds=1)
