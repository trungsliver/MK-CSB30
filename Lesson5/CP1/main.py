import oop

manager = oop.GradeManager()

while True:
    print("\n--- Quản lý điểm học sinh ---")
    print("1. Thêm học sinh")
    print("2. Ghi nhận điểm cho học sinh")
    print("3. Tính điểm trung bình của từng học sinh")
    print("4. Lưu dữ liệu")
    print("5. Thoát")
    print("-------------------------------")

    choice = input("Chọn một tùy chọn (1-5): ")

    if choice == "1":
        name = input("Nhập tên học sinh: ")
        manager.add_student(name)
    elif choice == "2":
        name = input("Nhập tên học sinh: ")
        grade = input("Nhập điểm: ")
        manager.record_grade(name, grade)
    elif choice == "3":
        manager.calculate_average()
    elif choice == "4":
        manager.save_data()
    elif choice == "5":
        print("Đang thoát...")
        break
    else:
        print("Tùy chọn không hợp lệ. Vui lòng chọn lại.")