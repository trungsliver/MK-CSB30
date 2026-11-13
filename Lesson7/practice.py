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