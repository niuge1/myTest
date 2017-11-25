# coding: utf8
operators = "+-*"

def isnumber(num):
    return num.isalnum()

def isoperator(op):
    return op in operators

def computes(s):

    s_list = list(s)
    for i in range(int((len(s)-1)/2)):
        res = eval(str(s_list[0]) + str(s_list[1]) + str(s_list[2]))
        s_list.pop(0)
        s_list.pop(0)
        s_list.pop(0)
        s_list.insert(0, res)
    return res

if __name__ == "__main__":
    s = "3+5*7+2-7"
    res = computes(s)
    print(res)
    print(computes(s))