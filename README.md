# Phần mềm Quản lý Học viên bằng Python
![Python](https://img.shields.io/badge/python-3.10+-blue.svg) ![PyQt5](https://img.shields.io/badge/Qt-PyQt5-green.svg) ![Database](https://img.shields.io/badge/database-MySQL-blue.svg)

Đây là một dự án ứng dụng desktop được xây dựng bằng Python và thư viện PyQt5, dùng để quản lý thông tin học viên một cách hiệu quả và trực quan. Ứng dụng cho phép thực hiện đầy đủ các thao tác CRUD (Thêm, Đọc, Sửa, Xóa) và các chức năng tiện ích khác.

## 📸 Hình ảnh Demo

**Cửa sổ Đăng nhập:**

![Screenshot 2025-06-24 215922](https://github.com/user-attachments/assets/7671cc52-6509-431c-938a-48d92184a46a)
**Cửa sổ Quản lý chính:**

![Screenshot 2025-06-24 215943](https://github.com/user-attachments/assets/9f83cbf5-c6c3-46de-9aaa-c386fb44469a)
**Cửa sổ Tìm kiếm & Thống kê:** 

![Screenshot 2025-06-24 215952](https://github.com/user-attachments/assets/6501966f-e9da-453f-a213-a9fb03bc659e)
![Screenshot 2025-06-24 220001](https://github.com/user-attachments/assets/7e731797-f888-4c4d-9f27-bd95f1baad53)
**Giao diện lấy lại mật khẩu**

![Screenshot 2025-06-24 215932](https://github.com/user-attachments/assets/0e60ad50-65fb-4567-a92d-1a2611834f95)
**UX(Loading)**

![image](https://github.com/user-attachments/assets/5c52dbec-a63a-479a-ac8a-c07f4a6f3e2f)

## ✨ Các tính năng chính

* **Đăng nhập & Bảo mật:**
    * Giao diện đăng nhập để xác thực người dùng.
    * Chức năng "Quên mật khẩu" mô phỏng.
    * Mật khẩu được mã hóa bằng thuật toán SHA-256 trước khi lưu trữ.
* **Quản lý Học viên (CRUD):**
    * **Thêm:** Thêm hồ sơ học viên mới vào cơ sở dữ liệu.
    * **Sửa:** Cập nhật thông tin chi tiết của học viên đã có.
    * **Xóa:** Xóa học viên khỏi cơ sở dữ liệu một cách an toàn (có hộp thoại xác nhận).
* **Tìm kiếm & Lọc:**
    * Giao diện tìm kiếm riêng biệt.
    * Tìm kiếm học viên theo Tên hoặc Mã học viên.
    * Lọc danh sách học viên theo Khóa học và Hệ đào tạo.
* **Thống kê & Báo cáo:**
    * Tính toán và hiển thị các số liệu thống kê dựa trên danh sách học viên hiện tại.
    * Thống kê tổng số lượng, tỷ lệ theo giới tính.
    * Thống kê phân bố học viên theo độ tuổi.
    * Thống kê số lượng theo từng khóa học và hệ đào tạo.
* **Trải nghiệm người dùng:**
    * Giao diện được thiết kế gọn gàng, trực quan.
    * Sử dụng hiệu ứng loading để phản hồi các tác vụ tương tác với cơ sở dữ liệu, tránh cảm giác chương trình bị "treo".

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python 3
* **Giao diện người dùng (GUI):** PyQt5
* **Cơ sở dữ liệu:** SQLite 3 (dạng file, không cần cài đặt server)
* **Công cụ:** Qt Designer, PyCharm/VS Code

## 🚀 Cài đặt và Chạy dự án

Để chạy dự án này trên máy của bạn, hãy làm theo các bước sau:

**1. Clone repository về máy:**
```bash
git clone https://github.com/hthoanganh/Quan_Ly_Hoc_Vien.git
cd [Quan_Ly_Hoc_Vien]
```

**2. Tạo và kích hoạt môi trường ảo:**
*Khuyên dùng để không ảnh hưởng đến các thư viện Python trên máy của bạn.*
```bash
# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt môi trường ảo (trên Windows)
.\.venv\Scripts\activate
```

**3. Cài đặt các thư viện cần thiết:**
*Tất cả các thư viện cần thiết đã được liệt kê trong file `requirements.txt`.*
```bash
pip install -r requirements.txt
```

**4. Chạy chương trình:**
*Lần chạy đầu tiên, chương trình sẽ tự động tạo ra một file `quanlihocvien.db` chứa cơ sở dữ liệu và các dữ liệu mẫu.*
```bash
python main.py
```

**5. Đăng nhập:**
* Sử dụng tài khoản mặc định sau để đăng nhập:
    * **Tên đăng nhập:** `hoanganh`
    * **Mật khẩu:** `admin123`

---
Cảm ơn bạn đã ghé thăm dự án!
