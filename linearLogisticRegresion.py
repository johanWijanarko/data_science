import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def plot_roc_curve(file_path, predictions=['Age', 'EstimatedSalary', 'Gender_Female', 'Gender_Male'], test_size=0.2, random_state=1):
    # Load the dataset
    df = pd.read_csv(file_path, encoding='latin1')

    # Drop unnecessary column
    data = df.drop(columns=['User ID'])

    # Perform one-hot encoding
    data = pd.get_dummies(data)

    # Separate features and labels
    X = data[predictions]
    y = data['Purchased']

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)

    # Train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predict probabilities for the positive class
    y_prob = model.predict_proba(X_test)[:, 1]

    # Compute ROC curve and ROC area for each class
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    # Plot ROC curve
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc='lower right')
    plt.show()

    print('AUC-ROC:', roc_auc)

# Example usage
directory_path = r'D:\python'
file_name = 'Social_Network_Ads.csv'
file_path = os.path.join(directory_path, file_name)

plot_roc_curve(file_path)
