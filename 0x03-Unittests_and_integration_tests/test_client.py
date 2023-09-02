#!/usr/bin/env python3
"""A github org client"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


@parameterized_class([{
                        "org_payload": TEST_PAYLOAD[0][0],
                        "repos_payload": TEST_PAYLOAD[0][1],
                        "expected_repos": TEST_PAYLOAD[0][2],
                        "apache2_repos": TEST_PAYLOAD[0][3]}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """setUpClass method"""
        cls.get_patcher = patch('requests.get')
        cls.mock_requests = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tearDownClass method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test_public_repos method"""
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """test_public_repos_with_license method"""
        test_class = GithubOrgClient("test")
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
