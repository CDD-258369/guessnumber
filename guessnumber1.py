# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:24:27 2024

@author: Administrator
"""

import random

# 生成一个1到100之间的随机数
secret_number = random.randint(1, 100)

# 初始化猜测次数
guesses = 0

print("欢迎来到猜数字游戏！我已经想好了一个1到100之间的数字。")

while True:
    # 用户输入猜测的数字
    try:
        guess = int(input("请输入你的猜测："))
    except ValueError:
        print("请输入一个有效的整数。")
        continue

    # 增加猜测次数
    guesses += 1

    # 检查猜测是否正确
    if guess < secret_number:
        print("太小了！再试一次。")
    elif guess > secret_number:
        print("太大了！再试一次。")
    else:
        print(f"恭喜你！你猜对了数字是 {secret_number}。")
        print(f"你总共猜了 {guesses} 次。")
        break