import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
sns.set_theme(style="whitegrid")

# Load the diamonds dataset
diamonds = sns.load_dataset("diamonds")
a = pd.DataFrame(diamonds).head()

# Plot the distribution of clarity ratings, conditional on carat
g = sns.displot(
    data=diamonds,
    x="carat", hue="cut",
    kind="kde", height=6,
    multiple="fill", clip=(0, None),
    palette="ch:rot=-.25,hue=1,light=.75",
)
print(a)
plt.show()