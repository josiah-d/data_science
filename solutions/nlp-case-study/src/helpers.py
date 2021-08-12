import unicodedata


def remove_accents(input_str:str) -> str:
    '''Removes accents from input string'''
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii.decode()

def filter_tokens(tokens:list, stops:object) -> list:
    """Filters tokens base on membership in stop list"""
#     split_punc = lambda x: 
    res = []
    check = [".", "-"]
    for token in tokens:
        if token not in stops and token.isalpha():
            if check[0] in token:
                res += token.partition(check[0])
            elif check[1] in token:
                res += token.partition(check[1])
            else:
                res.append(token)
    return res