import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
import umassScrape


different_utils = umassScrape.run()
# different_utils = ['Gas', 'Water', 'Electricity', 'Heat', 'Trash Removal',
#                    'Sewer', 'Air Conditioning', 'Internet', 'Cable']
# Load the data
X_full = pd.read_csv('housing_data.csv')

#Ploting Data
sns.set_theme()

features_1 = ['Distant From Campus', 'Bedroom(s)', 'Bathroom(s)', 'Size (square Feet)',
            'MAXIMUM Number of People']
for feature in features_1:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X_full[feature], y=X_full['Price/Bed'])
    plt.title(f'Price/Bed vs {feature}')
    plt.xlabel(feature)
    plt.ylabel('Price/Bed')
plt.show()

for feature in features_1:
    plt.figure(figsize=(10, 6))
    sns.regplot(x=X_full[feature], y=X_full['Price/Bed'])
    plt.title(f'Regression Plot: Price/Bed vs {feature}')
    plt.xlabel(feature)
    plt.ylabel('Price/Bed')
plt.show()

features_2 = ['Distant From Campus', 'Bedroom(s)', 'Bathroom(s)', 'Size (square Feet)',
            'MAXIMUM Number of People', 'Price/Bed']
plt.figure(figsize=(12, 8))
correlation_matrix = X_full[features_2].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(X_full, vars=features_2)
plt.show()

categorical_features = ['Bedroom(s)', 'Bathroom(s)', 'MAXIMUM Number of People']
for feature in categorical_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=X_full[feature], y=X_full['Price/Bed'])
    plt.title(f'Price/Bed vs {feature}')
    plt.xlabel(feature)
    plt.ylabel('Price/Bed')
plt.show()



#Transform the Included Util column
for util in different_utils:
    X_full[util] = 0

for index, row in X_full.iterrows():
    included_util = row['Included Utilities']
    if included_util is np.nan:
        included_util = ""
    included_util.strip()
    included_util = included_util.split(", ")
    for util in included_util[:len(included_util) - 1]:
        X_full.at[index, util] = 1

X_full.drop('Included Utilities', axis=1, inplace = True)

X_full.dropna(axis = 0, subset = ['Price/Bed'], inplace = True)
y = X_full['Price/Bed']

info_cols = ["Link", "Phone Number", "Name", "Address", "Price/Bed"]
X_full.drop(info_cols, axis = 1, inplace = True)

X_train, X_valid, y_train, y_valid = train_test_split(X_full, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)

#Impute Missing Data
this_imputer = SimpleImputer(strategy = 'mean')

imputed_X_train = pd.DataFrame(this_imputer.fit_transform(X_train, y))
imputed_X_valid = pd.DataFrame(this_imputer.transform(X_valid))

imputed_X_train.columns = X_train.columns
imputed_X_valid = X_valid.columns

model = RandomForestRegressor(n_estimators = 200, random_state = 0)
model.fit(X_train, y_train)
pred = model.predict(X_valid)
print(mean_absolute_error(y_valid, pred))

