import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("sample_data.csv")
sns.set(style="whitegrid")

# Prepare data
subcategory_totals = df.groupby("Subcategory")["Value"].sum().sort_values()
category_totals = df.groupby("Category")["Value"].sum().sort_values()

# Create figure and axes with custom layout
fig, axes = plt.subplots(2, 2, figsize=(18, 12), gridspec_kw={'height_ratios': [1.2, 1]})

# -------- Top Left: Horizontal Bar Chart --------
sns.barplot(x=subcategory_totals.values, y=subcategory_totals.index, palette="viridis", ax=axes[0, 0])
axes[0, 0].set_title("Total Value by Subcategory", fontsize=14)
axes[0, 0].set_xlabel("Total Value", fontsize=12)
axes[0, 0].set_ylabel("Subcategory", fontsize=12)

# -------- Top Right: Boxplot --------
sns.boxplot(data=df, x="Category", y="Value", palette="Set3", ax=axes[0, 1])
axes[0, 1].set_title("Value Distribution by Category", fontsize=14)
axes[0, 1].set_xlabel("Category", fontsize=12)
axes[0, 1].set_ylabel("Value", fontsize=12)
axes[0, 1].tick_params(axis='x', rotation=30)

# -------- Bottom Left: Pie Chart --------
axes[1, 0].pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%',
               startangle=140, colors=sns.color_palette("pastel"), textprops={'fontsize': 10})
axes[1, 0].set_title("Category Share (Pie Chart)", fontsize=14)

# -------- Bottom Right: Strip Plot --------
sns.stripplot(data=df, x="Category", y="Value", hue="Subcategory", dodge=True, jitter=True,
              palette="Set2", ax=axes[1, 1])
axes[1, 1].set_title("Value Spread by Category & Subcategory", fontsize=14)
axes[1, 1].set_xlabel("Category", fontsize=12)
axes[1, 1].set_ylabel("Value", fontsize=12)
axes[1, 1].tick_params(axis='x', rotation=30)

# Move legend outside the strip plot
axes[1, 1].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small', title='Subcategory')

# Adjust layout
plt.tight_layout(rect=[0, 0, 0.95, 1])  # Leave space for legend on the right
plt.savefig("clean_dashboard.png", dpi=300)
plt.show()

