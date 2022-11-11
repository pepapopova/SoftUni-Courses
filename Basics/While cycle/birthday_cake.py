width = int(input())
length = int(input())
cake_size = width * length
total_pcs = 0

while total_pcs < cake_size:
    current_pcs = input()
    if current_pcs == "STOP":
        break
    total_pcs += int(current_pcs)

diff = abs(total_pcs - cake_size)
if total_pcs <= cake_size:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")


    #2
width = int(input())
length = int(input())
cake_size = width * length
command = input()
cake_is_over = False
while command != "STOP":
    current_n_of_pcs = int(command)
    cake_size -= current_n_of_pcs
    if cake_size < 0:
        cake_is_over = True
        break
    command = input()


if cake_is_over:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")