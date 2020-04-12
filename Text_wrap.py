'''You are given a string  and width .
Your task is to wrap the string S into a paragraph of width w .

Input Format

The first line contains a string, S.
The second line contains the width,w .

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
''' SOLUTION'''

import textwrap

def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(max_width)
    word_list=wrapper.fill(text=string)
    return word_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)