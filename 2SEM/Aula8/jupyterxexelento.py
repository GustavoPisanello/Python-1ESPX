nums = []

def Media():

    for i in range(0, 5):
        num = int(input(f"Digite a {i+1}° nota: "))
        nums.append(num)

    plus = Plus(nums) 
    media = plus / len(nums)
    return media

def Plus(x):
    plus = 0
    for i in x:
        plus += i
    
    return plus


if __name__ == "__main__":
    print(Media())