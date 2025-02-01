numbers = [64, 25, 12, 22, 11]
words = ['elderberry', 'apple', 'cherry',  'date', 'banana']

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Bubble Sort numbers:", bubble_sort(numbers.copy()))
print("Bubble Sort words:", bubble_sort(words.copy()))


# 2. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Selection Sort numbers:", selection_sort(numbers.copy()))
print("Selection Sort words:", selection_sort(words.copy()))


# 3. Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # return the index of the element
    return -1  # return -1 if not found

target_number = 22
print(f"Linear Search for {target_number}: Index", linear_search(numbers, target_number))
target_word = 'date'
print(f"Linear Search for '{target_word}': Index", linear_search(words, target_word))

# # 3. Binary Search (assumes arr is sorted)
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
# sorted_numbers = bubble_sort(numbers.copy())
# sorted_words = bubble_sort(words.copy())
# print(f"Binary Search for {target_number}: Index", binary_search(sorted_numbers, target_number))
# print(f"Binary Search for '{target_word}': Index", binary_search(sorted_words, target_word))
#
# 
# # 5. Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# print("Quick Sort numbers:", quick_sort(numbers.copy()))
# print("Quick Sort words:", quick_sort(words.copy()))
