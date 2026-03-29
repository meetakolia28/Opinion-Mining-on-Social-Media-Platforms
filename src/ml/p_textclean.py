import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import p_name as name

lemmatizer = WordNetLemmatizer()
sn = SnowballStemmer('english')
stopword = set(stopwords.words('english'))
stopword.discard('not')


def clean(cstring):
    urlless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', cstring)
    userless_string = re.sub('@[^\s]+', '', urlless_string)
    hashless_string = re.sub('#[^\s]+', '', userless_string)
    symless_string = clear_punctuation(hashless_string)
    wosw_string = stopw(symless_string)
    rtless_string = re.sub('rt', '', wosw_string)
    return rtless_string


def clear_punctuation(s):
    clear_string = ""
    for symbol in s:
        if symbol not in string.punctuation:
            clear_string += symbol
    return clear_string


def stopw(sstring):
    lowstring = sstring.lower()
    sword = word_tokenize(lowstring)
    twords = []
    for w in sword:
        f = 0
        if w not in stopword:
            if name.rname(w) == 0 and f == 0:
                f = 1
            if name.fname(w) == 0 and f == 0:
                f = 1
            if name.lname(w) == 0 and f == 0:
                f = 1

            if f == 0:
                w = lemmatizer.lemmatize(w)
                w = sn.stem(w)
                twords.append(w)
    wstr = convert(twords)
    return wstr


def convert(s):
    str1 = " "
    return str1.join(s)
