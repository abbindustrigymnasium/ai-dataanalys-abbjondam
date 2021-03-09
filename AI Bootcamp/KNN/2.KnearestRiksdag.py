import numpy as np

from sklearn import preprocessing, neighbors, model_selection
import pandas as pd

df = pd.read_csv("votering.csv")
df.drop(["punkt"], 1, inplace=True)

df = df[["rost", "parti", "fodd", "kon", "intressent_id"]]

input_labels = ["kvinna", "man"]  # kvinna ---> 0  man ---> 1
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)
df["kon"] = encoder.transform(df["kon"])

input_labels = [
    "C",
    "KD",
    "M",
    "L",
    "MP",
    "V",
    "SD",
    "S",
    "-",
]  # - ---> 0 C ---> 1 KD ---> 2 L ---> 3 M ---> 4 MP ---> 5 S ---> 6 SD ---> 7 V ---> 8
encoder.fit(input_labels)
df["parti"] = encoder.transform(df["parti"])


input_labels = [
    "Ja",
    "Nej",
    "Frånvarande",
    "Avstår",
]  # Avstår ---> 0 Frånvarande ---> 1 Ja ---> 2 Nej ---> 3
encoder.fit(input_labels)
df["rost"] = encoder.transform(df["rost"])


for i, item in enumerate(encoder.classes_):
    print(item, "--->", i)

df.replace("?", "-9999", inplace=True)

print(df.head(4))

X = np.array(df.drop(["rost"], 1))
y = np.array(df["rost"])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
X_train = X_train.reshape(len(X_train), -1)
y_train = y_train.reshape(len(y_train), -1)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print("Accuracy is " + str(accuracy))
print(X_train[0])
# "Mikael Damsgaard","66036027425","M","Västmanlands län","Ja","sakfrågan","74","man","1976","2019-11-28"
# "Jonas Sjöstedt","383111552218","V","Västerbottens län","Nej","sakfrågan","138","man","1964","2019-11-28"
example_measure = np.array([[4, 1976, 1, 66036027425], [8, 1964, 1, 383111552218]])
example_measure = example_measure.reshape(len(example_measure), -1)
prediction = clf.predict(example_measure)
print(prediction)

decoded_list = encoder.inverse_transform(prediction)
print("Decoded", list(decoded_list))
