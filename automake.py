# 自动生成README文件
import os

with open("README.md","w",encoding="utf-8") as fin:
    fin.write("# Notice\n微软学生俱乐部的通知信息\n\n")
    for root , dirs, files in os.walk("."):
        if root == ".":
            files = sorted(files)
            for file in files:
                if file[4]==file[7]:
                    fin.write("- %s\n"%file)
