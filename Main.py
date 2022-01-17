import Lib
y = ''
match = ''
matcheslink = []
matches = []
matches2 = []
matches3 = []
mappool = ['Player']
apikey = ''


apikey = input('Type your osuapikey (can be obtained at https://osu.ppy.sh/p/api/) ')


while y != 'n':
    match = input('Type the mp number ')
    matcheslink.append(match)
    y = input('Do you want to add a new lobby for the leaderboard?[y/n] ').lower()


y = ''


while y != 'n':
    mappool.append(input('Type each map category on the mappool on a separate line[Ex: NM1, NM2, HD1, HD2] '))
    y = input('Continue?[y/n] ').lower()


for i in matcheslink:
    matches.append(Lib.get_full_match(i, apikey))


for i in matches:
    matches2.append(Lib.matchtodict(i))


for i in range(len(matches2)):
    for j in matches2[i]:
        matches3.append(j)


Lib.matchtocsv(mappool, matches3)
Lib.matchtoleaderboard(matches3)
