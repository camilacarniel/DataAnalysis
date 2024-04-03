import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv("OlympicData/dataset_olympics.csv", usecols=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])

#Show only Brazilian athletes
brazilian_athletes = data[data['Team'] == 'Brazil']

# Calculate statistics for age
age_stats = brazilian_athletes.groupby('Sex')['Age'].agg(['mean', 'median', 'var', 'std']).reset_index()
# Coefficient of variation 
mean_age_female = age_stats.loc[age_stats['Sex'] == 'F', 'mean'].values[0]
mean_age_male = age_stats.loc[age_stats['Sex'] == 'M', 'mean'].values[0]
std_female = age_stats.loc[age_stats['Sex'] == 'F', 'std'].values[0]
cv_female = std_female / mean_age_female
std_male = age_stats.loc[age_stats['Sex'] == 'M', 'std'].values[0]
cv_male = std_male / mean_age_male
# Quartiles
quartiles = brazilian_athletes['Age'].quantile([0.25, 0.5, 0.75])
quartile_values = quartiles.tolist() #prevent it from printing data types as well

# Print those brazilian statistics data
print(f"\nMean Female Age: {mean_age_female:.2f}\n")
print(f"\nMean Male Age: {mean_age_male:.2f}\n")
print(f"\nStandard Deviation Female: {std_female:.2f}\n")
print(f"\nStandard Deviation Male: {std_male:.2f}\n")
print(f"\nCoefficient of Variation (Female): {cv_female:.2f}\n")
print(f"\nCoefficient of Variation (Male): {cv_male:.2f}\n")
print(f"\nQuartiles: {quartiles}\n")

# Plot the data together!!!
fig, axes = plt.subplots(4, 1, figsize=(5, 20), gridspec_kw={'hspace': 0.5, 'height_ratios': [1, 1, 2, 1]})
custom_palette = ['yellow', 'green']
sns.set_palette(custom_palette)

#01.Histogram
sns.histplot(brazilian_athletes['Age'], bins=20, kde=True, ax=axes[0])
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Distribution of Age for Brazilian Athletes')

#02.Box plot
sns.boxplot(x='Age', y='Sex', data=brazilian_athletes, ax=axes[1])
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Sex')
axes[1].set_title('Distribution of Age for Brazilian Athletes by Sex')

#03.Perform linear regression for each sex
age_by_year_sex = brazilian_athletes.groupby(['Year', 'Sex'])['Age'].mean().reset_index()
regression_lines = {}
for sex in age_by_year_sex['Sex'].unique():
    subset = age_by_year_sex[age_by_year_sex['Sex'] == sex]
    slope, intercept, _, _, _ = linregress(subset['Year'], subset['Age'])
    regression_lines[sex] = (slope, intercept)

sns.lineplot(x='Year', y='Age', hue='Sex', data=age_by_year_sex, ax=axes[2])
for sex, (slope, intercept) in regression_lines.items():
    if sex == 'F':
        color = 'lightblue'  # Light blue for female
    else:
        color = 'blue'  # Blue for male
    axes[2].plot(age_by_year_sex['Year'], slope * age_by_year_sex['Year'] + intercept, label=f'{sex} Regression', color=color)
    axes[2].annotate(f'y = {slope:.2f}x + {intercept:.2f}', xy=(0.6, 0.1 - list(regression_lines.keys()).index(sex)*0.05), xycoords='axes fraction', color='black')
axes[2].set_xlabel('Year')
axes[2].set_ylabel('Mean Age')
axes[2].set_title('Mean Age of Brazilian Athletes by Year and Sex')
axes[2].legend(title='Sex', loc='upper left')
axes[2].grid(True)

#04.Bar plot
total_athletes = brazilian_athletes.groupby('Sex')['ID'].nunique().reset_index()
total_athletes.rename(columns={'ID': 'Total Athletes'}, inplace=True)
medal_athletes = brazilian_athletes[brazilian_athletes['Medal'].notnull()].groupby('Sex')['ID'].nunique().reset_index()
medal_athletes.rename(columns={'ID': 'Medal Athletes'}, inplace=True)
merged_data = pd.merge(total_athletes, medal_athletes, on='Sex')
sns.barplot(x='Sex', y='value', hue='variable', data=pd.melt(merged_data, id_vars=['Sex'], value_vars=['Total Athletes', 'Medal Athletes']), ax=axes[3])
axes[3].set_xlabel('Sex')
axes[3].set_ylabel('Number of Athletes')
axes[3].set_title('Total Athletes x Medal Athletes x Sex')
axes[3].legend(title=None, loc='upper right')

plt.tight_layout()
plt.show()
