import os
from jira import JIRA
import logging
from orange_hrm.infra.config_provider import ConfigProvider


class JiraHandler:
    """
    This class manages Jira actions.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(base_dir, '../orange_hrm.json')
    config = ConfigProvider().load_from_file(config_file_path)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    jira_file_path = os.path.join(base_dir, '../secret.json')
    jira_token = ConfigProvider().load_from_file(jira_file_path)


    def __init__(self):
        self._jira_url = self.config['jira_url']
        self._auth_jira = JIRA(
            basic_auth=(self.config['jira_mail'], self.jira_token['jira_token']),
            options={'server': self._jira_url})

    def create_issue(self, project_key, summary, description, issuetype='Bus'):
        """
        This method creates Jira issue.
        :param project_key:
        :param summary:
        :param description:
        :param issuetype:
        """
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype}
        }

        return self._auth_jira.create_issue(fields=issue_dict)

    def create_jira_issue_teardown(self, project_key, summary, description, issuetype):
        """
        This method creates Jira issue.
        :param project_key:
        :param summary:
        :param description:
        :param issuetype:
        :return:
        """
        jira_flag = JiraHandler()
        try:
            logging.info("Creating Jira issue...")
            issue = jira_flag.create_issue(
                project_key, summary,
                description, issuetype)
            if issue:
                logging.info("Jira issue created: " + issue.key)
            else:
                logging.info("Jira issue not created")
        except Exception as e:
            logging.error(f'Jira issue not created: {e}')
