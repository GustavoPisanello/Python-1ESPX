def ListSum(list):
    sum = 0

    for i in list:
        sum += i

    return sum

def SumLists():
    list1 = [40, 20, 30]
    list2 = [40, 20, 30]
    result = []
    i = 0

    while i < len(list1):
        result.append(list1[i] + list2[i])
        i += 1

    return result

list = [10, 15, 20, 25, 39, 48, 56, 45, 65]

print(SumLists())

print(ListSum(list))