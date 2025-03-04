import praw
import os
from dotenv import load_dotenv
load_dotenv()


username = os.getenv("usernam")
password = os.getenv("password")
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

reddit_instance = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent="test_bot",
            username=username,
)

# print(reddit_instance.user.me())
# subreddit = reddit_instance.subreddit("cats")
# top_25_submissions = subreddit.top(limit=25, time_filter="week")
# for submission in top_25_submissions:
#     print(submission.title)

# subreddit = reddit_instance.subreddit("testingground4bots")
# subreddit.submit(title="This is my test post for my bot", selftext="Hello world")

submission = reddit_instance.submission("1j3hutu")
comments = submission.comments

# comments.replace_more()
for comment in comments:
    if "orange" in comment.body:
        print(comment.body)