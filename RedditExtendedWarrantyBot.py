import praw
import re
from time import sleep
from prawcore.exceptions import Forbidden, RequestException, ServerError, ResponseException, SpecialError

reddit = praw.Reddit("extendedwarranty_bot", config_interpolation="basic")
subreddit = reddit.subreddit("all")
quote = ", I have been trying to reach you about your car's extended warranty"

print("RedditExtendedWarrantyBot started")
while True:
    try:
        for comments_post in subreddit.stream.comments(skip_existing=True):
            comment = comments_post.body
            x = re.search("\scar\s.*\swarranty|^car\s.*\swarranty|\scar\swarranty|^car\swarranty", comment, flags=re.I)
            if bool(x) == True:
                if comments_post.author != "extendedwarranty_bot":
                    comments_post.reply(str(comments_post.author) + quote)
    except Exception:
        print(Exception)
        sleep(20)