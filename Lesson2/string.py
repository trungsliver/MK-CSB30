# String: chuỗi / xâu ký tự
name = "Minh Nhật"

# len(): độ dài chuỗi
print('Độ dài chuỗi name:', len(name))

# Truy cập ký tự trong string bằng index
print('Ký tự đầu tiên:', name[0])
print('Ký tự cuối cùng:', name[-1])

# Duyệt string
    # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print(f'Index: {i}, Value: {name[i]}')
    # Cách 2: Dùng value
for char in name:
    print(f'Value: {char}')

# Xâu con (substring)
str1 = "Luu Xuan Tu"
str2 = "Xuan Tu"
str3 = "Nguyen"
    # Kiểm tra substring: in
print('str2 in str1:', str2 in str1)    # True
print('str3 in str1:', str3 in str1)    # False
    # Tìm vị trí substring: find()
print('Vị trí str2 trong str1:', str1.find(str2))    # 4
print('Vị trí str3 trong str1:', str1.find(str3))    # -1 (không tìm thấy)

# Slicing: cắt chuỗi
    # Cú pháp: string[start:stop:step]
name = 'hahahihihuhu'
    # Cắt ở vị trí bắt kì [start:stop]
print('name[4:8] =', name[4:8])      # hihi
    # Cắt từ đầu đến vị trí bất kì [:stop]
print('name[:4] =', name[:4])        # haha
    # Cắt từ vị trí bất kì đến cuối [start:]
print('name[4:] =', name[8:])        # huhu

# Tách string => trả về danh sách: split()
    # Mặc định tách khi gặp khoảng trắng
str1 = '1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('arr1 =', arr1)    
    # Tách khi gặp ký tự bất kì
str2 = 'a,b,c,d,e,f,g'
arr2 = str2.split(',')
print('arr2 =', arr2)

# Gộp chuỗi - join()
arr = ['r','o','n','a','l','d','o']
    # Kết hợp với khoảng trắng
str1 = ' '.join(arr)
print('str1 =', str1)      
    # Kết hợp với ký tự bất kì
str2 = '-'.join(arr)
print('str2 =', str2)

# xóa khoảng trắng thừa ở đầu cuối chuỗi: strip()
str1 = '        Khai Hoang            '
print('str1 =', str1)
print('str1 =', str1.strip())

# Thay thế substring: replace()
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ: replace(old, new)
print('song =', song.replace('doo', 'huy'))
    # Thay thế 1 phần: replace(old, new, count)
print('song =', song.replace('doo', 'huy', 3))

# Chuẩn háo string
name = 'kHuC bAo lAm'
    # Viết hoa tất cả: upper()
print('upper =', name.upper())
    # Viết thường tất cả: lower()
print('lower =', name.lower())
    # Viết hoa chữ cái đầu tiên: title()
print('title =', name.title())

# Bài tập 1: Chuyển đổi kiểu dữ liệu danh sách: str => int
arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # string
    # Cách 1:
arr1 = []
for item in arr:
    new_item = int(item)
    arr1.append(new_item)
print('arr1 =', arr1)      # int
    # Cách 2:
arr2 = [int(item) for item in arr]
print('arr2 =', arr2)      # int