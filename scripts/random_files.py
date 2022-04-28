import csv
import tempfile
import random
import uuid


def documents(ofs):
    themes = [
        'work', 'running', 'map', 'flower', 'cooking', 'cleaning', 'writing',
        'planning', 'club'
    ]
    situations = [
        'meeting', 'experience', 'invite', 'note', 'call', 'thought', 'date',
        'idea', 'schedule'
    ]
    contexts = [
        'at_office', 'with_Mark', 'with_Anne', 'at_night', 'in_the_morning'
    ]
    filetypes = ['.txt', '.md', '.docx', '.xlsx']

    for i in range(200):
        theme = random.choice(themes)
        situation = random.choice(situations)
        context = random.choice(contexts)
        date = f'{random.randint(2018,2022)}-{random.randint(1,12)}-{random.randint(1,31)}'
        filetype = random.choice(filetypes)
        name = f'/home/me/documents/{theme}_{situation}_{context}_{date}{filetype}'
        size = round(random.random() * 1, 6)
        value = round(random.random() * 1, 6)
        ofs.writerow([name, size, value])


def pictures(ofs):
    for place in [
            'vacation_spain_2019-07', 'christmas_2021-12', 'birthdays-2020-04'
    ]:
        for i in range(12, 19):
            for j in range(10):
                name = f'/home/me/pictures/{place}-{i}_{j}.jpeg'
                size = round(random.random() * 10, 6)
                value = round(random.random() * 1, 6)
                ofs.writerow([name, size, value])


def tempfiles(ofs):

    for i in range(100):
        name = tempfile.NamedTemporaryFile().name
        size = round(random.random() * 0.01, 6)
        value = round(random.random() * 0.001, 6)
        ofs.writerow([name, size, value])


def videos(ofs):
    for place in ['vacation_spain_2019-07', 'christmas_2021-12']:
        for i in range(12, 19):
            for j in range(random.randint(0, 5)):
                name = f'/home/me/videos/{place}-{i}_{j}.mp4'
                size = round(random.random() * 100, 6)
                value = round(random.random() * 3, 6)
                ofs.writerow([name, size, value])


with open('files.csv', 'w') as csvfile:
    ofs = csv.writer(csvfile, delimiter=',')
    ofs.writerow(["name", "size", "value"])
    documents(ofs)
    pictures(ofs)
    videos(ofs)
    tempfiles(ofs)
