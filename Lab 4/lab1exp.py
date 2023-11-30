def custom_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


S = input("Enter a string: ")
words = S.split(" ");
cnt = len(words)
print(f"Numer of words in sentence \"{S}\" is : {cnt}")

if cnt % 2 == 0:
    print("Number of words is even, The sorting will be in  Ascending direction")
    print(f"The sorted string using bubble sort is: {custom_bubble_sort(words)} ")
    sorted_string_sort_function = S.split()
    sorted_string_sort_function.sort()
    print(f"The sorted string using built-in sort function is {sorted_string_sort_function}")
else:
    print("Number of words is odd, The sorting will be in  Descending direction")
    sorted_string = custom_bubble_sort(words)
    sorted_string.reverse()
    print(f"The sorted string using bubble sort in reverse is: {sorted_string} ")
    sorted_string_sort_function = S.split()
    sorted_string_sort_function.sort(reverse=True)
    print(f"The sorted string using built-in sort function is {sorted_string_sort_function}")
