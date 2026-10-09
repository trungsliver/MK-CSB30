# Array / List:  Danh sách

# Khái niệm: là 1 cấu trúc dữ liệu
# Thao tác CRUD: Create, Read, Update, Delete

# Create - Khởi tạo
    # Tạo danh sách rỗng
arr = []
    # Danh sách có sẵn phần tử
csb30 = ["Tú", "Nhật", "Hoàng", "Lâm", "Huy"]
arr1 = ["Quang Huy", 15, 1.75, True, [8, 8.5, 9, 9.25]]

# Read - Duyệt, hiện phần tử
    # len(): độ dài / số lượng phần tử của danh sách
print("Số lượng phần tử arr:", len(arr))
print("Số lượng phần tử csb30:", len(csb30))
print("Số lượng phần tử arr1:", len(arr1))
    # Hiện phần tử bằng index
print('Phần tử đầu tiên:', csb30[0])
print('Phần tử cuối cùng:', csb30[-1])
print('Phần tử có index=3:', csb30[3])
    # Hiện tất cả phần tử (test)
print(csb30)
    # Duyệt và hiện phần tử
        # Cách 1: Dùng cả index và value
for i in range(len(csb30)):
    print(f'Index = {i}, Value = {csb30[i]}')
        # Cách 2: Dùng value
for item in csb30:
    print('Value =', item)
        # Cách 3: Dùng hàm có sẵn enumerate()
for index, value in enumerate(csb30):
    print(f'Index = {index}, Value = {value}')

# Update - Cập nhật
    # Thêm phần tử vào cuối danh sách - append(value)
csb30.append('Trung')
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
csb30.insert(2, 'Donald Trump')
    # Sửa phần tử cũ
csb30[2] = 'Putin'

# Delete - Xóa
    # Xóa phần tử theo index 
del csb30[2]
csb30.pop(5)
    # Xóa phần tử theo value - remove(value)
csb30.remove('Huy')
    # Xóa tất cả phần tử - clear()
csb30.clear()

# Sắp xếp
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Sắp xếp tăng dần - sort()
num_list.sort()
print('num_list: ', num_list)
    # Sắp xếp giảm dần - sort(reverse=True)
num_list.sort(reverse=True)
print('num_list: ', num_list)

# Tìm giá trị lớn nhất, nhỏ nhất trong danh sách
    # max(): giá trị lớn nhất
print('Max value:', max(num_list))
    # min(): giá trị nhỏ nhất
print('Min value:', min(num_list))

# Tìm vị trí phần tử lớn nhất, nhỏ nhất trong danh sách
    # index phần tử lớn nhất
print('Index of max value:', num_list.index(max(num_list)))
    # index phần tử nhỏ nhất
print('Index of min value:', num_list.index(min(num_list)))