# FUNGSI DALAM PYTHON
# Percobaan Fungsi 1 : Fungsi Berparameter
def message(number):
    print("Enter a number :", number)

number = 1234
message(1)
print(number)

# Percobaan Fungsi 2 : Multiparameter
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

# Percobaan Fungsi 3 : Perbedaan 3 percobaan
# Fungsi 1
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

# Fungsi 2
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

# Fungsi 3
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

# Percobaan Fungsi 4
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name= "Bond")
introduction(last_name= "Skywalker", first_name= "Luke")

# Percobaan Fungsi 5
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
adding(4, 3, c = 2)

# Percobaan Fungsi 6 : return, list, fungsi
# Pertama
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s
print(list_sum([5, 4, 3]))

# Kedua
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem
    
    return s
print(list_sum([5]))

# Bagaimana dengan ini?
def strange_list_fun(n):
    strange_list =[]

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list

print(strange_list_fun(5))

# Percobaan Fungsi 7 : Kasus BMI
def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))

# Percobaan fungsi 8 : Membuat fungsi dengan or atau and
# Fungsi pertama
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Fungsi kedua
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Fungsi ketiga
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

# Percobaan Fungsi 9 : Rumus segitiga
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** .5))
