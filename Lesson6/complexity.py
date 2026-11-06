# COMPLEXITY - ĐỘ PHỨC TẠP CỦA THUẬT TOÁN

# Khái niệm thuật toán: tập hợp các bước để giải quyết 1 vấn đề

# Độ phức tạp của thuật toán:
    # Dùng để đo lường hiệu quả của thuật toán
    # Biểu diễn bằng Big-O notation
        # Độ phức tạp: (O) = n * số phép toán (số bước)
        # n là kích thước của dữ liệu đầu vào

# Ví dụ:

# O(1) - độ phức tạp hằng số (constant): gán, nhập, xuất, tính toán 
name = 'Duc Trung'
print(name) 
print(1+1)

# O(n) - tuyến tính (linear)
a = [1, 2, 3, 4, 5]     # n = 5
for item in a:
    print(item)          # số bước = n = 5

# O(n^2) - bình phương (quadratic): 2 vòng lặp lồng vào nhau
    # In ra bảng cửu chương từ 1 đến 10
for i in range(1, 11):
    print(f'\nBảng cửu chương {i}:')
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')

# O(log n) - logarit (mặc định là log2(n))
    # Ví dụ: 2^3 = 8, log2(8) = 3

# Đề bài: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random) trong khoảng [1,100]
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
import random
special_number = random.randint(1, 100)
print('Số đặc biệt là:', special_number)  # In ra số đặc biệt để kiểm tra

guess = int(input('Nhập số bạn đoán (1-100): '))
count = 1

while guess != special_number:
    if guess < special_number:
        print('Số bạn đoán nhỏ hơn số đặc biệt')
    else:
        print('Số bạn đoán lớn hơn số đặc biệt')
    guess = int(input('\nNhập số bạn đoán (1-100): '))
    count += 1

print('Chúc mừng bạn đã đoán đúng số đặc biệt:', special_number)
print('Số lần bạn đoán là:', count)