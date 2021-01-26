def solution(s):
    word_list = s.split(" ")
    new_list =[]
    for word in word_list:
        new_words=""
        for i in range(len(word)):
            new_words+= word[i].lower() if i % 2 else word[i].upper()
        new_list.append(new_words)
    return " ".join(new_list)