import json
from jira import JIRA
from dotenv import load_dotenv
import os

load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_username = os.getenv('JIRA_USERNAME')
jira_api_token = os.getenv('JIRA_API_TOKEN')

if __name__ == "__main__":
    jira = JIRA(
        server=str(jira_url),
        basic_auth=(str(jira_username), str(jira_api_token))
    )
    
    issue = jira.issue('TES-1')
    print(json.dumps(issue.raw, indent=2))

    jql_query = 'project = "TES" ORDER BY created DESC'
    issues = jira.search_issues(jql_query)
    print(len(issues))
