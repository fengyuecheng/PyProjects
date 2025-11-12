
"""
确保input符合正则
"""
import re

def re_input(pattern, tip, error_message = "输入格式有误，请重新输入！"):

    while True:

        skip_pattern = r'.*skip.*'

        content = input(tip).strip()

        if result := re.fullmatch(pattern, content):

            return result

        if result := re.fullmatch(skip_pattern, content):

            return result

        else:
            print(error_message)







