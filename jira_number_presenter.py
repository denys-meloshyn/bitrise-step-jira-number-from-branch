#!/usr/bin/env python
import logging
import os
import sys

import jira_number

git_branch = sys.argv[1]
jira_prefix = sys.argv[2]
is_exit_number_missed = sys.argv[3] == 'true'

logging.basicConfig(level=logging.DEBUG)

jira_number = jira_number.extract_jira_number(git_branch=git_branch, jira_prefix=jira_prefix)
if jira_number is None and is_exit_number_missed:
    sys.exit(1)
elif jira_number is None:
    jira_number = ''

os.system('envman add --key JIRA_ISSUE_NUMBER_FROM_BRANCH --value "{}"'.format(jira_number))
