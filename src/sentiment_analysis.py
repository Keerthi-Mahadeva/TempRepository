def strip_punctuation(stringx):
    for punc_char in punctuation_chars:
        if punc_char in stringx:
            stringx = stringx.replace(punc_char, "")
    return stringx


def get_pos(stringx):
    stringx = stringx.lower()
    
    punctuation_stripped = strip_punctuation(stringx)
    words_list = punctuation_stripped.split()
    positive_words_dict = {}
    for word in words_list:
        if word in positive_words:
            if not word in positive_words_dict:
                positive_words_dict[word] = 1
            else:
                positive_words_dict[word] += 1

    #print(f"Positive Dictionary Content: {positive_words_dict}")
    total_positive_words = 0
    for pos_word in positive_words_dict:
        total_positive_words += positive_words_dict[pos_word]
    
    return total_positive_words


def get_neg(stringx):
    stringx = stringx.lower()
    
    punctuation_stripped = strip_punctuation(stringx)
    words_list = punctuation_stripped.split()
    negative_words_dict = {}
    for word in words_list:
        if word in negative_words:
            if not word in negative_words_dict:
                negative_words_dict[word] = 1
            else:
                negative_words_dict[word] += 1

    #print(f"Negative Dictionary Content: {negative_words_dict}")
    total_negative_words = 0
    for neg_word in negative_words_dict:
        total_negative_words += negative_words_dict[neg_word]
    
    return total_negative_words


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

twitter_data_file = open("project_twitter_data.csv")
resulting_data_file = open("resulting_data.csv", "w+")

for index, line in enumerate(twitter_data_file):
    #Strip Punctuation
    if index==0:
        header_fields = ["Number of Retweets"," Number of Replies", " Positive Score", " Negative Score", " Net Score"]
        final_header_line = ",".join(header_fields)
##        print(final_header_line) # Ready to Write Header Line
        resulting_data_file.write(final_header_line + "\n")
    else:
        content_line = line.split(",")
        content_line = [x.strip() for x in content_line] # Strip new lines
        stripped_punc_content = strip_punctuation(content_line[0]) # Call Function to Strip Punctuation Characters.
        #print(stripped_punc_content)
        my_pos_count = get_pos(stripped_punc_content) # Call Function to get positive word count in the sentence 'stripped_punc_content'
        #print(f"Positive Count:{my_pos_count}")
        my_neg_count = get_neg(stripped_punc_content) # Call Function to get negative word count in the sentence 'stripped_punc_content'
        #print(f"Negative Count:{my_neg_count}")
        my_netscore = my_pos_count - my_neg_count
##        print(f"Net Score:{my_netscore}")
        final_content_line = ",".join([content_line[1], content_line[2], str(my_pos_count), str(my_neg_count), str(my_netscore)])
##        print(final_content_line) # Ready to Write Content Line
        resulting_data_file.write(final_content_line + "\n")
twitter_data_file.close()
resulting_data_file.close()
    
