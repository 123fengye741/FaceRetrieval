# 人脸检索实验平台搭建计划(20150414)

	张延祥 | 蔡叶荷 | 黄江 | 杜俊逸 	


## 流程介绍

![face_retrieval](https://raw.githubusercontent.com/stdcoutzyx/FaceRetrieval/master/doc/face_retrieval.jpg)

## 目标
- 比较检索算法和分类算法在人脸检索上的优劣，（检索算法返回多个结果，因而可以预期检索算法比分类算法好）
- 比较多种不同的特征提取方式在人脸检索上的优劣，（DeepID是卷积神经网络，根据之前的使用AlexNet的经验，可以预期DeepID最强）
	


## 数据集

	youtube faces数据集

youbufaces是视频数据经过人脸识别与对齐后的图片集合。其目录结构如下所示：

- zhangyx
	- 0
		- img1.jpg
		- img2.jpg
		- ...
	- 1
		- img1.jpg
		- img2.jpg
		- ...
	- 2
		- img1.jpg
		- img2.jpg
		- ...
- yx
	- 0
		- img1.jpg
		- img2.jpg
		- ...

其中，每个一级文件夹都是一个人，里面的子文件夹是该人在不同视频里的表现。每个二级文件夹都是从对应视频中识别和对齐后的人脸。


### 数据集使用


- 被查询集：从每个一级目录下选择出max(n-1,1)个二级文件夹。即若一个人只有一个视频集，即被用于被查询集，若多于一个视频集，即选择一个作为查询集，剩余作为被查询集。
- 查询集：从每个一级目录下选择一个二级目录作为查询集，若一级目录下只有一个二级目录，则不从该一级目录下选择。


## 特征提取算法

> 有监督

- DeepID
- AutoEncoder

> 无监督

- LBP
- EigenFace
- FisherFace
- Haar
- ...

## 分类算法

- SVM
- LR
- GBDT
- RF
- ...

## 分工

> 为简便起见，尽量使用python中的库，方便写成统一的脚本运行。
> 如果实在找不到python的库，需要使用其他语言，请和张延祥讨论中间数据的格式。

- 张延祥
> 负责整个平台的融合以及最后结果的统计，在细节模块上，包括：

	- 图片预处理（包括查询集被查询集的切分、人脸的再次截取）
	- DeepID特征提取方式
	- 分类模块（各种分类算法）
	- 评测模块
- 蔡叶荷
	- AutoEncoder处理图像
	- Haar特征提取
	- LE特征提取
- 黄江
	- LBP特征提取
	- Gabor特征提取
	- HOG特征提取
- 杜俊逸
	- FisherFace
	- EigenFace
	- SIFT特征提取

	


























	