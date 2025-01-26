# What I want is a table of claims history for all of our customers

# I'll start with our standard data inputs:

import pandas as pd
import random
from datetime import datetime, timedelta


# Function to generate a random date within a given range
def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Define the date range (e.g., from 2015-01-01 to 2023-12-31)
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 12, 31)


# Read sample data
data = pd.read_csv('carinsurance/Untitled spreadsheet - data inputs.csv')

# Add three new columns with random values
# claim-cost,claim-date,policy-age
# What I'm thinking here is a table of moments in time where a claim occurred, what did that claim cost, when did that claim occur, and how many months into the policy was that driver when the claim was made?
data['claim-cost'] = [random.randint(0, 1000000) for _ in range(len(data))]
data['claim-date'] = [random_date(start_date, end_date).strftime('%Y-%m-%d') for _ in range(len(data))]
data['policy-age'] = [random.randint(1, 12) for _ in range(len(data))]


# Save the updated data to a new file
updated_file_path = 'data_inputs_updated.csv'
data.to_csv(updated_file_path, index=False)

print("Updated file saved as:", updated_file_path)

# Output results
data.to_csv('claims.csv', index=False)
print(data[['Customer ID', 'Age', 'claim-cost', 'claim-date', 'policy-age']])