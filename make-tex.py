#!/usr/bin/env python3

from jinja2 import FileSystemLoader, Environment
import csv
import operator

if __name__ == '__main__':
    talks = list()
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile)
        content = list(reader)[1:]                    # turn into list and skip header
        content.sort(key=operator.itemgetter(12))     # sort by start time
        for row in content:
            if row[7] == 'accepted' and row[8] == 'confirmed':
                talks.append({'title': row[1], 'subtitle': row[2],
                              'presenter': row[9]+' '+row[11], 'time': row[12]})

    loader = FileSystemLoader(searchpath="./")
    env = Environment(loader=loader)
    template = env.get_template('FOSDEM-intermission-slides.j2')
    r = template.render(talks=talks)
    print(r)
