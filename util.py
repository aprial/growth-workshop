import matplotlib.pyplot as plt
from sqlalchemy import *
import numpy as np
from sqlalchemy.orm import sessionmaker
from churndata import *
from pandas import DataFrame
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


def transform_column(df,column_name,fn):
    """
    Transforms a column with the given function
    """
    df[column_name] = df[column_name].apply(fn)


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

def vectorize(df,label_column):
    """
    Vectorize input features wrt a label column.
    """
    feature_names = []
    for feature_name in df.columns.values:
        if feature_name != label_column:
            feature_names.append(label_column)
    inputs = df[feature_name].to_dict()
    input_labels = df[label_column].to_dict()
    vectorizer = DictVectorizer()
    ret = vectorizer.fit_transform(inputs,input_labels)
    return ret


