from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers = deque([int(x) for x in input().split(", ")])
count_boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        last_element = papers.pop()
        first_element = papers.popleft()
        papers.append(first_element)
        papers.appendleft(last_element)
        continue
    current_paper = papers.pop()
    current_sum = current_paper + current_egg
    if current_sum <= 50:
        count_boxes += 1

if count_boxes >= 1:
    print(f"Great! You filled {count_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")