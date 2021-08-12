from string import punctuation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS


def lowercase_text(text):
    '''Returns a text string with all characters lower-cased.

    Parameters
    ----------
    text: str

    Returns
    -------
    text_lowercased: str

    Examples
    --------
    >>> lowercase_text('AbC')
    'abc'
    '''
    return text.lower()


def remove_punctuation(text, punctuation=punctuation):
    '''Returns a text string without punctuation.

    Parameters
    ----------
    text: str
    punctuation: str
        A string containing all the punctuation characters to remove.

    Returns
    -------
    text_nopunct: str

    Examples
    --------
    >>> remove_punctuation("here's johnny!")
    'heres johnny'
    '''
    return ''.join([c for c in text if c not in punctuation])


def remove_newline(text):
    '''Removes all newlines in a line of text

    Parameters
    ----------
    text: str

    Returns
    -------
    text_no_nl: str

    Examples
    --------
    >>> remove_newline('\nlife happens when youre busy\n making other plans\n')
    'life happens when youre busy making other plans'
    '''
    return text.replace('\n', '')


def split_text_into_words(text):
    '''Splits a text string into a word list

    Parameters
    ----------
    text: str

    Returns
    -------
    words: list of str

    Examples
    --------
    >>> split_text_into_words("get started by stop talking and begin doing")
    ['get', 'started', 'by', 'stop', 'talking', 'and', 'begin', 'doing']
    '''
    return text.split(' ')


def remove_stopwords(word_lst, stopwords_set):
    '''Removes words from word_lst if in the stopwords_set

    Parameters
    ----------
    word_lst: list of str
    stopwords_set: set of str

    Returns
    -------
    word_lst_no_sw: list of str

    Examples
    --------
    >>> remove_stopwords(['tell', 'me', 'and', 'i', 'forget'], set(['and', 'i']))
    ['tell', 'me', 'forget']
    '''
    return [word for word in word_lst if word not in stopwords_set]


def replace_names(word_lst, name_set, replacement_val):
    '''Replaces names in word_lst with replacement_val.  Names are identified in
    the name set.

    Parameters
    ----------
    word_lst: list of str
    name_set: set of str
    replacement_val: str
        The string to replace the names with.

    Returns
    -------
    word_lst_replaced_names: list of str

    Examples
    --------
    >>> replace_names(['daryl', 'daryl'], set(['larry', 'darryl']), 'person')
    ['person', 'person']
    '''
    word_lst_with_replacement = []
    for word in word_lst:
        if word in name_set:
            val = replacement_val
        else:
            val = word
        word_lst_with_replacement.append(val)
    return word_lst_with_replacement


def create_cleaned_textline_from_words(words):
    '''Makes a single string from a list of words.

    Parameters
    ----------
    words: list of str

    Returns
    -------
    cleaned_text: str

    Examples
    --------
    >>> create_cleaned_textline_from_words(['darkest', 'moments', 'focus', 'light'])
    'darkest moments focus light'
    '''
    text = ' '.join([word for word in words])
    return text


def line_cleaning_pipeline(text, stopwords_set, name_set, replace_val):
    '''Transforms raw text into clean text using text-cleaning functions above'''
    text_lc = lowercase_text(text)
    text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text_np)
    words = split_text_into_words(text_nnl)
    words_nsw = remove_stopwords(words, stopwords_set)
    words_cleaned = replace_names(words_nsw, name_set, replace_val)
    line_of_text_cleaned = create_cleaned_textline_from_words(words_cleaned)
    return line_of_text_cleaned


if __name__ == '__main__':
    # to help test functions and pipeline:
    text_str1 = "Seok-woo, a divorced fund manager, is a workaholic and absentee father to \nhis"
    text_str2 = "young daughter, Su-an. For her birthday the next day, she wishes for her father\n"
    text_str3 = "to take her to Busan to see her mother. \nThey board the KTX at Seoul Station."

    # your code below
    text = text_str1
    replace = 'person'
    names = set(['suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'ingil', 'yonghuk'
                 'jinhee'])
    # test functions
    text_lc = lowercase_text(text)
    text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text_np)
    words = split_text_into_words(text_nnl)
    words_nsw = remove_stopwords(words, stopwords)
    words_cleaned = replace_names(words_nsw, names, replace)
    line_of_text_cleaned = create_cleaned_textline_from_words(words_cleaned)

    # test pipeline
    line_text_pipeline = line_cleaning_pipeline(text, stopwords, names, replace)

    same_result = line_of_text_cleaned == line_text_pipeline

    # print results
    print(f"Original: {text}")
    print(f"Lowercased: {text_lc}.")
    print(f"Punctuation removed: {text_np}.")
    print(f"Without newlines: {text_nnl}")
    print(f"Into words: {words}")
    print(f"No stop words: {words_nsw}")
    print(f"Replaces names: {words_cleaned}")
    print(f"Lined of cleaned text: {line_of_text_cleaned}")
    print(f"\nDoes pipeline give same result? {same_result}")
