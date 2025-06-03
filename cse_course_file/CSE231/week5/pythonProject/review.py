import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Since the provided data is in an image, I cannot directly extract it. However, for demonstration purposes,
# I will recreate the data manually based on the image provided and then perform the calculations and plotting.
# Here is the manual recreation of the data:

# Recreating the data from the image
data = {
    "concentration": [0.000007992, 0.000005984, 0.000003996, 0.000001998],
    "absorbance": [0.915, 0.699, 0.461, 0.227],
    "concentration2": [0.00003248, 0.00002436, 0.00001624, 0.00000812],
    "absorbance2": [0.616, 0.353, 0.287, 0.147]
}

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Perform linear regression for both sets of concentration and absorbance
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['concentration'], df['absorbance'])
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df['concentration2'], df['absorbance2'])

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the first set of data
ax.scatter(df['concentration'], df['absorbance'], color='blue', label='Data set 1')
# Plot the regression line for the first set
ax.plot(df['concentration'], intercept1 + slope1 * df['concentration'], 'b--', label=f'Line 1: y={slope1:.2e}x+{intercept1:.2e} (R={r_value1:.2f})')

# Plot the second set of data
ax.scatter(df['concentration2'], df['absorbance2'], color='red', label='Data set 2')
# Plot the regression line for the second set
ax.plot(df['concentration2'], intercept2 + slope2 * df['concentration2'], 'r--', label=f'Line 2: y={slope2:.2e}x+{intercept2:.2e} (R={r_value2:.2f})')

# Set labels and title
ax.set_xlabel('Concentration')
ax.set_ylabel('Absorbance')
ax.set_title('Absorbance vs. Concentration')

# Add legend
ax.legend()

# Show the plot
plt.show()

# The R values and line equations are as follows:
# For the first data set: R = 0.9997, Line equation: y = 1.1527e+05 x + 2.3052e-05
# For the second data set: R = 0.9673, Line equation: y = 1.8140e+04 x - 0.0175
