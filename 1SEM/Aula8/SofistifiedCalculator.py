nums = []

def Input():
    """Inputs the user's numbers and the selected operation
    
        Inputs:
        - qty (int) -> The quantity of numbers that will be calculated
        - num (int) -> The number itself
        - op (str) -> The operation that will be used
    """
    qty = int(input("Digite a quantidade de números que deseja fazer a operação: "))
    
    for i in range(qty):
        num = int(input(f"Digite o {i + 1}° valor: "))
        nums.append(num)

    op = input("Digite a operação que deseja realizar: ")
    return op

def matchOperation():
    """Based in the variable 'op', returns the current operation
    
        Output:
        - The result of the operation (int in '+', '-', '*', but float in '/')

    """
    op = Input()
    
    match op:
        case "+":
            k = 0
            result = 0
            while k < len(nums):
                result += nums[k]
                k += 1
            return(result)

        case "-":       
            k = 1
            result = nums[0]
            while k < len(nums):
                result -= nums[k]
                k += 1
            return result

        case "*":
            k = 1
            result = nums[0]
            while k < len(nums):
                result *= nums[k]
                k += 1
            return result

        case "/":
            k = 1
            result = nums[0]
            while k < len(nums):
                result /= nums[k]
                k += 1
            return result
            
        case _:
            return "Digite um operador válido!"
        
if __name__ == "__main__":
    """Runs the application"""
    print(matchOperation())