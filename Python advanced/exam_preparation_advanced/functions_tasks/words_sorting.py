def words_sorting(*args):
    words_dict = {}
    total_sum = 0
    for word in args:
        current_sum = 0
        for ch in word:
            current_sum += ord(ch)
        total_sum += current_sum
        words_dict[word] = current_sum

    word_list = []
    if total_sum % 2 == 0:
        for key, values in sorted(words_dict.items(), key=lambda x: x[0]):
            word_list.append(f"{key} - {values}")
    else:
        for key, values in sorted(words_dict.items(), key=lambda x: -x[1]):
            word_list.append(f"{key} - {values}")
    return "\n".join(word_list)


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
