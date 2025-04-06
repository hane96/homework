import json
import numpy as np
import os
from sklearn import metrics
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import sys
import graderUtil

#######################################################################
# Do not make any change in this block
# a dict stores the final result
task_result = {
    "y_pred": []
} 

# read task file content
training_filename = sys.argv[1]
testing_filename = sys.argv[2]
answer_filename = sys.argv[3]

df = graderUtil.load_file(training_filename)
X_test = graderUtil.load_testing_file(testing_filename)
y_test = graderUtil.load_answer_file(answer_filename)

#print(df.sample(5))
#print(X_test.sample(5))
#print(y_test)
#
##########################################################
# BEGIN_YOUR_CODE

# x, y 分離
x = df.drop(columns=['Target'])
y = df['Target'].values  # 将 y 转换为 numpy 数组

# 兩種標準化 MinMaxScaler ,StandardScaler 實驗幾次後發現Z-score效果比較好
############
scaler = StandardScaler().fit(x)  # Z-score normalization
#scaler = MinMaxScaler().fit(x)   # Min-max normalization

x_scaled = scaler.transform(x)
x_test_scaled = scaler.transform(X_test)

# 分割訓練集和驗證集 0.1的部分拿來驗證
x_train, x_val, y_train, y_val = train_test_split(x_scaled, y, test_size=0.1, random_state=1)

y_len=len(y)
# perceptron learning
def perceptron_learning_rule(X, y, learning_rate=0.01, epochs=1000):
    weight = np.zeros(X.shape[1])
    bias = 0
    for epoch in range(epochs):
        for i in range(len(y)):
            keep = np.dot(X[i], weight) + bias
            pred = 1 if keep >= 0 else 0
            update = learning_rate * (y[i] - pred)
            weight = update * X[i] + weight
            bias = update + bias
    return weight, bias
#learn
weight, bias = perceptron_learning_rule(x_train, y_train)

# 預測
y_pred = []
for i in range(len(X_test)):
    keep = np.dot(x_test_scaled[i], weight) + bias
    pred = 1 if keep >= 0 else 0
    y_pred.append(pred)

# 更新 task_result
task_result["y_pred"] = y_pred

#task_result["y_pred"] = list(np.random.randint(2, size=y_test.shape[0]))

# END_YOUR_CODE
# Do Not Make Any Change BELOW
#######################################################################

# output your final result
print("Prediction:")
print(task_result["y_pred"])
print("Score(80%): " + str(graderUtil.accuracy_score(task_result['y_pred'],y_test['Target'])))

