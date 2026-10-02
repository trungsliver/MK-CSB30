# Variables - Biến số
    # Dùng để lưu trữ dữ liệu
    # Có thể thay đổi giá trị khi lập trình
name = 'Duc Trung'
a, b, c = 1, 2, 3

# Quy tắc đặt tên biến:
    # chỉ gồm chữ cái tiếng anh, số, dấu gạch dưới
    # không được bắt đầu bằng số
    # không được trùng với từ khóa của Python

# 2 kiểu đặt tên biến:
    # camelCase: viết hoa chữ cái đầu của mỗi từ, trừ từ đầu tiên
myFullName = 'Bui Duc Trung'
    # snake_case: mỗi từ cách nhau bởi dấu gạch dưới
my_full_name = 'Bui Duc Trung'

# Data types - Kiểu dữ liệu
    # string - Chuỗi / xâu ký tự
name = 'Duc Trung'
    # int (integer): số nguyên
age = 2
    # float: số thực (số thập phân)
score = 8.5
    # boolean/bool: logic, chỉ có giá trị True/False
isMale = True

# 4 cách hiển thị dữ liệu
    # Cách 1: Dùng dấu +
print('Name: ' + name)
    # Cách 2: Dùng dấu ,
print('Age:', age)
    # Cách 3: Dùng f-string
print(f'Tôi tên là {name}, đang {age} tuổi, điểm TB = {score}')
    # Cách 4: Hiển thị dữ liệu trên nhiều dòng
print(f'''
===== THÔNG TIN =====
Họ tên: {name}
Tuổi: {age}
Điểm: {score}
Giới tính nam: {isMale}
=====================''')

    # Lưu ý:
        # \n: xuống dòng
print('Dòng 1 \nDòng 2 \nDòng 3')
        # \t: tab (1 tab = 4 khoảng trắng)
print('Cột 1\tCột 2\tCột 3')
        # end = ' ' : thay đổi ký tự cuối cùng
print('không xuống dòng đâu', end = ' ')
print('Vẫn ở dòng trên nè') 

# Kiểm tra kiểu dữ liệu - type()
print("Kiểu dữ liệu của biến name:", type(name))
print("Kiểu dữ liệu của biến age:", type(age))
print("Kiểu dữ liệu của biến score:", type(score))
print("Kiểu dữ liệu của biến is_male:", type(isMale))

# Nhập dữ liệu - input()
    # Mặc định: dữ liệu nhập vào là string
score1 = input('Nhập điểm: ')
print('Kiểu dữ liệu score1: ', type(score1))
    # Xác định kiểu dữ liệu khi nhập
score2 = float(input('Nhập điểm: '))
print('Kiểu dữ liệu score2: ', type(score2))
