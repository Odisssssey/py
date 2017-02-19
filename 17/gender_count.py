import pandas as pd
import os

def top_sum_baby(all_names, years):

    sort_gender = all_names.groupby('Gender').sum()
    n = 1
    sort_year = {}
    sort_year_f = []
    sort_year_m = []
    while (n < len(years) + 1):
        arg = 'row.Count'+str(n)
        f = sort_gender.apply(lambda row: [eval(arg)], axis=1)[0][0]
        sort_year_f.append(f)
        m = sort_gender.apply(lambda row: [eval(arg)], axis=1)[1][0]
        sort_year_m.append(m)
        n += 1
    sort_year['F'] = sort_year_f
    sort_year['M'] = sort_year_m

    return sort_year

def open_file(path, all_names, n):
    names = pd.read_csv(path, names=['Name', 'Gender', 'Count'])
    suff = [str(n), str(n+1)]

    if(n == 0):
        return names
    else:
        all_names = pd.merge(all_names, names, on=['Name', 'Gender'], suffixes=(suff))
        return all_names


def print_top_year(years):
    directory = os.path.dirname(os.path.realpath(__file__))
    my_directory = os.path.join(directory, "names")
    all_names = []
    n = 0

    for year in years:
        my_year = "yob" + str(year) + ".txt"
        my_file = os.path.join(my_directory, my_year)
        all_names = open_file(my_file, all_names, n)
        n += 1

    total_top = top_sum_baby(all_names, years)

    return total_top


print(print_top_year([2005, 2006, 2007, 2008, 2009, 2010]))
