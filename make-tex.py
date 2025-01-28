#!/usr/bin/env python3

from jinja2 import FileSystemLoader, Environment
import datetime
import json
import operator

if __name__ == '__main__':
    talks = list()
    with open('data.json') as jsonfile:
        # print(jsonfile)
        content = json.load(jsonfile)
        # print(data)
        # content.sort(key=operator.itemgetter('Start', ''))     # sort by start time
        for row in content:
            if row['Proposal state'] == 'confirmed' and row['Track']['en'] == 'DNS':
                title = row['Proposal title']
                talks.append({'title': title, 'subtitle': "",
                              'presenter': ', '.join(row['Speaker names']),
                              'time': datetime.datetime.fromisoformat(row['Start']).astimezone().strftime("%H:%M")})

    talks.sort(key=operator.itemgetter('time'))

    loader = FileSystemLoader(searchpath="./")
    env = Environment(loader=loader)
    template = env.get_template('FOSDEM-intermission-slides.j2')
    r = template.render(talks=talks)
    print(r)
