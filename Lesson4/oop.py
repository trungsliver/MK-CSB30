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

    # Hiển thị toàn bộ thông tin player
    def show_all_players(self):
        for player in self.players_list:
            player.show_info()

    # Thêm 1 player mới
    def add_player(self):
        if len(self.players_dict) > 0:
            # id của player cuối cùng + 1
            new_id = self.players_dict[-1]['id'] + 1
        else:
            new_id = 1
        # Nhập thông tin player mới
        new_name = input('Enter player name: ')
        new_dob = input('Enter player DOB (YYYY-MM-DD): ')
        new_region = input('Enter player region: ')
        new_position = input('Enter player position: ')
        new_club = input('Enter player club: ')
        new_worth = input('Enter player worth (optional): ')
        
        try:
            # Tạp object player mới
            new_player = Player(new_id, new_name, new_dob, new_region, new_position, new_club, new_worth)
            # Add vào danh sách object
            self.players_list.append(new_player)
            # Chuyển từ object sang dictionary và ghi vào file json
            self.object_to_dict()
            # Thông báo thành công
            print('New player added successfully!')
        except:
            print('Error: Cant add new player!')

    # Find player by ID
    def find_player_by_id(self, player_id):
        try:
            # Chuyển player_id sang int (số nguyên)
            player_id = int(player_id)
            # Duyệt danh sách object
            for player in self.players_list:
                if player.id == player_id:
                    # Tìm thấy -> return object player
                    return player
            # Nếu không tìm thấy -> return None
            return None
        except:
            print('Error: Cant find player!')

    # Update player by ID
    def update_player_by_id(self, player_id):
        try:
            player = self.find_player_by_id(player_id)
            if player:
                new_id = player_id
                # Nhập thông tin player mới
                new_name = input('Enter player name: ')
                new_dob = input('Enter player DOB (YYYY-MM-DD): ')
                new_region = input('Enter player region: ')
                new_position = input('Enter player position: ')
                new_club = input('Enter player club: ')
                new_worth = input('Enter player worth (optional): ')
                # Tạo object player mới
                new_player = Player(new_id, new_name, new_dob, new_region, new_position, new_club, new_worth)
                # Cập nhật thông tin player
                player.update(new_player.__dict__)
                # Chuyển từ object sang dictionary và ghi vào file json
                self.object_to_dict()
                # Thông báo thành công
                print('Player updated successfully!')
            else:
                print('Player not found.')
        except:
            print('Error: Cant update player!')

    # Delete player by ID
    def delete_player_by_id(self, player_id):
        try:
            player = self.find_player_by_id(player_id)
            if player:
                # Xóa player khỏi danh sách object
                self.players_list.remove(player)
                # Chuyển từ object sang dictionary và ghi vào file json
                self.object_to_dict()
                # Thông báo thành công
                print('Player deleted successfully!')
            else:
                print('Player not found.')
        except:
            print('Error: Cant delete player!')