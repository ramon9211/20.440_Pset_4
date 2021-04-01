#imports
import os
from subprocess import check_output

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_style("ticks")
matplotlib.rcParams.update({'font.size': 18})

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import sklearn.cluster as cluster
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

# set folder path
folderPath = os.path.join('..','..','Project','data',
        'GSE139598_Week13_Stimulated.Cells.UMI.collapsed.CHUNKED',
        'csv_test')

# set result path to save figure
resultPath = os.path.join('results',
        'GSE139598_Week13_Stimulated.Cells.UMI.collapsed.CHUNKED',
        'csv_test')

# get list of file names
files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
print(files)

# initialize list to safe data chunks in
dataList = []
i=0

for file_ in files:
    #read data
    data = pd.read_csv(
        os.path.join(folderPath,
        file_
        ), 
        #compression='gzip',
        header=0, 
        sep=',', 
        quotechar='"')

    data = data.drop(data.columns[0], axis=1)
    nRow, nCol = data.shape
    print('There are {} rows and {} columns in the current data chunk.'.format(nRow, nCol))
    dataList.append(data)

# transform data list into panda dataframe
dataAll = pd.concat(dataList) 
nRow, nCol = dataAll.shape
print('There are {} rows and {} columns in the whole dataset.'.format(nRow, nCol))

# some prints to check data from console
print('DATA INFORMATION: \n')
print(data.info())
print('DATA First 5 lines: \n')
print(data.head(5))

#Creating dataframe for labels
labels = pd.read_csv(
    os.path.join('..',
    '..',
    'Project',
    'data',
    'Original',
    'GSE139598_Week13.All.Cells.Metadata.csv',
    ), 
    delimiter=',')

nRow, nCol = labels.shape

# some prints to check labels from console
print('There are {} rows and {} columns in labels dataframe.'.format(nRow, nCol))
print(labels.info())
print(labels.head(5))
print('shape: ', labels.shape)

#Find unique classes of cell types
print(labels['Week13CellType'].unique())

#Create a 2D numpy array of values in data.
X = data.values
print(X[0:5])

#Standardize the features before performing dimensionality reduction, (mean=0,standard deviation =1)
X_std = StandardScaler().fit_transform(X)

#Visualize data using Principal Component Analysis.
print("Principal Component Analysis (PCA)")
fig = plt.figure(num=None, figsize=(10, 10), dpi=80)
ax1  = fig.add_subplot(111)
pca = PCA(n_components = 2).fit_transform(X_std)
pca_df = pd.DataFrame(data=pca, columns=['PC1','PC2']).join(labels)
palette = sns.color_palette("muted", n_colors=8)
sns.set_style("white")
ax1 = sns.scatterplot(x='PC1', 
                y='PC2',
                hue='Week13CellType',
                data=pca_df, 
                palette=palette, 
                linewidth=0.2, 
                s=30, 
                alpha=1).set_title('PCA')

fig.savefig(resultPath, bbox='tight')
plt.show()
