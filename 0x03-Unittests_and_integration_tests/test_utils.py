#!/usr/bin/env python3
"""
Unit tests module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    class to test if utils.access_nested_map  returns what it is
    supposed to return
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, ans):
        """
        Assert test
        """
        self.assertEqual(access_nested_map(nested_map, path), ans)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test if KeyError is raised on KeyError
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)

        expected_error_msg = "{}".format(path[-1])
        self.assertIn(expected_error_msg, str(error.exception))


class TestGetJson(unittest.TestCase):
    """
    Class to test url request
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Method to test if that utils.get_json returns expected results
        """
        # Configure the mock to return the test_payload when json() is called
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        # Assert that the mock get method is called once with the correct URL
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
