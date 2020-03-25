import os
import requests
from github import Github, InputFileContent
import http.client

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

# conn = http.client.HTTPSConnection("apis-sandbox.bancosantander.es")

# headers = {'accept': "application/json"}

# conn.request("GET", full_url, headers=headers)

# res = conn.getresponse()
# res.flush()
# data = res.read()
# print(full_url)
# print(data.decode("utf-8"))



def start_api():
    g = Github(GITHUB_TOKEN)
    me = g.get_user()
    for repo in me.get_repos():
        # print(help(repo))
        


if __name__ == '__main__':
    start_api()
