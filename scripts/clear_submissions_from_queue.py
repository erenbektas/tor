from datetime import datetime, timedelta

from praw import Reddit
# from praw.exceptions import RedditAPIException

r = Reddit('bot2')

UNCLAIMED = 'Unclaimed'
IN_PROGRESS = 'In Progress'


def remove_old_crap(posts):
    for item in posts:
        if item.link_flair_text == UNCLAIMED:
            submission_time = datetime.fromtimestamp(item.created_utc)
            if submission_time < current_time - timedelta(days=1):
                print(f"Removing {item.name}, posted on {str(submission_time)}")
                item.mod.remove()


if __name__ == '__main__':
    current_time = datetime.now()
    for x in range(30):
        # I know for a fact that sometimes reddit will only show 4 posts on the page,
        # but each one of these options will only pull one of them. Just ask for all
        # of them, smash them together, and process.
        submissions = list(r.subreddit("transcribersofreddit").hot(limit=None))
        submissions += list(r.subreddit("transcribersofreddit").new(limit=None))
        submissions += list(r.subreddit("transcribersofreddit").top(limit=None))
        submissions += list(r.subreddit("transcribersofreddit").controversial(limit=None))
        remove_old_crap(submissions)

        # try:
        #     item.reply(
        #         "This submission has been open for at least three days and is listed as in progress"
        #         " -- it has been removed to make room for other submissions in the queue. Please contact"
        #         " itsthejoker if there is an issue."
        #     )
        # except RedditAPIException:
        #     pass
