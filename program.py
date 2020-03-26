import api


if __name__ == '__main__':
    api_ = api.init()
    me = api_.get_user()
    pulls = api.get_hacktober_progress(me)
    progress = len(pulls)
    print(f'The progress on your hacktober bar is {progress}/4')
