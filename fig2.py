import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="whitegrid")

penguins = sns.load_dataset("penguins")
a = pd.DataFrame(penguins).head()
# Draw a nested barplot by species and sex
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
print(a)
g.despine(left=True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")
plt.show()