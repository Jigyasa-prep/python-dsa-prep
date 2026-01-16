#List = multiple values store karne ka box
#for loop = repeat karne ke liye
#- append() = list me value add karna
#- New list bana sakte hain old list se

nums=[5,10,15,20]
for num in nums:
    print(num)
new_list=[]
for num in nums:
    new_list.append(num*2)
print(new_list)


list=[1,2,3,4,5]
square_list=[]
for item in list:
    square_list.append(item*item)
print(square_list)
