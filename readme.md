# Classifcation Project

### Project Goals:
- Goal 1: find drivers of churn for Telco customers

- Goal 2: build a machine learning model that accurately predicts customer churn

### Project Description:

- The project will include data acquisition, data cleaning / wrangling, data exploration, machine learning modeling for predicting customer churn, and predictions of customer churn based on the current telco dataset

- The project wil conclude with a final report that summarizes the project's findings and includes the code necessary to replicate the findings and a .csv file with predictions of churn based on the best performing model

- 

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

- 

### How to Reproduce this Project and Findings:

To reproduce my findings on this project you will need:

- An env file with you own credentials (hostname, username, password) to access the database and pull the telco dataset

- The acquire.py file in this repository to pull the correct data from the database

- The prepare.py file in this repository to clean and split the dataset

- The jupyter notebook in this repository named "final_report_classification_project" which contains the code used to produce the project including the random_state identifiers to make sure and randomization of the data is consistent.

- Libraries used are numpy, pandas, seaborn, sklearn, and matplotlib. All imports are included at the top of the notebook.

### Key Findings, Reccomendations, and Takeaways:

- 



