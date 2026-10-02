# Các phép toán:
    # Cơ bản: + - * /
    # Chia lấy nguyên: //
print('15 // 4 =', 15 // 4)
    # Chia lấy dư: %
print('8 % 3 =', 8 % 3)
    # Lũy thừa: **
print('2^3 =', 2**3)
    # Lưu ý: lũy thừa sẽ được thực hiện từ phải qua trái
print('2^2^3 =', 2**2**3)

# Toán tử quan hệ (phép so sánh)
    # So sánh bằng: ==
print('5 == 5:', 5 == 5)
    # So sánh khác: !=
print('5 != 5:', 5 != 5)
    #  So sánh lớn / nhỏ hơn: > < <= >=
print('5 > 5', 5 > 5)   
print('5 >= 5', 5 >= 5)         

# Toán tử logic: and (&&), or (||), not (!)
# Ví dụ: trà sữa - gàn rán

# Câu điều kiện (3 dạng)
    # Dạng thiếu
age = 2
if age >= 18:
    print('Bạn đã đủ điều kiện lái xe')

    # Dạng đủ
num = 9
if num % 2 == 0:
    print(num, 'là số chẵn')
else:
     print(num, 'là số lẻ')

    # Dạng đa nhánh
score = 8.5
if 8 <= score <= 10:
    print('Học lực: Giỏi')
elif 6.5 <= score < 8:
    print('Học lực: Khá')
elif 5 <= score <= 6.5:
    print('Học lực: Trung bình')
elif 0 <= score < 5:
    print('Học lực: Yếu')
else:
    print('Điểm không hợp lệ')