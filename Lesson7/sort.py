arr = [8, 6, 4, 2, 0, 1, 3, 5, 7, 9]

# ============== BUBBLE SORT ==============
def bubble_sort(arr:list):      # Độ phức tạp: O(n^2)
    # Duyệt toàn bộ danh sách
    for i in range (len(arr)):
        # So sánh từng cặp phần tử cạnh nhau
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Hoán đổi nếu phần tử hiện tại lớn hơn phần tử tiếp theo
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# print("BUBBLE SORT: ", bubble_sort(arr.copy()))

# ============= SELECTION SORT ==============
    # Cách 1: slides MindX
def selection_sort_1(arr:list):      # Độ phức tạp: O(n^2)
    # Tạo danh sách rỗng
    arr_sorted = []
    while len(arr) > 0:
        # Tìm phần tử lớn nhất
        max_value = max(arr)
        # Thêm phần tử lớn nhất vào danh sách đã sắp xếp
        arr_sorted.append(max_value)
        # Xóa phần tử lớn nhất khỏi danh sách ban đầu
        arr.remove(max_value)
    return arr_sorted

# print("SELECTION SORT (Cách 1): ", selection_sort_1(arr.copy()))

    # Cách 2: youtube
def selection_sort_2(arr:list):      # Độ phức tạp: O(n^2)
    # Duyệt toàn bộ danh sách
    for i in range(len(arr)):
        # Giả sử min_index nằm tại i
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Hoán đổi phần tử nhỏ nhất với phần tử tại i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# print("SELECTION SORT (Cách 2): ", selection_sort_2(arr.copy()))

# =============== INSERTION SORT ================
    # Giống xếp bài tú lơ khơ trên tay
def insertion_sort(arr):        # Độ phức tạp: O(n^2)
    # Duyệt từ phần tử thứ hai đến phần tử cuối cùng
    for i in range(1, len(arr)):
        # Phần tử cần chèn
        key = arr[i]
        # So sánh key với các phần tử trước nó  
        j = i - 1
        # Dịch chuyển các phần tử lớn hơn key về bên phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Chèn key vào vị trí đúng
        arr[j + 1] = key
    return arr

# print("Insertion Sort:", insertion_sort(arr))