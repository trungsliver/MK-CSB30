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
        # Đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object
        self.players_list = list()
        # Danh sách dạng dictionary (dữ liệu từ file json)
        self.players_dict = data_io.load_json_data(file_path)

    # Chuyển từ dictionary (json) sang object
    def dict_to_object(self):
        new_players = []
        # Duyệt danh sách dictionary
        for player in self.players_dict:
            # Khởi tạo player dạng object từ dictionary
            new_player = Player(**player)
            new_players.append(new_player)
        # Gán danh sách vào thuộc tính players_list
        self.players_list = new_players

    # Chuyển từ object sang dictionary (json)
    def object_to_dict(self):
        new_players = []
        for player in self.players_list:
            # Chuyển object sang dictionary
            new_player = player.__dict__
            new_players.append(new_player)
        # Gán danh sách vào thuộc tính players_dict
        self.players_dict = new_players
        # Ghi dữ liệu vào file json
        data_io.write_json_data(self.file_path, self.players_dict)
        return self.players_dict