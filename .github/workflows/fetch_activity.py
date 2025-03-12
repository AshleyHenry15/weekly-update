import requests

# GitHub token and API URL
TOKEN = 'YOUR_GITHUB_TOKEN'
ORG_NAMES = ['org1', 'org2']  # Add your organizations here

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_activity():
    activity = {}
    
    for org in ORG_NAMES:
        org_repos_url = f'https://api.github.com/orgs/{org}/repos'
        repos = requests.get(org_repos_url, headers=headers).json()
        
        for repo in repos:
            repo_name = repo['name']
            activities = {
                'prs_opened': 0,
                'prs_reviewed': 0,
                'issues_opened': 0,
                'issues_commented': 0
            }
            
            # Fetch PRs and issues
            pr_url = f'https://api.github.com/repos/{org}/{repo_name}/pulls?state=all'
            issue_url = f'https://api.github.com/repos/{org}/{repo_name}/issues?state=all'
            
            prs = requests.get(pr_url, headers=headers).json()
            issues = requests.get(issue_url, headers=headers).json()
            
            # Process PRs
            for pr in prs:
                if pr['user']['login'] == 'YOUR_GITHUB_USERNAME':
                    activities['prs_opened'] += 1
                if pr.get('requested_reviewers'):
                    activities['prs_reviewed'] += 1

            # Process Issues
            for issue in issues:
                if issue['user']['login'] == 'YOUR_GITHUB_USERNAME':
                    activities['issues_opened'] += 1
                if issue.get('comments'):
                    activities['issues_commented'] += 1

            activity[f'{org}/{repo_name}'] = activities
    
    return activity

if __name__ == "__main__":
    activity = get_activity()
    with open('activity_data.json', 'w') as f:
        json.dump(activity, f)
