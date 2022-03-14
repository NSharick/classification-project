# Classifcation Project

### Project Goals:
- Goal 1: find drivers of churn for Telco customers

- Goal 2: build a machine learning model that accurately predicts customer churn

### Project Description:

- The project will include data acquisition, data cleaning / wrangling, data exploration, machine learning modeling for predicting customer churn, and predictions of customer churn based on the current telco dataset

- The project wil conclude with a final report that summarizes the project's findings and includes the code necessary to replicate the findings and a .csv file with predictions of churn based on the best performing model

### Initial Questions:

- Is a customer's chosen payment method related to customer churn?

- Is a customer's internet service type related to customer churn?

- Is a customer's participation in our support and backup programs related to customer churn?

- Is a customer's participation in our security and protection programs related to customer churn?

### Data Dictionary:

| Variable | Meaning |
|----------|---------|
| Churn    | a variable representing if a customer has left the company with a '1' representing they have left and a '0' representing they have not left|
|Payment Type | a variable representing what payment method a customer has selected (mailed check, electronic check, automatic bank transfer, or automatic credit card payment)|
|Internet Service Type | a variable representing what type of internet service the customer has chosen (fiber optic internet, dsl internet, or no internet)|
|Tech Support| a variable representing if the customer has signed up for our internet technical support program (yes, no, or no internet service)|
|Online Backup| a variable representing if the customer has our online cloud back up services as part of their plan (yes, no, or no internet service)|
|Online Security | a variable representing is the customer has purchased our internet security softeware as part of their plan (yes, no, or no internet service)|
|Device Protection| a variable representing if the customer has purchased insurance on their device through our company (yes, no, or no internet service)|

### Project Planning:

- First, write a function to pull the correct dataset from the database and save it as a csv in the local directory.

- Save the data acquision function in a seperate acquire.py file for future use

- Then, write a function that prepares the data by dealing with missing values, removing unneeded columns, and encoding categorical variables as needed for use in machine learning models

- The data preparation function should also split the dataset into train, validate, and test sets for modeling

- Save the data preparation function in a acquire.py file for later use

- Document four specific questions that will be asked of the data to guide the data exploration

- Explore the data by visualizing key features related to the questions and how they relate to customer churn

- Continue to explore the data by running statistical tests to verify statistical significance of the relationships between the variables

- Document initial takeaways from the data exploration

- Develop initial classification machine learning models using the features identified in the exploration phase

- Refine those models using the train dataset by adjusting feature input and hyperparameter values

- Document the models performance on the train dataset

- Choose the three best performing models to validate using the validate dataset

- Document the performance of the models on the validate dataset

- Choose the model that performed the best and best fit the needs of the buisness question and test it using the test dataset

- Document key findings, recomendations, and next steps

### How to Reproduce this Project and Findings:

To reproduce my findings on this project you will need:

- An env file with you own credentials (hostname, username, password) to access the database and pull the telco dataset

- The acquire.py file in this repository to pull the correct data from the database

- The prepare.py file in this repository to clean and split the dataset

- The jupyter notebook in this repository named "final_report_classification_project" which contains the code used to produce the project including the random_state identifiers to make sure and randomization of the data is consistent.

- Libraries used are numpy, pandas, seaborn, sklearn, and matplotlib. All imports are included at the top of the notebook.

### Key Findings:

- Customer Payment type:
    - Customers with the electronic check payment method had a higher churn rate than those with other payment methods and a higher churn rate than the overall customer churn rate.
        
    - Statistical testing showed that customer payment type is not independent of customer churn rate
    
- Internet Service Type:
    - Customers with fiber optic internet service had a higher curn rate than those with other internet service types and a higher churn rate than the overall customer churn rate
    
    - Statistical testing showed that customer internet service type is not independent of customer churn rate
    
- Participation in Support and Backup Programs:
    - Customers who do not participate in our tech support and/or our online backup programs had a higher churn rate than those that did participate and a higher churn rate than the overall customer churn rate
    
    - Statistical testing showed that customer participation in our support and backup programs is not independent of customer churn rate
    
- Participation in Security and Protection Programs:
    - Customers who do not participate in our online security and/or our device protection programs had a higher churn rate than those that did participate and a higher churn rate than the overall customer churn rate
    
    - Statistical testing showed that customer participation in our security and protection programs is not independent of customer churn rate
    
- Predictive Modeling (machine learning):
    - The best performing model was a K-Nearest Neighbors model with a n-neighbors value of 5
    
    - The final test of this model on the 'test' dataset produced an accuracy score of .76 which is 3% above baseline values and a recall score of .53 which was notably higher than the recall value of the other models in the validate stage

### Reccomendations:

- For churn rate related to customer payment type I reccomend incentivizing customers to switch to one of our two automatic payment methods

- For churn rate related to internet service type I recommend first collecting more information on customer opinion of our fiber optic internet service. Since this is a better quality service than the dsl it is suprising that customers with this type of service have a significantly higher churn rate. There may also be a connection between fiber optic service issues and customers not participating in tech support to get things fixed.

- For particiaption in our support/backup and our security//protection programs I reccomend we focus on marketing targeted at increased customer participation and engagement


### Next Steps:

- Since our highest performing model had an accuracy score only 3% higher than baseline the focus of further work would be on refining the model to increase predictive accuracy

- To do this:
    - I would use the data/information produced from the above recomended actions to bolster our understanding of drivers of customer churn and to refine our machine learning models to better predict customer churn

    - I would further investigate features and feature engineering that could help increase our model's predictive accuracy

    - I would further investigate the interrelationship of customer features could produce additional drivers of customer churn and actionable items to reduce that churn


