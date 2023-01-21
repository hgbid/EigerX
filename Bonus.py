"""
the function gets a list and return the maximum number in it,
 and how many times this number appears in the list
"""

def recursive(list, max_num=0, count=0):
    if len(list) == 0:
        return max_num, count

    next_num = list.pop(0)
    if next_num > max_num:
        return recursive(list, next_num, 0)
    if next_num == max_num:
        return recursive(list, max_num, count+1)
    return recursive(list, max_num, count)


if __name__ == '__main__':
    ans = recursive([1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0])
    print(ans)
