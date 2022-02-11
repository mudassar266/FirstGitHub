# steps for visualiztion
## step 1 import liberaries 
import seaborn as sns
import matplotlib.pyplot as plt 

## step 2 set a theme 
sns.set_theme(style="ticks", color_codes=True)

## step 3 import data set (you can also import your own data set too)
kashti = sns.load_dataset("titanic")
print(kashti)

# ## step 4, plot basic graph (count plot for single variable)
# p = sns.countplot(x="sex", data=kashti)
# plt.show()

## step 5, plot basic graph (count plot for 2 variable)
p = sns.countplot(x="sex", data=kashti, hue="class")
plt.show()

## step 6, plot basic graph (count plot for 2 variable) with title 
p = sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("Count plot for 2 variables")
plt.show()