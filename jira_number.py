#!/usr/bin/env python
import re


def extract_jira_number(git_branch, jira_prefix):
    git_branch = git_branch.strip()

    # Figure out which branch we're on
    # git_branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip().decode("utf-8")

    print('On branch: \'{0}\''.format(git_branch))

    if git_branch.find(jira_prefix + '-') != -1:
        print('Oh hey, it\'s JIRA \'{}\' ticket branch.'.format(jira_prefix))
        result = re.match('(.*)({}-([0-9]*))'.format(jira_prefix), git_branch)
        return result.group(2)
    else:
        print('Couldn\'t find JIRA \'{0}\' issue number in branch \'{1}\''.format(jira_prefix, git_branch))
        return None
