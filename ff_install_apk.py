import uiautomator2 as u2

order = u2.connect('emulator-5560') #链接手机&模拟器
order.app_install('http://some-domain.com/some.apk') #安装包：url类型

 #安装包：.apk完整
 #安装split版本，自动放入obb和json

 #拉取log
 #拉取json


