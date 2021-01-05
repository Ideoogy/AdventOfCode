fileinput ="test.txt"
with open(fileinput) as input:
    adapters = []
    for line in input:
        adapters.append(int(line))
    adapters.append(52)
    adapters_set = set(adapters)
    adapters = sorted(adapters)
    previous_jolt = 0
    found_paths = {}
    print(adapters)
    def findDistinctPaths(adapter):
        if adapter == adapters[len(adapters)-1]:
            return 1
        distinct_paths = 0
        for i in range(1,4):
            if (adapter+i) in adapters_set:
                distinct_paths += findDistinctPaths(adapter+i)
        return distinct_paths

    print(findDistinctPaths(adapters[0]))

