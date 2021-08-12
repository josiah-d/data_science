import re
import sys
import os
"""
TODO:
    more docstrings
    make less fragile
"""

repo_root = 'https://github.com/GalvanizeDataScience/'
lect_root = 'https://github.com/GalvanizeDataScience/lectures/tree/%campus%/'

class Repo:
    def __init__(self, string):

        self.assignment = True
        self.lecture = True
        self.branch = None

        string = string.strip()
        if string:
            if string[0] == '!':
                self.lecture = False
                string = string[1:]
            if string[0] == '%':
                self.assignment = False
                self.lecture = False
                string = string[1:]
            if self.assignment and '/' in string:
                loc = string.find('/')
                self.branch = string[loc + 1:]
                string = string[:loc]
            self.name = string
        else:
            self.assignment = False
            self.lecture = False
            self.name = ''

def csv_split(line):
    return [field.strip() for field in line.split(',')]

def dedup_list(lst):
    """Remove consecutive duplicated elements from list
    (for use in daily instructor list)"""
    prev = None
    result = []
    for element in lst:
        if element != prev:
            result.append(element)
            prev = element
    return result

def read_descriptions(filename):
    descriptions = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            repo, description = csv_split(line)
            descriptions[repo] = description
    return descriptions


def read_instructors(filename):
    instructors = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            fields = csv_split(line)
            instructors[fields[0]] = fields[1:]
    return instructors


def read_books(filename):
    books = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            book, link = csv_split(line)
            books[book] = link
    return books

def count_resource_columns(config):
    """
    Count the number of columns of the form resources0, resource1, etc.
    Write warning if columns not standard.
    """
    column_numbers = []
    for key in config:
        #  should switch to walrus operator
        match = re.match('resources(\d+)', key)
        if match:
            column_numbers.append(match.group(1))
    column_numbers = sorted(int(x) for x in column_numbers)
    if column_numbers != list(range(len(column_numbers))):
        raise ValueError("Resource column labels ('resources*') in config.csv must be consecutive from 0")
    return len(column_numbers)

def get_resource_columns(resources):
    """Get the number of resource columns from the resources, and fill with substitution strings"""
    for value in resources.values():
        count = len(value)
        break

    return [f'%resources{d}%' for d in range(count)]

def read_resources(filename, books, n_columns):
    """
    Read the resources (recommended readings, videos, etc)
    from the given file.

    Returns: a dict (keyed by repo name)
             of a list (for each column)
             of a list of the resources
    """
    resources = {}
    with open(filename) as f:
        for line in f:
            # comment, skip blank lines
            if line[0] == '#' or not line.strip():
                continue
            # end of file character
            if line[0] == '$':
                break
            if line[0] == '?':
                optional = True
                line = line[1:]
            else:
                optional = False

            fields = csv_split(line)
            if len(fields) >= 4:
                repo, column, title, link = fields[:4]
                column = int(column)
                if link in books:
                    link = books[link]
                text = f'[{title}]({link})'
                if len(fields) >= 5:
                    text += f' ({",".join(fields[4:])})'
            else:
                raise ValueError(f'Resources line has {len(fields)} fields: {line}')
            if optional:
                text += '(Optional)'

            if repo not in resources:
                resources[repo] = [[] for _ in range(n_columns)]

            resources[repo][column].append(text)

    return resources


def read_days(filename):
    """Read the days.csv file
    Returns a dictionary of weeks with
        keys of the week names, and
        values of dictionaries of days with
            keys of the dates, and
            values of lists of Repo objects
    """
    weeks = {}
    with open(filename) as f:
        for line in f.readlines():
            if line[0] == '!':
                week = line[1:].strip()
                if week in weeks:
                    raise ValueError('Each week in days.csv must have a unique name')
                weeks[week] = {}
            elif line[0] == '#' or not line.strip():
                continue
            else:
                fields = csv_split(line)
                weeks[week][fields[0]] = [Repo(s) for s in fields[1:]]
    return weeks

def read_config(filename):
    config = {}
    with open(filename) as f:
        for line in f.readlines():
            if not line.strip() or line[0] == '#':
                continue
            key, value = csv_split(line)
            config[key] = value
    for required_key in ['solutions', 'cohortid', 'campus']:
        if required_key not in config:
            print(f"Key {required_key} missing from {filename}",
                  file=sys.stderr)
    return config

def format_weeks(weeks):
    """Return string with table of contents for the course outline"""
    out = '| Date | Topic |\n| --- | --- |\n'
    for week in weeks:
        # generate link text. This is not comprehensive, and should be replaced
        # by whatever is used to generate the html
        link = re.sub('[ :]+', '-', week.strip().lower())
        #name = re.sub('.*:', '', week).strip()
        name = week.strip()
        first_day = list(weeks[week])[0]
        # remove day of week. Again, this is fragile
        first_day = re.sub('[ A-Za-z]', '', first_day)
        out += f'| {first_day} | [{name}](#{link})\n'
    return out


def format_days(weeks, descriptions, instructors, resources):
    """Return string with daily schedule for the course outline"""

    resource_columns = get_resource_columns(resources)

    extras = set(resources) - set(descriptions)
    if extras:
        print(f"Warning: Missing Description for repos: {extras}", file=sys.stderr)

    out = ''
    for week in weeks:
        out += f"<br/>\n\n### {week}\n"


        line1 = "| Day "
        line2 = "|:--:"
        for resource_column in resource_columns:
            line1 += f"| {resource_column}"
            line2 += "|:------------------------------" 
        line1 += "| Repos (Standards) "
        line2 += "|:--"
        if instructors is not None:
            line1 += "| Lead "
            line2 += "|:--:"
        line1 += "| Lecture Materials | \n"
        line2 += "|:--:| \n"
        out += line1 + line2

        for day in weeks[week]:
            out += f'|{day}| '
            repos = weeks[week][day]

            # resources
            for i, resource_column in enumerate(resource_columns):
                for repo in repos:
                    if not repo:
                        continue
                    if repo.name in resources:
                        for resource in resources[repo.name][i]:
                            out += resource + ' <br/> '
                out += ' | '

            # assignment repos
            for repo in repos:
                if not repo.name:
                    continue
                # is it an actual repo, or just some text?
                if not repo.assignment:
                    out += repo.name + ' <br/> '
                else:
                    if repo.branch is None:
                        out += f'[{descriptions[repo.name]}]({repo_root + repo.name}) '
                    else:
                        out += f'[{descriptions[repo.name]}]({repo_root + repo.name}/tree/{repo.branch}) '

                    if os.path.exists(f'../standards/{repo.name}.md'):
                        out += f'([std](standards/{repo.name}.md))'
                    else:
                        print(f'Missing standards for {repo.name}',
                              file=sys.stderr)
                    out += ' <br/>'

            # instructors
            if instructors is not None:
                instructor_list = []
                for repo in repos:
                    if not repo:
                        continue
                    if repo.name in instructors:
                        instructor_list.extend(instructors[repo.name])
                    elif repo.assignment:
                        print(f'No instructors listed for {repo.name}',
                              file=sys.stderr)

                    instructor_list = dedup_list(instructor_list)
                out += f'| {", ".join(instructor_list)}'
            out += ' | '

            # lectures
            # NB this is ugly
            time = 'AM'
            for repo in repos:
                if not repo:
                    continue
                if repo.lecture:
                    out += f'[{time}]({lect_root + repo.name}) <br/> '
                    if time == 'AM':
                        time = 'PM'
            out += '|\n'
    return out

def render_template(filename, **kwargs):
    with open(filename) as f:
        text = f.read()
        for kwarg in kwargs:
            text = re.sub(f'\%{kwarg}\%', kwargs[kwarg], text)
    return text


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("""Usage:
python build_outline.py
Example:
python build_outline.py
""", file=sys.stderr)
        exit()


    weeks = read_days('days.csv')
    descriptions = read_descriptions('descriptions.csv')
    if os.path.isfile('instructors.csv'):
        instructors = read_instructors('instructors.csv')
    else:
        instructors = None
    books = read_books('books.csv')
    config = read_config('config.csv')

    n_columns = count_resource_columns(config)    
    resources = read_resources('resources.csv', books, n_columns)

    main = ''
    if config['campus'].lower() == 'main':
        main = """<h2>This is the main branch of the course outline.
               Links and dates may not match any particular campus.
               Use the branch corresponding to your cohort.</h2>
               """
    text = render_template('template.md',
                           main=main,
                           weeks=format_weeks(weeks),
                           days=format_days(weeks,
                                            descriptions,
                                            instructors,
                                            resources),
                           **config)
    print(text)
