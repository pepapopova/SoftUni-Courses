def even_odd_filter(**kwargs):
    filtered_dict = {}
    for key, value in kwargs.items():
        parity = 0 if key == "even" else 1
        filtered_dict[key] = [x for x in kwargs[key] if x % 2 == parity]
    return dict(sorted(filtered_dict.items(), key=lambda x: -len(x[1])))
# the same as {key: value for key, value in filtered_dict.items(), key=lambda x: -len(x[1]))}



print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
