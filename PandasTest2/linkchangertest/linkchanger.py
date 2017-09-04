import os

list_of_changes = {'http://bit.ly/chiporders':'chipotle.tsv', 'http://bit.ly/uforeports':'ufo.csv', 'http://bit.ly/imdbratings':'imdb_1000.csv', 'http://bit.ly/drinksbycountry':'drinks.csv'}
pathtofile = './test/'

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            #print "{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        #print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)

for fname in os.listdir(pathtofile):
    if fname.endswith(".py"):
        for a in list_of_changes:
            inplace_change(pathtofile + fname, a, list_of_changes[a])


