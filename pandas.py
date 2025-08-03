import pandas as pd
import numpy as np

employees = {'ID': ('1', '2', '3', '4'), 'Name': 
('Pankaj', 'Meghna', 'David', 'Lisa'),
'Role': ('CEO'), 'Salary': ('100', '200')}

df = pd.DataFrame(employees)
print("dataframe of employees")
print(df.info())
