for i in range(len(test)):
    print(i, test[i])
    
    
def size(str):
    size = 0;
    for i in range(6):
            size += len(str[i])
    return size



def findString(allMatches, found, searchingFor):
    values = []
    hadPerfetMatch = False;
    for candidate in candidates:
        case = figlet.renderText(found + candidate)
        case = case.split("\n")
        matches = 0
        if(size(case) > size(searchingFor)):
            continue;
        perfectMatch = True
        for i in range(6):
            for j in range(len(case[i])-3):
                if(case[i][j] != searchingFor[i][j]):
                    perfectMatch = False
                    
        
        if(size(searchingFor) == size(case) and perfectMatch):
            matches = True;
            for i in range(6):
                for j in range(len(case[i])):
                    if(case[i][j] != searchingFor[i][j]):
                        matches = False;
               
            if matches:
                return found + candidate;
        
        if(perfectMatch):
            hadPerfetMatch = True;
            values.append(findString(matches, found+candidate, searchingFor))
    if not (hadPerfetMatch):
        return
    else:
        for value in values:
            if value != None:
                return value;
