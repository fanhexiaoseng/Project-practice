## linux基础知识
1.字体变大：Ctrl+shift+“+”<br>
2.字体变小：Ctrl+“-”<br>
3.清理屏幕：clear<br>
4.当前路径下的文件：ls，ll<br>
5.当前路径：pwd<br>
6.切换路径：cd+路径<br>
   		  cd ./A 当前路径下的A文件夹<br>
   		  cd.. 上层路径<br>
           cd../..上上层路径<br>
           cd~ 家目录<br>
           cd- 回到上次目录<br>          
7.创建文件：touch+文件名<br>
8.创建文件夹：mkdir+文件夹名字<br>
            mkdir A/B/C/D -p 创建递归目录<br>
9.命令格式：command（命令）+[-options]（选项）+[parameter]（参数）<br>
10.ls -a 全都显示，包括隐藏的<br>
   ls -l 显示文件详细内容<br>
   ls -h -l 文件以K显示，合适的单位<br>
11.自动补全：Tab<br>
12.查看文件内容：cat<br>
13.历史记录：history<br>
14.删除：rm<br>
15.重定向：ls > xxx.txt ls的内容放在xxx.txt文件中<br>
          ls >> xxx.txt 追加<br>
16.大文件的显示：more+文件<br>
               ls -alh /bin |more<br>
17.相对路径：当前路径算起<br>
   绝对路径：从根目录算起<br>
18.软连接：ln -s 1.txt 1-softlink.txt(快捷方式)<br>
   硬连接：ln 1.txt 1-softlink.txt（原文件删除后还可以使用）<br>
19.重命名：mv 1-softlin.txt 1-softlink.txt<br>
   移动文件：mv 1.txt wenjianjia/<br>
20.合并两个文件：cat 1.txt 2.txt > xxx.txt<br>
21.查找内容：grep （-n 行数）（-v 反向查找）0“NTFS” xxx.txt<br>
22.复制：cp 2.txt A<br>
23.查找：find / -name "*name*"<br>
               -size 大小
               -perm 权限
24.压缩文件：打包 tar -cvf text.tar *.py<br>
            解包 tar -xvf text.tar<br>
            打包压缩 tar -zcvf text.tar.gz *.py<br>
            解包压缩 tar -zxvf text.tar.gz<br>
            另一种打包：tar -jcvf text.tar.bzz<br>
            打包 zip zzz.zip *.py<br>
            解包 unzip zzz.zip<br>
25.查看命令在哪个文件夹下：which<br>
26.日历：cal<br>
        cal -y 2008 2008年日历<br>
27.日期：date<br>
        data > text.txt<br>
        data "+%Y===%m===%d"<br>
28.进程：ps -aux<br>
        top 单独界面显示进程<br>
        htop 详细单独界面进程<br>
        kill 杀死进程<br>
29.重启：reboot<br>
   关机：shutdown-h+时间<br>
30.查看硬盘：ds<br>
   查看当前路径使用情况：du<br>
31.查看网络信息：ifconfig<br>
   检验连接是否成功：ping ip地址<br>
32.添加用户：useradd<br>
   添加密码：passwd<br>
   当前用户：whoami<br>
   退出：exit<br>
33.远程登录：
