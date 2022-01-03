import time

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def cryption():
    global text
    text = input("Text: ")
    global s
    s = int(input("Shift Amount: "))
    print("\n==END OF USER INPUT==\n")
    print("Text : " + text)
    print("Shift : " + str(s))
    print("Encrypted : " + encrypt(text, s))
    
    cipher = encrypt(text, s)
    x = 0
    listyy = []
    tinkc = time.perf_counter()
    while x<=26:
        dresult = ""
        for i in range(len(cipher)):
            char = cipher[i]
            if char.isupper():
                dresult += chr((ord(char) + x-65) % 26 + 65)
            elif char.islower():
                dresult += chr((ord(char) + x-97) % 26 + 97)
            else:
                dresult += char
        listyy.append(dresult)
        x+=1
    print("\n\nBrute Force Input : " + cipher + "\n")
    print("Resulting Sample Space: \n")
    for e in range(len(listyy)):
        print(listyy[e])
    tonkc = time.perf_counter()
    print(f"\nTime Taken to decrypt: {tonkc - tinkc:0.8f} seconds")
    print("\n<==END OF BRUTE FORCE SCRIPT, BEGINNING FREQUENCY ANALYSIS...==>\n")
cryption()

def space(string):
    return string.replace(" ", "")

text = encrypt(text, s)
processedtext = space(text.strip().lower())
anum = 0

tic = time.perf_counter()
for a in text:
    anum += 1
print("\nCharacters: " + str(anum) + "\n")

an = processedtext.count("a")
bn = processedtext.count("b")
cn = processedtext.count("c")
dn = processedtext.count("d")
en = processedtext.count("e")
fn = processedtext.count("f")
gn = processedtext.count("g")
hn = processedtext.count("h")
inc = processedtext.count("i")
jn = processedtext.count("j")
kn = processedtext.count("k")
ln = processedtext.count("l")
mn = processedtext.count("m")
nn = processedtext.count("n")
on = processedtext.count("o")
pn = processedtext.count("p")
qn = processedtext.count("q")
rn = processedtext.count("r")
sn = processedtext.count("s")
tn = processedtext.count("t")
un = processedtext.count("u")
vn = processedtext.count("v")
wn = processedtext.count("w")
xn = processedtext.count("x")
yn = processedtext.count("y")
zn = processedtext.count("z")

proc = {"a": an, "b": bn, "c": cn, "d": dn, "e": en, "f": fn, "g": gn, "h": hn, "i": inc, "j": jn, "k": kn, "l": ln,
        "m": mn, "n": nn, "o": on, "p": pn, "q": qn, "r": rn, "s": sn, "t": tn, "u": un, "v": vn, "w": wn, "x": xn,
        "y": yn, "z": zn}
print("Alphabetical Dict: ")
print(proc)
print("\nOrdered Dict: ")
procsort = dict(sorted(proc.items(), key=lambda item: item[1], reverse=True))
print(procsort)
procmax = max(procsort, key=procsort.get)
print("\nMost common ciphertext letter: " + procmax)
comlet = str(procmax)
if comlet == "a":
    comlet = 1
elif comlet == "b":
    comlet = 2
elif comlet == "c":
    comlet = 3
elif comlet == "d":
    comlet = 4
elif comlet == "e":
    comlet = 5
elif comlet == "f":
    comlet = 6
elif comlet == "g":
    comlet = 7
elif comlet == "h":
    comlet = 8
elif comlet == "i":
    comlet = 9
elif comlet == "j":
    comlet = 10
elif comlet == "k":
    comlet = 11
elif comlet == "l":
    comlet = 12
elif comlet == "m":
    comlet = 13
elif comlet == "n":
    comlet = 14
elif comlet == "o":
    comlet = 15
elif comlet == "p":
    comlet = 16
elif comlet == "q":
    comlet = 17
elif comlet == "r":
    comlet = 18
elif comlet == "s":
    comlet = 19
elif comlet == "t":
    comlet = 20
elif comlet == "u":
    comlet = 21
elif comlet == "v":
    comlet = 22
elif comlet == "w":
    comlet = 23
elif comlet == "x":
    comlet = 24
elif comlet == "y":
    comlet = 25
elif comlet == "z":
    comlet = 26

realshift = int(comlet - 5)
strrealshift = str(realshift)
print("Distance from letter 'e': " + strrealshift)
oppshift = int(26 - realshift)
stroppshift = str(oppshift)
print("Predicted anti-shift: " + stroppshift)

def encrypt():
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + oppshift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + oppshift - 97) % 26 + 97)
        else:
            result += char
    print("Predicted Original Message: " + result + "\n")
    return result
encrypt()

toc = time.perf_counter()
print(f"Time Taken to decrypt: {toc - tic:0.8f} seconds")
timed = str(f"{toc - tic:0.8f} seconds")
