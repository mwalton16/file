### Imports
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn

### Data
animal_classes = pd.read_csv('animal_classes.csv')
animals_test = pd.read_csv('animals_test.csv')
animals_train = pd.read_csv('animals_train.csv')

### Creating the Prediction

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X=animals_train.iloc[:,0:16],y=animals_train["class_number"])

x_test = animals_test.iloc[:,1:]
predicted = knn.predict(X=x_test)


animal_name_class = pd.DataFrame(animal_classes[['Class_Number','Animal_Names']])
expected_names = animals_test.iloc[:,0]
animal_name = []
for i,j in zip(animal_name_class['Class_Number'],animal_name_class['Animal_Names']):
    names = j.split(', ')
    temp_dict = {}
    temp_dict[i] = names
    animal_name.append(temp_dict)

### Comparing Expected Results and Predictions
print("Test:")

expected = []
expected_class = []
for name in expected_names:
    b = 0
    for row in animal_name:
        a = list(row.values())
        if name in a[0]:
            b += 1
#            print(b)
            expected.append(b)
        else:
            b += 1

c = animal_classes[['Class_Number','Class_Type']]
for row in predicted:
    print()
print(c)





