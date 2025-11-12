import re

from input_functions import re_input

pattern = r'(\d+\.?\d*|\d*\.?\d+)(\s*([-+*/])\s*(\d+\.?\d*|\d*\.?\d+))+'

zero_pattern = r'.*/0+(\.0*[^1-9])?(\s*([-+*/])\s*(\d+\.?\d*|\d*\.?\d+))*|.*/\.0*[^1-9](\s*([-+*/])\s*(\d+\.?\d*|\d*\.?\d+))*'

#/0.000 /0. /0.000001
tip = "输入计算式："

while True:

    match = re_input(pattern, tip)

    if 'skip' in match.string:

        print("bye")

        break

    expression = match.string.replace('\n', '').replace('\t', '').replace(' ', '')

    if re.fullmatch(zero_pattern, expression):

        print("除数不能为0")
    else:
        result = eval(expression)

        print(f"{expression}={result}")




