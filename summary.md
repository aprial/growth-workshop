The overall objective of this workshop is to gain an understanding of how to deal with user data and, using their actions on the site, gain better long term value, increase retention, and drive sales.


Using a simulated setting of a pinterest like restaurant website where users can like, share, or buy different kinds of food we will explore a post social campaign and gain an understanding of how different users from different referral sources (social networks) can act



Visualizations - Basic Data Munging


         1. Basic SQL using SQLAlchemy to query data from an sqllite database
         
         2. Visualize different sorts of data using matplotlib with histograms using output from sql
         
         3. See what users tend to do what via ratios of user referral types 
         to counts through graphs - this allows us to discover trends by just looking at 
         the data in a more pleasing way
         
         4. Discuss insights that are supposed to be gained from visualizing the data
         
         5. Go through a few more visualizations comparing 
         different columns of the tables to understand biases 
         and trends in data purely through plotting different points against each other



Numerical insights:

        1. Data Preparation - Using SQL to query our customer database, we'll load the data into a Pandas DataFrame to            do the extensive data transforms to get the data ready to feed into scikit-learn models. Basic Supervised and           Unsupervised Machine Learning techniques will be leveraged to combat the problems of data to turn data in to            actionable insights.
       
        2. Cohort Analysis:
                  
                 - What is cohort analysis and why does it matter?
                  
                 - Regression vs. classification and the trade-offs of each - 
                   making sense of the output of these models and how to interpret them
                  
                  
        Business objectives will also be covered, specifically:
                    
                    profit curves
                    lift curves
                    life-time value (LTV)
                    customer targeting
           
            Some Objectives:
            
            - Calculate churn of likes, shares, and other business metrics vs doing "nothing", 
           
            - Predict who is likely to buy more leading to better data driven desicision making.
              This includes which users to target with an ad campaign, and who are your most profitable
              customer relationships to focus on
       
       3. Leveraging what we know about user tendencies (facebook users tend to like food x) 
          build a mini collaborative filter to demonstrate how to reccomend actions to users,
          which will lead to conversions (likes/shares/buys



Real World DataSet - website traffic logs:

   
      1. More ETL with Pandas (in this case from a CSV)
   
      2. Visualizing the data using matplotlib:
            
            - Cover statistics and inference with data
            
            - Calculate inferential statistics such as average site visit times
            
            - Look at and understand what metrics are good in the data and what the reasoning behind data objectives                  should be given columns present
   
      3. Regression over certain columns to see what can correlate - 
         explain r^2 and also be able to use the features (columns) 
         to predict the probability a user will actually 
         log in in 6 months
