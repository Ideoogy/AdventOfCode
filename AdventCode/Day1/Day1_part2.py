filepath = 'input.txt'
entries_remainders = {}
solution_c = {}
sum = 2020
with open(filepath) as input:
    for line in input:
        value = int(line)
        if value in solution_c:
            a = solution_c[value][0]
            b = solution_c[value][1]
            print(value*a*b)
        if entries_remainders: 
            for entry, remainder in entries_remainders.items():
                if value!=entry:
                    solution_c[remainder-value] = (entry,value)
        entries_remainders[value] = sum-value
    

        
        

        
