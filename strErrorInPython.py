def word_count(str):
    counts = dict()
    words = str.split(" ")
    print(words)
    count = 0

    for word in words:
        #print word
        if word in counts:
            counts[word] = counts[word]+ 1
            #print counts[word]
        else:
            counts[word] = 1
            #print counts[word]
        count = count +1
    #print(counts["the"])
    print count
    return counts



print(word_count('the quick brown fox jumps over the lazy dog.'))
