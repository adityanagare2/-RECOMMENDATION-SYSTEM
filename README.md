# -RECOMMENDATION-SYSTEM
COMPANY: CODTECH IT SOLUTIONS

NAME: Aditya Nagare

INTERN ID: CT12WH88

DOMAIN: Machine Learning

DURATION: 12 weeks

MENTOR: NEELA SANTOSH

## DESCRIPTION OF TASK

## Project Title: Movie Recommendation System Using Collaborative Filtering (SVD)
## Overview
In the world of digital content, recommendation systems play a crucial role in improving user experience. From Netflix suggesting movies, to Amazon recommending products, these intelligent systems help users discover items they’re most likely to enjoy. In this project, we build a Movie Recommendation System using Collaborative Filtering and Matrix Factorization (SVD) — a technique that helps predict how much a user will like a movie based on their past behavior and the behavior of others.

The dataset used is MovieLens 100k, which contains 100,000 ratings from 943 users on 1,682 movies. It is a widely-used benchmark dataset for collaborative filtering research and is pre-built into the Surprise library.
## Tools and Technologies Used
Python: The programming language used for building the model.

scikit-surprise (or just Surprise): A Python library specifically built for building and analyzing recommender systems. It provides tools for matrix factorization, collaborative filtering, and evaluation.

Pandas: For data manipulation and analysis.

Matplotlib: For visualizing the predicted rating distribution.

VS Code (Visual Studio Code): A code editor used for writing and running the Python script.

Jupyter Notebook (optional): Can be used if you prefer an interactive coding environment with visual outputs inline.
## How It Works
This recommendation engine uses Matrix Factorization via SVD (Singular Value Decomposition). Here’s how it works in plain English:

Each user and each movie are represented by a set of latent features (invisible attributes that define their preferences and properties).

The model learns from user ratings to uncover these hidden features.

It then predicts how a specific user would rate a movie they haven’t seen, based on similarities in user preferences and movie characteristics.

## Workflow
Data Loading: The MovieLens dataset is loaded directly from the Surprise library.

Model Selection: We use the SVD algorithm — a form of matrix factorization that performs well in collaborative filtering tasks.

Training: The model is trained on 80% of the dataset (training split).

Testing: The remaining 20% is used to evaluate the model’s prediction accuracy.

Evaluation Metrics:

RMSE (Root Mean Square Error): Measures the difference between predicted and actual ratings.

MAE (Mean Absolute Error): Measures average prediction error.

Recommendations: The model predicts top N movies a user is likely to enjoy.

Visualization: A histogram shows the distribution of predicted ratings across all test samples.

## Implementation Use-Cases
This type of system is extremely practical and can be implemented in real-world scenarios such as:

Streaming platforms (e.g., Netflix, Hulu): To recommend personalized movies and TV shows.

E-commerce websites (e.g., Amazon, Flipkart): To suggest products based on user history.

Online education platforms (e.g., Coursera, Udemy): To recommend courses based on learner preferences.

News portals (e.g., Google News): To personalize news feeds for readers.

Social media platforms (e.g., YouTube, TikTok): To recommend videos that match user interests.

## Benefits of This System
Improves user engagement and satisfaction.

Helps businesses increase conversion rates.

Reduces user churn by offering relevant content.

Continuously improves as more data is collected.


## This project gives you a hands-on understanding of how collaborative filtering and matrix factorization work in real-life recommendation engines. It's a powerful example of how machine learning can personalize digital experiences using nothing more than the preferences of users and items. With a well-tuned model, you can scale this system to millions of users and items, making it a robust tool for any data-driven business.




## OUTPUT:-


![Image](https://github.com/user-attachments/assets/bcc8cf29-1d83-4cfa-bf5c-25224dd08486)

![Image](https://github.com/user-attachments/assets/16be9ebf-2288-4965-bb1b-92bbcbe3b2f5)
