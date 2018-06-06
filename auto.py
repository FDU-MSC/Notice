# 自动生成README文件
import os

with open("README.md","w",encoding="utf-8") as fin:
    fin.write("# Notice\n微软学生俱乐部的通知信息\n\n")
    for root , dirs, files in os.walk("."):
        if root == ".":
            for file in files:
                if file.endswith(".md"):
                    fin.write("- %s\n"%file)
# - 12月2日俱乐部大会.md
# - 研究院项目俱乐部参与情况.md
# - 俱乐部核心成员.md
# - 俱乐部活动积分规则.md
# - 俱乐部积分统计.md
# - MSC微软学生俱乐部9-10月Newsletter.jpg
