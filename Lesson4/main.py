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

# Hiển thị toàn bộ thông tin player
print('\nDanh sách player:')
# db.show_all_players()

# Menu tùy chọn
while True:
    print("\n===== Player Management Menu =====")
    print('1. Show all players')
    print('2. Add new player')
    print('3. Find player by ID')
    print('4. Update player by ID')
    print('5. Delete player by ID')
    print('6. Exit')
    print('==================================')
    choice = input('Enter your choice: ')

    if choice == '1':
        db.show_all_players()
    elif choice == '2':
        db.add_player()
    elif choice == '3':
        player_id = input('Enter player ID to find: ')
        player = db.find_player_by_id(player_id)
        if player:
            print('Player found:')
            player.show_info()
        else:
            print('Player not found.')
    elif choice == '4':
        player_id = input('Enter player ID to update: ')
        db.update_player_by_id(player_id)
    elif choice == '5':
        player_id = input('Enter player ID to delete: ')
        db.delete_player_by_id(player_id)
    elif choice == '6':
        break
    else:
        print('Invalid choice. Please try again.')

