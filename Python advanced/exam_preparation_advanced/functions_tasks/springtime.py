
def start_spring(**kwargs):
    new_dict = {}
    result = []
    for key, value in kwargs.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(key)
    for kind, values in sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{kind}:")
        for value in sorted(values):
            result.append(f"-{value}")

    return "\n".join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}

print(start_spring(**example_objects))
