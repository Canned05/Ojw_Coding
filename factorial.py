'''
def factorial(num):
    if num <= 1:
        return  1

    else:
        
        return num * factorial(num-1)

print("0부터 입력한 숫자까지의 곱을 구합니다")
n = int(input("숫자를 입력하시오: "))
print(factorial(n)) 
'''

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num-2) 

print(fibonacci(5))
