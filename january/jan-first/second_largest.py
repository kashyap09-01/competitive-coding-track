class Solution:

    def __init__(self, arr) -> None:
        self.arr = arr

    def second_largest_solution(self):
        if len(self.arr) == 1:
            return -1
        
        largest = self.arr[0]
        sec_largest = -float('inf')

        for i in range(len(self.arr)):
            if self.arr[i] > largest:
                sec_largest = largest
                largest = self.arr[i]
            elif self.arr[i] > sec_largest and largest!=self.arr[i]:
                sec_largest = self.arr[i]

        print("Largest: ", largest)
        print("Second Largest: ", sec_largest)

        return sec_largest

    def second_smallest_solution(self, arr):

        if len(arr) == 1:
            return -1
        
        smallest = float('inf')
        sec_smallest = float('inf')

        for i in range(len(arr)):
            if arr[i] < smallest:
                sec_smallest = smallest
                smallest = arr[i]
            elif arr[i] < sec_smallest and smallest!=arr[i]:
                sec_smallest = arr[i]

        print("Smallest: ", smallest)
        print("Second Smallest: ", sec_smallest)

        return sec_smallest

arr_test = [float('-inf'), 1, 4, 2, 7, 7, 5, float('inf')]

test_solution = Solution(arr_test)

print("Test Array Second Largest: ", test_solution.second_largest_solution())

user_input_array = list(map(float, input("Enter the Array: ").split()))

print("User Input Second Smallest: ", test_solution.second_smallest_solution(user_input_array))
