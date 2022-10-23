""" def containsduplicate(self,num:list[int]) ->bool:
    hashset=set()
    for n in num:
        if n in hashset:
            return True
        hashset.add(n)
    return False""" 





def missingnumber(self,nums:list[int])->int:
    n=nums.length
    expectedTotal=(n*(n+1))/2
    total=0
    for num in range (nums):
        total+=num
    return expectedTotal-total
    

