import numpy as np
import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('dis_CBD_twoPs_03_19.csv')

# 提取点的编号
df[['point1', 'point2']] = df['twoPs'].str.split('_', expand=True)
df['point1'] = df['point1'].apply(lambda x: int(x[1:]))
df['point2'] = df['point2'].apply(lambda x: int(x[1:]))

# 获取点的数量
num_points = max(df['point1'].max(), df['point2'].max()) + 1

# 创建邻接矩阵
adj_matrix = np.zeros((num_points, num_points))

# 填充邻接矩阵
for _, row in df.iterrows():
    adj_matrix[row['point1'], row['point2']] = row['distance']
    adj_matrix[row['point2'], row['point1']] = row['distance']  # 如果是无向图

# 保存为npy文件
np.save('adj_matrix.npy', adj_matrix)
