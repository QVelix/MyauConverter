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

text = input('Enter text: ')

print(convertTextToMyau(text))
