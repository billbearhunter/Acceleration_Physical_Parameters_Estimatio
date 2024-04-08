import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the DataFrame from the CSV file
df = pd.read_csv('x_diff_data.csv', index_col=0)

# Define the parameters to plot
frames = range(1, 9)
x_diff_columns = [f'x_diff_{i:02}' for i in frames]

plt.figure(figsize=(10, 6))

for index, row in df.iterrows():
    plt.plot(frames, [row[col] for col in x_diff_columns], marker='o')

plt.xlabel('Frame')
plt.ylabel('x_diff value')
plt.title('x_diff values across different frames')
plt.grid(True)

# Add second plot
plt.figure(figsize=(10, 6))

# x_diff with previous frame
for index, row in df.iterrows():
        differences = [row[x_diff_columns[0]]]  
        for i in range(1, len(x_diff_columns)):
            difference = row[x_diff_columns[i]] - row[x_diff_columns[i - 1]]
            differences.append(difference) 
        
        plt.plot(frames, differences, marker='o')

plt.xlabel('Frame')
plt.ylabel('x_diff with previous frame')
plt.title('x_diff values with previous frame')
plt.grid(True)

plt.show()
