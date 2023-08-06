
Please develop a command line dictionary program that can be used to lookup definition of a english word(s).

Usage example:
```bash
$ python3 dict.py link
The definition of 'link':
\n*[liŋk]\nn. 环, 连结物, 链接, 火把\nvt. 连结, 联合, 挽住\nvi. 连接起来\n【计】 连接, 链路\n【化】 环节\n【经】 环节, 连接, 联系
```

the dictionary data is `dict.txt` file. Each line is a word and it's definition. The format of the line is:
```
[word || definition]
```

## history feature
save the dictionary lookup history to `history.txt` file. Each line is a history word/phrase lookup.

For example, after the first lookup `link`, the history file should be
```
link
```
Then after lookup `think`, the file should be
```
link
think
```

## multiple keyword support
User can provide more than 1 keyword in the command line arguments when running this program.
Example:
```
$ python3 dict.py zoom zoo zebra apple
The definition of 'zoom':
*[zu:m]
n. 急速上升, 变焦摄影, 嗡嗡声
vi. 猛增, 急速上升, 摄象机移动
vt. 使摄象机移动
【计】 缩放
========
The definition of 'zoo':
*[zu:]
n. 动物园
========
The definition of 'zebra':
*['zi:brә]
n. 斑马
========
The definition of 'apple':
*['æpl]
n. 苹果, 家伙
【医】 苹果
```

Efficiency requirement:
- The the dict.txt file can only be read once
- linear search is not allowed, python dict is allowed to speed up the search.
