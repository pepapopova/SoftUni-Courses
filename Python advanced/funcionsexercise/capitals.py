

def capitals():
    county_names = input().split(", ")
    capitals = input().split(", ")
    my_dict = dict(zip(county_names, capitals))

    for country, capital in my_dict.items():
        print(f"{country} -> {capital}")

capitals()
