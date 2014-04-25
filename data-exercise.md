Extract transform load - vectorizing Data

Overview
========================

The core objective of this exercise is to understand sql queries, pandas data frames, and general exploratory data analysis.

Towards the end, we will learn how to take our basic tools for exploratory data analysis and transform the inputs in to something

appropriate for a machine learning algorithm.


For our baseline classes, we will be using the classes from churndata.py . This contains all of the necessary classes from which

we will derive all of our analysis.

The associated database forjar.db contains our actual data set. We will need to use sql alchemy to load the data in.




Loading Data Via SQLAlchemy
====================================

First we will be loading the data from our sql lite database and doing a simple join.

Our objective here will be to get a list of the users who have bought something.

If we think in terms of our objectives of the site, it is to maximize revenue.

In any given day, we need to understand which of our users actually tend to buy things on the site.

If they aren't buying anything, we should do something about it given the data we know about them.


Exercise:

     1. Load data from an sql database such that each you load a join of the users and events. We only want the users who bought something.

     2. Load the results in to a pandas data frame


The goal with this particular exercise is to understand which users are buying things so we can understand what attributes are successful.

Resources:
SQLLite/SQLAlchemy - http://docs.sqlalchemy.org/en/rel_0_9/dialects/sqlite.html
Basic Querying -     http://docs.sqlalchemy.org/en/rel_0_9/orm/query.html
Pandas Data Structures - http://pandas.pydata.org/pandas-docs/stable/dsintro.html


If you are still stuck, here is a solution:

Gist


Ranking
======================

Now we will want to perform some sort of ranking, understanding attributes of who bought the most will allow us

to understand who our most profitable users are. Users who buy the most do not necessarily have the highest life time value,

but it is a great low hanging fruit for understanding where to begin understanding your users.


Exercise:
         Create a ranked grouping of the users who bought the most


Means and Statistics on our Data
========================================


Now we will use Pandas to start doing some exploratory analysis.  Let's take some time to load data from SQLAlchemy in to a data frame.

Exercise:

      Load the data from sql alchemy in to a pandas data frame
      Using pandas, calculate the mean number of times each user from each campaign type (facebook,twitter,pinterest,...) trigger a buy event.
      This will involve some filtering and grouping.


Ranking using pandas
================================

Now we want to find out different kinds of tendencies for users, Each user campaign type may tend to buy certain kinds of food, share more, or even churn more.

We want to understand how to do basic campaign wise cohort analysis (note that this is different from the time based cohort analysis)

Exercise:

       For each event type, load the count of the number of times each kind of user (by campaign type) performed certain events



Visualizing Data
============================

Pandas has very powerful plotting built in to it alongside matplotlib. Let's generate scatterplots for all of the various user campaign to event types.

This will allow us to see correlations in events all at once.


Machine Learning Data input prep
===========================================

For Machine Learning Algorithms, they can only accept numbers. Our specific task here will be to predict a label.


Exercise:

Let's build out a data frame such that we have an outcome label. Set the outcome label to be event type.

From here, binarize the event type outcome to be == bought or not.


Data Normalization
=====================================================

Machine Learning algorithms typically work better if you scale the data (squish the data in to 0,1 range)

Exercise:

       Transform the data in to numerical (ordinal etc)
       Split out the feature set columns from the outcome label and normalize the given features.
