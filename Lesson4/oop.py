import data_io

class Player:
    def __init__(self, id, name, dob, region, position, club, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.position = position
        self.club = club
        # Nếu có thì định dạng float, không có thì mặc định = 0
        self.worth = float(worth) if worth else 0

    def show_info(self):
        print('\n===== Player Infomation =====')
        print('ID: ', self.id)
        print('Name: ', self.name)
        print('DOB: ', self.dob)
        print('Position: ', self.position)
        print('Region: ', self.region)
        print('Club: ', self.club)
        print('Worth: ', self.worth)
        print('==============================')

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # Có thuộc tính thì mới gán giá trị mới
            if value:
                setattr(self, key, value)

class PlayerManager:
    def __init__(self, file_path):
        # Đường dẫn đén file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object
        self.players_list = list()
        # Danh sách dạng dictionary (dữ liệu từ file json)
        self.players_dict = data_io.load_json_data(file_path)