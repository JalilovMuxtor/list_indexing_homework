def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    s=list1
    i=0
    while i<len(s):
        if s[i]==0:
            s[i]=False
        i+=1

    return s
print(main([0,1,1,0,0,]))