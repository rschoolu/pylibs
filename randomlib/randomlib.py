import random, sys, json

with open(sys.argv[1].strip("--"), "r") as tegst:
    text = tegst.read()
times = int(sys.argv[2].strip("--"))
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
print(loggedWords)
with open("./rlResources.json", "r") as sdsd:
    yyyyye = sdsd.read()
yyyyy = json.loads(yyyyye)
class rlResource():
    def __init__(self):
        self.nouns = yyyyy["nouns"]
        self.verbs = yyyyy["verbs"]
        self.adjectives = yyyyy["adjectives"]
        self.adverbs = yyyyy["adverbs"]
rlResources = rlResource()
for i in range(times):
    newtext = text
    for i in loggedWords:
        if i["text"] == "verb":
            randomchoice = random.choice(rlResources.verbs)
        elif i["text"] == "noun":
            randomchoice = random.choice(rlResources.nouns)
        elif i["text"] == "adj":
            randomchoice = random.choice(rlResources.adjectives)
        elif i["text"] == "adv":
            randomchoice = random.choice(rlResources.adverbs)
        newtext = newtext.replace(f"<{i['text']}>",randomchoice,1)
    print(newtext)