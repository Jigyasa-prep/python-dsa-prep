#Shuffle the Array using list and index
def shuffle(nums,n):
    ans=[]
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans
list=[1,2,3,4,5,6]
print(shuffle(list,3))

#two sum 
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
nums=[1,2,3,4]
print(twosum(nums,5))