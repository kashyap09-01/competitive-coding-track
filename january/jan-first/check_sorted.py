class Solution:

    def __init__(self, arr) -> None:
        self.arr = arr
    
    def asc_sorted_check(self) -> bool:
        if len(self.arr) == 1:
            return True
        
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                return False
        
        return True

    def desc_sorted_check(self) -> bool:
        if len(self.arr) == 1:
            return True
        
        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[i-1]:
                return False
        
        return True

test_arr = [1, 2, 3, 4]
test_solution = Solution(test_arr)

print("Is Test Array Ascending Sorted: ", test_solution.asc_sorted_check())

user_input_arr = list(map(int, input("Enter Elements of the Array: ").split()))
user_solution = Solution(user_input_arr)

print("Is User Input Array Descending Sorted: ", user_solution.desc_sorted_check())

