import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import post, parse_json


@pytest.mark.POST
@pytest.mark.negative
class TestPostPositive(BaseTest):

    link = "http://dummy.restapiexample.com/api/v1/create"
    data = {"name": "test", "salary": 123, "age": 23}
    full_response = post(link, data)
    response_data = parse_json(full_response)

    def test_post_content_type_on_no_data(self):
        self.check_content_type("application/json")

    def test_post_cookies_on_no_data(self):
        self.check_cookies()

    @pytest.mark.xfail(reason="Server returns success instead of error.")
    def test_post_response_status_on_no_data_is_not_successful(self):
        self.check_response_status("error")

    @pytest.mark.xfail(reason="Server returns success instead of error.")
    def test_post_response_message_is_successful(self):
        self.check_response_message("Not enough data for adding a record.")

    @pytest.mark.xfail(reason="Server returns 200 instead of 400.")
    def test_post_returns_successful_status_code(self):
        self.check_http_status(400)

    def test_post_time_is_small(self):
        # Time of response is subject to adjust to conform to
        # performance requirements.
        assert self.full_response.elapsed < datetime.timedelta(seconds=1)
