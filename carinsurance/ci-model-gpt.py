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
data = pd.read_csv('data_inputs.csv')

data['Premium'] = data.apply(calculate_premium, axis=1)
data['Eligibility'] = data.apply(determine_policy_eligibility, axis=1)

# Output results
data.to_csv('insurance_premium_output.csv', index=False)
print(data[['Customer ID', 'Premium', 'Eligibility']])
