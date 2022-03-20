from configs import CHANNELS_LINKS, HOURLY_RESULT_DF, API_ID, API_HASH, OUTPUT_PATH, GMT2, HOURS_TO_CHECK
from datetime import datetime, timedelta
from telethon.sync import TelegramClient
import re
from graphs import pie_topics_plot

def message_collector():
    with TelegramClient("algo59", API_ID, API_HASH) as client:
        for channel in CHANNELS_LINKS:
            for message in client.iter_messages(channel,
                                                offset_date=datetime.now() - timedelta(hours=HOURS_TO_CHECK + GMT2),
                                                reverse=True):
                HOURLY_RESULT_DF.loc[HOURLY_RESULT_DF.shape[0]] = [channel, str(datetime.strptime(
                    re.findall("\d{4}-\d\d-\d\d \d\d:\d\d:\d\d", str(message.date))[0],
                    "%Y-%m-%d %H:%M:%S") + timedelta(hours=2)), message.text]


def writer():
    HOURLY_RESULT_DF.to_excel(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    message_collector()
    writer()
    pie_topics_plot(HOURLY_RESULT_DF)

