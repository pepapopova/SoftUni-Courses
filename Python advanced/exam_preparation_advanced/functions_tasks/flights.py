def flights(*args):
    flights_info = {}
    count = 0
    last_city = ""
    for info in args:
        if info == "Finish":
            break
        if count % 2 == 0:
            if info not in flights_info:
                flights_info[info] = 0
            last_city = info
        else:
            flights_info[last_city] += int(info)
        count += 1
    return flights_info

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))