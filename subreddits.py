from praw import Reddit

from config import config

MIN_SCORE = config.get('reddit', 'min_score')

class Subreddits:
    def __init__(self,
                 subreddits=None) -> None:
        self._subreddits = subreddits
        self._reddit = Reddit(client_id=config.get('reddit', 'client_id'),
                              client_secret=config.get('reddit', 'client_secret'),
                              user_agent=config.get('reddit', 'user_agent'))
        self._reddit.config.reddit_url = config.get('reddit', 'url')

    def get_subreddits_info(self):
        subreddits_response = []
        for subreddit in self._subreddits.split(';'):
            subr = self._get_subreddit_info(name=subreddit)
            if subr:
                subreddits_response.append(subr)
        return subreddits_response

    def _get_subreddit_info(self, name=None):
        subr_infos = []
        for subreddit in self._reddit.subreddit(name).top('all'):
            if subreddit.score >= MIN_SCORE:
                comments = f"{self._reddit.config.reddit_url}{subreddit.permalink}"
                link = f"{self._reddit.config.reddit_url}/{subreddit.subreddit_name_prefixed}"
                subr_infos.append(dict(subreddit=subreddit.subreddit_name_prefixed,
                                       score=subreddit.score,
                                       link=link,
                                       title=subreddit.title,
                                       comments=comments))
        return subr_infos
