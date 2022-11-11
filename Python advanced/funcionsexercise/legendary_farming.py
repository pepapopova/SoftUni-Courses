def print_func(farming_items, junk_items_dict, special_item):
    print(f"{special_item} obtained!")

def legendary_farming():
    my_dict = {'Shards': 0, 'Motes': 0, 'Fragments': 0}
    junk_items_dict = {}
    while_condition = False

    while True:
        farming_items = input().split(" ")

        for value, material in zip(farming_items[0::2], farming_items[1::2]):
            material = material
            value = int(value)
            if material in ['shards', 'fragments', 'motes']:
                if material not in farming_items:
                    farming_items[material] = value
                else:
                    farming_items[material] += value
            if farming_items[material] >= 250:
                farming_items[material] -= 250
                special_item = ""
                if material == "shards":
                    special_item = "Shadowmourne"
                elif material == "fragments":
                    special_item = "Valanyr"
                elif material == "motes":
                    special_item = "Dragonwarth"

                print(farming_items, junk_items_dict, special_item)
                while_condition = True


            else:
                if material not in junk_items_dict:
                    junk_items_dict[material] = value
                else:
                    junk_items_dict[material] += value

                if while_condition:
                    break
            if while_condition:
                break

legendary_farming()