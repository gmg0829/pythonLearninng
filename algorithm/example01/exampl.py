def seq_search(items: list, elem) -> int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
   print(seq_search([35, 97, 12, 68, 55, 73, 81, 40], 350))