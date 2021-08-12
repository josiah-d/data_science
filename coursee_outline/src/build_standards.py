import pandas as pd
import sys

#URL = "https://docs.google.com/spreadsheets/d/1czHo4_3R337teFEJtM9n2D4Fmeq9mD_Jd_-2FrCfQP4"
STANDARDS_FILE = "Final Standards 2020 - Standards.tsv"
IMPORTANCE = {1: 'H',
              2: 'MH',
              3: 'M',
              4: 'ML',
              5: 'L'}

def load_tsv(file):
    return pd.read_csv(file, sep='\t')

def write_file(repo, df):
    """Write a single standards file based on a dataframe for that repo."""
    sys.stderr.write(f"Writing {len(df)} standards for {repo}\n")
    md_file = open(f'../standards/{repo}.md', 'w')
    md_file.write("## Standards for {}\n".
                    format(repo.
                            translate(str.maketrans({'-': ' '})).
                            title()))
    md_file.write("Students should be able to\n")
    for _, row in df.sort_values('Importance').iterrows():
        md_file.write(f' * ({IMPORTANCE[row["Importance"]]}) ')
        md_file.write(f"{row['Standard']}\n")
    md_file.write("""
<br/>Priorities for Standards:
 * H:  Must achieve to graduate
 * MH: Should achieve to graduate
 * M:  Important skill though mastery not necessary
 * ML: Useful skill; encouraged to learn
 * L:  May be useful but not a focus of this program""")
    md_file.close()

def write_files(df):
    for repo, sub_df in df.groupby('Repo'):
        write_file(repo, sub_df)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = STANDARDS_FILE
    df = load_tsv(file)
    write_files(df)

