# 基于Pandas库 分析男女电影打分差异
# 2020-12-10
# fyj

import numpy as np
import pandas as pd

# 读取文件
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=unames)   # 读取文件，指定分隔符

rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=rnames)

# 数据筛选
users_df = users.loc[:, ['user id', 'gender']]  # loc进行数据选取
ratings_df = ratings.loc[:, ['user id', 'rating']]
rating_df = pd.merge(users_df, ratings_df)  # 合并

# 按性别计算rating的标准差
result1 = rating_df.groupby('gender').rating.std()
print("***********************************")
print(result1)

# 实现数据的动态排列以及分类汇总，根据user id，gender计算男女标准差
df1 = rating_df.groupby(['user id', 'gender']).apply(np.mean)
result2 = pd.pivot_table(df1, values='rating', index='gender', aggfunc=pd.Series.std)
print("***********************************")
print(result2)
