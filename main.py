from configs import HOURLY_RESULT_DF
from graphs import pie_topics_plot
from telegram_funcs import message_collector
from utils_funcs import writer


if __name__ == "__main__":
    message_collector()
    writer()
    pie_topics_plot(HOURLY_RESULT_DF)
