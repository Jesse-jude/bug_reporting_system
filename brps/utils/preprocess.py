import nltk
def preprocess_text(text):
    #Download nltk resources
    nltk.download('punkt') #download sentence tokenizer
    nltk.download('stopwards') #download stop words

    #lowercase the texts
    text = text.lower

    #remove punctuation
    #tokens = [word for word in tokens if word.isalpha()]

    #tokenize the text (split into words)
    stop_words = nltk.corpus.stopwords.words('english')
    tokens = [word for word in tokens if word not in stop_words]

    #stemming or lemmatization(optional)
    #you can choose either stemming (reduce words to base form) or lennatization(reduce to dictionary form)
    #porter = nltk.stem.PorterStemmer()
    #lancaster = nltk.stem.LancasterStemmer()
    #wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()
    #tokens = [porter.stem(word) for word in tokens] # example using porter stemmer

    #join the preprocessed tokens back into text
    preprocessed_text = ''.join(tokens)

    return preprocessed_text