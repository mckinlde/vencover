# looks like chatGPT's zeroshot is a math-based solution, and IMO misses 'the bitter lesson'

# oh well, here's a command line output anyways:
'''
douglasmckinley@Douglass-MacBook-Pro vencover % /Users/douglasmckinley/VSCodeProjects/vencover/.venv/bin/python /Users/douglasmckinl
ey/VSCodeProjects/vencover/carinsurance/ci-model-gpt.py
     Customer ID  Premium Eligibility
0              1     1400    Eligible
1              2      500    Eligible
2              3     1450    Eligible
3              4      100    Eligible
4              5      750    Eligible
..           ...      ...         ...
495          496      400    Eligible
496          497     1300    Eligible
497          498      900    Eligible
498          499     1100    Eligible
499          500     1500    Eligible

[500 rows x 3 columns]
douglasmckinley@Douglass-MacBook-Pro vencover % 
'''

import pandas as pd

def calculate_premium(row):
    base_premium = 500  # Base premium amount
    
    # Age-based adjustments
    if row['Age'] < 25:
        base_premium += 200
    elif row['Age'] > 50:
        base_premium -= 100

    # Employment stability factor
    if row['Employment (Years)'] < 3:
        base_premium += 150
    elif row['Employment (Years)'] > 20:
        base_premium -= 50
    
    # Accident history
    if row['Accidents (Last 5 Years)'] > 0:
        base_premium += row['Accidents (Last 5 Years)'] * 250

    # Vehicle age impact
    if row['Vehicle Age (Years)'] > 10:
        base_premium += 150
    elif row['Vehicle Age (Years)'] < 3:
        base_premium -= 50
    
    # Vehicle type impact
    if row['Vehicle Type'] == 'Sports Car':
        base_premium += 300
    elif row['Vehicle Type'] == 'SUV':
        base_premium += 100

    # ICE vs EV
    if row['ICE or EV'] == 'ICE':
        base_premium += 100
    else:
        base_premium -= 50
    
    # Location-based adjustments
    if row['Location'] == 'Urban':
        base_premium += 200
    elif row['Location'] == 'Rural':
        base_premium -= 100

    # Annual mileage factor
    if row['Annual Mileage'] > 15000:
        base_premium += 200
    elif row['Annual Mileage'] < 7000:
        base_premium -= 100

    return base_premium

def determine_policy_eligibility(row):
    if row['Accidents (Last 5 Years)'] > 2 or row['Age'] < 18:
        return 'Not Eligible'
    return 'Eligible'

# Read sample data
data = pd.read_csv('carinsurance/Untitled spreadsheet - data inputs.csv')

data['Premium'] = data.apply(calculate_premium, axis=1)
data['Eligibility'] = data.apply(determine_policy_eligibility, axis=1)

# Output results
data.to_csv('insurance_premium_output.csv', index=False)
print(data[['Customer ID', 'Premium', 'Eligibility']])
