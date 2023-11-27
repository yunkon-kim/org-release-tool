import json

import requests


def main():
    # Read config.json
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    access_token = config["access_token"]
    owner = config["owner"]
    repositories = config["repositories"]
    tag_name = config["tag_name"]
    release_name = config["release_name"]

    # Add token to headers
    headers = {
        "Authorization": f"token {access_token}",
        "Content-Type": "application/json",
    }

    for repo in repositories:
        # API request URL
        url = f"https://api.github.com/repos/{owner}/{repo}/releases"

        # Data creation
        data = {
            "tag_name": tag_name,
            "name": release_name,
            "draft": False,
            "prerelease": False,
            "generate_release_notes": True,
        }

        # Send a POST request to create a release
        response = requests.post(url, headers=headers, json=data, timeout=10)

        # Check the response
        if response.status_code == 201:
            print(f"Release가 {repo}에 성공적으로 생성되었습니다.")
        else:
            print(
                f"Release 생성 실패 ({repo}):", response.status_code, response.text
            )


if __name__ == "__main__":
    main()
