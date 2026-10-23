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