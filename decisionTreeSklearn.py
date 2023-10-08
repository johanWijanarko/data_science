import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz
# Provide the directory path
directory_path = r'D:\python'

# Provide the file name separately
file_name = 'iris.csv'
# Combine the directory path and file name to create the full file path
file_path = os.path.join(directory_path, file_name)

# Read the CSV file from the specified path with a specific encoding (e.g., 'latin1')
iris = pd.read_csv(file_path, encoding='latin1')

iris.info()

iris.head()

iris.drop('Id',axis=1,inplace=True)

# memisahkan atribut dan label
X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm' ]]
y = iris['Species']

# Membagi dataset menjadi data latih & data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=123)

tree_model = DecisionTreeClassifier() 
 
# melakukan pelatihan model terhadap data
tree_model = tree_model.fit(X_train, y_train)

# Evaluasi Model
y_pred = tree_model.predict(X_test)

acc_secore = round(accuracy_score(y_pred, y_test), 3)
print('Accuracy: ', acc_secore)

# prediksi model dengan tree_model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
print(tree_model.predict([[6.2, 3.4, 5.4, 2.3]])[0])

export_graphviz(
    tree_model,
    out_file = "iris_tree.dot",
    feature_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
    class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica' ],
    rounded= True,
    filled =True
)

# Convert DOT file to PNG
graph = graphviz.Source.from_file("iris_tree.dot", format="png")
graph.render(filename='iris_tree', view=False)

# Display the PNG image
Image(filename='iris_tree.png')