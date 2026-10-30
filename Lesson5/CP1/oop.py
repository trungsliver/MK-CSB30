import json
from pathlib import Path

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.avg_grade = 0.0

    def add_grade(self, grade):
        try:
            grade = float(grade)
            if 0 <= grade <= 10:
                self.grades.append(grade)
                self.calculate_average()
            else:
                print('Điểm không hợp lệ. Vui lòng nhập điểm từ 0 đến 10.')
        except:
            print('Điểm không hợp lệ. Nhập sai kiểu dữ liệu điểm.')

    def calculate_average(self):
        if self.grades:
            self.avg_grade = sum(self.grades) / len(self.grades)
        else:
            self.avg_grade = 0.0

class GradeManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        data_file = Path(__file__).with_name("data.json")
        try:
            with data_file.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Không tìm thấy file dữ liệu {data_file}.")
            return
        except json.JSONDecodeError:
            print(f"File dữ liệu {data_file} không đúng định dạng JSON.")
            return

        for student_data in data:
            # Tạo học sinh với tên
            student = Student(student_data["name"])
            # Lấy data danh sách điểm
            student.grades = student_data.get("grades", [])
            # Tính điểm trung bình của mỗi học sinh
            student.avg_grade = student.calculate_average()
            # Thêm học sinh vào danh sách quản lý
            self.students.append(student)

    def add_student(self, name):
        # Kiểm tra xem học sinh đã tồn tại chưa
        for student in self.students:
            if student.name == name:
                print(f"Học sinh {name} đã tồn tại.")
                return
        # Kiểm tra tên có hợp lệ không (bắt buộc có chữ cái, có thể chủa khoảng trắng, không có số & ký tự đặc biệt)
        if not name.replace(" ", "").isalpha():
            print("Tên học sinh không hợp lệ. Vui lòng nhập tên chỉ chứa chữ cái và khoảng trắng.")
            return
        # Tạo học sinh mới và thêm vào danh sách
        new_student = Student(name)
        self.students.append(new_student)

    def record_grade(self, name, grade):
        try:
            # Tìm học sinh theo tên
            for student in self.students:
                if student.name == name:
                    student.add_grade(grade)
                    print(f"Đã ghi điểm {grade} cho học sinh {name}.")
                    return True
            print(f"Học sinh {name} không tồn tại.")
            return False    
        except:
            print("Đã xảy ra lỗi khi ghi điểm.")
            return False

    def calculate_average(self):
        try:
            # Kiểm tra xem danh sách có học sinh không
            if len(self.students) == 0:
                print("Danh sách học sinh trống.")
                return 
            else:
                total_avg = 0
                print('Điểm trung bình của từng học sinh:')
                for student in self.students:
                    print(f"{student.name}: {student.avg_grade:.2f}")
                    total_avg += student.avg_grade
                overall_avg = total_avg / len(self.students)
                print('Điểm trung bình của tất cả học sinh:', f"{overall_avg:.2f}")
        except:
            print("Đã xảy ra lỗi khi tính điểm trung bình.")

    def save_data(self, filename="data.json"):
        if not filename.endswith('.json'):
            filename += '.json'
        data = []
        for student in self.students:
            student_data = {
                'name': student.name,
                'grades': student.grades,
                'avg_grade': student.avg_grade
            }
            data.append(student_data)
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Dữ liệu đã được lưu vào {filename}.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu dữ liệu: {e}")