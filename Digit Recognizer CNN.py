import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.utils import to_categorical



#reading data
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

#print(test_data.head())

x_train = train_data.drop(columns=['label']).values
y_train = train_data['label'].values
x_test = test_data.values

#print(x_test)

x_train = x_train/255.0
x_test = x_test/255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

#print(x_test)

y_train = to_categorical(y_train, num_classes = 10)

#CNN
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam',  metrics=['accuracy'])
#20 times
model.fit(x_train, y_train, epochs=20, validation_split=0.2)

#predict
y_test_pred = model.predict(x_test)
y_test_labels = np.argmax(y_test_pred, axis=1)

#output
submission = pd.DataFrame({'ImageId': np.arange(1, len(y_test_labels) + 1), 'Label': y_test_labels})
submission.to_csv('submission.csv', index=False)



