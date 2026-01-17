#function definition
def add_two_numbers(a,b):
    result=a+b
    return result
#function calling
add = add_two_numbers(3,5)
print(add)

def square(num):
    return num*num
print(square(4))

#function with list
def make_square_list(nums):
    result=[]
    for num in nums:
        result.append(num*num)
    return result
print(make_square_list([1,2,3,4]))

def double_list(nums):
    double=[]
    for num in nums:
        double.append(num*2)
    return double
print(double_list([1,2,3,4,5]))