__author__ = 'iToR'
def MergeSort(List):
    if len(List) == 1:
        return

    mid = len(List)/2
    left_side = List[:mid]
    right_side = List[mid:]

    MergeSort(left_side)
    MergeSort(right_side)

    left_count, right_count, list_count = 0, 0, 0

    while left_count < len(left_side) and right_count < len(right_side):
        if left_side[left_count] <= right_side[right_count]:
            List[list_count] = left_side[left_count]
            left_count += 1
        elif right_side[right_count] < left_side[left_count]:
            List[list_count] = right_side[right_count]
            right_count += 1
        list_count += 1
    while left_count < len(left_side):
        List[list_count] = left_side[left_count]
        left_count += 1
        list_count += 1
    while right_count < len(right_side):
        List[list_count] = right_side[right_count]
        right_count += 1
        list_count += 1

    return List