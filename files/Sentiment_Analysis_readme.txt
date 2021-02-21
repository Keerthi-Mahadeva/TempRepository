{
    "Twitter Data":"project_twitter_data.csv",
}
# Contains: 1. Text of a tweet
            2. The number of retweets of that tweet
            3. The number of replies of that tweet

{
    "Positive Words":"positive_words.txt"
}
# Contains: Words that express positive sentiment.

{
    "Negative Words":"negative_words.txt"
}
# Contains: Words that express negative sentiment. 


Project:
    Build a sentiment classifier, which will detect how positive or negative each tweet is.
    At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

Milestones:
    1. Create a CSV file which contains:
        a. Columns for
        b. Nubmer of Retweets
        c. Number of Replies
        d. Positive Score
        e. Negative Score (How many Happy or Angry words are in the tweet)


Uncategorized:
    
    Step 1: Define a function called strip_punctuation which takes one parameter,
    a string which represents a word, and removes characters considered punctuation from everywhere in the word.
    (Hint: remember the .replace() method for strings.)
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    # code start
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    def strip_punctuation(stringx):
        """ Strip punctuation from the string """
        for punc_char in punctuation_chars:
            if punc_char in stringx:
                stringx = stringx.replace(punc_char, "")
        return stringx

    # code end

    Step 2: Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter,
            a string which represents one or more sentences, and calculates how many words in the string are considered positive words.
            Use the list, positive_words to determine what words will count as positive.
            The function should return a positive integer - how many occurrences there are of positive words in the text.
            Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

    # code start
    def strip_punctuation(stringx):
        print("\nRunning strip_punctuation function: Stripping Punctuation...")
        for punc_char in punctuation_chars:
            if punc_char in stringx:
                stringx = stringx.replace(punc_char, "")
        print("Punctuation Stripped.")
        print("Returning string: {}\n".format(stringx))
        return stringx


    def get_pos(stringx):
        print("Running get_pos function:")
        print("Converting string to lower case")
        stringx = stringx.lower()
        
        print("Calling strip_punctuation function on: {}".format(stringx))
        punctuation_stripped = strip_punctuation(stringx)
        print("get_pos: \nObtained string: {}\n".format(punctuation_stripped))
        words_list = punctuation_stripped.split()
        print("Splitting string to list of words...")
        print("Obtained List: {}".format(words_list))
        positive_words_dict = {}
        for word in words_list:
            print("Processing Word: {}".format(word))
            if word in positive_words:
                print("{} is a Positive Word".format(word))
                if not word in positive_words_dict:
                    print("{} is not in Dictionary...adding word.".format(word))
                    positive_words_dict[word] = 1
                    print("Dictionary Contnet: {}\n".format(positive_words_dict))
                else:
                    positive_words_dict[word] += 1

        total_positive_words = 0
        print("Computing total number of Positive words...")
        for pos_word in positive_words_dict:
            total_positive_words += positive_words_dict[pos_word]
        print("Total Positive Words is: {}...Returning Count\n".format(total_positive_words))
        return total_positive_words


    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    positive_words = [] #List will be filled through "positive_words.txt" file
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())


    print(get_pos('Testing "what a truly wonderful day it is today! #incredible"'))

    # code end

    Step 3: Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter,
            a string which represents one or more sentences, and calculates how many words in the string are considered negative words.
            Use the list, negative_words to determine what words will count as negative.
            The function should return a positive integer - how many occurrences there are of negative words in the text.
            Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

    # code start
    def strip_punctuation(stringx):
    for punc_char in punctuation_chars:
        if punc_char in stringx:
            stringx = stringx.replace(punc_char, "")
    return stringx

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

        total_negative_words = 0
        for neg_word in negative_words_dict:
            total_negative_words += negative_words_dict[neg_word]
        
        return total_negative_words


    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

    # code end

    Step 4: Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv,
            which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
            Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
            Copy the code from the code windows above, and put that in the top of this code window.
            Now, you will write code to create a csv file called resulting_data.csv,
            which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet),
            Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet.
            The file should have those headers in that order. Remember that there is another component to this project.
            You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets.
            Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.
    
