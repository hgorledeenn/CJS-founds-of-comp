names = ['Jack', 'Mulbs', 'Boxcar']

print(names)

for name in names:
    print(name)


# can multiply strings
print("="*20)


numbers = [3,4,1,2]
print(sum(numbers))

# jack = {
#     'name': 'Jack',
#     'age': 6,
#     'color': 'white'
# }

## List slicing
numbers_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18.19,20]
print(numbers_2[:3])

## 0th to 4th (not invlusive)
print(numbers_2[0:3])

## Up to the 3rd from the last
print(numbers_2[:-3])
print(numbers_2[-3:])


## if I know something works:
for url in urls:
    whatever xxx

## if I want to test if a list works (try it on the first 5)
for url in urls[:5]:
    whatever xxx