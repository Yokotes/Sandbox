def merge_sort(array, start, end):
    if end - start > 1:
        q = int((end-start+1)/2)
        array1 = array[start:q]
        array2 = array[q:end]
        array1 = merge_sort(array1, 0, len(array1))
        array2 = merge_sort(array2, 0, len(array2))
        new_array = array
        k, j = 0, 0
        array1.append(-1)
        array2.append(-1)

        for i in range(end):
            if array1[k] > array2[j]:
                new_array[i] = array1[k]
                k += 1
            else:
                new_array[i] = array2[j]
                j += 1

        return new_array
    else: return array

a = [5, 10, 18, 1, 5, 85]

print(merge_sort(a, 0, len(a)))