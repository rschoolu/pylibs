with open(input('File Directory: '), "r") as tegst:
    text = tegst.read()
detection = False
curLoggedWord = ""
curLoggedIndex = 0
curLoggedLength = 0
loggedWords = []
for i in range(len(text)):
    #print(i)
    if text[i-1] == "<":
        detection = True
        #curLoggedIndex = i
        curLoggedLength = 0
    if detection == True:
        curLoggedWord += text[i]
        #curLoggedLength += 1
    try:
        if text[i+1] == ">":
            curLoggedLength += 1
            loggedWords.append({
                "text": curLoggedWord
            })
            curLoggedWord = ""
            detection = False
    except:
        pass
#print(loggedWords)
newtext = text
for i in loggedWords:
    if i["text"] == "verb":
        randomchoice = input('Enter a verb (future tense): ')
    elif i["text"] == "verbing":
        randomchoice = input('Enter a verb (current): ')
    elif i["text"] == "verbed":
        randomchoice = input('Enter a verb (past tense): ')
    elif i["text"] == "noun":
        randomchoice = input('Enter a noun: ')
    elif i["text"] == "nouns":
        randomchoice = input('Enter a noun (plural): ')
    elif i["text"] == "adj":
        randomchoice = input('Enter a adjective: ')
    elif i["text"] == "adv":
        randomchoice = input('Enter a adverb: ')
    elif i["text"] == "name":
        randomchoice = input('Enter a name: ')
    else:
        randomchoice = input(f'Enter a {i["text"]}: ')
    newtext = newtext.replace(f"<{i['text']}>",randomchoice,1)
print(newtext)
input('\n')