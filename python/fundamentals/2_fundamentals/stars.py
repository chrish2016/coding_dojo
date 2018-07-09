# Part 1

val = [34, 8, 12, 4, 14, 3]

def draw_stars(val):
    for x in val:
        print "*" * x

draw_stars(val)


# Part 2

val = ["honky", "Will", 12, "Bob", 124, "Joe"]

def stars_part2(val):
    for x in val:
        if isinstance(x, int):
            print "*" * x
        
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length
        

stars_part2(val)




































# def stars(nums):
#     for x in nums:
#         print "*" * x


# nums = [6,2,5,7,9]
# stars(nums)


# def stars_people():
#     starlist = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#     new_str = ' '
#     new_sum = 0

#     for x in starlist:
#         if isinstance(x, int) or isinstance(x, float):
#             print "*" * x    
#         elif isinstance(x, str):
#             length = len(x)
#             letter = x[0].lower()
#             print letter * length
# stars_people()
