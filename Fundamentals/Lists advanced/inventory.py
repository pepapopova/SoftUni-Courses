

def inventory(collection):
    command = input()
    while command != "Craft!":
        current_command = command.split(" - ")
        item = current_command[1]
        if current_command[0] == "Collect":
            if item not in collection:
                collection.append(item)
        elif current_command[0] == "Drop":
            if item in collection:
                collection.remove(item)
        elif current_command[0] == "Combine Items":
            items = current_command[1].split(":")
            if items[0] in collection:
                index_to_take = collection.index(items[0])
                collection.insert(index_to_take + 1, items[1])
        elif current_command[0] == "Renew":
            if item in collection:
                collection.remove(item)
                collection.append(item)
        command = input()
    print(", ".join(collection))


collectible_items = input().split(", ")
inventory(collectible_items)