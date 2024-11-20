
# Python Reddit Bot

This project consists of two Python scripts using [the PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/) library to interact with Reddit. The scripts demonstrate fetching and processing posts from subreddits and replying to specific posts based on a condition.


## Files

1. `bot_read.py`
\
This script connects to a subreddit and retrieves the top 5 posts from its "hot" section. It prints details of each post, including its title, text, and score.  
 

#### Features:
- Fetches posts from the `learnpython` subreddit.
- Displays the title, text, and score of each post.

#### How to Use:
- Ensure you have a Reddit bot configuration named `bot1` in your PRAW `praw.ini` file.
- Run the script:
```bash 
python bot_read.py
```
- Observe the output in the terminal.


2. `reply_post.py`
\
This script automates replying to Reddit posts based on specific keywords in the title. It also keeps track of posts it has replied to using a `posts_replied_to.txt` file to avoid duplicate replies.

 
#### Features:
- Searches for posts in the `pythonforengineers` subreddit.
- Looks for posts with the phrase `1 2 3 bot testing` in their titles.
- Replies to matching posts with a pre-defined message.
- Maintains a list of replied posts in a file (`posts_replied_to.txt`).

#### How to Use:
- Set up the `bot1` configuration in the PRAW `praw.ini` file.
- Ensure `posts_replied_to.txt` exists in the same directory (it can be an empty file).
- Run the script:
```bash
python reply_post.py
```


## Configuration
Both scripts rely on a properly configured `praw.ini` file. The `praw.ini` file can be found in your Python installation folder under your virtual environment:
```plaintext
PyReddit\Lib\site-packages\praw\praw.ini
```
Here, `PyReddit` is the name of your virtual environment. Edit this file to include your bot credentials:
```ini
[bot1]
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
username=YOUR_USERNAME
password=YOUR_PASSWORD
user_agent=YOUR_USER_AGENT
```
Replace the placeholders with your Reddit app's credentials.