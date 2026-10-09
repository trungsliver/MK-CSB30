# Function (hàm / chương trình con)
# Ý nghĩa: tập hợp các câu lệnh có thể tái sử dụng

    # Hàm không có giá trị trả về
def say_hello():
    print("Hello Trung!")
    print("Hello Minh Nhật!")
# say_hello()
# say_hello()

    # Hàm có tham số truyền vào
def say_hello_to(name):
    print("Hello", name)
# say_hello_to("Linh")
# say_hello_to("Huong")

    # Hàm có giá trị trả về
def add(a:float, b:float):
    return a + b
print("Tổng:", add(5, 7))