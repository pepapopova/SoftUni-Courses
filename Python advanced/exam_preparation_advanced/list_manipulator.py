from collections import deque

def list_manipulator(ll, command, place, *args):
    ll = deque(ll)
    if command == "add":
        if place == "beginning":
            for num in reversed(args):
                ll.appendleft(num)
        elif place == "end":
            for num in reversed(args):
                ll.append(num)
    elif command == "remove":
        if place == "beginning":
            if len(args) < 1:
                ll.popleft()
            else:
                if len(ll) > len(args):
                    for num in range(len(args) + 1):
                        ll.popleft()
                else:
                    ll = []
        elif place == "end":
            if len(args) < 1:
                ll.pop()
            else:
                if len(ll) > len(args):
                    for num in range(len(args) + 1):
                        ll.pop()
                else:
                    ll = []
    return list(ll)






# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
