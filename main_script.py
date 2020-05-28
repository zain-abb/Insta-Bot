from InstagramAPI import InstagramAPI
from time import sleep
import pprint


USERNAME = 'your_username'  # your instagram username
PASSWD = 'your_password'  # instagram password

api = InstagramAPI(USERNAME, PASSWD)

tag_count = 0
mention_count = 0
i = 0  # for the first iteration...

# if your credentials are correct then it will check for the tagged posts of you...
if api.login():
    while True:
        result = api.getRecentActivity()
        result = api.LastJson
        min_result = result['old_stories']
        string = str(min_result)
        substring = '\'comment_notif_type\': \'mention\''
        get = [i for i in range(len(string))
               if string.startswith(substring, i)]
        if mention_count < len(get):
            # gets total number of tags
            mention_count = len(get)
            if i != 0:
                print('Someone mentioned you!')

        api.getSelfUsernameInfo()
        tag = api.LastJson
        if tag_count < tag['user']['usertags_count']:
            # gets total number of tags
            tag_count = tag['user']['usertags_count']
            if i != 0:
                print('Someone tagged you!')
        i += 1
        sleep(5)
else:
    print('Error in loging in...')
