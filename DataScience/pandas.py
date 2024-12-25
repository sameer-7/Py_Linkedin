# Pandas is a powerful data manipulation and analysis library. It provides data structures like Series and DataFrame, which are essential for handling structured data.
import pandas as pd

#create a dataframe
data = {
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25,30,35],
    'City' : ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame\n",df)

#Basic operation
print("Mean Age: ", df['Age'].mean())

#Filtering data
filtered_df = df[df['Age']>30]
print("Filtered DataFrame:\n",filtered_df)