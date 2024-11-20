import praw
import pdb
import re
import os

reddit = praw.Reddit("bot1")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("post_replied.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("pythonforengineers")
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("1 2 3 bot testing", submission.title, re.IGNORECASE):
            submission.reply("Thank you Shantanu Tiwari for this amazing project.")
            print(f"Bot replying to: {submission.title}")

            posts_replied_to.append(submission.id)


with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
