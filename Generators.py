''' Generators Intro
    Advantages over the List'''
#Functions returs squring numbers
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)

#Result : [1, 4, 9, 16, 25, 36]

#Convert function to Generator
print("***Generator***")
def square_numbers_gen(nums):
    result = []
    for i in nums:
        yield (i*i)
my_nums_gen = square_numbers_gen([1,2,3,4,5])
print(my_nums_gen)
#Result: <generator object square_numbers at 0x7fc7644da840>
'''Reason for the above result is Generators would not hold the 
entire result in the meomry.It yilelds one result at a time.really, it is waiting for us ask for next result.'''
print(next(my_nums_gen))
#Result:1
print(next(my_nums_gen))
#Result:4
print(next(my_nums_gen))
#Result:9
print(next(my_nums_gen))
#Result:16
print(next(my_nums_gen))
#Result:25
#print(next(my_nums_gen))
#Result:Error: StopIteration
''' To Avoid the Error write for loop.'''
for num in my_nums_gen:
    print(num)
#Result:1
#4
#9
#16
#25
'''for loop knows when to stop.'''

print('******* List Comprehesion link to generator *************')
# this list comprehension does the same job.
my_lc_nums = [x*x for x in [1,2,3,4,5]]

print(my_lc_nums)
#Result:[1, 4, 9, 16, 25]
for num in my_lc_nums:
    print(num)
#Result:1
#4
#9
#16
#25

print(' we can convert this list comprehesion to Generator')
#replace square brackets with the curve.
my_lcg_nums = (x*x for x in [1,2,3,4,5])

print(my_lcg_nums)
#Result:[1, 4, 9, 16, 25]
for num in my_lcg_nums:
    print(num)
print('printing all the result from the gen function')
my_lcg_nums = (x*x for x in [1,2,3,4,5])
print(list(my_lcg_nums))
#Result:[1, 4, 9, 16, 25]
#Observation: If i run the above immedtely after for loop. result was empty. as it it As it already yielded the results.

'''Generator Is very usefull when we are working with huge volume of data.
as it doesnot hold the memory.you will loose the performance.'''
# lets see an example.

#import mem_profile
import memory_profiler
import random
import time

names = ['thulasi','kumar','kandahti','saanvi','hem','supriya']
majors = ['Computer','Electronic','Electric','Mech','Communication','Business']

#print('Memory (Before): {}Mb'.format(mem_profile.memory_useage_resource()))
print('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))
#regular function
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id': i,'name': random.choice(names),'major': random.choice(majors)}
        result.append(person)
    return result
#Generator
def People_gene(num_people):
    for i in xrange(num_people):
        person = {'id': i,'name': random.choice(names),'major': random.choice(majors)}
        yield person

#testing the function first
t1  = time.clock()
people = People_gene(100000)
t2  = time.clock()

#print('Memory (After) : {}Mb'.format(mem_profile.memory_useage_resource))
print('Memory (After): {}Mb'.format(memory_profiler.memory_usage()))
print('Took {} Seconds'.format(t2-t1))
# ******* Result for List
#Memory (Before): [43.5625]Mb
#Memory (After): [71.2109375]Mb
#Took 0.20999999999999996 Seconds

# ******* Result for Gene
#Memory (Before): [43.5625]Mb
#Memory (After): [43.5625]Mb
#lTook 0.0 Seconds
