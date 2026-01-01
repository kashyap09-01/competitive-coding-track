class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i+=1
            j+=1
        
        return i

test_array = [1, 2, 2, 3, 3, 3, 4, 5, 6] 
test_solution = Solution().removeDuplicates(nums=test_array)
print("Test Solution Index Returned: ", test_solution)
print("Test Solution: ")
for i in range(test_solution):
    print(test_array[i], end=' ')