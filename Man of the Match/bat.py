# def bat(a):
    


p1 = { 'name': 'Virat Kohli', 'role' : 'bat', 'runs': 112, '4' : 10, '6': 0, 'balls': 119, 'field':0}

p2 = { 'name': 'de Plessis', 'role' : 'bat', 'runs': 120, '4' : 11, '6': 2, 'balls': 112, 'field':0}


score = (p1['runs'] // 2)

if ((p1['runs'])> 50 ):
    score = score + 5
    if((p1['runs'])> 100):
        score = score + 10
        if(((p1['runs'])/(p1['balls'])*100)> 80 and ((p1['runs'])/(p1['balls'])*100) < 100 ):
            score = score + 2
            if (((p1['runs'])/(p1['balls'])*100)> 100):
                score = score + 4

score = score + (p1['4']) + ((p1['6']) * 2)

print(score)

run = (p2['runs'] // 2)

if ((p2['runs'])> 50 ):
    run = run + 5
    if((p2['runs'])> 100):
        run = run + 10
        if (((p2['runs'])/(p2['balls'])*100) > 100):
            run = run + 4

run = run + (p2['4']) + ((p2['6']) * 2)

print(run)

# a = ((p2['runs'])/(p2['balls'])*100)
# print(a)














