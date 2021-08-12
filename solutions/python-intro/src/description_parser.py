from string import punctuation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS
import argparse

import text_parsing_functions as tpf

def read_lines_in_file(filepath, sw, nm, rep):
    lines_cleaned = [] 
    with open(filepath) as fp: 
        for line in fp:
            line_cleaned = tpf.line_cleaning_pipeline(line, sw, nm, rep)
            lines_cleaned.append(line_cleaned)
    return lines_cleaned

def write_lst_to_file(lst, filepath):
    with open(filepath, mode='w', encoding='utf-8') as fp:
        fp.write('\n'.join(lst))


if __name__ == '__main__':
    replace = 'person'
    names = set(['suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'ingil', 'yonghuk'
                 'jinhee'])
    line_text = "pregnant wife Seong-kyeong, a high school baseball team, rich-yet-egotistical" 
    cleaned_text = tpf.line_cleaning_pipeline(line_text, stopwords, names, replace)
    #print(cleaned_text)

    # Argument parsing
    parser = argparse.ArgumentParser() 
    parser.add_argument("--input", "-i", type=str, required=True)
    parser.add_argument("--output", "-o", type=str, required=True)
    args = parser.parse_args()
    
    #  read in file
    filepath_in = args.input
    lines_cleaned = read_lines_in_file(filepath_in, stopwords, names, replace)

    # write the file
    filepath_out = args.output
    write_lst_to_file(lines_cleaned, filepath_out)
