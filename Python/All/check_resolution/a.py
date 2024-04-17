# pip install screeninfo
from screeninfo import get_monitors


def get_val_str(str):
    split = str.split(',')
    sub = {}
    for word in split:
        sub = get_val_after_special_char(sub, word, '=')
    return sub


def get_val_after_special_char(array, word, special_char):
    if special_char in word:
        split = word.split(special_char)
        if 'Monitor(' in split[0]:
            split[0] = split[0].replace("Monitor(", "")
        array[split[0]] = split[1]
    return array

main = []
for m in get_monitors():
    main_array = get_val_str(str(m))
    main.append(main_array)

print(main)





