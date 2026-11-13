# ============= SO SÁNH HIỆU SUẤT =============
import time, random, sort

def measure_time(func, arr):
    # Thời gian bắt đầu
    start_time = time.time()
    # thực hiện hàm tìm kiếm
    func(arr)
    # Thời gian kết thúc
    end_time = time.time()
    # Tính thời gian thực hiện
    return end_time - start_time

# Bài 1: So sánh tốc độ 3 thuật toán sắp xếp vừa học với mảng có kích thước lớn (tính tổng thời gian 10 lần chạy và lấy trung bình)

    # Số lần thực hiện
n = 10
    # Tính tổng thời gian thực hiện của từng thuật toán
total_bubble = 0
total_selection_1 = 0
total_selection_2 = 0
total_insertion = 0

for i in range(n):
    # Tạo danh sách ngẫu nhiên cho mỗi lần lặp
    random_list = [random.randint(1, 20000000) for _ in range(10000)]
    # Tính thời gian thực hiện của từng thuật toán
    total_bubble += measure_time(sort.bubble_sort, random_list.copy())
    total_selection_1 += measure_time(sort.selection_sort_1, random_list.copy())
    total_selection_2 += measure_time(sort.selection_sort_2, random_list.copy())
    total_insertion += measure_time(sort.insertion_sort, random_list.copy())

# Tính trung bình thời gian thực hiện của từng thuật toán
print(f"Avg Time Selection Sort 1: {total_selection_1/n:.8f} giây")
print(f"Avg Time Selection Sort 2: {total_selection_2/n:.8f} giây")
print(f"Avg Time Bubble Sort: {total_bubble/n:.8f} giây")
print(f"Avg Time Insertion Sort: {total_insertion/n:.8f} giây")