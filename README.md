# Trending_Youtube_Videos Project
#### Project Summary
YouTube (the world-famous video sharing website) maintains a List of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments And likes). Note that they’re Not the most-viewed videos overall For the calendar year”.
This dataset is a daily record of the top trending YouTube videos. The dataset is public available on https://www.kaggle.com/datasnaek/youtube-new


The project has two parts. The first part is Trending Youtube videos data ETL by Spark and python, leveraging AWS Redshift. The second part is using Keras LSTM to do time series prediction on trending vidoes views(likes, dislikes, comment_counts).


## File Descriptions
There are 3 python files implement the product.

github_youtube_etl.ipynb--Trending Youtube videos data ETL(the first part of the project).

kaggle_lstm-prediction-on-trending-youtube-videos-views.ipynb--Trending predictions by Keras LSTM(the second part of the project).

sql_queries.py--DLL,DML and queries for creating tables and droping tables in AWS Redshift.


