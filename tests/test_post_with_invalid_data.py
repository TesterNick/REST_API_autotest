import datetime

import pytest

from classes.base_test import BaseTest
from classes.methods import post, parse_json


@pytest.mark.POST
@pytest.mark.negative
class TestPostWitInvalidData(BaseTest):

    link = "http://dummy.restapiexample.com/api/v1/create"
    # Actually, there should be separate tests for each valid field
    # with invalid data as well as invalid field name (e. g. "id"),
    # and the only difference between them is one incorrect field.
    # All checks are the same. As long as there are no requirements,
    # tests are combined.
    data = {"id": 42, "name": "", "salary": -123, "age": "null"}
    full_response = post(link, data)
    response_data = parse_json(full_response)

    def test_post_content_type_on_invalid_data(self):
        self.check_content_type("application/json")

    def test_post_cookies_on_invalid_data(self):
        self.check_cookies()

    @pytest.mark.xfail(reason="Server returns success instead of error.")
    def test_post_response_status_on_invalid_data_is_not_successful(self):
        self.check_response_status("error")

    @pytest.mark.xfail(reason="Server returns success instead of error.")
    def test_post_response_message_is_not_successful_on_invalid_data(self):
        self.check_response_message("Invalid data.")

    @pytest.mark.xfail(reason="Server returns 200 instead of 400.")
    def test_post_returns_not_successful_status_code_on_invalid_data(self):
        self.check_http_status(400)

    def test_post_time_is_small_on_invalid_data(self):
        # Time of response is subject to adjust to conform to
        # performance requirements.
        assert self.full_response.elapsed < datetime.timedelta(seconds=1)
