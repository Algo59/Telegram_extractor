from configs import HOURLY_RESULT_DF, OUTPUT_PATH


def writer():
    HOURLY_RESULT_DF.to_excel(OUTPUT_PATH, index=False)