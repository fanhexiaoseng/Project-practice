## python核心知识
********************
- ### 正则表达式
1. 查找，取出<br>
```
In [6]: reslt = re.match("itcast","itcastitheima")
In [7]: reslt.group()
Out[7]: 'itcast'
```
2. .   匹配任意1个字符（除了\n）<br>
[]   匹配[]中列举的字符<br>
\d   匹配数字0-9<br>
\D   匹配非数字<br>
\s   匹配空白，空格tab键<br>
\S   匹配非空白<br>
\w   匹配单词字符，a-z、A-Z、0-9、_<br>
\W   匹配非单词字符<br>
```
ret = re.match("[hH]","hello")
```
3. \*   匹配前一个字符出现0次或者无限次。即可有可无<br>
\+   匹配前一个字符出现1次或者无限次，即至少有1次<br>
?   匹配前一个字符出现1次或者0次，即要么有1次，要么没有<br>
{m}   匹配前一个字符出现m次<br>
{m,}   匹配前一个字符至少出现m次<br>
{m,n}   匹配前一个字符出现m到n次<br>
```
In [15]: re.match("\d*","abc").group()
Out[15]: ''
In [16]: re.match("\d*","1bc").group()
Out[16]: '1'
```
4. ^ 匹配字符串开头<br>
$ 匹配字符串结尾<br>
\b 匹配一个单词的边界<br>
\B 匹配非单词边界<br>
```
In [2]: re.match(r"\w{4,20}@163\.com","xiaowang@163.com").group()
Out[2]: 'xiaowang@163.com'
In [3]: re.match(r".*\bver\b","ho ver abc").group()
Out[3]: 'ho ver'
```
5. | 匹配左右任意一个表达式<br>
(ab) 将括号中字符作为一个分组<br>
\num 引用分组num匹配到的字符串<br>
(?P<name>) 分组起别名<br>
(?p=name) 引用别名为name分组匹配到的字符串<br>
```
In [4]: re.match(r"[1-9]?\d$|100","100").group()
Out[4]: '100'
In [5]: re.match(r"[1-9]?\d$|100","55").group()
Out[5]: '55'
In [6]: re.match(r"\w{4,20}@(163|126|qq)\.com","xiaowang@163.com").group()
Out[6]: 'xiaowang@163.com'
In [12]: ret = re.match(r"<([a-zA-Z]*)>\w*</\1>","<html>hello</html>")

In [13]: ret.group()
Out[13]: '<html>hello</html>'
In [14]: re.match(r"<(?P<key1>\w*)>.*</(?P=key1)>","<html>hello</html>")
Out[14]: <_sre.SRE_Match object; span=(0, 18), match='<html>hello</html>'>
```
6. search<br>
```
In [15]: re.search(r"\d+","阅读次数为：9999")
Out[15]: <_sre.SRE_Match object; span=(6, 10), match='9999'>

```
7. findall<br>
```
In [16]: ret = re.findall(r"\d+","python = 9,php = 6")

In [17]: ret
Out[17]: ['9', '6']

```
8. sub<br>
```
In [18]: re.sub(r"\d+","666","阅读次数为：9999")
Out[18]: '阅读次数为：666'

```
9. split<br>
```
In [19]: re.split(r":| ","info:hello world")
Out[19]: ['info', 'hello', 'world']
```
10. re默认为贪婪模式，用？开启非贪婪模式<br>
```
In [20]: s = "This is a number 234-235-22-423"

In [22]: re.match(r".+(\d+-\d+-\d+-\d+)",s).group(1)
Out[22]: '4-235-22-423'
In [23]: re.match(r".+?(\d+-\d+-\d+-\d+)",s).group(1)
Out[23]: '234-235-22-423'

```
