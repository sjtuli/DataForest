# DataForest 🌲
### It's a learning share platform

**使用：**
<!--##0、Python3 安装 -->
<!--###Linux(Cent OS):-->
<!--which pyhton  #查看python版本-->
<!--wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz-->
<!--tar -zxvf Python-3.7.12.tgz-->
<!--yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make-->
<!--./configure --prefix=/root/training/Python-3.6.5-->
<!--make-->
<!--make install-->
<!--###Micsoft:-->
<!--手动安装-->
<!--https://www.python.org/downloads/windows/-->
<!--###Mac:-->
<!--手动安装-->
<!--https://www.python.org/downloads/macos/-->
<!---->
<!--##1、django 安装-->
<!--pip install django==2.2.3-->
<!---->
<!--##2、mdeditor 安装-->
<!--pip install mdeditor-->
<!---->
<!--##3、pillow 安装-->
<!--pip install pillow-->
<!---->
<!--##4、更新SQLite3/MySQL-->
<!--###Linux:-->
<!--wget https://sqlite.org/2019/sqlite-autoconf-3290000.tar.gz-->
<!--tar zxvf sqlite-autoconf-3290000.tar.gz-->
<!--cd sqlite-autoconf-3290000-->
<!--./configure-->
<!--make-->
<!--sudo make install-->
<!--###Micsoft:-->
<!--手动安装-->
<!--http://www.sqlite.org/-->
<!--###Mac:-->
<!--出厂自带-->

<!--pip uninstall django django-notifications-hq pillow django-mdeditor-->

0.安装python，不要忘记勾选PATH
1.在当前文件夹下(DataForest)运行 pip install --no-index --find-link="pip/" django django-notifications-hq pillow django-mdeditor
2.运行python manage.py runserver

**功能：** 
0. 数据库添加功能： 
    - 使用Markdown书写并提交
    - 根据创建时间对问题进行排序
1. zTree文档管理功能：
    - zTree 文档管理工具
    - 可以利用Markdown书写节点内容
    - 上传文件至节点
2. 分区功能：
    - 可以分类展示不同类型的实验数据
3. 搜索功能：
    - 通过输入关键字对数据文档、数据内容、文件进行搜索
    - 搜索结果中数据文档、数据内容、文件按照发布日期等进行排序
    - 可以选择搜索结果的类别
4. 用户注册功能：
    - 注册用户
    - 上传头像
    - 修改个人资料
  
**需要安装的拓展包：**
0. django('version: 2.2.3')
1. Markdown(`version: 3.2.1`) # 用于前端显示
2. Pillow(`version: 7.1.2`)
3. django-notifications-hq(`version: 1.6.0`)
4. django-mdeditor  # 用于后台编辑

**版本信息：**
0. python(`version: 3.7.12`)
1. Django(`version: 2.2.3`)

**运行方式：**
1. 在本地下载目录
1. 配置python解释器及虚拟环境
1. 在命令行输入python manage.py runserver
1. 在网页输入网址`http://127.0.0.1:8000/`
