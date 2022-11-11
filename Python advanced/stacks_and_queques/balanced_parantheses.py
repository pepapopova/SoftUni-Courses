expression = input()

opening_brackets = []
is_balanced = True
pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}

for ch in expression:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        is_balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            is_balanced = False
            break

if not is_balanced or opening_brackets:
    print('NO')
else:
    print('YES')