word =input()
sensored = "CAMBRIDGE"
for sensor in sensored:
    if sensor in word:
        word = word.replace(sensor,"")
print(word)
