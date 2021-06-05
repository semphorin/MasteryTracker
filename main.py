# There are 32 (current) total prime frames

import json

x = open('primeparts.json')

data = json.load(x)

x.close()

ui = ''


def retrievestate():
    for instance in data['Frames']:
        print(instance)


def chooseinstance(name):
    global counter
    counter = -1
    for instance in data['Frames']:
        counter +=1
        if instance['name'] == name:
            global tempdict
            tempdict = instance
            return tempdict
            break


def modifydict(name, key, value):
    chooseinstance(name)
    tempdict[key] = value
    data['Frames'][counter] = tempdict
    return data


def savechanges():
    try:
        with open('primeparts.json', 'w') as x:
            y = json.dumps(data, indent=4)
            x.write(y)
            x.close()
        print('Saved successfully.')
    except Exception:
        print('Failed to save.')


def showmastery():
    mastery = 0
    for instance in data['Frames']:
        if instance['mastered'] == True:
            mastery += 6000
    return mastery


def showcommands():
    print('\nCommands:'
          '\n1) Show unmastered frames'
          '\n2) Show needed components'
          '\n3) Show total mastery'
          '\n\'q\' to quit.\n')


print('Primed Mastery Tracker Alpha v1')
showcommands()

while ui != 'q':
    ui = input()
    om = False
    if ui == '1':
        for instance in data['Frames']:
            if instance['mastered'] == False:
                print(instance['name'])
                om = True
        if not om:
            print('You\'ve mastered everything!')
    elif ui == '2':
        print('placeholder, soz')
        showcommands()
    elif ui == '3':
        print(showmastery())
        print()
        showcommands()
    elif ui == 'q':
        print('See you later, space cowboy.')
    else:
        showcommands()
