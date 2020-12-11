# 使用scikit-learn库，按成绩将6个人分为两类
# 2020-12-10
# fyj

import numpy as np
from sklearn.cluster import KMeans

# 6个人的成绩
list1 = [88, 74, 96, 85]
list2 = [92, 99, 95, 94]
list3 = [91, 87, 99, 95]
list4 = [78, 99, 97, 81]
list5 = [88, 78, 98, 84]
list6 = [100, 95, 100, 92]

data = np.array([list1, list2, list3, list4, list5, list6])

kmeans = KMeans(n_clusters= 2).fit(data)
pred = kmeans.predict(data)
print(pred)

for i in range(0, len(data)):
    if pred[i] == 0:
        print("{}号是学霸".format(i+1))
for i in range(0, len(data)):
    if pred[i] == 1:
        print("{}号不是学霸".format(i+1))