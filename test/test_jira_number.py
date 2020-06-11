import unittest

from jira_number import extract_jira_number


class TestExtractJiraNumber(unittest.TestCase):
    def test_extract_number_with_one_existed_number(self):
        self.assertEqual(extract_jira_number(git_branch='PROJECT-123', jira_prefix='PROJECT'),
                         'PROJECT-123')

    def test_extract_number_with_multiple_existed_number(self):
        self.assertEqual(extract_jira_number(git_branch='PROJECT-123/PROJECT-456', jira_prefix='PROJECT'),
                         'PROJECT-456')

    def test_extract_number_with_any_existed_number(self):
        self.assertIsNone(extract_jira_number(git_branch='bugfix/wrong-return-type', jira_prefix='PROJECT'))


if __name__ == '__main__':
    unittest.main()
