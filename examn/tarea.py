def solution(s):
    lista = s.split(" ")
    indices = list(map(lambda x: x[-1],[x for x in lista]))
    values = list(map(lambda x: x[:-1], [x for x in lista]))
    myvalues = []
    for i in range(len(indices)):
        myvalues.append((indices[i], values[i]))
    sortlist = sorted(myvalues, key=lambda t: t[0])
    final = list(map(lambda x: x[1], [x for x in sortlist]))
    return final

def solution2(s):
    
    lista = s.split(" ")
    if len(lista) > 9:
        return ""
    myvalues = list(map(lambda x: (x[-1],x[:-1]) ,  [x for x in lista]))
    sortlist = sorted(myvalues, key=lambda t: t[0])
    final = list(map(lambda x: x[1], sortlist))
    print(final)

solution2("red2 blue2 black4 green1")
