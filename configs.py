import pandas as pd
import os

HOURS_TO_CHECK = 2
GMT2 = 2
API_ID = 18690322
API_HASH = "e81cc2024ef52e8c743512032db44e5f"
CHANNELS_LINKS = ["https://t.me/AdirLM1", "https://t.me/abualiexpress", "https://t.me/amarassadi",
                  "https://t.me/Intellinews", "https://t.me/news_kodkodgroup", "https://t.me/GLOBAL_Telegram_MOKED",
                  "https://t.me/AbuSaleh_israel_reports", "https://t.me/Lebanon_24"]
HOURLY_RESULT_DF = pd.DataFrame(columns=["Source", "Time", "Content"])
OUTPUT_PATH = "Testing_output.xlsx"
GRAPH_PATH = f"{os.getcwd()}/graphs/"