# IPL Score Predictor

## Overview
This project aims to predict the total runs a team will score in an innings of an IPL match. 
Using historical ball-by-ball data, we extract relevant features and train an ML model to estimate the final score based on real-time match progress.

## Dataset
The dataset consists data for IPL matches, which is preprocessed to extract ball-by-ball details.

## Project Workflow
### 1. Data Extraction
*Importing match data from YAML format
*Converting it into a structured Pandas DataFrame
*Creating backups at different stages for easy recovery

### 2. Data Cleaning
*Removing unnecessary columns
*Handling missing values
*Dropping redundant columns

### 3. Feature Engineering
We extract the following features to make predictions:
1. Batting & Bowling Team
2. City
3. Current Score
4. Balls Left
5. Wickets Left
6. Current Run Rate (CRR)
7. Runs in Last 5 Overs
8. Total Runs Scored
9. Filtering venues where at least 600 balls have been played to avoid data bias

## Model Development
The cleaned dataset is used to train machine learning models like:

...

## Conclusion
This project provides a structured approach to predicting IPL innings totals using machine learning.
By leveraging historical data and extracting meaningful features, we try to improve the accuracy of score predictions
