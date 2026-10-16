# OOP - Object Oriented Programming
# Lập trình hướng đối tượng

# Tổng quát: OOP là cách mô tả thế giới thực vào chương trình máy tính

# Class (lớp): đối tượng tổng quát
# Object (đối tượng): đối tượng cụ thể

# Ví dụ: mô tả con người (Human)
    # Thuộc tính (Attribute): đặc điểm của đối tượng (tên, tuổi, giới tính)
    # Phương thức (methods): hành động của đối tượng (ăn, ngủ, đi, nói,...)

# 4 tính chất của lập trình hướng đối tượng:
    # Đóng gói (Encapsulation): che dữ liệu (password, info,...)
    # Kế thừa (Inheritance): dùng lại dữ liệu cũ
    # Đa hình (Polymorphism): cùng 1 tên hàm, hành động khác nhau
    # Trừu tượng (Abstraction): khai báo phương thức trước, ghi hành động sau

# Khai báo lớp đối tượng (class)
class Human:
    # Khởi tạo đối tượng (constructor)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} - {self.age} - {self.gender}"

    # Phương thức hiển thị thông tin
    def display_info(self):
        print("\n===== HUMAN INFO =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print("======================")

    # Phương thức hát
    def sing(self, song):
        print(f"{self.name} is singing {song}")

# Khai báo đối tượng cụ thể (object)
human1 = Human("Quang Huy", 14, "male")
human2 = Human("Xuân Tú", 18, "male")

print(human1)
human1.display_info()
human2.display_info()
human1.sing("Happy Birthday")

# Tính chất kế thừa (Inheritance)
class Student(Human):
    def __init__(self, name, age, gender, school):
        # Gọi phương thức khởi tạo của lớp cha (Human)
        super().__init__(name, age, gender)
        self.school = school

    def display_info(self):
        print("\n===== STUDENT INFO =====")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"School: {self.school}")
        print("======================")

# Khởi tạo đối tượng Student
stu1 = Student("Bảo Lâm", 15, "male", "Vinschool")
stu1.display_info()
stu1.sing("Baby Shark")