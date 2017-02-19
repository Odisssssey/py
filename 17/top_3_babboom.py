import pandas as pd
import os

def top_sum_baby(all_names, years):
    n = 1
    arg = ['row.Name', 'row.Gender', 'row.Count1']

    if (len(years) % 2 == 0):
        while (n < len(years)+1):
            new_arg = arg[2]+'+row.Count'+str(n)
            arg.pop()
            arg.append(new_arg)
            n +=1
    else:
        while (n < len(years)+1):
            if (n == len(years)):
                new_arg = arg[2] + '+row.Count'
            else:
                new_arg = arg[2]+'+row.Count'+str(n)
            arg.pop()
            arg.append(new_arg)
            n +=1

    my_top = all_names.apply(lambda row:[eval(arg[0]), eval(arg[1]), eval(arg[2])] , axis=1)

    Sort_top =[]
    for line in my_top:
        Sort_top.append(line)

    top = pd.DataFrame(Sort_top, columns=['Name', 'Gender', 'Count'])
    sort_count = top.sort_values(by='Count', ascending=False).head(3).apply(lambda row:[eval(arg[0])] , axis=1)
    Sort_top = []
    for line in sort_count:
        Sort_top.append(line[0])

    return Sort_top

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


print(print_top_year([1990, 1991, 1993, 1980]))
