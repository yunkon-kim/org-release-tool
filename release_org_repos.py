import json

import requests


def create_release(
    access_token,
    owner,
    repo,
    tag_name,
    target_commitish,
    release_name,
    draft,
    prerelease,
    generate_release_notes,
):
    """
    Create a release using the GitHub API.

    Parameters:
        access_token (str): GitHub Access Token
        owner (str): Repository owner
        repo (str): Repository name
        tag_name (str): Tag name for the release
        target_commitish (str): Target commitish for the release
        release_name (str): Release name
        release_notes (str): Release notes content
        draft (bool): Whether the release is a draft
        prerelease (bool): Whether the release is a prerelease

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    headers = {
        "Authorization": f"token {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "name": release_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }

    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code == 201:
        print(f"{tag_name} release has beend created successfully for {repo}.")
    else:
        print(f"Failed to create release for {repo}: {response.status_code}")
        print(response.text)


def generate_release_notes_content(
    access_token, owner, repo, tag_name, target_commitish, previous_tag_name
):
    """
    Generate release notes using the GitHub API.

    Parameters:
        access_token (str): GitHub Access Token
        owner (str): Repository owner
        repo (str): Repository name
        tag_name (str): Tag name for the release
        target_commitish (str): Target commitish for the release
        previous_tag_name (str): Previous tag name

    Returns:
        str: Generated release notes
    """
    url = (
        f"https://api.github.com/repos/{owner}/{repo}/releases/generate-notes"
    )

    headers = {
        "Authorization": f"token {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
    }

    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code == 200:
        return response.json().get("body", "")
    else:
        print(
            "Failed to generate release notes:",
            response.status_code,
            response.text,
        )
        return ""


def create_release_with_custom_notes(
    access_token,
    owner,
    repo,
    tag_name,
    target_commitish,
    release_name,
    release_notes,
    draft,
    prerelease,
):
    """
    Create a release using the GitHub API.

    Parameters:
        access_token (str): GitHub Access Token
        owner (str): Repository owner
        repo (str): Repository name
        tag_name (str): Tag name for the release
        target_commitish (str): Target commitish for the release
        release_name (str): Release name
        release_notes (str): Release notes content
        draft (bool): Whether the release is a draft
        prerelease (bool): Whether the release is a prerelease

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"

    headers = {
        "Authorization": f"token {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "name": release_name,
        "body": release_notes,
        "draft": draft,
        "prerelease": prerelease,
    }

    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code == 201:
        print(f"Release successfully created for {repo}.")
    else:
        status_code = response.status_code
        text = response.text
        print(f"Failed to create release for {repo}: {status_code}, {text}")


def main():
    # Read configuration from the file
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    access_token = config["access_token"]
    owner = config["owner"]
    repositories = config["repositories"]
    tag_name = config["tag_name"]
    # previous_tag_name = config["previous_tag_name"]
    target_commitish = config["target_commitish"]
    release_name = config["release_name"]
    draft = config["draft"]
    prerelease = config["prerelease"]
    generate_release_notes = config["generate_release_notes"]

    for repo in repositories:
        create_release(
            access_token,
            owner,
            repo,
            tag_name,
            target_commitish,
            release_name,
            draft,
            prerelease,
            generate_release_notes,
        )

        # # Generate release notes
        # release_notes = generate_release_notes_content(
        #     access_token,
        #     owner,
        #     repo,
        #     tag_name,
        #     target_commitish,
        #     previous_tag_name,
        # )

        # if release_notes:
        #     # Create the release with the generated notes
        #     create_release_with_custom_notes(
        #         access_token,
        #         owner,
        #         repo,
        #         tag_name,
        #         target_commitish,
        #         release_name,
        #         release_notes,
        #         draft,
        #         prerelease,
        #     )


if __name__ == "__main__":
    main()
