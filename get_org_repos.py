import json

import requests


def get_organization_repos(org_name, access_token=None):
    """
    Get a list of repositories for a given organization.

    Parameters:
        org_name (str): Name of the organization
        access_token (str): GitHub Access Token (optional)

    Returns:
        list of str: List of repository names
    """
    url = f"https://api.github.com/orgs/{org_name}/repos"
    headers = {}
    if access_token:
        headers["Authorization"] = f"token {access_token}"

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        repos = response.json()
        print("Retrieved repositories successfully.")
        print(f"Number of repositories: {len(repos)}")
        return [repo["name"] for repo in repos]
    else:
        status_code = response.status_code
        text = response.text
        print(
            f"Failed to retrieve repos for {org_name}: {status_code}, {text}"
        )
        return []


def main():
    # Read configuration from the file
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    access_token = config["access_token"]
    org_name = config["owner"]

    repositories = get_organization_repos(org_name, access_token)

    # Print the list of repositories separated by commas
    print(", ".join(repositories))


if __name__ == "__main__":
    main()
