import pandas as pd
import sqlite3
import sys
import os


def create_dataframe(arg1):

    if not(os.path.exists(arg1)):
        raise ValueError("Invalid Path ")
    else:
        # Conncting to the sqlite3 data base
        connection = sqlite3.connect(arg1)
        df = pd.read_sql_query("""SELECT video_id, category_id,'us' AS language FROM USvideos UNION
                                SELECT video_id, category_id,'ca' AS language FROM CAvideos UNION
                                SELECT video_id, category_id,'de' AS language FROM DEvideos UNION
                                SELECT video_id, category_id,'fr' AS language FROM FRvideos UNION
                                SELECT video_id, category_id,'gb' AS language FROM GBvideos""", connection)

    return df


def checkColumnName(df):
    columnName = list(df)  # https://stackoverflow.com/a/19483025
    numberofColumn = len(columnName)
    if(numberofColumn == 3):
        if set(['video_id', 'language', 'category_id']).issubset(
                set(columnName)):  # https://stackoverflow.com/a/6159356
            return True
        else:
            return False

# There are at least 10 rows in the DataFrame.


def checkRowSize(df):
    Count_Row = df.shape[0]  # https://stackoverflow.com/a/35523946
    if(Count_Row >= 10):
        return True
    else:
        return False


def checkKey(df):
    Count_Row = df.shape[0]
    # https://stackoverflow.com/a/19378497
    video_idset = len(set(df['video_id'].map(str) + df["language"].map(str)))
    # print(Count_Row)  # 35950
    # print(video_idset)  # 30697 (without concatenate )  35920 with
    # concatenate
    if (Count_Row == video_idset):
        return True
    else:
        return False
