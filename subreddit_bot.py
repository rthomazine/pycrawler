import json
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from config import config
from subreddits import Subreddits

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def subreddit_crawler(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text('You must provide some subreddits as a semicolon separated string')
        return
    subreddits_req = context.args[0]
    subr = Subreddits(subreddits=subreddits_req)
    subr_info = subr.get_subreddits_info()
    if subr_info:
        update.message.reply_text(json.dumps(subr_info))
    else:
        update.message.reply_text(f"No subreddit that worth reading for {subreddits_req}")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start_bot():
    """Start the bot."""
    updater = Updater(config.get('telegram', 'token'), use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('NadaPraFazer', subreddit_crawler, pass_args=True))
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    logger.info('Subreddit bot up and running...')
    updater.idle()
