# Sapphire
seu自动登陆程序

## 使用方法
### 图形界面（大多数用户适用）
* [下载客户端](https://github.com/HanyuuFurude/seuLogin/releases)
* 双击运行即可食用

### 命令行下调用

*　`git clone git@github.com:HanyuuFurude/seuLogin.git`
* 切换到目录下
* 在account.conf文件中填写您的账号密码然后使用下述命令即可登录

## 参数

```
-login: 登录
-logout: 登出
-userName: 设置用户名（一卡通号）#暂未添加
-password: 设置密码 #暂未添加
```

## Log
### 2019/05/07
* v0.0.2A版本
* 修正了一些闪退场景
* TODO
  * 发现了网络延时高的情况下导致界面卡顿的问题，将在后期版本修正
  * 密码框设为密码样式
  * 为无线网络场景下添加自动连接指定wifi功能
### 2019/05/03

*   v0.0.2alpha版本
*   新增功能（for 用户）
    *   定时检测登陆状态，若发现断线则自动登录
*   新增功能（for 开发者）
    *   新的查询函数
    *   将主地址从参数中移出成为单独的全局变量（后期将会移动到配置文件）
    *   少许的代码优化
*   TODO
    *   将参数移动到配置文件中以便运行时修改
    *   更快的启动速度（√）（pyinstaller的硬伤2333）

### 2019/05/03
* v0.0.1alpha 版本已经完成并且已经打包推送release
* 有任何反馈请[和我交流](mailto:Furude_Hanyuu@outlook.com),非常感谢
### 2019/05/02
* gui基本功能完成！
* 正在演进
* 初版gui已经发布（尚未打包成exe，有能力的手子请自行package，我将在功能更加完善之后进行打包）
### 2019/05/01
* 恢复更新，正在开发带有GUI界面的自动化登陆程序
* TODO
  * 考虑根据用户选项写入自动启动功能
  * 考虑加入常驻后台自动维护网络连接功能
### 2019/03/29
* 账号密码与代码分离（就这么一个简单的东西咕到现在我也是服了自己了）
* 我开始继续更新啦~敬请期待

### 2019/03/07
* 添加注销常驻功能
* 添加log系统日志功能
* 添加一定的异常处理机制
* 暂时……咕咕咕一会……

### 2019/02/28
* 目前仅完成登陆功能部分，用户界面和常驻后台之类的留待实现……

