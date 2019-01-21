抖音视频抓取小工具
环境与硬件依赖
1、系统 ubuntu 18.04（本人使用环境） 
2、mitmproxy 抓包工具 
3、android adb 
4、android 手机一只

基本思路
利用抖音android客户端请求下来网络数据，然后通过mitmproxy抓包，通过过滤抓到的数据，下载相应的视频

使用方法
1、手机安装mitmproxy证书 
2、mitmproxy -s getNetworkData.py -p 8787 手机通过mitmproxy代理上网 
3、打开手机抖音 
4、执行脚本slideScreen.sh 
5、视频数据将会下载到python脚本path对应的路径
