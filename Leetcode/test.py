    dic = {}
    def backtrack(index):
        if index == len(digits):
            combs.append("".join(comb))
        else:
            digit = digits[index]
            for letter in dic[digit]:
                comb.append(letter)
                backtrack(index + 1)
                comb.pop()
    comb = list()
    combs = list()
    backtrack(0)
    return combs
