x = '''['https://nekos.life/api/hug', 'https://nekos.life/api/kiss', 'https://nekos.life/api/lizard', 'https://nekos.life/api/neko', 'https://nekos.life/api/pat', 'https://nekos.life/api/v2/img/slap', 'https://nekos.life/api/v2/img/cuddle', 'https://nekos.life/api/v2/img/avatar', 'https://nekos.life/api/v2/img/poke', 'https://nekos.life/api/v2/img/feed']'''
y = []

splitted = x.split(",")
splitted[-1] = splitted[-1][:-1]
splitted[0] = splitted[0][1:]

for i in splitted:
    y.append(str(i).strip()[1:-1])

for j in y:
    print(j)
