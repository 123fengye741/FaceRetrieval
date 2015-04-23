# Report

## Direct Retrieval on Pixels

	基于像素直接计算，包括Euclidean和Cosine，其中Cosine与Norm+Inner_Product等价。
	
|Distance Merit| Top-1 | Top-5 | top-10 |
|--------------|-------|-------|--------|
|Euclidean     |5.86%  |5.15%  |4.32%   |
|Cosine        |6.85%  |5.59%  |4.55%   |

## Dimension Reduction by PCA

	使用PCA降到160-d，添加whiten噪声。

|Distance Merit| Top-1 | Top-5 | top-10 |
|--------------|-------|-------|--------|
|Euclidean     |5.24%  |3.27%  |2.26%   |
|Cosine        |9.28%  |6.75%  |5.03%   |
