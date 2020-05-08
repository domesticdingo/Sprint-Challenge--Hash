def intersection(arrays):
    hash_table = {}
    result = []

    # Go through each array, count 1 each time the number is shown
    for array in arrays:
        for val in array:
            if val not in hash_table:
                hash_table[val] = 1
            else:
                hash_table[val] += 1

    # If the count for a number is equal to number of arrays, add to returned result
    for key, value in hash_table.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
