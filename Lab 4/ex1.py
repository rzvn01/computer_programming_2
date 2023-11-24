# def custom_bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
#
# S = input("Enter a sentence: ")
# words = S.split()
# word_count = len(words)
#
# if word_count % 2 == 1:  # Odd word count
#       # Sort words in alphabetical order using custom bubble sort
#       bubble_sorted_words = custom_bubble_sort(words)
#         # Sort words in reverse order using the sorted() function
#      sorted_words = sorted(words, reverse=True)
# else:  # Even word count
#         # Sort words in reverse alphabetical order using custom bubble sortbubble_sorted_words = custom_bubble_sort(words)
#      bubble_sorted_words.reverse()
#         # Sort words in alphabetical order using the sorted() function
#      sorted_words = sorted(words)
#
# print("Word count:", word_count)
# print("Words sorted with custom bubble sort:", ' '.join(bubble_sorted_words))
# print("Words sorted with sorted() function:", ' '.join(sorted_words))
