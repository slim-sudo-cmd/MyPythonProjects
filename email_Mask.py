
mask = lambda e: e[0] + "***@" + e.split('@')[1]

print(mask("yuvenals@gmail.com"))

mask_Two = lambda e: (s := e.split('@'))[0][0] + '***' + s[0][-1] + '@' + s[1]
print(mask_Two("yuvenals@gmail.com"))

