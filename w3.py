exlist = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
def quick_sort(list, left, right):
    if left >= right:
        return list

    l = left
    r = right
    pivot = list[(left + right) // 2]

    while l <= r:
        while list[l] < pivot:
            l += 1
        while list[r] > pivot:
            r -= 1
        if l <= r:
            list[l], list[r] = list[r], list[l]
            l += 1
            r -= 1

    quick_sort(list, left, r)
    quick_sort(list, l, right)
    print(list)
    return list
sorted_list = quick_sort(exlist, 0, len(exlist) - 1)
print(sorted_list)