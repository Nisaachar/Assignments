##### Code For Question 2 (a) #####

print('\n\n##### Intermediate steps for Question 2 (a) #####\n\n')
#function to create heap.
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Given array
A = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98]

#initializing an empty array to store the resulting heap
heap = []

# Building the heap step by step
for i in range(len(A)):
    # Add the element to the heap
    current_element = A[i]

    # demonstrating the intermediate result after adding the current element
    print(f"After adding element {current_element}:")
    heap[:i + 1] = [current_element] + A[:i]
    for j in range(len(A) // 2 - 1, -1, -1):
        max_heapify(heap, len(heap), j)
    print(heap[:i + 1])
    print("--------")

print(f'\nThe final heap formed from the given array is: {heap}')


print('\n\n##### Intermediate steps for Question 2 (b) #####\n\n')

##### Code For Question 2 (b) #####

sorted_array = []

while heap:
    #popping the first element of max-heap which will be maximum of heap by the definition of max-heap.
    sorted_array.append(heap.pop(0))

    #Now there's no gurantee that the second element will be the largest so we need to adjust the heap to maintain the max-heap property.
    i = 0
    while (2 * i + 1) < len(heap):
        left_child = 2 * i + 1
        right_child = 2 * i + 2 if (2 * i + 2) < len(heap) else left_child

        max_child = left_child if heap[left_child] > heap[right_child] else right_child

        if heap[i] < heap[max_child]:
            heap[i], heap[max_child] = heap[max_child], heap[i]
            i = max_child
        else:
            break

    # Display the intermediate arrays
    print(f"Intermediate sorted array: {sorted_array}")
    print("--------")

# Final sorted array (descending order)
print(f"\nThe final sorted array (descending order): {sorted_array}\n\n")\

