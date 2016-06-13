
import os
#from hurry.filesize import size

def convert_human(size):
    if (size >= 1024):
        size_hr = str(int(round(size/1024.0, 0))) +"K"
    else:
        size_hr = str(size)
    return(size_hr)

def gettop10(directory_path):
    whole_list = []
    single_item = []
    os.chdir(directory_path)
    print "you are here:", directory_path
    list_of_files = os.listdir(directory_path)
    print type(list_of_files)
    # print "here are the files", list_of_files
    for file in list_of_files:
        print "File name:", file
        full_path_to_file = str(directory_path) + "\\" + str(file)
        #print "full path:", full_path_to_file
        size = os.path.getsize(full_path_to_file)
        print type(size)
        print "\tSize:", size
        single_item = [full_path_to_file, os.path.getsize(full_path_to_file)]
        #print "Single item:", single_item
        whole_list.append(single_item)
    return(whole_list)

def getKeyToSort(item):
    # item is a list, return the value at the position that you want
    # the list of lists to be sorted by
    # in our case it is the second item, the size
    return item[1]

def sortfiles(array_files):

    sortedList = sorted(array_files, key = getKeyToSort)
    # student_tuples = [
    # ('john', 'A', 15),
    # ('jane', 'B', 12),
    # ('dave', 'B', 10),
    # ]
    # >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    # Python supports the creation of anonymous functions
    # (i.e. functions that are not bound to a name) at runtime,
    # using a construct called "lambda".

        # >>> def getKey(item):
        # ...     return item[0]
        # >>> l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
        # >>> sorted(l, key=getKey)
        # [[1, 43], [2, 3], [3, 34], [6, 7], [24, 64]]

    return (sortedList)

def printfiles(sorted_files):
    for file in sorted_files:
        print "name: ", file[0], "\n"
        print "\t size:", convert_human(file[1]), "\n"

    return

cwd = os.getcwd()
unsortedList = gettop10(cwd)
sortedList = sortfiles(unsortedList)
printfiles(sortedList)


#top_doc = 'C:\Users\RNICHOLL\Documents'
#gettop10(top_doc)
