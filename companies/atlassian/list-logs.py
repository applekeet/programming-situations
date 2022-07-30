from collections import defaultdict

log1 = [
    [334, "user_1", "r1"],
    [434, "user_1", "r2"],
    [534, "user_1", "r3"],
    [634, "user_1", "r2"],
    [635, "user_1", "r3"],
    [636, "user_1", "r3"],
    [637, "user_1", "r3"],
    [638, "user_1", "r1"],
    [734, "user_1", "r2"],
    [754, "user_1", "r2"],
    [804, "user_1", "r2"],
    [904, "user_1", "r2"],
]


def highest_occurence(input_log):

    siz = len(input_log)
    hashmap = defaultdict(int)
    highest_list = []

    start_time = input_log[0][0]
    end_time = start_time + 300
    start_resource_name = input_log[0][2]

    # fill the hashmap
    for i in range(siz):
        resource_name = input_log[i][2]
        if input_log[i][0] < end_time:
            hashmap[resource_name] += 1
        else:
            break
    print(hashmap)

    for j in range(1, siz):
        start_time = input_log[j][0]
        end_time = start_time + 300

        print(input_log[j])

        hashmap[start_resource_name] -= 1
        start_resource_name = input_log[j][2]

        if i + j < siz and input_log[i + j][0] < end_time:
            end_resource_name = input_log[i + j][2]
            hashmap[end_resource_name] += 1

        print(hashmap)
        max_key = max(hashmap, key=lambda x: hashmap[x])
        highest_list.append([max_key, hashmap[max_key]])
    print(highest_list)
    high_number = max(highest_list, key=lambda x: highest_list[x][1])
    return highest_list[high_number]


highest_occurence(log1)
