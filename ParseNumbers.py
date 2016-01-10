import re

# Ctrl - /    <= to comment out lines


file_name = 'regex_sum_42.txt'
def findnum(text_to_parse):
    list_of_nums = re.findall(r'\b([0-9]+)\b', text_to_parse)
    #list_of_nums = re.findall('(\w*[0-9]+\w*)', text_to_parse)
    return (list_of_nums)

def get_total(num_list):
    total = 0
    for number_str in num_list:
        #if (number_str.isdigit()):
            number = int(number_str)
            total = total + number
    return(total)

#open file and look through lines
text_file = open(file_name)
my_total = 0
for line in text_file:
    line = line.rstrip()
    num_list = findnum(line)
    print num_list
    my_total += get_total(num_list)

print "Grand total is:", str(my_total)


# total = 0
# for number_str in num_list:
#     number = int(number_str)
#     total = total + number
#
# print total
