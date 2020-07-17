records = [
    ('Corey', 'IOS'),
    ('Tyler', 'DS'),
    ('Logan', 'Web'),
    ('Anika', 'DS'),
    ('Carlos', 'Web')
]
track = {}


build_index(records):
    for record in records:
        name,track = record
        if track not in index:
            index[track] = []
        return index