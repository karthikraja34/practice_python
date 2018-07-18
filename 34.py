import json

birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

with open("birthdays.json", "w") as f:
    json.dump(birthdays, f)

with open("birthdays.json", "r") as f:
    birthday = json.load(f)
name = raw_input("Who\'s birthday do you want to look up? \n")
if name in birthday:
    print '{}\'s birthday is {}.'.format(name, birthdays[name])
else:
    print 'Sadly, we don\'t have {}\'s birthday.'.format(name)
