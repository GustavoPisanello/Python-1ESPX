qty = int(input("Digite a quantidade de números que deseja fazer a operação: "))
nums = []

for i in range(qty):
    num = int(input(f"Digite o {i + 1}° valor: "))
    nums.append(num)

op = input("Digite a operação que deseja realizar: ")
print(nums)

if op == "+":
    k = 0
    result = 0
    while k < len(nums):
        result += nums[k]
        k += 1
        print(result)

elif op == "-":
    k = 1
    result = nums[0]
    while k < len(nums):
        result -= nums[k]
        k += 1
        print(result)

elif op == "*":
    k = 1
    result = nums[0]
    while k < len(nums):
        result *= nums[k]
        k += 1
        print(result)

elif op == "/":
    k = 1
    result = nums[0]
    while k < len(nums):
        result /= nums[k]
        k += 1
        print(result)
        

