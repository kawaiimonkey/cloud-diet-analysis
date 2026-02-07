import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('All_Diets.csv')

# 2. Data Cleaning: Handling missing values
# Fill missing values in numeric columns with the mean to avoid errors with string columns
numeric_cols = ['Protein(g)', 'Carbs(g)', 'Fat(g)']
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# 3. Calculate average macronutrients for each diet type
avg_macros = df.groupby('Diet_type')[numeric_cols].mean()
print("--- Average Nutrients by Diet Type ---\n", avg_macros)

# 4. Get the top 5 recipes with the highest protein content per diet type
top_5_protein = df.sort_values(['Diet_type', 'Protein(g)'], ascending=[True, False]).groupby('Diet_type').head(5)

# 5. Calculate new metrics: Protein-to-Carbs ratio and Carbs-to-Fat ratio
# Note: Added a tiny constant (1e-5) to prevent DivisionByZero errors
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / (df['Carbs(g)'] + 1e-5)
df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / (df['Fat(g)'] + 1e-5)

# 6. Data Visualization
sns.set_theme(style="whitegrid")

# --- Chart 1: Bar Chart (Average Protein Content) ---
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'], palette='viridis')
plt.title('Average Protein by Diet Type')
plt.xlabel('Diet Type')
plt.ylabel('Average Protein (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('avg_protein_bar.png')
plt.show()

# --- Chart 2: Heatmap (Nutrient Distribution by Diet Type) ---
plt.figure(figsize=(10, 8))
sns.heatmap(avg_macros, annot=True, cmap='YlGnBu', fmt=".1f")
plt.title('Nutrient Distribution Heatmap')
plt.xlabel('Nutrients')
plt.ylabel('Diet Type')
plt.savefig('nutrient_heatmap.png')
plt.show()

# --- Chart 3: Scatter Plot (Top 5 Protein Recipes Distribution) ---
plt.figure(figsize=(12, 7))
sns.scatterplot(data=top_5_protein, x='Cuisine_type', y='Protein(g)', hue='Diet_type', s=100)
plt.title('Top 5 Protein-Rich Recipes by Diet & Cuisine')
plt.xlabel('Cuisine Type')
plt.ylabel('Protein (g)')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Diet Type')
plt.tight_layout()
plt.savefig('top_protein_scatter.png')
plt.show()