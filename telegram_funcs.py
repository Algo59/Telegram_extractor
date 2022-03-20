from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from configs import CHANNELS_LINKS, HOURLY_RESULT_DF, API_ID, API_HASH, GMT2, HOURS_TO_CHECK
import re


def message_collector():
    with TelegramClient("algo59", API_ID, API_HASH) as client:
        for channel in CHANNELS_LINKS:
            for message in client.iter_messages(channel,
                                                offset_date=datetime.now() - timedelta(hours=HOURS_TO_CHECK + GMT2),
                                                reverse=True):
                HOURLY_RESULT_DF.loc[HOURLY_RESULT_DF.shape[0]] = [channel, str(datetime.strptime(
                    re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", str(message.date))[0],
                    "%Y-%m-%d %H:%M:%S") + timedelta(hours=2)), message.text]