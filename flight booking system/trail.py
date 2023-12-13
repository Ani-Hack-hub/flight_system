# from itertools import product

# def min_operations(nums1, nums2):
#     n = len(nums1)
#     min_swaps = float('inf')

#     for swaps in product(range(n + 1), repeat=n):
#         nums1_copy = nums1[:]
#         nums2_copy = nums2[:]
#         for i in range(n):
#             if swaps[i] > 0:
#                 nums1_copy[i], nums2_copy[i] = nums2_copy[i], nums1_copy[i]
#         if all(nums1_copy[i] < nums1_copy[i+1] and nums2_copy[i] < nums2_copy[i+1] for i in range(n - 1)):
#             min_swaps = min(min_swaps, sum(swaps))

#     return min_swaps if min_swaps != float('inf') else -1

# # Test cases
# nums1_1 = [1, 3, 5, 4]
# nums2_1 = [1, 2, 3, 7]
# print(min_operations(nums1_1, nums2_1))  # Output: 1

# nums1_2 = [0, 3, 5, 8, 9]
# nums2_2 = [2, 1, 4, 6, 9]
# print(min_operations(nums1_2, nums2_2))  # Output: 1

#min time
# def min_operations(nums1, nums2):
#     n = len(nums1)
#     swap_count = [0, 1] if nums1[0] < nums2[0] else [float('inf'), 1]

#     for i in range(1, n):
#         new_swap_count = [float('inf'), float('inf')]
#         if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
#             new_swap_count[0] = min(new_swap_count[0], swap_count[0])
#             new_swap_count[1] = min(new_swap_count[1], swap_count[1] + 1)

#         if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
#             new_swap_count[1] = min(new_swap_count[1], swap_count[0] + 1)
#             new_swap_count[0] = min(new_swap_count[0], swap_count[1])

#         swap_count = new_swap_count

#     return min(swap_count) if min(swap_count) != float('inf') else -1

# # Test cases
# nums1_1 = [1, 3, 5, 4]
# nums2_1 = [1, 2, 3, 7]
# print(min_operations(nums1_1, nums2_1))  # Output: 1

# nums1_2 = [0, 3, 5, 8, 9]
# nums2_2 = [2, 1, 4, 6, 9]
# print(min_operations(nums1_2, nums2_2))  # Output: 1

#min space
def min_operations(nums1, nums2):
    n = len(nums1)
    swap_count = [0, 1] if nums1[0] < nums2[0] else [float('inf'), 1]

    for i in range(1, n):
        new_swap_count = [float('inf'), float('inf')]
        if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
            new_swap_count[0] = min(new_swap_count[0], swap_count[0])
            new_swap_count[1] = min(new_swap_count[1], swap_count[1] + 1)

        if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
            new_swap_count[1] = min(new_swap_count[1], swap_count[0] + 1)
            new_swap_count[0] = min(new_swap_count[0], swap_count[1])

        swap_count = new_swap_count

    return min(swap_count) if min(swap_count) != float('inf') else -1

# Test cases
nums1_1 = [1, 3, 5, 4]
nums2_1 = [1, 2, 3, 7]
print(min_operations(nums1_1, nums2_1))  # Output: 1

nums1_2 = [0, 3, 5, 8, 9]
nums2_2 = [2, 1, 4, 6, 9]
print(min_operations(nums1_2, nums2_2))  # Output: 1
