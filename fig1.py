# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")
a = pd.DataFrame(tips).head()
# Create a visualization
sns.lmplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker",height = 5
)
print(a)
plt.show()