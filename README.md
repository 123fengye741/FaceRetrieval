# FaceRetrieval

## 已完成程序使用说明

目录如下：

```
py-src/
├── data_prepare
│   ├── __init__.py
│   ├── vectorize_img.py
│   ├── youtube_data_split.py
│   └── youtube_img_crop.py
└── retrieval
    ├── evaluate.py
    ├── __init__.py
    ├── load_data.py
    ├── parse.py
    ├── pre_process.py
    └── retrieve.py
```

其中，data_prepare为retrieval准备数据，两者几乎互相没有影响。

### data prepare

#### img_crop

在data_prepare中，首先运行*_img_crop.py，将图像处理成50×50大小。
> 注意，这个程序是专门为某个数据集写的，每添加一个数据集，除非数据特别类似（包括图片信息和文件夹结构等），否则一般都需要添加一个处理程序。
使用方法：

	python *_img_crop.py old_folder new_folder

- old_folder是原始图片文件夹
- new_folder是与old_folder相同结构的文件夹，只不过图片都是50×50的了。

#### data_split

其次，需要运行*_data_split.py，将上述new_folder中的图片分为查询集和被查询集，该程序生成两个csv文件，一个保存查询集的图片路径，另一个保存被查询集的图片路径。

> 注意，该程序文件每遇到一个新数据集，一般需要重新写一个程序来划分查询集和被查询集。

	python data_split.py src_folder query_set_file searched_set_file

- src_folder: img_crop.py生成的new_folder
- query_set_file: csv文件，保存查询集的图片路径。格式为path,label.
- searched_set_file: csv文件，保存被查询集的图片路径。格式为path,label.

#### vectorize_img

最后，需要运行vectorized_img.py来将图像转换为向量，以进行向量计算。在这个过程中，将生成的向量集合和类别标号保存在pickle输出中。为了不使单个文件过大，将样本每1000个存储在一个文件中，格式为(x,y)，其中，x为1000×2500的矩阵，y为长度为1000的向量，都是numpy中的类型。

	python vectorize_img.py query_set_file searched_set_file query_vector_folder searched_vector_folder
	
- query_set_file: data_split.py生成
- searched_set_file: data_split.py生成
- query_vector_folder: 查询集的文件夹，里面是1000个样本的小文件的集合
- searched_vector_folder: 被查询集的文件夹，里面是1000个样本的小文件的集合

至此，图像准备阶段完成，得到两个文件夹，一个文件夹中存储着查询集的小文件集合，另一个文件夹中存储着被查询集的小文件集合。

直观的，针对youtube数据集，生成的保存向量的文件夹，如下所示：

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


### retrieval

该模块虽然包含五个py程序文件，只有retrieve.py可执行，其他文件都是被retrieve.py调用。

各个程序文件的作用如下：

- pre_process.py 预处理程序，定义各种预处理手段，包括归一化和降维算法，目前距离度量方式也定义在此文件中。
- load_data.py 载入数据，将上述data prepare阶段生成的向量文件载入进内存。
- parse.py 用来解析配置文件中定义的参数，配置文件的格式下面会叙述。
- evaluate.py 得到查询结果后，调用此文件中得函数得到top-n的准确率。
- retrieve.py 定义检索流程，通过调用上面四个文件中的模块来得到不同配置下的检索结果。

运行retrieve.py得到检索评测结果(top-1/top-5/top-10)。

	python retrieve.py param_file
- param_file: 配置文件

#### 配置文件说明

<pre>
test_data_folder: test_vec
train_data_folder: train_vec
# this should be in the same folder with test_vec and train_vec
# and the program should be executed in the same folder with this file

[exp_1]
description: direct retrieval based on pixels with Euclidean
pre_process_method: None
sim_metric_method: euc

[exp_3]
description: retrieval based on pca dimension reduction to 160 with Euclidean
pre_process_method: pca
sim_metric_method: euc
components: 160

[exp_6]
description: retrieval based on pca dimension reduction to 500 with cosine
pre_process_method: pca
sim_metric_method: cos
components: 500

</pre>

前5行定义基本信息

- line 1：查询集向量文件夹
- line 2：被查询集向量文件夹
- line 3/4：注释内容
- line 5：空行

再下面定义每个实验的实验参数，以exp_6为例：

- line 1: 实验id，可以随意命名，必不可少
- line 2: 实验描述，对实验总体描述，必不可少
- line 3: 预处理方法，目前只有pca和None两种，必不可少
- line 4: 距离度量方法，目前只有cos和euc两种，必不可少
- line 5-? : 预处理方法所需要的其他参数，可以为多个，如pca处理方式在此时的参数为components，即主成分数目。当然，参数名需要和实现函数中一一对应上，实验函数也在pre_process.py中。

> 注意，预处理方法和距离度量方法可使用的名称可在pre_process.py文件中最下方找到，目前可选用的方法为：

	pre_process_methods_set = {'pca': pca_data, 'None':None}
	sim_metric_methods_set  = {'euc': sim_metric_euc, 'cos': sim_metric_cos}




