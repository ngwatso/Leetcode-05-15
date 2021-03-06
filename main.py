class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        counts = []

        for i in nums:
            x = 0
            for j in nums:
                if j < i:
                    x += 1
                else:
                    continue

            counts.append(x)            

        return counts
            
        
'''

U:

[1, 2, 3, 4, 5]
output = [0, 1, 2, 3, 4]

[1, 1, 1, 2, 3]
output = [0, 0, 0, 3, 4]

[5, 4, 3, 2, 1]
output = [4, 3, 2, 1, 0]

P:

create var x, which will count integers, less than i.  Iterate through nums, returning x for i.

'''

# ===============

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        newList = []

        for i in range(len(nums)-1):
            num_2 = nums[i+1]
            if i == 0 or i % 2 == 0:
                count = nums[i]
                while count > 0:
                    newList.append(num_2)
                    count -= 1
            else:
                continue

        return newList    
        
'''

U:

[2, 4, 1, 3, 3, 4]
output = [4, 4, 3, 4, 4, 4]

[5, 2]
output = [2, 2, 2, 2, 2]

P:

create a loop to iterate through nums, where i is even and where j = i+1, for each pair, append j to newList i times.


'''

# ===============

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        
        newList = []
        
        for n in range(len(nums)):
            newList.insert(index[n], nums[n])
        return newList
        
        
'''

U:

nums = [0, 1, 2, 3, 4]
index = [4, 0, 2, 3, 1]
output = [1, 4, 2, 3, 0]


nums = [7, 4, 6, 2, 9]
index = [0, 2, 1, 0, 3]
output = [2, 7, 6, 9, 4]

P:

Iterate through nums(n) and index(i), insert n into newList at index i.
'''