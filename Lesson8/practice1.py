# ============== ÔN TẬP ==============
# Bài 1: Cho 2 mảng số nguyên nums1 và nums2
# Viết chương trình trả về mảng là giao của 2 mảng trên
# Đánh giá độ phức tạp của thuật toán

    # Khởi tạo 2 danh sách
nums1 = [i for i in range(5, 16)]   # 5 đến 15
nums2 = [i for i in range(10, 21)]  # 10 đến 20 

    # Cách 1: Độ phức tạp O(n^2)
arr1 = []   # Danh sách lưu phần tử chung
for item1 in nums1:
    for item2 in nums2:
        if item1 == item2:
            arr1.append(item1)
print("Các phần tử chung:", arr1)

    # Cách 2: Độ phức tạp O(n log m)
def binary_search(arr, target):         # O(log n)
    # left, right chỉ số index bắt đầu và kết thúc (chặn đầu và chặn cuối)
    left = 0
    right = len(arr) - 1

    while left <= right:  
        # Tìm chỉ số index của phần tử ở giữa
        mid = (left + right) // 2
        # So sánh phần tử ở giữa với target
        if arr[mid] == target:
            return mid    # Trả về vị trí của phần tử nếu tìm thấy
        elif arr[mid] < target:
            left = mid + 1  # Tìm kiếm nửa bên phải
        else:
            right = mid - 1  # Tìm kiếm nửa bên trái
    return -1  # Trả về -1 nếu không tìm thấy

arr2 = []
if len(nums1) < len(nums2):
    # swap phần tử 2 danh sách => nums1 luôn là danh sách dài hơn
    nums1, nums2 = nums2, nums1 
for item in nums2:  # O(n)
    if binary_search(nums1, item) != -1:  # O(log m)
        arr2.append(item)

print("Các phần tử chung:", arr2)

# Bài 2: Cho mảng nums gồm n quả bóng có màu đỏ, trắng, xanh.
    # Viết chương trình sắp xếp mảng này sao cho:
    # những quả bóng có màu giống nhau thì được sắp xếp cạnh nhau
    # có thứ tự từ đỏ đến trắng đến xanh
    # Đánh giá độ phức tạp của thuật toán.
nums = ['red', 'white', 'blue', 'red', 'white', 'blue', 'red', 'white', 'blue']

def sort_balls(arr): # O(n)
    # Biến đếm số lượng mỗi màu
    count_red, count_white, count_blue = 0, 0, 0
    for item in arr:
        if item == 'red':
            count_red += 1
        elif item == 'white':
            count_white += 1
        elif item == 'blue':
            count_blue += 1
    # Tạo mảng mới với các quả bóng đã được sắp xếp
    sorted_arr = ['red'] * count_red + ['white'] * count_white + ['blue'] * count_blue
    return sorted_arr

print("Mảng sau khi sắp xếp:", sort_balls(nums))

# ================= LUYỆN TẬP =================
# Thực hiện và xác định độ phức tạp thuật toán của các bài tập sau

# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers: list):  # O(n)
    total = 0
    for num in numbers:
        if num % 2 != 0:  # Kiểm tra số lẻ
            total += num
    return total
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Tổng các số lẻ trong mảng:", sum_odd(arr))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n): # Độ phức tạp O(√n)
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime2(n): # Độ phức tạp O(n)
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2: return True
    else: return False

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s): # O(n)
    # strip(): loại bỏ khoảng trắng ở đầu và cuối chuỗi
    # split(): tách chuỗi sau mỗi khoảng trắng
    words = s.strip().split()  
    return len(words)  # Trả về số lượng từ
print("Số lượng từ trong chuỗi:", count_words("  Hello world! This is a test.  "))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n): # O(log(10) n)
    total = 0
    while n > 0:
        total += n % 10  # Lấy chữ số cuối cùng
        n //= 10         # Loại bỏ chữ số cuối cùng
    return total
print("Tổng các chữ số của số 12345:", sum_of_digits(12345))

def sum_of_digits2(n): # Độ phức tạp O(log(n)) 
    total = 0
    # len(str(n)): số chữ số của n
    for i in range(len(str(n))):
        total += int(str(n)[i])
    return total

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(numbers): # O(n)
    max_value = numbers[0]
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
    return max_index

def find_max2(numbers): # Độ phức tạp O(n)
    max_value = max(numbers)
    for i in range(len(numbers)):
        if numbers[i] == max_value:
            return i

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.

    # Cách 1: Sử dụng vòng lặp for
def sum_to_n(n): # O(n)
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Tổng các số từ 1 đến 10:", sum_to_n(10))

    # Cách 2: Sử dụng Công thức gauss
def sum_to_n2(n): # O(1)
    return n * (n + 1) // 2  # Công thức tính tổng các số từ 1 đến n
print("Tổng các số từ 1 đến 10:", sum_to_n2(10))