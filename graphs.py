import pandas as pd
import matplotlib.pyplot as plt
from configs import GRAPH_PATH
from graph_utils import topic_checker_util


def pie_topics_plot(df):
    df = df.apply(lambda row: topic_checker_util(row), axis=1)
    df = df.dropna(subset=['Topic'])
    topics = df['Topic'].drop_duplicates().tolist()
    ordered_df = pd.DataFrame(columns=['Topic', "Amount"])
    for topic in topics:
        ordered_df.loc[ordered_df.shape[0]] = [topic[::-1], df[df['Topic'] == topic].shape[0]]
    ordered_df.groupby(['Topic']).sum().plot(kind='pie', y='Amount', figsize=(25, 15), autopct='%1.1f%%')
    plt.savefig(f"{GRAPH_PATH}pie of most talked subject in the last day")
