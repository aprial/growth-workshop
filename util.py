import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *
from pandas import DataFrame
from time import mktime
from sklearn.feature_extraction import DictVectorizer


campaign_to_num = {
	'TW' : 1,
	'RE' : 2,
    'FB' : 3,
    'PI' : 4
}

event_to_num = {
   'like' : 1,
   'share' : 2,
   'nothing' : 3,
   'bought' : 4
}

meal_to_num = {
   'japanese':  1,
   'chinese' : 2,
   'french' : 3,
    'german' : 4,
    'italian' : 5,
    'mexican' : 6,
    'vietnamese' : 7
}



campaign_to_cost = {
    'TW' : .25,
    'RE' : .35,
    'FB' : .45,
    'PI' : .55
}
def num_rows(df):
    return len(df.index)

def transform_column(df,column_name,fn):
    """
    Transforms a column with the given function
    """
    df[column_name] = df[column_name].apply(fn).astype('float')


def hist_and_show(df,column_name):
    """
    Histogram the given column for the data frame
    and render it
    """
    df.hist(column_name)
    plt.show()


def to_percentage(df,column_name):
    """
     Given a numeric field column name, converts each field
     to a percentage that a given element in a row contributed to the overall sum of a column
    """
    column_sum = df[column_name].sum()
    df[column_name] = df[column_name] / column_sum



def df_column_wise_norm(df):
     """
     Column wise norm. Calculates the norm of each column.
     The formula is:
           df - df.mean / df.max - df.min
     """
     df_norm = (df - df.mean()) / (df.max() - df.min())
     return df_norm


def query_to_df(session,query):
    """
    Convert an sql query to a pandas data frame
    """
    result = session.execute(query)
    d = DataFrame(result.fetchall())
    d.columns = result.keys()
    return d






def to_milliseconds(dt):
    """
    Converts the given date time to epoch milliseconds
    """
    sec_since_epoch = mktime(dt.timetuple()) + dt.microsecond/1000000.0
    millis_since_epoch = sec_since_epoch * 1000
    return millis_since_epoch

def vectorize(df,label_column):
    """
    Vectorize input features wrt a label column.
    """
    feature_names = []
    for feature_name in df.columns.values:
        if feature_name != label_column:
            feature_names.append(label_column)
    inputs = df[feature_names].values
    return inputs

def vectorize_label(df,label_column,num_labels,target_outcome):
    """
    Vectorize input features wrt a label column.
    """
    inputs = df[label_column].apply(lambda x: x== target_outcome).values

    return inputs



