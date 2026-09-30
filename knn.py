#KNN classification using iris dataset
from sklearn. datasets import load_iris
from sklearn .model_selection import train_test_split
from sklearn . preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score
#
# step 1:load iris dataset
#
iris_data = load_iris()
x=iris_data.data
y=iris_data.target
print("dataset shape:",x.shape)
print("number of samples:",len(x))
print("number of features:",x.shape[1])
print("target classes:",iris_data .target_names)
#
#step 2: split dataset
#
x_train,x_test,y_train,y_test=train_test_split(x,y,stratify=y)
print("\n dataset eplitting")
print("     ")
print("training samples:",len(x_train))
print("testing samples:",len(x_test))
#
#step 3:feature sealing
#

scales = StandardScaler()
x_train=Scaler_file.transform(x_train)
x_test=scaler:transform(x_test)

#
#step 4:create KNN model
#
KNN=KNeighborsClassifier(n_neighbors=5)

#
#step 5:train the model
#
KNN.fit(x_train,y_train)

#
#step 6:malee predictions
#

x_pred.KNN predict(x_test)

#
#step 7:calculate Evaluation
#
acccuracy=accuracy_score(y_test,y_pred)
em:confusion_matrix(y_test,y_pred)
    precision:precision.score(y_test,y_pred
    )
