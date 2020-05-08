def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}

    # Enumerate weights gives count(index) + weight
    for i, weight in enumerate(weights):
        # if the difference between the limit and the weight is present in keys, adds to hashtable
        if limit - weight in hash_table.keys():
            return sorted((hash_table[limit - weight], i), reverse=True)
        hash_table[weight] = i

    return None
