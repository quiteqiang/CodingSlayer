
def quick_sort(nlst):
    '''快速排序法'''
    if len(nlst) <= 1:
        return nlst
    left = []
    right = []
    piv = []
    pivot = nlst[0]
    for val in nlst:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + piv + quick_sort(right)
data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
print("原始串列：", data)
print("排序串列：", quick_sort(data))