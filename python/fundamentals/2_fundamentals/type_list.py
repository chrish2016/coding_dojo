ml = ['magical unicorns',19,'hello',98.98,'world']
il = [2,3,1,7,4,12]
sl = ['magical','unicorns']

def id_list_type(lst):
    new_str = ' '
    new_sum = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            new_sum += value
        elif isinstance(value, str):
            new_str += value
    
    if new_str and new_sum:
        print "The array you entered is of mixed type"
        print "String:", new_str
        print "Total:", new_sum
    
    elif new_str:
        new_str += value
        print "The list you entered is a sentence."
        print "String: ", new_str


print id_list_type(ml)
print id_list_type(il)
print id_list_type(sl)


