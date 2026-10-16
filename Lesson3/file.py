import json

# Khai báo danh sách đối tượng (data)

students = [
    {"name": "Xuân Tú", "age": 18, "gender": "male", "school": "Thành Đô"},
    {"name": "Minh Nhật", "age": 14, "gender": "male", "school": "Ngô Quyền"},
    {"name": "Khải Hoàng", "age": 14, "gender": "male", "school": "Vĩnh Hưng"},
    {"name": "Quang Huy", "age": 15, "gender": "male", "school": "Vinschool"},
    {"name": "Bảo Lâm", "age": 15, "gender": "male", "school": "Vinschool"}
]

# Ghi nội dung vào file JSON
with open("data.json", "w", encoding="utf-8") as f:
    # indent=4: định dạng giúp file dễ đọc
    # ensure_ascii=False: để giữ nguyên ký tự Unicode (giữ nguyên tiếng việt)
    json.dump(students, f, indent=4, ensure_ascii=False)

# Đọc nội dung từ file JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)