from partitions import hoare_partition, lomuto_partition


def quick_sort_hoare(list):
    _quick_sort_hoare(list, 0, len(list) - 1)


def _quick_sort_hoare(list, start, end):
    while start < end:
        pivot = hoare_partition(list, start, end)
        _quick_sort_hoare(list, start, pivot-1)
        start = pivot


def quick_sort_lomuto(list):
    _quick_sort_lomuto(list, 0, len(list)-1)


def _quick_sort_lomuto(list, start, end):
    while start < end:
        pivot = lomuto_partition(list, start, end)
        _quick_sort_lomuto(list, start, pivot-1)
        start = pivot + 1