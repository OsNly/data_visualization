import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Set style
sns.set(style="whitegrid")

# -------- 1. Bar Chart: Total Value per Category --------
category_totals = df.groupby("Category")["Value"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=category_totals.values, y=category_totals.index, palette="Blues_d")
plt.title("Total Value by Category")
plt.xlabel("Value")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("bar_chart_category.png")
plt.show()

# -------- 2. Grouped Bar Chart: Subcategories per Category --------
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Category", y="Value", hue="Subcategory", palette="tab20")
plt.title("Subcategory Values by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grouped_bar_chart.png")
plt.show()

# -------- 3. Pie Chart: Share by Category --------
plt.figure(figsize=(8, 8))
plt.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Category Share (Pie Chart)")
plt.tight_layout()
plt.savefig("pie_chart_category.png")
plt.show()

#----End Of Cell----

