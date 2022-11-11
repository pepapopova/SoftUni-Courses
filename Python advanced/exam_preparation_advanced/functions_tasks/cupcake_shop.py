from collections import deque

def stock_availability(inventory_boxes, command, *args):
    # inventory_boxes = deque(inventory_boxes)
    if command == "delivery":
        for box in args:
            inventory_boxes.append(box)
    elif command == "sell":
        for info in args:
            if isinstance(info, int):
                inventory_boxes = inventory_boxes[info::]
            else:
                inventory_boxes = [x for x in inventory_boxes if x != info] # how to replace every element in list
        if command == "sell" and not args:
            inventory_boxes = inventory_boxes[1::]
    return inventory_boxes





#
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
