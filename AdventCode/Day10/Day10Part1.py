fileinput ="input.txt"
with open(fileinput) as input:
    adapters = []
    for line in input:
        adapters.append(int(line))
    adapters = sorted(adapters)
    print(adapters)
    previous_jolt = 0
    diff_3_count = 1
    diff_1_count = 0
    for adapter in adapters:
        diff = adapter-previous_jolt
        previous_jolt = adapter
        if diff == 1:
            diff_1_count+=1
        elif diff == 3:
            diff_3_count+=1
    print(diff_1_count*diff_3_count)