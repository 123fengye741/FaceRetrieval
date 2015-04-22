# Progress of Plan

## Dataset Released (20150415/张延祥)


- 图像经过如下处理：
	- 被裁减，得到其最中间的部分，长宽各变为原来的二分之一。
	- 缩放，成为50×50的图像
- 按照计划文档中的方法，得到查询集和被查询集。
- 数据集位置：
	- 目录
	```
	dell2:/home/zhangyx/face_retrieval/data/
	```
	- 图像数据
	```
	half_center_50_50
	```
	- 查询集路径及类别, 共5020张
	```
	query_set.csv
	```
	- 被查询集路径及类别, 共24210张
	```
	searched_set.csv
	```

## Basic Process Completed (20150422/张延祥)

	完成基本流程的搭建，并测出直接基于像素的相似度搜索。结果见report文档。

### 已完成程序使用说明

目录如下：
<pre>
py-src/
├── data_prepare
│   ├── data_split.py
│   ├── img_crop.py
│   ├── __init__.py
│   ├── vectorize_img.py
└── retrieval
    ├── evaluate.py
    ├── __init__.py
    ├── load_data.py
    └── retrieve.py
</pre>

其中，data_prepare为retrieval准备数据，两者几乎互相没有影响。

#### data prepare

在data_prepare中，首先运行img_crop.py，将图像处理成50×50大小（具体操作如上所述），注意，这只是针对本数据集，若是其他数据集，程序需要修改。
使用方法：

	python img_crop.py aligned_db_folder new_folder

- aligned_db_folder是原始图片文件夹
- new_folder是与aligned_db_folder相同结构的文件夹，只不过图片都是50×50的了。

其次，需要运行data_split.py，将上述new_folder中的图片分为查询集和被查询集，该程序生成两个csv文件，一个保存查询集的图片路径，另一个保存被查询集的图片路径。

	python data_split.py src_folder query_set_file searched_set_file

- src_folder: img_crop.py生成的new_folder
- query_set_file: csv文件，保存查询集的图片路径。格式为path,label.
- searched_set_file: csv文件，保存被查询集的图片路径。格式为path,label.

最后，需要运行vectorized_img.py来将图像转换为向量，以进行向量计算。在这个过程中，将生成的向量集合和类别标号保存在pickle输出中。为了不使单个文件过大，将样本每1000个存储在一个文件中，格式为(x,y)，其中，x为1000×2500的矩阵，y为长度为1000的向量，都是numpy中的类型。

	python vectorize_img.py query_set_file searched_set_file query_vector_folder searched_vector_folder
	
- query_set_file: data_split.py生成
- searched_set_file: data_split.py生成
- query_vector_folder: 查询集的文件夹，里面是1000个样本的小文件的集合
- searched_vector_folder: 被查询集的文件夹，里面是1000个样本的小文件的集合

至此，图像准备阶段完成，得到两个文件夹，一个文件夹中存储着查询集的小文件集合，另一个文件夹中存储着被查询集的小文件集合。

直观的，如下所示：

<pre>
test_vec/
├── 0.pkl
├── 1.pkl
├── ...
└── 5.pkl
train_vec/
├── 0.pkl
├── 1.pkl
├── ...
├── 23.pkl
└── 24.pkl
</pre>


#### retrieval

该模块包括检索模块和评测模块。

首先，运行retrieval.py得到检索结果。

	python retrieve.py test_data_folder train_data_folder search_results_file

- test_data_folder: 数据准备模块得到(查询集)
- train_data_folder: 数据准备模块得到(被查询集)
- search_results_file: 检索结果，存储每个查询样本的前top-10的检索结果。

	**TODO:由于只是基本实现，因而特征提取模块还未添加，预处理模块和相似度计算模块也并未切分出来。**


其次，运行evaluate.py得到检索结果评价，目前实现了top-1，top-5，top-10的准确率预估。

	python evaluate.py search_results_file

- search_results_file: 上一步产生的结果文件

