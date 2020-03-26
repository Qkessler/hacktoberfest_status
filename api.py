import os
import requests
from github import Github, InputFileContent
import http.client

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
api = Github(GITHUB_TOKEN)


def get_repos_user(user):
    return list(user.get_repos())


if __name__ == '__main__':
    me = api.get_user()
    repos = get_repos_user(me)
    print(repos)
    # print(f'{api}, {me}')
