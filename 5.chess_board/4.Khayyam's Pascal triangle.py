#Making Kayyam`s Pascal Triangle ⨇
number_of_rows = int(input("Enter number of rows : "))

pascal_triangle = []
for row in range(1, number_of_rows + 1):  
    number = 1
    pascal_triangle.append([])
    for num in range(1, row + 1):
        pascal_triangle[row - 1].append(number) 
        number = int(number * (row - num) / num)

for row2 in pascal_triangle:
        for num2 in row2:
            print("{:5}".format(num2), end = "")
        print()
