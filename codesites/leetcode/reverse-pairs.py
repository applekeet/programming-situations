
## https://leetcode.com/problems/reverse-pairs/

class Solution:
    def reversePairs(nums) -> int:
        
        new2 = []
        lineee = len(nums)-1
        
        for i in nums:
            new2.append(2*i)
        
        dude=0
        print(new2)
        
        for count, i2 in enumerate(reversed(new2)):
        	print("head is me..", count, lineee, lineee-count)
        	for qq in range((lineee-count-1), 0):
        		print("head is2 me..")
        		print(i2, nums[qq])
        		if(i2 < nums[qq]):
        			dude+=1
        return dude

lit = [1,3,2,3,1]

print(Solution.reversePairs(lit))

