**愣头青的工作速查手册**
--------------
**重复搜索超过两次的内容都应该被记录下来**
**根据使用频次和好忘程度排序**
## sublime ##
sublime是世界上最好的编辑器，不服也不跟你辩

	1. 常用功能快捷键
		在本文件内查找：cmd + f
		在本文件内查找并替换： cmd + option + f
		文件夹查找很鸡肋，不用管
		回到上次编辑的地方：ctrl + -
		回到光标所在行的头：cmd + 左键
		回到光标所在行的尾：cmd + 右键
		切换已打开的文件：ctrl + tab(或用 cmd + 数字)
		选中光标所在的当前行：cmd + l
		分屏：cmd + option + 2
		取消分屏：cmd + option + 1
		整体代码缩进：cmd + [, cmd + ]
		快速移动光标：option + 方向键
		last but not least：cmd ＋ p means you can go anywhere and find everything

			 
	2. subl file name or project name
		见鬼不要再用在命令行下subl打开一个文件夹了，直接点击project，拖拽进去即可，我受够了各种alias，export，ln。

## linux ##
一些简单的常用命令还是应该知道的，一些太复杂的命令就直接用脚本吧
使用任何工具的第一件事就是搜索，学会查找你就再也不会在纷繁迷乱的Linux中迷路了
linux中关于查找的有这样几个命令，find，grep，whereis，locate等，但是你只要会find基本上就可以对付80％以上的查找场景了，这里把grep放在这里可能并不合适，毕竟人家是文本查找，但是我经常搞混和忘记，所以就酱紫吧。
find使用实例：![启动不了ipython，找ipython安装包](https://github.com/AlwaysLately/hackrankrankrank/blob/master/find_1.png)
发现没有，打印输出的有好多错误信息，其实 可以利用重定向来解决
    find / -name access_log  > /dev/null
    $? is used to find the return value of the last executed command.
    echo $?


## git ##
你不会只会用git add， git commit， git push吧
1.![这是大体印象，要有](https://github.com/AlwaysLately/hackrankrankrank/blob/master/git%E5%B7%A5%E4%BD%9C%E6%B5%81.png)  
2. git status和git log  
~字符用于表示提交的父节点的相对引用。比如，3157e~1指向3157e前一个提交,HEAD~3是当前提交的回溯3个节点的提交。  
3.git checkout   
4.git revert 和 git reset  
撤销(revert)被设计为撤销 公开 的提交的安全方式，git reset被设计为重设 本地 更改。因为两个命令的目的不同，它们的实现也不一样：重设完全地移除了一堆更改，而撤销保留了原来的更改，用一个新的提交来实现撤销。



## python ##
去用你的ruby和java吧，我没什么意见

 1. 工程相关
		 [All about import](http://www.codingpy.com/article/python-import-101/?)  
		 [What is data serialization ](http://stackoverflow.com/questions/11817950/what-is-data-serialization)  
		[unit test](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)		
 2. 语言本身
		[decorator](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000)  



## MySQL ##
	
> Written with [StackEdit](https://stackedit.io/).