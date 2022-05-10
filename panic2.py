phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
newsrez = ''.join(plist[1:3])
base = newsrez + ''.join([plist[5] + plist[4] + plist[7] + plist[6]])
print(plist)
print(base)
