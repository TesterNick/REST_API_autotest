import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import get, parse_json


@pytest.fixture(scope="class", autouse=True)
def set_up(request):
    link = "http://dummy.restapiexample.com/api/v1/employee/1"
    request.cls.full_response = get(link)
    request.cls.response_data = parse_json(request.cls.full_response)
    request.cls.employee_data = request.cls.response_data["data"]


@pytest.mark.GET
@pytest.mark.positive
class TestGetPositive(BaseTest):

    def test_get_content_type(self):
        self.check_content_type("application/json")

    def test_get_cookies(self):
        self.check_cookies()

    def test_get_employee_age(self):
        assert self.employee_data["employee_age"] == 61

    def test_get_employee_id(self):
        assert self.employee_data["id"] == 1

    def test_get_employee_image(self):
        assert self.employee_data["profile_image"] == ""

    def test_get_employee_name(self):
        assert self.employee_data["employee_name"] == "Tiger Nixon"

    def test_get_employee_salary(self):
        assert self.employee_data["employee_salary"] == 320800

    def test_get_headers(self):
        self.check_response_headers()

    def test_get_response_status_is_successful(self):
        self.check_response_status()

    def test_get_response_message_is_successful(self):
        self.check_response_message("Successfully! Record has been fetched.")

    def test_get_returns_successful_status_code(self):
        self.check_http_status(200)

    def test_get_time_is_small(self):
        # Time of response is subject to adjust to conform to
        # performance requirements.
        assert self.full_response.elapsed < datetime.timedelta(seconds=1)
