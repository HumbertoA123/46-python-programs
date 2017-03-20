import functools
'''
If you are using python 3 you will have to import the functools module to use
the reduce() function. If you are using python2 you don't have to do anything.
'''

lst = [20, 35, 100, 5, 36, 13]

max_num = functools.reduce(lambda a, b : a if a > b else b, lst)
print (lst)
print ('Max number in list: ', max_num)