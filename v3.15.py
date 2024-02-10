def is_max(array, index):
    if index < 0 or index >= len(array):
        return False
    return True if max(array) == array[index] else False
 

