# Report

## Direct Retrieval on Pixels

	基于像素直接计算，包括Euclidean和Cosine，其中Cosine与Norm+Inner_Product等价。

             
|Distance Merit| Top-1 | Top-5 | Top-10 |
|--------------|-------|-------|--------|
|Euclidean     |5.86%  |7.79%  |9.46%   |
|Cosine        |6.85%  |8.59%  |10.04%  |

## Dimension Reduction by PCA

	使用PCA降到160-d，添加whiten噪声。

|Distance Merit| Top-1 | Top-5 | Top-10 |
|--------------|-------|-------|--------|
|Euclidean     |5.24%  |6.91%  |7.86%   |
|Cosine        |9.28%  |13.31% |15.88%  |

	使用PCA降到500-d，添加whiten噪声。

|Distance Merit| Top-1 | Top-5 | Top-10 |
|--------------|-------|-------|--------|
|Euclidean     |1.73%  |2.33%  |3.07%   |
|Cosine        |9.16%  |13.33% |15.90%  |

## EigenFace (Center Face and PCA)

	降维到160-d，添加whiten噪声。
	
|Distance Merit| Top-1 | Top-5 | Top-10 |
|--------------|-------|-------|--------|
|Euclidean     |4.96%  |6.43%  |7.59%   |
|Cosine        |9.08%  |13.28% |16.02%  |

	降维到500-d，添加whiten噪声。

|Distance Merit| Top-1 | Top-5 | Top-10 |
|--------------|-------|-------|--------|
|Euclidean     |1.61%  |2.21%  |2.85%   |
|Cosine        |8.49%  |13.01% |15.71%  |
	
