def maxProduct1(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    product = [0]*(n+1)
    product[0],product[1],product[2],product[3] = 0,1,2,3
    for i in range(4,n+1):
        sup = 0
        for j in range(i//2+1):
            pro = product[j]*product[i-j]
            if pro > sup:
                sup = pro
        product[i] = sup
    return product[n]

def maxProduct2(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    nn = n//3
    if n%3 == 1:
        product = pow(3,nn-1)*4
    elif n%3 == 2:
        product = pow(3,nn)*2
    else:
        product = pow(3,nn)
    return product

if __name__ == '__main__':
    sup1 = maxProduct1(20)
    print(sup1,end="\n")
    sup2 = maxProduct2(20)
    print(sup2)