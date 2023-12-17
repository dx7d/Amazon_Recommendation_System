# Amazon_Recommendation_System

# Overview
This project implements a collaborative filtering-based recommendation model for an e-commerce platform, specifically tailored to Amazon's diverse product categories. The recommendation engine utilizes Singular Value Decomposition (SVD) and correlation analysis to provide personalized product recommendations to users.

# Code Explanation
The code is structured to handle multiple datasets corresponding to different product categories, such as Electronics, Shoes, Watches, Cell Phones & Accessories, and Sports & Outdoors. The primary steps include data parsing, processing, combining datasets, user subset selection, and model-based collaborative filtering using SVD.

# Key Components:
## Data Parsing Functions:

Utilizes generators and functions (parse and getDF) to read and process gzip-compressed datasets.
## Data Processing:

Applies data cleaning, handling duplicates, and converting data types for different product categories.
## Combining Datasets:

Merges processed datasets using outer joins to create a comprehensive dataset.
## Subset Selection:

Filters users who have given 40 or more ratings, focusing on engaged users.
## Model-Based Collaborative Filtering (SVD):

Performs SVD on the user-item interaction matrix to identify latent factors influencing user preferences.
## Recommendation Function:

Defines a function (result) to provide recommendations based on a given product ID, leveraging correlation analysis.
## Saving Model Files:

Includes a commented-out section for saving the recommendation function using the joblib library.

# Streamlit:
Purpose: Designed for creating interactive data science and machine learning web applications.
Ease of Use: Simple and quick setup with minimal code required.
Features: Ideal for data dashboards, visualizations, and basic user interfaces.
Limitations: May not be suitable for complex web applications with advanced features.


# reccomend.py Explanation
The reccomend.py script performs collaborative filtering-based recommendation using SVD and correlation analysis. It includes steps such as importing libraries, loading data, creating a ratings matrix, applying SVD decomposition, calculating a correlation matrix, and defining a recommendation function (result).

## Model-Based Similarity
Model-Based Collaborative Filtering Steps:
Create a Ratings Matrix:

Form a matrix where users and products are represented, with ratings as matrix entries.
Apply Truncated SVD:

Use Truncated SVD to simplify the matrix and identify underlying factors influencing user preferences.
Calculate Correlation:

Measure similarities between users and products based on their preferences using correlation coefficients.
# Generate Recommendations:

Recommend products to users based on the preferences of similar users, leveraging calculated correlations.
# Conclusion
This recommendation model provides a framework for building personalized recommendations on Amazon-like platforms, utilizing collaborative filtering techniques. The choice between Streamlit and Flask depends on the project's complexity, with Streamlit being suitable for rapid data-focused web apps and Flask offering more control for comprehensive web applications.
