import oop

# Khởi tạo PlayerManager
db = oop.PlayerManager('data.json')

# Hiển thị kích thước 2 danh sách
print('Object list:', len(db.players_list))
print('Dictionary list:', len(db.players_dict))

# Chuyển từ dictionary sang object
print('\nSau khi convert sang object:')
db.dict_to_object()
print('Object list:', len(db.players_list))
print('Dictionary list:', len(db.players_dict))