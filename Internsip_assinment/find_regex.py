import re
v = 'aeiou'
c = 'bcdfghjklmnpqrstvwxyz'
x = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c), input(), flags = re.I)
print('\n'.join(x or ['-1']))