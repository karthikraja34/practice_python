birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

print 'Welcome to the birthday dictionary. We know the birthdays of:'
for name in birthdays:
    print(name)

name = raw_input("Who\'s birthday do you want to look up? \n")
if name in birthdays:
    print '{}\'s birthday is {}.'.format(name, birthdays[name])
else:
    print 'Sadly, we don\'t have {}\'s birthday.'.format(name)