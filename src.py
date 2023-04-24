import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

data = pd.read_csv('Book2.csv')
data.head()


count_classes = pd.value_counts(data['Type'],sort = True).sort_index()
count_classes.plot(kind='bar')
plt.title("F")
plt.xlabel("F")
plt.ylabel("F")

from sklearn.preprocessing import StandardScaler

X = data.loc[:, data.columns != 'Type'] 
y = data.loc[:, data.columns == 'Type'] 
number_records_fraud = len(data[data.Type == 1]) 
fraud_indices = np.array(data[data.Type == 1].index) 
normal_indices = data[data.Type == 0].index

random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace = False)
random_normal_indices = np.array(random_normal_indices)
under_sample_indices = np.concatenate([fraud_indices,random_normal_indices]) 
under_sample_data = data.iloc[under_sample_indices,:] 
X_undersample = under_sample_data.loc[:, under_sample_data.columns != 'Type'] 
y_undersample = under_sample_data.loc[:, under_sample_data.columns == 'Type']

print(len(under_sample_data[under_sample_data.Type==0])/len(under_sample_data))
print(len(under_sample_data[under_sample_data.Type==1])/len(under_sample_data))
print(len(under_sample_data))

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=0)
X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_undersample, y_undersample, test_size = 0.3, random_state = 0)
print("")
print("Number transactions train dataset: ", len(X_train_undersample))
print("Number transactions test dataset: ", len(X_test_undersample))
print("Total number of transactions: ", len(X_train_undersample)+len(X_test_undersample))

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, roc_auc_score, roc_curve, recall_score, classification_report

lr = LogisticRegression(C = 0.05, penalty = 'l1',solver='liblinear')
lr.fit(X_train_undersample, y_train_undersample.values.ravel())
y_pred_undersample = lr.predict(X_test_undersample.values)

cnf_matrix = confusion_matrix(y_test_undersample,y_pred_undersample)
print(cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))

lr = LogisticRegression(C = 0.01, penalty = 'l1',solver='liblinear')
lr.fit(X_train,y_train.values.ravel())
y_pred = lr.predict(X_test.values)
print(lr.score(X_test,y_test))

cnf_matrix = confusion_matrix(y_test,y_pred)
print(cnf_matrix[1,1]/(n[1,0]+cnf_matrix[1,1]))


