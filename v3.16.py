def is_max(array, index):
    if index < 0 or index >= len(array):
        return False
    return True if min(array) == array[index] else False
 

array = [int(i) for i in input("Введите элементы массива, разделенные пробелом: ").split()]
index = int(input("Введите индекс"))
print(f"Элемент по индексу {index} является глобальным минимом: {is_max(array, index)}")
