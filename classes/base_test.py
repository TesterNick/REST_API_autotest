class BaseTest:

    full_response = None
    response_data = None

    def check_cookies(self):
        """
        Check if cookies in response are expected.

        :return: None
        :rtype: NoneType
        """
        assert list(self.full_response.cookies) == []

    def check_http_status(self, expected_status: int):
        """
        Check if status code in response equals to expected one.

        :param expected_status: expected status code
        :type expected_status: int
        :return: None
        :rtype: NoneType
        """
        assert self.full_response.status_code == expected_status

    def check_response_encoding(self):
        """
        Check if encoding of response is expected.

        :return: None
        :rtype: NoneType
        """
        assert self.full_response.encoding == "iso-8859-1"

    def check_response_message(self, expected_message: str):
        """
        Check if "message" field of response data equals to
        expected one.

        :param expected_message: expected message text
        :type expected_message: str
        :return: None
        :rtype: NoneType
        """
        assert "message" in self.response_data
        assert self.response_data["message"] == expected_message

    def check_response_status(self):
        """
        Check if "status" field of response data is "success".

        :return: None
        :rtype: NoneType
        """
        assert "status" in self.response_data
        assert self.response_data["status"] == "success"
