def kth_smallest(array, k):
    array.sort()

    print(array[k - 1])


if __name__ == '__main__':
    array_list = [12, 3, 5, 7, 19]
    kth_smallest(array_list, 2)
