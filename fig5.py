import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme()

# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
a = pd.DataFrame(flights_long).head()
flights = flights_long.pivot("month", "year", "passengers")
print(a)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()