Machine Learning for Growth Engineers
==================================================


Before Beginning:

       We need to install python if you don't have it already. If you are on windows, please go here and install it:


               https://www.python.org/download/releases/2.7.6/

        After this, we will be leveraging the scipy stack and will thus need to set this up as well:

              http://www.scipy.org/install.html



        OSX users will already have python installed.

      You will also need git. If you are on windows go here:

              http://git-scm.com/download/win









In this workshop, we will be covering how to interpret website visits and growth metrics to predict everything from customer churn, to figuring out how to estimate a customers life time value. We will be using 2 different data sets. One is a data set based on a pinterest like website for food where users have different activities they can perform:

            Buying
            Liking
            Sharing


 The food items on the website are broken in to very simple categories for the sake of brevity:


            japanese
            chinese
            french
            german
            italian
            mexican,
            vietnamese



 These users come from different social networks:



           Facebook
           Twitter
           Reddit
           Pinterest


The goal for the first set of exercises will be to analyze and find different tendencies of users coming from different social networks.

We will be doing a series of exercises that amounts to first understanding the data we have been given, and from there running a series of tests

on the data to compute various statistics that we can then use to make inferences.



First we will need to visualize the data. We need to understand the distribution (counts) of users and run comparisons across different metrics and activities.

From there, we will be able to make educated guesses about the data as well as what goes in to basic data exploratory analysis.

Let's start with a basic understanding of the data with just some histograms. Histograms are a visualization to show the counts of different types of a user.

An example might be:
                   
                   Facebook 32
                   Twitter  55
                   Reddit 66
                   Pinterest 72

A histogram is just a visual representation of the random variable (think of it like a database column) and the counts of the different values they take on.


First let's doing some data exploration. We will need to visualize the data in order to understand it.

Let's open up visualize.py.

We will see some basic visualization code. One thing of importance is the following:


          campaign_to_num = {
	             'TW' : 1,
	             'RE' : 2,
                  'FB' : 3,
                 'PI' : 4
           } 

A histogram in matplotlib takes what amounts to bins of numbers. When we want to do different counts, we will want to translate whatever metric we want to look at to a numerical discrete or ordinal value.


The key takeaway here is how to use visualizations to understand a distribution of data. We will notice that there is a pretty even count of each type.

We won't find much information here, let's move on to trying to derive tendencies of different kinds of users.

Let's think about what kind of questions we want to ask. When we want to understand different kinds of users, we want to understand their behavior.

Their behavior allows us to optimize for business objective such as ad spend (where do I advertise?), what users are likely to buy what categories of items,

and perhaps, what users are likely to share. We can use the sum of these underlying insights to drive profits, increase conversions, and make more educated, 

data driven decision in our day to day coding and product management decisions.


Next we will want to dive in to the tendencies and bias of different users. We can use this to target ad spend at each social network and figure out how to coordinate social media efforts with respect to certain goals.

Let us plot user vs action now. As defined earlier, users can take certain actions on the site:

             Buying
            Liking
            Sharing


            applicable to different kinds of food items:


            japanese
            chinese
            french
            german
            italian
            mexican,
            vietnamese



Right now, we want to look at per site actions in aggregate. Let's now build a series of histograms that show per social network actions.


First, we need to figure out how to get per user events and their aggregate counts. This is going to involve some database table joins.

A common join that is often used is a natural join.


###Most Profitable Users

Let's now home in on profits. We all want to know who our most profitable users are. Let us do this by homing in on the buy action and grouping these by campaign.





###Lift Curves

Lift curves are a predictive model for identifying the percent gained over a baseline model. This is used in evaluating models.

First a baseline is established, such that an empirical study is done with a previously defined model vs a newer model that is being validated.

The first concept we need to understand to work with lift curves is the idea of a response model. This is picking a field (column) that we will use

as a response metric. A positive response with respect to our model could be likes, shares or buying. What we will want to do is optimize for one of these

and try to see what happens when we run certain campaigns, iterate, and see if a given campaign did worse or better.

From here, we will simulate 2 different campaigns. We will use our first database as a baseline and from there, measure improvement in certain metrics
 with another dataset. This next data set will be used to represent another campaign.

 Our base line metric will be profit. Let us assume that a buy action is represented by $1. We can then use this as a basseline to determine gain of profits
 relative to certain campaigns.

 From here, we will visualize a lift curve and see how to interpret the results.



A few things of note here:

     The campaign-3.db will be after a campaign2-db. This will be assumed to be users taking action within the last month. Anything that isn't bought (what we are optimizing for)
     will be treated as a negative action. We till then see how many more users bought food vs not over the past month.



###Life time value:

      Now, using the a different data set we will get in to calculating life time value for users. This will involve a bit of data aggregation (purchases by user)
      as well as identifying things like most profitable food category, and ranking users by their life time value. We will then use this to figure out who our most profitable demographic is.


      Life time value is usually calculated as:

             Order Value * Num Repeat Sales * Average Retention Time

      Realistically, order value is not static. We want to calculate an average.


      We can do this very easily, for simplicity, the price of each food category is $1. Therefore, our average price is:

            $1 * num categories.

       If the food prices were different, it would be:

           sum(i,n) = price(i) / n

       From here, we could calculate the number of repeat sales, by looking at the average number of times a particular user

       will buy things within a month.

       To evaluate the life time value of a particular kind of user, let us calculate the average number of times a user

       from  a particular social network buys per month.

       To calculate retention time, we calculate the average number of months a user will buy a meal over the course of a year.





