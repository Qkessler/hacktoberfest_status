import os
from github import Github


GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
api = Github(GITHUB_TOKEN)


def init():
    return api


def get_hacktober_progress(user):
    pulls = []
    repos = list(user.get_repos())
    for r in repos:
        for l in r.get_labels():
            if l.name == 'Hacktoberfest':
                pulls.append(r.get_pulls(sort='created'))
    return pulls
