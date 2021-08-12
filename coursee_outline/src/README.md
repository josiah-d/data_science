## Rebuilding the course outline README.md

This directory contains a tool (`build_outline.py`) for rebuilding the `README.md` for the course outline based on the files in this directory. DO NOT modified `README.md` directly; it should be considered object code and hand edits will make maintenance more difficult.

If you are following the main schedule exactly you will only need to modify two files. The instructors teaching each individual lesson are in `instructors.csv`. Removing this file will cause the corresponding column to be dropped from the output (this is not recommended). The file `config.csv` has additional configuration details: the campus name (used as a branch in the `lectures` repo, the solutions repo based on the [directions for creating a solutions branch](https://github.com/GalvanizeDataScience/solutions/blob/master/README.md), and the cohort id in learn used for assessment links).

The other files contain the sequence of days (`days.csv`), a short descriptions of each repo (`descriptions.csv`), additional resources for each repo (`resources.md`), links commonly used in resources (`books.csv`), and a template to insert it all in (`template.md`).

To use, run:
```
python build_outline.py > ../README.md
```
from this directory.

## Rebuilding the standards files

The files in `../standards/` contain the standards for the DSI program, which students are expected to be able to achieve. These can be rebuilt from the [standards spreadsheet](https://docs.google.com/spreadsheets/d/1czHo4_3R337teFEJtM9n2D4Fmeq9mD_Jd_-2FrCfQP4).

1. Clone this repo locally.
2. Download standards file from the google sheets as a `.tsv` file.
3. From this directory, run `python build_standards.py file.tsv` where `file.tsv` is the path of the downloaded file.
4. Verify that the changed files look good.
5. Add, commit, and push the changes.
