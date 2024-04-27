qty = int(input("Digite a quantidade de números que deseja fazer a operação: "))
nums = []
k = 0


for i in range(qty):
    num = int(input(f"Digite o {i + 1}° valor: "))
    nums.append(num)

op = input("Digite a operação que deseja realizar: ")
print(nums)
d = len(nums) - 1

if op == "+":
    while k < len(nums):
        d -= k
        result = nums[k] + nums[d]
        k += 1
        print(result)
    
        

