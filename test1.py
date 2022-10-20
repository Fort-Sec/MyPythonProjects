favorite_languages = {
    'collins': 'c#',
    'maye': 'java',
    'fortune': 'python',
    'ebi' : 'ruby',
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pascal',
}

friends = ['collins','maye','fortune','ebi','jen','sarah','edward','phil','great','sharon']
for friend in friends:
    print('\n')
    print(friend.title())

    if friend in favorite_languages.keys(): 
        print('Thanks' + ' ' + friend.title() + ' ' + 'for taking the poll' + '.')
    else:
        print(friend.title() + ',please take the poll, we would really love that ' + '.')        

    
    