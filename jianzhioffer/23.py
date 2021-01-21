def IsValue(s):
    if s == None:
        return False
    index1 = s.find('.')
    index2 = max(s.find('e'),s.find('E'))
    #保证:如果有.和eE，BC不为空
    if index1 == 0 and len(s) == 1:
        return False
    if index2 == len(s)-1:
        return False

    if index1 == 0:
        if index2 == -1:
            #.B
            return ScanNum(s[1:])
        else:
            #.BeC
            return ScanNum(s[1:index2]) and ScanSignedNum(s[index2:])
    elif index1 == -1:
        if index2 == -1:
            #A
            return ScanSignedNum(s)
        else:
            #AeC
            return ScanSignedNum(s[:index2]) and ScanSignedNum(s[index2+1:])
    else:
        if index2 == -1:
            #A.B
            return ScanSignedNum(s[:index1]) and ScanNum(s[index1+1:])
        else:
            #A.BeC
            return ScanSignedNum(s[:index1]) and ScanNum(s[index1+1:index2]) and ScanSignedNum(s[index2:])

def ScanSignedNum(s):
    if s[0] == '+' or s[0] == '-':
        return ScanNum(s[1:])
    else:
        return ScanNum(s)

def ScanNum(s):
    for i in range(len(s)):
        #或者ord(s[i])不在48-57里
        if s[i] not in ['0','1','2','3','4','5','6','7','8','9']:
            return False
    return True


if __name__ == '__main__':
    sList = ['+100','5e2','-123','3.1415','-1E-16','12e','1a3.14','1.2.3','+-5','12e+5.4']
    for s in sList:
        print(IsValue(s))





