# Loan Eligibility Prediction

Predicting loan eligibility is a crucial task for financial institutions. Our model uses logistic regression to predict the eligibility of a loan applicant based on their credit history and other information.

## Features
- Predicts loan eligibility using logistic regression
- Accepts data on applicant's credit history and other information
- Outputs a probability of loan eligibility

## Usage
1. Clone the repository and install the necessary dependencies

### `git clone https://github.com/steve-cse/Loan-Eligibility-LR.git`
### `git clone pip install -r requirements.txt`


2. Run the model on your data


## Data
The model accepts data in a CSV file with the following columns:
- `income`: Applicant's annual income
- `age`: Applicant's age
- `loan_amount`: Loan amount applied for
- `credit_score`: Applicant's credit score
- `property_type`: Type of property being purchased (e.g. house, apartment, etc.)

## Results
The output of the model is a probability of loan eligibility, with a probability greater than 0.5 indicating that the applicant is likely to be approved for the loan, and a probability less than 0.5 indicating that the applicant is likely to be denied the loan.

## Contribution
Contribution are always welcome. Feel free to open an issue or create a pull request if you want to improve the model or add new features.

## License
This project is licensed under the terms of the MIT license.
