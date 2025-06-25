import pymysql
from pymysql import MySQLError as Error
import hashlib

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'quanlihocvien'
}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_db_connection():
    try:
        conn = pymysql.connect(**DB_CONFIG, cursorclass=pymysql.cursors.DictCursor)
        return conn
    except Error as e:
        print(f"Lỗi khi kết nối tới MySQL: {e}")
        return None


def initialize_database():
    """Khởi tạo CSDL, cả 2 bảng users, students và dữ liệu mặc định nếu cần."""
    conn = get_db_connection()
    if conn is None: return
    try:
        with conn.cursor() as cursor:
            # Tạo bảng users
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS users
                           (
                               username
                               VARCHAR
                           (
                               50
                           ) PRIMARY KEY,
                               password_hash VARCHAR
                           (
                               256
                           ) NOT NULL,
                               email VARCHAR
                           (
                               100
                           ) UNIQUE NOT NULL
                               )
                           ''')
            # Tạo bảng students
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS students
                           (
                               ma_hv
                               VARCHAR
                           (
                               20
                           ) PRIMARY KEY,
                               ho_ten VARCHAR
                           (
                               100
                           ) NOT NULL,
                               ngay_sinh DATE,
                               gioi_tinh VARCHAR
                           (
                               10
                           ),
                               dia_chi TEXT,
                               khoa_hoc VARCHAR
                           (
                               100
                           ),
                               he_dt VARCHAR
                           (
                               50
                           ),
                               sdt VARCHAR
                           (
                               20
                           )
                               )
                           ''')

            # Thêm dữ liệu người dùng mặc định nếu bảng users trống
            cursor.execute("SELECT COUNT(*) as count FROM users")
            if cursor.fetchone()['count'] == 0:
                default_users = [
                    ("hoanganh", hash_password("admin123"), "hoanganh@gmail.com"),
                    ("gv01", hash_password("gv123"), "gv01@gmail.com")
                ]
                cursor.executemany("INSERT INTO users (username, password_hash, email) VALUES (%s, %s, %s)",
                                   default_users)

            # Thêm dữ liệu học viên mặc định nếu bảng students trống
            cursor.execute("SELECT COUNT(*) as count FROM students")
            if cursor.fetchone()['count'] == 0:
                default_students = [
                    ("SV001", "Nguyễn Văn An", "2000-01-15", "Nam", "Hà Nội", "Công nghệ thông tin", "Đại học",
                     "0901112221"),
                    ("SV002", "Trần Thị Bình", "2001-05-01", "Nữ", "TP. Hồ Chí Minh", "Tin học", "Cao đẳng",
                     "0902223332"),
                    ("SV003", "Lê Văn Cường", "2002-05-20", "Nam", "Cao Lãnh", "Tin học", "Cao đẳng", "0903334443"),
                    ("SV004", "Phạm Thị Dung", "1999-08-22", "Nữ", "Đà Nẵng", "Khoa học máy tính", "Đại học",
                     "0904445554"),
                    ("SV005", "Vũ Hoàng Giang", "2002-03-10", "Nam", "Cần Thơ", "Công nghệ thông tin", "Cao đẳng",
                     "0905556665"),
                    ("SV006", "Đỗ Mỹ Hạnh", "2001-12-01", "Nữ", "Hải Phòng", "Tin học", "Đại học", "0906667776"),
                    ("SV007", "Bùi Anh Kiên", "2000-07-30", "Nam", "Nha Trang", "Khoa học máy tính", "Cao đẳng",
                     "0907778887"),
                    ("SV008", "Hồ Thị Lan", "2003-01-05", "Nữ", "Vũng Tàu", "Công nghệ thông tin", "Đại học",
                     "0908889998"),
                    ("SV009", "Trịnh Văn Minh", "1998-11-25", "Nam", "Huế", "Tin học", "Cao đẳng", "0909990009"),
                    ("SV010", "Đinh Ngọc Oanh", "2002-09-18", "Nữ", "Biên Hòa", "Khoa học máy tính", "Đại học",
                     "0901011010")
                ]
                cursor.executemany("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", default_students)

        conn.commit()
    finally:
        conn.close()


# --- Các hàm cho User ---
def verify_user(username, password):
    conn = get_db_connection()
    if not conn: return False
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
    finally:
        conn.close()

    if user and user['password_hash'] == hash_password(password):
        return True
    return False


def find_user_by_email(email):
    conn = get_db_connection()
    if not conn: return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT username FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
    finally:
        conn.close()
    return user['username'] if user else None


def update_user_password(username, new_password):
    conn = get_db_connection()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users SET password_hash = %s WHERE username = %s",
                           (hash_password(new_password), username))
        conn.commit()
    finally:
        conn.close()


# --- Các hàm cho Student ---
def get_all_students():
    conn = get_db_connection()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students ORDER BY ma_hv")
            students_dict = cursor.fetchall()
    finally:
        conn.close()
    return [[v for v in student.values()] for student in students_dict]


def add_student(data):
    conn = get_db_connection()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            student_data = tuple(data.values())
            cursor.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", student_data)
        conn.commit()
    finally:
        conn.close()


def update_student(data):
    conn = get_db_connection()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            student_data = (data['ho_ten'], data['ngay_sinh'], data['gioi_tinh'], data['dia_chi'], data['khoa_hoc'],
                            data['he_dt'], data['sdt'], data['ma_hv'])
            cursor.execute(
                "UPDATE students SET ho_ten=%s, ngay_sinh=%s, gioi_tinh=%s, dia_chi=%s, khoa_hoc=%s, he_dt=%s, sdt=%s WHERE ma_hv=%s",
                student_data)
        conn.commit()
    finally:
        conn.close()


def delete_student(ma_hv):
    conn = get_db_connection()
    if not conn: return
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE ma_hv = %s", (ma_hv,))
        conn.commit()
    finally:
        conn.close()


def student_id_exists(ma_hv):
    conn = get_db_connection()
    if not conn: return False
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1 FROM students WHERE ma_hv = %s", (ma_hv,))
            student = cursor.fetchone()
    finally:
        conn.close()
    return student is not None


def search_students(term, course, program):
    conn = get_db_connection()
    if not conn: return []
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM students WHERE 1=1"
            params = []
            if term:
                query += " AND (ma_hv LIKE %s OR ho_ten LIKE %s)"
                params.extend([f"%{term}%", f"%{term}%"])
            if course:
                query += " AND khoa_hoc = %s"
                params.append(course)
            if program:
                query += " AND he_dt = %s"
                params.append(program)
            query += " ORDER BY ma_hv"
            cursor.execute(query, tuple(params))
            students_dict = cursor.fetchall()
    finally:
        conn.close()
    return [[v for v in student.values()] for student in students_dict]