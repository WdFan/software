# 人脸识别+教学管理系统
项目开发代码仓库[https://github.com/WdFan/software](https://github.com/WdFan/software)

<br>

## 目录结构
<img src=img/dir.png width=40% />

software-main目录下为前端代码

facereco目录下为人脸识别客户端

其余目录为后端django模块


<br>

## 技术栈

### 后端

**Django**

### 前端

**Vue + Vue-Router + Vuex + Axios +  ElementUI**

<br/>

## 开发环境

conda：4.10.3

python：3.6.2 

node：v16.13.1

IDE：VSCode

<br/>

## 下载运行

#### 1、下载项目到本地

```bash
git clone https://github.com/Yin-Hongwei/music-website.git
```

#### 2、下载项目依赖

项目根目录下使用conda创建的python3.6.2环境下执行
```python
pip install -r requirements.txt
```

```js
cd software-main/course-platform
npm insatll
```

#### 3、启动项目

- **启动后端**：进入项目根目录，运行下面命令启动

```python
python manage.py runserver
```

django已设管理员账号密码：

```
zhoubo 123456
```

- **启动前端客户端**：进入 /software-main/course-platform 目录，运行下面命令

```js
vue-cli-service serve
```

客户端已设用户密码：
```
1：fanwendi 123456
2：zhoubo 123456
```

- **启动人脸识别客户端**：进入 /facereco.py 目录，运行下面命令

```python
python signIn.py
```
由于人脸识别照片占用空间较大用户已清空

请在客户端中自行创建用户

<br/>

## 人脸识别客户端使用

<img src=img/face1.png width=50% /><br/>
1.点击新增用户

<br/>

<img src=img/face2.png width=50% /><br/>
2.进入用户注册页面，点击注册新用户

<br/>

<img src=img/face3.png width=50% /><br/>
3.输入学号，姓名
```diff
- 注意学号要求13位
```
点击完成

<br/>

<img src=img/face4.png width=50% /><br/>
4.点击开始采集按钮

<br/>

<img src=img/face5.png width=50% /><br/>
5.当人脸追踪红框出现时，点击拍摄，拍摄完成后，点击结束人脸采集

<br/>

<img src=img/face6.png width=50% /><br/>
6.点击上传数据，上传数据后点击退出按钮，返回主页面

<br/>

<img src=img/face7.png width=50% /><br/>
7.主页面点击用户管理按钮进入管理界面，在管理界面点击开始训练，等待训练完成，训练完成后退出

<br/>

<img src=img/face8.png width=50% /><br/>
8.在主页面勾选人脸识别后开启摄像头，即可开始人脸识别，人脸识别成功后会在数据库中写入识别时间。
```diff
- 若摄像头无法打开，可退出程序后重新进入，可能出现摄像头被注册进程抢占情况
```

<br/>