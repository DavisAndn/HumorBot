import praw
import os

CID=os.environ['CLIENT_ID']

CSecret=os.environ['CLIENT_SECRET']
useragent=os.environ['USER_AGENT']

Uname=os.environ['USERNAME']

Pwd=os.environ['PASSWORD']
subname=os.environ['SUB_NAME']

reddit = praw.Reddit(client_id=CID,
client_secret=CSecret,
user_agent=useragent,
username=Uname,
password=Pwd)

subreddit = reddit.subreddit(subname)

for submission in subreddit.stream.submissions(skip_existing=True):
    unixtime = submission.created_utc
    tim = (unixtime//86400)%7
    sec = (unixtime//3600)%24
    if(submission.link_flair_text == "Humor & Memes"): 
        if(not(((tim ==  1) and (sec >=21)) or (tim == 2) or (tim == 3) or ((tim == 4) and (sec <= 6)))):
            submission.mod.remove()
            submission.mod.send_removal_message('Rule 11: Humor & Meme posts will be limited to weekends. Humor Weekend Starts at Friday, 5:00 PM Eastern and ends Monday, 2 AM Eastern. Humor posts outside this time frame will be removed. Please resubmit your humor post on the weekend.I am a bot, and this action was performed automatically. [Please contact the moderators of this subreddit if you have any questions or concerns](https://www.reddit.com/message/compose/?to=/r/ClashOfClans).', title='ignored', type='public')
