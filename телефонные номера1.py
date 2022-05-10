def reformat(string):
    string = string.replace('-', '').replace('(', '').replace(')', '')
    return string[-10:] if len(string) > 7 else '495' + string[-7:]


s = 4
notes = [input() for _ in range(s)]
for nottt in notes[1:]:
    print('YES' if reformat(notes[0]) == reformat(nottt) else 'NO')
