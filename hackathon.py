#Hackathon File
def analyze_file(file_path):
  '''Non optimized file'''
    file = open(file_path, "r")
    text = file.read()
    file.close()
    
    text = text.lower()
    text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    words = text.split()
    
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    result = "Total words: " + str(len(words)) + "\n"
    result += "Unique words: " + str(len(word_count)) + "\n"
    result += "Top 10 common words:\n"
    for i in range(10):
        if i < len(sorted_words):
            result += sorted_words[i][0] + ": " + str(sorted_words[i][1]) + "\n"
    
    output_file = open("output.txt", "w")
    output_file.write(result)
    output_file.close()

