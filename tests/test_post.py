import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import post


@pytest.mark.POST
class TestPostPositive(BaseTest):

    link = "http://dummy.restapiexample.com/api/v1/create"
    data = {"name": "test", "salary": 123, "age": 23}
    full_response, response_data, employee_data = post(link, data)

    def test_post_cookies(self):
        self.check_cookies()

    def test_post_employee_age(self):
        assert self.employee_data["age"] == 23

    def test_post_employee_id(self):
        assert self.employee_data["id"] > 0

    def test_post_employee_name(self):
        assert self.employee_data["name"] == "test"

    def test_post_employee_salary(self):
        assert self.employee_data["salary"] == 123

    def test_post_headers(self):
        exp = ['Alt-Svc', 'CF-Cache-Status', 'CF-RAY', 'Connection',
               'Content-Encoding', 'Content-Type', 'Date', 'NEL', 'Report-To',
               'Server', 'Transfer-Encoding', 'cache-control', 'display',
               'expires', 'host-header', 'referrer-policy', 'response', 'vary',
               'x-ezoic-cdn', 'x-middleton-display', 'x-middleton-response',
               'x-origin-cache-control', 'x-ratelimit-limit',
               'x-ratelimit-remaining', 'x-sol']
        assert sorted(list(self.full_response.headers.keys())) == exp

    def test_post_response_status_is_successful(self):
        self.check_response_status()

    def test_post_response_message_is_successful(self):
        self.check_response_message("Successfully! Record has been added.")

    @pytest.mark.xfail(reason="Bug on the server.")
    def test_post_returns_successful_status_code(self):
        self.check_http_status(201)

    def test_post_time_is_small(self):
        # Time of response is subject to adjust to conform to
        # performance requirements.
        assert self.full_response.elapsed < datetime.timedelta(seconds=1)
