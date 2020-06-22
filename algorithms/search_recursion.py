def search_recursion(array, number):
    if len(array)+1 > 1:
        q = int(len(array)+1/2)
        array1 = array[:q]
        array2 = array[q+1:]
        array1 = search_recursion(array1, number)
        array2 = search_recursion(array2, number)

        if (array1[0] == number): return number
        if (array2[0] == number): return number
    else:
        return True

a = [1, 2, 3, 4, 5]
print(search_recursion(a, 6))