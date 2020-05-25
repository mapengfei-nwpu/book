## 写入操作

**跟踪** 将文件纳入版本控制。

**状态** 未修改、已修改、放入暂存区

**开始跟踪一个文件** **将已跟踪命令放入暂存区**  ```git add filename```

**查看暂存区和工作区的文件的区别**  `git diff`

**解除跟踪(删除工作区和暂存区文件)** `git rm file`

**解除跟踪(删除暂存区文件，保留工作区文件)** `git rm file`（不小心将文件添加到暂存区时可以使用）

 **查看暂存区和已提交的文件的区别** `git diff --cached` 或者`git diff --staged`

**提交暂存区文件** `git commit -m "message"`

**提交所有已经跟踪的文件** `git commit -a -m "message"`

## 查看操作

**查看文件状态** `git status -s` 

- MM 工作区的文件修改了 暂存区的文件修改了
- ?? 为跟踪文件
- A 新添加到暂存区的文件

**查看提交历史** `git log` 参数 `-p` 显示内容交易，`-stat` 显示每次提交状态

## 撤销操作

**覆盖上一次提交** `git commit --amend`

**取消暂存区文件** `git reset HEAD filename`

**将工作区的文件退回到上一次提交** `git checkout -- filename`

**将工作区的文件退回为暂存区文件** 没有找到命令。可以先将暂存区文件提交，然后再`git checkout -- filename`

## 打标签

**查看已有标签** `git tag`

**在当前提交打上附注标签** `git tag -a -m "message"`

**在当前提交打上轻量标签** `git tag v1.0`

**显示与标签对应的提交信息** `git show`

**签出标签并建立一个分支** `git checkout -b branchname tag`



