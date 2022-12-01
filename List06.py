def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = list1
    i = 0
    while i < len(a):
        if a[i] == 1:
            a[i] = True
        i +=1
    return a
print(main([1,0,1,1,1,0]))