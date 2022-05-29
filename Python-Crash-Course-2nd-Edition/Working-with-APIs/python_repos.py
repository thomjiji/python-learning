import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()  # use json() method to convert the information to a Python dictionary.
print(f"Total repositories: {response_dict['total_count']}")
print(f"Incomplete results: {response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']  # repo_dicts is a list containing lots of dictionaries.
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")