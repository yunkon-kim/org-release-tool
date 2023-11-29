# Organization Release Tool

This is a tool that can be used when creating releases within a GitHub organization.
You can create releases of the same version (e.g. v0.1.0) in multiple repositories. 


## Setup environment

(optional) Configure virutalenv
```bash
# Create venv (venv path is .venv here)
python3 -m venv .venv

# Activate venv
source .venv/bin/activate
```

Install dependancy
```bash
# Install requirements
pip3 install -r requirements.txt
```


## Prepare GitHub personal access token

See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) by GitHub Docs

Note - For now, it would be better to use a personal access token (classic).


## Create config.json

- Refer `template-config.json`
- Modify the values appropriately

```json
{
    "access_token": "YOUR_GITHUB_ACCESS_TOKEN",
    "owner": "org or username",
    "repositories": [
        "repo1",
        "repo2",
        "repo3"
    ],
    "tag_name": "v0.0.1",
    "previous_tag_name": "v0.0.0",
    "target_commitish": "main",
    "release_name": "Release Title or v0.0.1",
    "draft": false,
    "prerelease": false,
    "generate_release_notes": true
}
```


## Get repos in an org

This is optional! 
It can be used when you want to know the entire repository of the organization.

It operates normally only when the `owner` in `config.json` is org.

The obtained repository list can be applied to `config.json` repositories.
Unnecessary repositories should be removed.

```bash
python3 ./get_org_repos.py
```


## Release repos

```bash
python3 ./release_org_repos.py
```


## Output

See the following link, https://github.com/yunkon-kim/org-release-tool/releases