#!/usr/bin/env python3
"""A github org client"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.called_once(f'https://api.github.com/orgs/{org_name}')

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos_url(self, mock_public_repos_url):
        """test_public_repos_url method"""
        mock_public_repos_url.return_value = "www.holberton.com"
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class._public_repos_url, "www.holberton.com")

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """test_public_repos method"""
        mock_get_json.return_value = [{"name": "google"}, {"name": "abc"}]
        mock_public_repos_url.return_value = "www.holberton.com"
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), ["google", "abc"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
