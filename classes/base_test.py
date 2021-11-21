class BaseTest:

    full_response = None
    response_data = None

    def check_cookies(self) -> None:
        """
        Check if cookies in response are expected.

        :return: None
        :rtype: NoneType
        """
        assert list(self.full_response.cookies) == []

    def check_content_type(self, expected_type: str) -> None:
        """
        Check if header contains expected content type.

        :param expected_type: expected content type
        :type expected_type: str
        :return: None
        :rtype: NoneType
        """
        assert self.full_response.headers["Content-Type"] == expected_type

    def check_response_headers(self) -> None:
        """
        Check if response headers are expected.

        :return: None
        :rtype: NoneType
        """
        exp = ['Alt-Svc', 'CF-Cache-Status', 'CF-RAY', 'Connection',
               'Content-Encoding', 'Content-Type', 'Date', 'NEL', 'Report-To',
               'Server', 'Transfer-Encoding', 'cache-control', 'display',
               'expires', 'host-header', 'referrer-policy', 'response', 'vary',
               'x-ezoic-cdn', 'x-middleton-display', 'x-middleton-response',
               'x-origin-cache-control', 'x-ratelimit-limit',
               'x-ratelimit-remaining', 'x-sol']
        assert sorted(list(self.full_response.headers.keys())) == exp

    def check_http_status(self, expected_status: int) -> None:
        """
        Check if status code in response equals to expected one.

        :param expected_status: expected status code
        :type expected_status: int
        :return: None
        :rtype: NoneType
        """
        assert self.full_response.status_code == expected_status

    def check_response_encoding(self) -> None:
        """
        Check if encoding of response is expected.

        :return: None
        :rtype: NoneType
        """
        assert self.full_response.encoding == "iso-8859-1"

    def check_response_message(self, expected_message: str) -> None:
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

    def check_response_status(self, expected_status: str = "success") -> None:
        """
        Check if "status" field of response data is expected.

        :param expected_status: expected status text
        :type expected_status: str
        :return: None
        :rtype: NoneType
        """
        assert "status" in self.response_data
        assert self.response_data["status"] == expected_status
