# Progress of Plan

## Youtube Face Dataset Released (20150415/张延祥)

- 图像经过如下处理：
	- 被裁减，得到其最中间的部分，长宽各变为原来的二分之一。
	- 缩放，成为50×50的图像
- 按照计划文档中的方法，得到查询集和被查询集。
- 数据集位置：
	- 目录
	```
	dell2:/home/zhangyx/face_retrieval/youtube_data/
	```
	- 图像数据
	```
	half_center_50_50/
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

- 生成youtube数据的向量文件，目录也在上面所述的服务器目录中，
	- test_vec/ 对应query_set.csv文件中的图像
	- train_vec/ 对应searched_set.csv文件中的图像
	- test_vec/ 与 train_vec/ 中的文件是以1000张图片为单位，pickle类型的文件，文件格式为(x,y).

- 完成基本流程的搭建，并测出直接基于像素的相似度搜索。结果见report_on_youtube.md文档。

## Exp with Configure File (20150427/张延祥) 

- PCA降维实验，降到160/500维，然后使用余弦相似度/欧式距离进行相似度查询，结果见report_on_youtube.md
- 使用配置文件的方式定义实验，实现实验的自动化。具体参见README.md文档的程序使用介绍


