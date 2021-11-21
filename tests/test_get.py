import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import get


@pytest.mark.GET
class TestGet(BaseTest):

    link = "http://dummy.restapiexample.com/api/v1/employee/1"
    full_response, response_data, employee_data = get(link)

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
