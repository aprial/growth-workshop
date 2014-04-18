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


