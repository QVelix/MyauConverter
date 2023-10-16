def convertTextToMyau(text):
    textAr = text.split()
    dictionary = [",", ".", "?", "!"]
    newMyauTextAr = []
    for word in textAr:
        newWord = ''
        if word[0].istitle()==True:
            newWord+="М"
        else:
            newWord+="м"
        if len(word) > 3:
            i = 0
            modifier = 2
            for d in dictionary:
                if word.find(d)!=-1:
                    modifier+1
            while i < len(word)-modifier:
                newWord+="а"
                i+=1
        else:
            newWord+="а"
        newWord+="у"
        for d in dictionary:
                if word.find(d)!=-1:
                    newWord+=d
        newMyauTextAr.append(newWord)
    newMyauText = ""
    for myauWord in newMyauTextAr:
        newMyauText+=myauWord+" "
    return newMyauText

def convertTextToMyauBySyllables(text):
    dictionary = ['a', 'e', 'u', 'o', 'i'] 
    textAr = text.split()
    newMyauText = ""
    for word in textAr:
        wordLength = len(word)
        newWord = ""
        for d in dictionary:
            if word[0].find(d)!=-1:
                newWord+="Мяу"
        if len(newWord)>0:
            i = 1
        else: 
            newWord+="Мяу"
            i=2
        while i<wordLength:
            for d in dictionary:
                if word[i].find(d)!=-1:
                    newWord+="мяу"
            i+=1
        newMyauText+=newWord+" "
    return newMyauText

text = input('Enter text: ')

print(convertTextToMyau(text))
print(convertTextToMyauBySyllables(text))
