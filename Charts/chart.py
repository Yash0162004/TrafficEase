import pandas as pd
import matplotlib.pyplot as plt

# Path to your CSV file
csv_path = "charts/chart.csv"

# Columns to use from the CSV file
columns = ['Static', 'Dynamic']

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path, usecols=columns)

# Plot the DataFrame
df.plot(marker='s', linestyle='-', figsize=(10, 6))

# Set labels and title
plt.xlabel('Simulation Attempts')
plt.ylabel('No. of Vehicles passed per 1 Simulation')
plt.title('Comparison: Current Static System vs Our Dynamic System', fontsize=15)

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()
