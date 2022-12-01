def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    b=list1
    i=0
    while i<len(b):
        if b[i]==0:
            b[i]=False
        if b[i]==1:
            b[i]=True
        i+=1
    return b
print(main([1,1,1,0,1,0]))