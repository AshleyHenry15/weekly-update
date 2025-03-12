import requests

# Your GitHub API token
GITHUB_TOKEN = 'your_github_token'

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com"

# Headers to include authorization token
headers = {
    'Authorization': f'token {GITHUB_TOKEN}'
}

def get_all_activity(username):
    """Fetch all activity for the given GitHub username"""
    events_url = f"{GITHUB_API_URL}/users/{username}/events"
    response = requests.get(events_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return list of events (activity)
    else:
        print(f"Failed to fetch events for {username}: {response.status_code}")
        return []

def get_activity():
    """Main function to gather activity"""
    username = 'your_username'  # Replace with your GitHub username
    
    activity = get_all_activity(username)
    print("All Activity:", activity)
    
    return activity

if __name__ == "__main__":
    activity = get_activity()
