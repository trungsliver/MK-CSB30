# ========== FOR LOOP - Vòng lặp hữu hạn =============
# Vòng lặp hữu hạn: vòng lặp biết trước số lần lặp

# Cú pháp đầy đủ: range(start, stop, step)
    # start: giá trị bắt đầu (không bắt buộc, mặc định = 0)
    # stop: giá trị kết thúc (bắt buộc)
    # step: bước nhảy (không bắt buộc, mặc định = 1)
# lưu ý: chạy từ start đến stop - 1 (không bào gồm stop)

# TH1: range(start, stop, step)
for i in range(1, 10, 1):
    print(i, end = ' ')
print()

# TH2: range(start, stop)
for i in range(5, 15):  # range(5, 15, 1)
    print(i, end = ' ')
print()

# TH3: range(step)
for i in range(8):      # range(0, 8, 1)
    print(i, end = ' ')
print()

# =========== WHILE LOOP - Vòng lặp vô hạn ===========
# Vòng lặp vô hạn - không biết trước số lần lặp
# Lặp đến khi nào điều kiện sai thì dừng

# Ví dụ: In ra các số từ 0 đến 5
for i in range(6):
    print(i, end = ' ')
print()

i = 0
while i <= 5:
    print(i, end = ' ')
    i = i + 1   # i += 1
print()

# Các lệnh điều khiển vòng lặp
    # break: thoát khỏi vòng lặp, bỏ qua tất cả các lần lặp còn lại
    # continue: bỏ qua lần lặp hiện tại, tiếp tục với lần lặp tiếp theo
print("\nSử dụng break:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')

print("\nSử dụng continue:")
for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')