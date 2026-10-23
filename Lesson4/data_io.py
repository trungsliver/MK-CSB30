import json

# Đọc dữ liệu
def load_json_data(file_path):
    dict_data = list()
    # with open(): dùng để mở file, tự đóng sau khi thực hiện
    # 'r': read, chế độ đọc file
    with open(file_path, 'r') as file:
        data = json.load(file)
    dict_data.extend(data)
    return dict_data    

# Ghi dữ liệu
def write_json_data(file_path, dict_data):
    # 'w': write, chế độ ghi file
    with open(file_path, 'w', encoding='utf-8') as file:
        # ensure_ascii=False: để không mã hóa các ký tự Unicode
        json.dump(dict_data, file, ensure_ascii=False, indent=4)