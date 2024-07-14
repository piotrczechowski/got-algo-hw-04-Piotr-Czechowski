import random
import timeit
import numpy as np

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to test built-in sorted (Timsort)
def timsort(arr):
    return sorted(arr)

# Generate random data
def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]

# Measure execution time
def measure_time(sort_function, data):
    return timeit.timeit(lambda: sort_function(list(data)), number=1)

# Data sizes for testing
data_sizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Collecting execution times
execution_times = {
    'merge_sort': [],
    'insertion_sort': [],
    'timsort': []
}

for size in data_sizes:
    data = generate_data(size)
    
    merge_sort_time = measure_time(merge_sort, data)
    insertion_sort_time = measure_time(insertion_sort, data)
    timsort_time = measure_time(timsort, data)
    
    execution_times['merge_sort'].append(merge_sort_time)
    execution_times['insertion_sort'].append(insertion_sort_time)
    execution_times['timsort'].append(timsort_time)
    
    print(f"Data Size: {size}")
    print(f"Merge Sort: {merge_sort_time:.6f} seconds")
    print(f"Insertion Sort: {insertion_sort_time:.6f} seconds")
    print(f"Timsort: {timsort_time:.6f} seconds\n")

# Analysis and Conclusion
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(data_sizes, execution_times['merge_sort'], label='Merge Sort', marker='o')
plt.plot(data_sizes, execution_times['insertion_sort'], label='Insertion Sort', marker='o')
plt.plot(data_sizes, execution_times['timsort'], label='Timsort', marker='o')
plt.xlabel('Data Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithms Execution Time Comparison')
plt.legend()
plt.grid(True)
plt.show()
