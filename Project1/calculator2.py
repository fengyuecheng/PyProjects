"""
第一板计算器
两位运算加减乘除
键盘输入
终端输出
"""

from input_functions import re_input

operators = {
    '+' : lambda a, b : a+b,

    '-' : lambda a, b : a-b,

    '*' : lambda a, b : a*b,

    '/' : lambda a, b : a/b if b!=0 else "除数不能为0"
}

pattern = r'(\d+\.?\d*|\d*\.?\d+)\s*([-+*/])\s*(\d+\.?\d*|\d*\.?\d+)'

tip = "输入计算式："

while True:

    match = re_input(pattern, tip)

    if 'skip' in match.string:

        print("bye")

        break

    num1 = float(match.group(1))

    operator = match.group(2)

    num2 = float(match.group(3))

    result = operators[operator](num1, num2)

    if type(result) is str:

        print(result)

    else:
        if result == int(result):

            print(f"{match.string}={int(result)}")

        else:
            print(f"{match.string}={result}")








