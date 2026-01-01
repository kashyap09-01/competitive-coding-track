arr = [float('-inf'), 1, 4, 2, 7, 7, 5, float('inf')]

if len(arr) == 1:
    print(-1)
    exit

largest = arr[0]
sec_largest = -float('inf')

for i in range(len(arr)):
    if arr[i] > largest:
        sec_largest = largest
        largest = arr[i]
    elif arr[i] > sec_largest and largest!=arr[i]:
        sec_largest = arr[i]

print("Largest: ", largest)
print("Second Largest: ", sec_largest)

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
