filepath = 'input.txt'
entries = {set()}
sum = 2020
with open(filepath) as input:
    for line in input:
        value = int(line)
        if value in entries:
            print(value*abs(sum-value))
        else:
            entries.add(abs(sum-value))
