numbers = [1,1,2,3,4,5,6,7,8,9,0]
even = []

even = [i for i in numbers if i%2 == 0]
print(even)

sqr_nums = [ i*i for i in numbers]
print(sqr_nums)

#set comprehensions

s = set([1,2,3,4,5,4,5,6])
even2 = {i for i in s if i%2 == 0}
print (even2)

#dictionaries comprehensions

countries = ["Greece", "France", "Germany", "Russia"]
cities = ["Athens", "Paris", "Berlin", "Moscow"]

z = zip(countries,cities)

for a in z :
    print(a)

d = {city:country for city, country in zip(cities,countries)}
print(d)

