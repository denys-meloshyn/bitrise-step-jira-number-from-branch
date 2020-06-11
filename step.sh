#!/bin/bash
set -ex

THIS_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python "${THIS_SCRIPT_DIR}/jira_number_presenter.py" ${bitrise_jira_branch_name} ${bitrise_jira_number_prefix} ${bitrise_jira_number_should_fail}

#
# --- Exit codes:
# The exit code of your Step is very important. If you return
#  with a 0 exit code `bitrise` will register your Step as "successful".
# Any non zero exit code will be registered as "failed" by `bitrise`.

exit 0
