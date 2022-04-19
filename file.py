### Imports
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

### Data
animal_classes = pd.read_csv('animal_classes.csv')
animals_test = pd.read_csv('animals_test.csv')
animals_train = pd.read_csv('animals_train.csv')

### Creating the Prediction


knn = KNeighborsClassifier()
knn.fit(X=animals_train.iloc[:,0:16],y=animals_train["class_number"])

#Note:
#x_train = animals_train.iloc[:,0:16]
#y_train = animals_train['class_number']

x_test = animals_test.iloc[:,1:]
y_test = knn.predict(X=x_test)

# We now have our predicted values (y_test). We then convert them into class types.
animal_classes = animal_classes[['Class_Number','Class_Type']]
class_type_list = []
for item in y_test:
    item_1 = item - 1
    class_type_list.append(animal_classes.loc[item_1]['Class_Type'])
final_data_dict = {}
for animal,type in zip(animals_test['animal_name'],class_type_list):
    print(animal)
    print(type)
    final_data_dict[animal] = type

solution = pd.DataFrame(data={'animal_name':final_data_dict.keys(),
'prediction':final_data_dict.values()})
print(solution)
solution.to_csv('predictions_solution.csv')
