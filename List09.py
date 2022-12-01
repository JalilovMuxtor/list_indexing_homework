def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    k = 0

    while i < len(list1) - 1:

        if list1[i] == list1[i+1]:
            k = True

            return True
        else:
            k = False    

            return False    

    return k 
    
print(main([0,0,0,0,0]))