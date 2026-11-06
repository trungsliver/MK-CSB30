# ============= THUẬT TOÁN TÌM KIẾM =============
arr = [2, 5, 3, 1, 9, 7, 4, 8, 6]

# Tìm kiếm tuyến tính / tuần tự (Linear Search)
def linear_search(arr, target):         # Độ phức tạp: O(n)
    # Duyệt qua từng phần tử trong mảng
    for i in range(len(arr)):
        # Nếu tìm thấy phần tử cần tìm, trả về chỉ số của nó
        if arr[i] == target:
            return i
    # Nếu không tìm thấy, trả về -1
    return -1

# Tìm kiếm nhị phân (Binary Search)
    # Lưu ý: Danh sách cần được sắp xếp trước
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

# ============ SO SÁNH HIỆU SUẤT ============
import time, random

def measure_time(func, arr, target):
    # Thời gian bắt đầu
    start_time = time.time()
    # thực hiện hàm tìm kiếm
    func(arr, target)
    # Thời gian kết thúc
    end_time = time.time()
    # Tính thời gian thực hiện
    return end_time - start_time

# Khởi tạo 1 danh sách lớn (nhiều dữ liệu)
random_list = [random.randint(1, 999999999) for _ in range(200000000)]  # 200 triệu phần tử
target_value = random.choice(random_list)  # Chọn ngẫu nhiên 1 phần tử trong danh sách

# Linear search
linear_time = measure_time(linear_search, random_list, target_value)
print(f"Thời gian tìm kiếm tuyến tính: {linear_time:.8f} giây")

# Binary search
sorted_random_list = sorted(random_list)
binary_time = measure_time(binary_search, sorted_random_list, target_value)
print(f"Thời gian tìm kiếm nhị phân: {binary_time:.8f} giây")