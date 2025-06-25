import sys
from cx_Freeze import setup, Executable

# Các file chính và file giao diện cần được đóng gói
included_files = [
    "database.py",
    "dangnhap.py",
    "Qlhv.py",
    "quenmk.py",
    "timkiem.py",
    ("giaodien", "giaodien") # Đóng gói cả thư mục 'giaodien'
]

# Các gói thư viện cần thiết
packages = [
    "os", "sys", "re", "datetime", "collections",
    "PyQt5.QtWidgets", "PyQt5.QtCore", "PyQt5.QtGui",
    "dateutil.relativedelta",
    "pymysql"
]

build_exe_options = {
    "packages": packages,
    "include_files": included_files,
    "excludes": [], # Có thể bỏ qua các thư viện không dùng để giảm kích thước
    "optimize": 2,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Để ẩn cửa sổ console màu đen khi chạy

setup(
    name="QuanLyHocVienApp",
    version="2.0",
    description="Ứng dụng quản lý học viên Python PyQt5 và MySQL",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="giaodien/app_icon.ico")] # Thay 'app_icon.ico' bằng icon của bạn nếu có
)