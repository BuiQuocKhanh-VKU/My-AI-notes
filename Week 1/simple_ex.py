# Khai bao cac kieu du lieu
x = 10
y = "Hello, Khanh!"
z = [1, 2, 3, 4, 5]
t = (10, 20,30)
d = {"name": "Khanh", "age": 20}

# In ra cac kieu du lieu
print("x:", x, "Type:",  type(x))
print("y:", y, "Type:",  type(y))
print("z:", z, "Type:",  type(z))   
print("t:", t, "Type:", type(t))
print("d:", d, "Type:", type(d))

#####################################
print("########################################")
# Vong lap for
numbers = [12,20,30,40,50]
for num in numbers:
    print(num)

# Vong lap for voi range
for i in range(5): 
    print("for with range:", i)  

# Vong lap for voi range va buoc nhay
for i in range(0, 10, 2):
    print("for with steps:", i)

# Vong lap for voi chuoi
for char in "Hello":
    print("Character:", char)

# Vong lap for voi tuple
for item in (1, 2, 3):
    print("Tuple item:", item)  

# Vong lap for voi dictionary
for key, value in {"name": "Khanh", "age": 20}. items():
    print("Key:", key, "Value:", value)

# Vong lap for voi list
for index, value in enumerate([10, 20, 30, 40]):
    print("Index:", index, "Value:", value)     

# Vong lap while
i = 1
while i<5:
    print(i)
    i += 1  # Tang i len 1

# Vong lap while voi break
i = 1   
while i < 10:
    if i == 7:
        break  # Dung vong lap khi i = 5
    print(i)
    i += 1

# Tinh tong tu 1 den 10
total = 0
for s in numbers:
    total += s  # Cong tong cac so trong list
print("Tong tu 1 den 10:", total)

######################################
print("########################################")
# Su dung ham trong python'''
"""def function_name(parameters):
    return value
    """
def greeting (name):
    print("Hello "+ name + "!")

greeting("Khanh")  # Goi ham greeting voi tham so "Khanh"   

##
def add (a,b):
    return a + b

result = add(5, 10)  # Goi ham add voi tham so 5 va 10
print("Tong:", result)  # In ra ket qua tong

##
def is_even(number):
    return number % 2 == 0

# Gọi hàm và in ra kết quả
print(is_even(6))  # True
print(is_even(7))  # False

##
#len(): Trả về độ dài của một đối tượng (danh sách, chuỗi, tuple, v.v.).
print("####")
my_list = [1, 2, 3, 4, 5]
print( "len: ",len(my_list))  # In ra: 5

#max(): Trả về giá trị lớn nhất trong một dãy.
numbers = [1, 2, 3, 4, 10]
print( "max: ",max(numbers)) 

#sum(): Tính tổng các phần tử trong một dãy.
numbers = [1, 2, 3, 4, 5]
print("sum: ",sum(numbers))  # In ra: 15

#sorted(): Sắp xếp một dãy và trả về một danh sách mới.
unsorted_list = [5, 2, 9, 1, 5, 6]  
sorted_list = sorted(unsorted_list)
print("sorted: ",sorted_list)  # In ra: [1, 2, 5, 5, 6, 9]

#filter(): Lọc các phần tử trong một dãy dựa trên một hàm điều kiện.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  
print("filter: ",even_numbers)  # In ra: [2, 4, 6]

#range(): Tạo ra một dãy số theo một phạm vi cho trước.
for i in range(1,6):  # Tạo ra dãy số từ 0 đến 5
    print("range: ",i)  # In ra: 0, 1, 2, 3, 4, 5

#round(): Làm tròn một số đến một số chữ số thập phân nhất định.
number = 3.14159
print(round(number, 2))  # In ra: 3.14

#type(): Trả về kiểu dữ liệu của đối tượng.
my_var = 10
print(type(my_var))  # In ra: <class 'int'>

#zip(): Kết hợp các phần tử từ nhiều dãy thành một dãy mới.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("zip: ",zipped)  # In ra: [(1, 'a'), (2, 'b'), (3, 'c')]

#map(): Áp dụng một hàm cho mỗi phần tử trong một dãy.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  
print("map: ",squared_numbers)  # In ra: [1, 4, 9, 16, 25]

#enumerate(): Trả về một dãy các cặp (chỉ số, giá trị) từ một dãy.
my_list = ['a', 'b', 'c']   
for index, value in enumerate(my_list):
    print("enumerate: ",index, value)  # In ra: 0 a, 1 b, 2 c

#input(): Nhận dữ liệu từ người dùng.   
name = input("Enter your name: ")
print("Hello, " + name)
