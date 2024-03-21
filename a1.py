import random
import time
import matplotlib.pyplot as plt


def bubble_sort(my_list):
    n = len(my_list)
    operations = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            operations += 1
            if my_list[j] > my_list[j + 1]:
                operations += 1
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return operations


def selection_sort(my_list):
    n = len(my_list)
    operations = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            operations += 1
            if my_list[j] < my_list[min_index]:
                operations += 1
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return operations


def insertion_sort(my_list):
    n = len(my_list)
    operations = 0
    for i in range(1, n):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            operations += 2
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return operations


def quick_sort(my_list):
    stack = [(0, len(my_list) - 1)]
    operations = 0
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(my_list, low, high, operations)
            stack.append((low, pivot_index))
            stack.append((pivot_index + 1, high))
    return operations


def partition(my_list, low, high, operations):
    pivot = my_list[low]
    i = low + 1
    j = high

    while True:
        while i <= j and my_list[i] < pivot:
            operations += 1
            i += 1
        while i <= j and my_list[j] > pivot:
            operations += 1
            j -= 1

        if i >= j:
            break

        my_list[i], my_list[j] = my_list[j], my_list[i]
        operations += 1
        i += 1
        j -= 1

    my_list[low], my_list[j] = my_list[j], my_list[low]
    return j


def merge_sort(my_list):
    operations = 0
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        operations += merge_sort(left_half)
        operations += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            operations += 2
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            operations += 1
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            operations += 1
            my_list[k] = right_half[j]
            j += 1
            k += 1

    return operations


def print_sorted_lists():
    # Generate a list of 100 random integers
    unsorted_list = random.sample(range(1000), 100)
    print("Unsorted List:", unsorted_list)

    # Create a copy of the unsorted list for each sorting function
    bubble_list = unsorted_list.copy()
    selection_list = unsorted_list.copy()
    insertion_list = unsorted_list.copy()
    quick_list = unsorted_list.copy()
    merge_list = unsorted_list.copy()

    # Perform the above sorting operations
    bubble_sort(bubble_list)
    # print(bubble_list)
    selection_sort(selection_list)
    # print(selection_list)
    insertion_sort(insertion_list)
    # print(insertion_list)
    quick_sort(quick_list)
    # print(quick_list)
    merge_sort(merge_list)
    # print(merge_list)


def main():
    print_sorted_lists()

    list_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]

    bubble_tn_values = []
    selection_tn_values = []
    insertion_tn_values = []
    quick_tn_values = []
    merge_tn_values = []

    bubble_times = []
    selection_times = []
    insertion_times = []
    quick_times = []
    merge_times = []

    for size in list_sizes:
        print('Processing size: ', size)
        # Generate a worst-case scenario list of the given size
        worst_case_list = list(range(size, 0, -1))

        # print(worst_case_list)

        # Calculate T(n) for each sorting algorithm and time taken

        start_time = time.time()
        bubble_tn = bubble_sort(worst_case_list)
        bubble_time = time.time() - start_time
        bubble_times.append(bubble_time)

        start_time = time.time()
        selection_tn = selection_sort(worst_case_list.copy())
        selection_time = time.time() - start_time
        selection_times.append(selection_time)

        start_time = time.time()
        insertion_tn = insertion_sort(worst_case_list.copy())
        insertion_time = time.time() - start_time
        insertion_times.append(insertion_time)

        start_time = time.time()
        quick_tn = quick_sort(worst_case_list.copy())
        quick_time = time.time() - start_time
        quick_times.append(quick_time)

        start_time = time.time()
        merge_tn = merge_sort(worst_case_list.copy())
        merge_time = time.time() - start_time
        merge_times.append(merge_time)

        # Append T(n) values to the respective lists
        bubble_tn_values.append(bubble_tn)
        selection_tn_values.append(selection_tn)
        insertion_tn_values.append(insertion_tn)
        quick_tn_values.append(quick_tn)
        merge_tn_values.append(merge_tn)

    # Plotting T(n) vs. n
    plt.plot(list_sizes, bubble_tn_values, label='Bubble Sort')
    plt.plot(list_sizes, selection_tn_values, label='Selection Sort')
    plt.plot(list_sizes, insertion_tn_values, label='Insertion Sort')
    plt.plot(list_sizes, quick_tn_values, label='Quick Sort')
    plt.plot(list_sizes, merge_tn_values, label='Merge Sort')

    plt.xlabel('List Size (n)')
    plt.ylabel('T(n)')

    plt.title('T(n) vs. n for Worst-Case Scenario')

    plt.legend()
    plt.show()

    # Plotting algorithm completion time vs. n
    plt.plot(list_sizes, bubble_times, label='Bubble Sort')
    plt.plot(list_sizes, selection_times, label='Selection Sort')
    plt.plot(list_sizes, insertion_times, label='Insertion Sort')
    plt.plot(list_sizes, quick_times, label='Quick Sort')
    plt.plot(list_sizes, merge_times, label='Merge Sort')
    plt.xlabel('List Size (n)')
    plt.ylabel('Algorithm Completion Time (seconds)')

    plt.title('Algorithm Completion Time vs. n (Worst-Case Scenario)')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
