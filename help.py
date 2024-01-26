import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('ind_nifty50list.csv')

# Specify the file name where you want to save the output
output_file = 'output.txt'

# Open the file in write mode
with open(output_file, 'w') as file:
    # Iterate through the 'Company Name' column and write to the file
    for company_name in df['Company Name']:
        # Write the lowercase version of the company name
        file.write(f"    '{company_name.lower()}': [\n")
        file.write('        { id: 101, name: \'Product A\', price: 50 },\n')
        file.write('        { id: 102, name: \'Product B\', price: 75 },\n')
        file.write('    ],\n')

print(f"Output written to {output_file}")
