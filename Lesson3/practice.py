# Bài 1: Tạo lớp Rectangle với các thuộc tính: length, width.  
# Tạo phương thức tính diện tích và chu vi của hình chữ nhật. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print("\n===== RECTANGLE INFO =====")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print("===========================")

rectangle1 = Rectangle(5, 3)
rectangle1.display_info()

# Bài 2: Tạo lớp BankAccount với các thuộc tính: 
            # account_number: số tài khoản 
            # owner: tên chủ tài khoản
            # balance: số dư tài khoản
    # Tạo phương thức:
            # deposit(amount): nạp tiền vào tài khoản
            # withdraw(amount): rút tiền từ tài khoản
            # display_balance(): hiển thị số dư tài khoản
            # (amount: số tiền nạp/rút theo đơn vị $)
class BankAccount:
    def __init__ (self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display_info(self):
        print("\n===== BANK ACCOUNT INFO =====")
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance}")
        print("==============================")

    def deposit(self, amount):
        if amount <= 0:
            print('Lỗi! Số tiền nạp không hợp lệ!')
        else:
            # Cập nhật số dư
            self.balance += amount
            print(f"Đã nạp ${amount} vào tài khoản!")
        self.display_info()

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print('Lỗi! Số tiền rút không hợp lệ!')
        else:
            # Cập nhật số dư
            self.balance -= amount
            print(f"Đã rút ${amount} từ tài khoản!")
        self.display_info()

acc = BankAccount("99999", "Khải Hoàng", 1000)
acc.display_info()
    # Nạp thành công
acc.deposit(500)
    #  Nạp thất bại
acc.deposit(-100)
    # Rút thành công
acc.withdraw(200)
    # Rút thất bại 
acc.withdraw(2000)
acc.withdraw(-50)
# Bài 3:
    # Tạo class Animal gồm các thuộc tính: tên, loài
    # Viết 2 phương thức cho class Animal

    # Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
    # Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
    # Viết 1 phương thức mới cho class Dog

# Bài 4:
    # Hãy xây dựng các lớp cha và lớp con như đã xác định. Lưu ý lớp cha có những đặc điểm sau:
    # 	hang: Tên của hãng xe
    # 	mau_sac: Màu sắc của xe
    # 	gia_tien: GIá tiền của xe.
    # Phương thức khoi_dong(): In ra màn hình “Xe {hãng} đang khởi động”

    # Lớp con có những phương thức sau khác lớp cha:
    # 	Phương thức dap_bang_hai_chan(): In ra màn hình “Xe {hãng} đang được đạp về phía trước”
    # 	Phương thức chay_bang_bon_banh(): In ra màn hình “Xe {hãng} đang chạy về phía trước bằng động cơ”
    # Hãy chọn phương thức phù hợp với từng lớp và hoàn thiện các lớp con có sử dụng kế thừa.