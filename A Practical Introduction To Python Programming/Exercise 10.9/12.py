# The number 1961 reads the same upside-down as right-side up. Print out all the numbers
# between 1 and 100000 that read the same upside-down as right-side up

def gen_strobogrammatic(n):
    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result

for i in range(1, 100001):
    print(gen_strobogrammatic(i))

