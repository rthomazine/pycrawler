import argparse
import json
import logging

from subreddit_bot import start_bot
from subreddits import Subreddits

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def run_as_robot():
    logger.info('Starting in bot mode')
    start_bot()


def run_single_command(subreddits):
    logger.info('Starting in command mode')
    subr = Subreddits(subreddits=subreddits)
    subr_info = subr.get_subreddits_info()
    if subr_info:
        print(json.dumps(subr_info))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c',
                       '--command',
                       help='Command running mode with provided subreddits as semicolon separated string. Ex. askreddit;worldnews;cats',
                       metavar='SUBREDDITS',
                       type=str,
                       nargs=1)
    group.add_argument('-b',
                       '--bot',
                       help='Bot running mode',
                       action="store_true")
    args = parser.parse_args()
    if args.robot:
        run_as_robot()
    else:
        run_single_command(args.command[0])
