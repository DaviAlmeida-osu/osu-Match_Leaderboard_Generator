import requests
import json
import csv

def getname(id, apikey):
    r = requests.get(f'https://osu.ppy.sh/api/get_user?k={apikey}&u={id}')
    tudo = json.loads(r.text)
    return (f"{tudo[0]['username']}")



def get_full_match(id, apikey):
    matchtemp = []
    matchtemp2 = []
    match = []
    r = requests.get(f'https://osu.ppy.sh/api/get_match?k={apikey}&mp={id}')
    mp1 = json.loads(r.text)
    apimatch = mp1
    for j in range(len(apimatch['games'])):
        for i in range(len(apimatch['games'][j]['scores'])):
            matchtemp.append(getname(apimatch['games'][j]['scores'][i]['user_id'], apikey))
            matchtemp.append(apimatch['games'][j]['scores'][i]['score'])
            matchtemp2.append(matchtemp[:])
            matchtemp.clear()
        match.append(matchtemp2[:])
        matchtemp2.clear()

    return match



def matchtodict(matchlist):
    nomestotal = []
    nomes = []
    names = {}
    temp = []
    temp3 = []

    for i in range(len(matchlist)):
        for j in range(len(matchlist[i])):
            if matchlist[i][j][0] not in names.keys():
                names[matchlist[i][j][0]] = []

    for i in range(len(matchlist)):
        for j in matchlist[i]:
            if j[0] in names.keys():
                names[j[0]].append(int(j[1]))
            
    for i in range(len(matchlist)):
        for j in range(len(matchlist[i])):
            nomes.append(matchlist[i][j][0])
        nomestotal.append(nomes[:])
        nomes.clear()
        


    for i in range(len(matchlist)):
        set_diff = set(names.keys()) - set(nomestotal[i])
        list_diff = list(set_diff)
        if list_diff != []:
            for j in list_diff:
                names[j].insert(i, 0)

    for key, value in names.items():
        temp.append(key)
        for i in value:
            temp.append(i)
        temp3.append(temp[:])
        temp.clear()

    '''with open('osuMatchLeaderboard/Matches.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(mappoollist)
            write.writerows(temp3)'''
        
    return temp3



def matchtocsv(mappoollist, rows):
    with open('Matches.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(mappoollist)
            write.writerows(rows)
    print('Match database successfully exported to csv')



def matchtoleaderboard(match):
    sum = 0
    temp = []
    temp2 = []
    for i in range(len(match)):
        temp.append(match[i][0])
        for j in range(1, len(match[i])):
            sum = sum + match[i][j]
        temp.append(sum)
        temp2.append(temp[:])
        temp.clear()
        sum = 0
    
    header = ['#', 'Player', 'Score']

    temp2.sort(key = lambda x: x[1], reverse=True)
    
    for i in range(len(temp2)):
        temp2[i].insert(0, i+1)

    print(temp2)

    with open('Leaderboard.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(header)
            write.writerows(temp2)
    print('Match Leaderboard successfully created, Thank you for using this script!')


    

