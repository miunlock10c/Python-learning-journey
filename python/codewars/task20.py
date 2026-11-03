def number(bus_stops):
    num_of_ppl = 0
    for i in bus_stops:
        num_of_ppl += i[0]
        num_of_ppl -= i[1]
    return num_of_ppl
print(number([[10, 0], [5, 2], [7, 1], [13, 13]]))
