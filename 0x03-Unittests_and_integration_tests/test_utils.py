#!/usr/bin/env python3
"""
Unit tests module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
