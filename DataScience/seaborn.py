# Seaborn is a statistical data visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive statistical graphics.
import seaborn as sns
import matplotlib.pyplot as plt

#load sample dataset
tips = sns.load_dataset("tips")

#creating a scatter plot with regression line
sns.scatterplot(data=tips,x="total_bill",y="tip",hue="day")
sns.regplot(data=tips,x="total_bill",y="tip",scatter = False)

plt.title("Scatter Plot with Regression Line")
plt.show()