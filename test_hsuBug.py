import unittest
from bug import Bug
from functions import checkLink, getEnv
import os

class TestLucashsu(unittest.TestCase):

    def test_bug_initialization(self):
        url = "https://example.com"
        bug = Bug(url)
        self.assertEqual(bug.url, url)
        self.assertEqual(bug.domain, "https://example.com")

    def test_bug_setup(self):
        url = "https://example.com"
        bug = Bug(url)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = bug.setup(headers)
        self.assertEqual(result, '設置成功')
        self.assertIsNotNone(bug.soup)

    def test_check_link(self):
        valid_url = "https://www.google.com"
        invalid_url = "https://thisisaninvalidurl.com"
        self.assertTrue(checkLink(valid_url))
        self.assertFalse(checkLink(invalid_url))

    def test_get_env(self):
        os.environ['TEST_ENV'] = 'test_value'
        self.assertEqual(getEnv('TEST_ENV'), 'test_value')
        with self.assertRaises(Exception):
            getEnv('NON_EXISTENT_ENV')

if __name__ == '__main__':
    unittest.main()