#Shuffle the Array using list and index
def shuffle(nums,n):
    ans=[]
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans
list=[1,2,3,4,5,6]
print(shuffle(list,3))