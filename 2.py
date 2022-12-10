

def generate_similar(word):
    if word=="":
        return [""]
    dictionary={"C":["K"],"K":["C"],"U":["OO"],"OO":["U"],"I":["EE","Y"],"Y":["I","EE"],"EE":["Y","I"],
                "F":["PH"],"PH":["F"],"QU":["KW"],"KW":["QU"],"V":["W"],"W":["V"],"Z":["S"],"S":["Z"]}
    words=[]
    if word[:2] in dictionary:
        l=dictionary[word[:2]]+[word[:2]]
        l2=generate_similar(word[2:])
        return [b+s for b in l for s in l2]
    elif word[:1] in dictionary:
        l=dictionary[word[:1]]+[word[:1]]
        l2=generate_similar(word[1:])
        return [b+s for b in l for s in l2]
    return [word[0]+k for k in generate_similar(word[1:])]

# print(generate_similar("MURTHY"))



