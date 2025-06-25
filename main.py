import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QLineEdit
import re
from datetime import datetime
from collections import Counter, defaultdict
from dateutil.relativedelta import relativedelta

from dangnhap import Ui_MainWindow as Ui_DangNhapWindow
from Qlhv import Ui_MainWindow as Ui_QLHVWindow
from quenmk import Ui_MainWindow as Ui_QuenMKWindow
from timkiem import Ui_MainWindow as Ui_TimKiemWindow
import database


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangNhapWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Đăng Nhập")
        self.ui.nutdangnhap.clicked.connect(self.handle_login)
        self.ui.nutquenmk.clicked.connect(self.show_forgot_password_action)
        self.ui.hienmk.stateChanged.connect(self.toggle_password_visibility)
        self.ui.nhapmk.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_3.clicked.connect(
            lambda: QMessageBox.information(self, "Thông báo", "Chức năng chưa triển khai."))

    def toggle_password_visibility(self):
        self.ui.nhapmk.setEchoMode(QLineEdit.Normal if self.ui.hienmk.isChecked() else QLineEdit.Password)

    def handle_login(self):
        main_app.show_loading_screen(self)
        QtCore.QTimer.singleShot(100, lambda: self._process_login(self.ui.nhapuser.text().strip(),
                                                                  self.ui.nhapmk.text().strip()))

    def _process_login(self, username, password):
        if not username or not password:
            main_app.show_delayed_messagebox(self, "Lỗi Đăng Nhập", "Vui lòng nhập tên đăng nhập và mật khẩu.",
                                             QMessageBox.Warning)
            return

        if database.verify_user(username, password):
            message = f"Đăng nhập thành công với tài khoản {'Quản trị viên' if username == 'hoanganh' else 'Người dùng'}: {username}!"
            main_app.show_delayed_messagebox(self, "Thành công", message, QMessageBox.Information,
                                             on_close_action=lambda: main_app.show_qlhv_window(username))
        else:
            main_app.show_delayed_messagebox(self, "Lỗi Đăng Nhập", "Tên đăng nhập hoặc mật khẩu không đúng.",
                                             QMessageBox.Warning,
                                             on_close_action=lambda: (self.ui.nhapmk.clear(), self.ui.nhapuser.clear(),
                                                                      self.ui.nhapuser.setFocus()))

    def show_forgot_password_action(self):
        main_app.show_quenmk_window()

class ForgotPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QuenMKWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Quên Mật Khẩu")

        # Sửa kết nối của nút "Xác nhận" để gọi hàm handle_
        self.ui.nutxacnhan.clicked.connect(self.handle_reset_password_action)
        self.ui.nutthoat.clicked.connect(main_app.show_login_window)
        self.ui.hienmk.stateChanged.connect(self.toggle_password_visibility)
        self.ui.nhapmkmoi.setEchoMode(QLineEdit.Password)
        self.ui.xacnhanmkmoi.setEchoMode(QLineEdit.Password)

    def toggle_password_visibility(self):
        is_checked = self.ui.hienmk.isChecked()
        mode = QLineEdit.Normal if is_checked else QLineEdit.Password
        self.ui.nhapmkmoi.setEchoMode(mode)
        self.ui.xacnhanmkmoi.setEchoMode(mode)

    # HÀM 1: Dùng để kích hoạt hiệu ứng khi nhấn nút
    def handle_reset_password_action(self):
        # DÒNG THÊM VÀO: Hiện hiệu ứng loading
        main_app.show_loading_screen(self)

        # Đặt một bộ đếm thời gian ngắn để gọi hàm xử lý chính
        # Việc này giúp giao diện có thời gian để vẽ hiệu ứng loading lên màn hình
        QtCore.QTimer.singleShot(100, self._process_reset_password)

    # HÀM 2: Xử lý logic chính sau khi hiệu ứng đã hiện
    def _process_reset_password(self):
        # Dùng try...finally để đảm bảo hiệu ứng loading luôn được tắt
        try:
            email = self.ui.nhapemail.text().strip()
            username_to_recover = database.find_user_by_email(email)
            if not username_to_recover:
                # Gọi hàm thông báo có độ trễ
                main_app.show_delayed_messagebox(self, "Lỗi", "Email này chưa được đăng ký trong hệ thống.",
                                                 QMessageBox.Warning)
                return  # Thoát sớm nếu có lỗi

            new_password = self.ui.nhapmkmoi.text().strip()
            confirm_password = self.ui.xacnhanmkmoi.text().strip()

            if new_password and new_password == confirm_password and len(new_password) >= 6:
                database.update_user_password(username_to_recover, new_password)
                # Gọi hàm thông báo có độ trễ và hành động đi kèm
                main_app.show_delayed_messagebox(self, "Thành Công",
                                                 f"Mật khẩu cho tài khoản '{username_to_recover}' đã được cập nhật thành công!",
                                                 QMessageBox.Information, on_close_action=main_app.show_login_window)
            else:
                main_app.show_delayed_messagebox(self, "Lỗi", "Mật khẩu mới không hợp lệ hoặc không khớp.",
                                                 QMessageBox.Warning)
        finally:

            # (Hàm show_delayed_messagebox đã có sẵn hide_loading_screen nên dòng này có thể không cần,
            # nhưng thêm vào để đảm bảo sự chắc chắn)
            main_app.hide_loading_screen()

class QLHVWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QLHVWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Quản Lý Học Viên")
        self.current_user = "N/A"
        self.timkiem_window = None
        self.ui.bang.setColumnCount(8)
        self.ui.bang.setHorizontalHeaderLabels(
            ["Mã HV", "Họ Tên", "Ngày Sinh", "Giới Tính", "Địa Chỉ", "Khóa Học", "Hệ ĐT", "SĐT"])
        self.load_students_from_db()
        self.ui.nutthem.clicked.connect(self.add_student_action)
        self.ui.nutsua.clicked.connect(self.edit_student_action)
        self.ui.nuttxoa.clicked.connect(self.delete_student_action)
        if hasattr(self.ui, 'nutclear'): self.ui.nutclear.clicked.connect(self.clear_inputs_and_selection)
        self.ui.nuttimkiem.clicked.connect(self.show_search_window_action)
        self.ui.nutthoat.clicked.connect(self.logout_action)
        self.ui.bang.itemClicked.connect(self.load_student_to_form)
        self.ui.bang.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.bang.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.bang.setColumnWidth(0, 70);
        self.ui.bang.setColumnWidth(1, 140);
        self.ui.bang.setColumnWidth(2, 100);
        self.ui.bang.setColumnWidth(3, 60);
        self.ui.bang.setColumnWidth(4, 120);
        self.ui.bang.setColumnWidth(5, 150);
        self.ui.bang.setColumnWidth(6, 80);
        self.ui.bang.setColumnWidth(7, 90)

    def set_current_user(self, username):
        self.current_user = username
        if hasattr(self.ui, 'nguoidung'):
            self.ui.nguoidung.setText(f"Người dùng: {username}")

    def load_students_from_db(self):
        try:
            all_students = database.get_all_students()
            self.populate_table(all_students)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu học viên: {e}")

    def populate_table(self, data):
        self.ui.bang.setRowCount(0)
        for student_data in data:
            row_position = self.ui.bang.rowCount()
            self.ui.bang.insertRow(row_position)
            for col_idx, cell_data in enumerate(student_data):
                self.ui.bang.setItem(row_position, col_idx, QTableWidgetItem(str(cell_data)))

    def _get_student_data_from_form(self):
        ma_hv = self.ui.mahocvien.toPlainText().strip()
        ho_ten = self.ui.hoten.toPlainText().strip()
        ngay_sinh = self.ui.ngaysinh.date().toString("yyyy-MM-dd")
        gioi_tinh = "Nam" if self.ui.nam.isChecked() else ("Nữ" if self.ui.nu.isChecked() else "")
        dia_chi = self.ui.Diachi.toPlainText().strip()
        khoa_hoc = self.ui.Khoahoc.currentText()
        he_dt = self.ui.heDT.currentText()
        sdt = self.ui.SDT.toPlainText().strip()
        if not ho_ten or not gioi_tinh or self.ui.Khoahoc.currentIndex() == 0 or self.ui.heDT.currentIndex() == 0:
            return None, "Vui lòng nhập đầy đủ các trường bắt buộc."
        if sdt and not sdt.isdigit():
            return None, "Số điện thoại chỉ được chứa số."
        return {"ma_hv": ma_hv, "ho_ten": ho_ten, "ngay_sinh": ngay_sinh, "gioi_tinh": gioi_tinh, "dia_chi": dia_chi,
                "khoa_hoc": khoa_hoc, "he_dt": he_dt, "sdt": sdt}, None

    def add_student_action(self):
        data, error_msg = self._get_student_data_from_form()
        if error_msg: QMessageBox.warning(self, "Lỗi Nhập Liệu", error_msg); return
        if not data["ma_hv"]: QMessageBox.warning(self, "Lỗi", "Vui lòng nhập Mã học viên."); return

        main_app.show_loading_screen(self)
        QtCore.QTimer.singleShot(100, lambda: self._process_add_student(data))

    def _process_add_student(self, data):
        if database.student_id_exists(data["ma_hv"]):
            main_app.show_delayed_messagebox(self, "Lỗi", f"Mã học viên '{data['ma_hv']}' đã tồn tại.",
                                             QMessageBox.Warning)
        else:
            database.add_student(data)
            self.load_students_from_db()
            main_app.show_delayed_messagebox(self, "Thành công", "Thêm học viên thành công!", QMessageBox.Information,
                                             on_close_action=self.clear_inputs_and_selection)

    def edit_student_action(self):
        if not self.ui.bang.selectedRanges(): QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một dòng để sửa."); return
        data, error_msg = self._get_student_data_from_form()
        if error_msg: QMessageBox.warning(self, "Lỗi Nhập Liệu", error_msg); return

        main_app.show_loading_screen(self)
        QtCore.QTimer.singleShot(100, lambda: self._process_edit_student(data))

    def _process_edit_student(self, data):
        database.update_student(data)
        self.load_students_from_db()
        main_app.show_delayed_messagebox(self, "Thông báo", "Sửa thông tin học viên thành công.",
                                         QMessageBox.Information, on_close_action=self.clear_inputs_and_selection)

    def delete_student_action(self):
        if not self.ui.bang.selectionModel().hasSelection():
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn học viên để xóa.")
            return

        reply = QMessageBox.question(self, 'Xác nhận xóa', "Bạn có chắc muốn xóa học viên này?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No: return

        selected_row = self.ui.bang.currentRow()
        ma_hv_to_delete = self.ui.bang.item(selected_row, 0).text()

        main_app.show_loading_screen(self)
        QtCore.QTimer.singleShot(100, lambda: self._process_delete_student(ma_hv_to_delete))

    def _process_delete_student(self, ma_hv):
        database.delete_student(ma_hv)
        self.load_students_from_db()
        main_app.show_delayed_messagebox(self, "Thành công", "Xóa học viên thành công.", QMessageBox.Information,
                                         on_close_action=self.clear_inputs_and_selection)

    def load_student_to_form(self, item):
        row = item.row()
        self.ui.mahocvien.setPlainText(self.ui.bang.item(row, 0).text())
        self.ui.hoten.setPlainText(self.ui.bang.item(row, 1).text())
        self.ui.ngaysinh.setDate(QtCore.QDate.fromString(self.ui.bang.item(row, 2).text(), "yyyy-MM-dd"))
        if self.ui.bang.item(row, 3).text() == "Nam":
            self.ui.nam.setChecked(True)
        else:
            self.ui.nu.setChecked(True)
        self.ui.Diachi.setPlainText(self.ui.bang.item(row, 4).text())
        self.ui.Khoahoc.setCurrentText(self.ui.bang.item(row, 5).text())
        self.ui.heDT.setCurrentText(self.ui.bang.item(row, 6).text())
        self.ui.SDT.setPlainText(self.ui.bang.item(row, 7).text())
        self.ui.mahocvien.setReadOnly(True)

    def clear_inputs_and_selection(self):
        self.ui.mahocvien.setPlainText("");
        self.ui.mahocvien.setReadOnly(False)
        self.ui.hoten.setPlainText("");
        self.ui.Diachi.setPlainText("");
        self.ui.SDT.setPlainText("")
        self.ui.ngaysinh.setDate(QtCore.QDate.currentDate())
        self.ui.nam.setAutoExclusive(False);
        self.ui.nu.setChecked(False);
        self.ui.nam.setAutoExclusive(True)
        self.ui.Khoahoc.setCurrentIndex(0);
        self.ui.heDT.setCurrentIndex(0)
        self.ui.bang.clearSelection()

    def show_search_window_action(self):
        main_app.show_search_window(self)

    def logout_action(self):
        reply = QMessageBox.question(self, 'Xác nhận', "Bạn có muốn đăng xuất?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes: main_app.show_login_window()


class TimKiemWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_TimKiemWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tìm Kiếm và Thống Kê")
        self.main_window = main_window  # Lưu lại cửa sổ chính để quay về

        # Kết nối các nút với hàm xử lý
        self.ui.nutquaylai.clicked.connect(self.go_back_to_qlhv_action)
        self.ui.nutthoat.clicked.connect(self.close)
        self.ui.nuttim.clicked.connect(self.perform_search_action)
        self.ui.pushButton_4.clicked.connect(self.export_to_excel_placeholder)
        self.ui.nutapdung.clicked.connect(self.calculate_statistics_action)

    def showEvent(self, event):
        """Được gọi mỗi khi cửa sổ được hiển thị."""
        super().showEvent(event)
        # Reset các trường lọc và tải dữ liệu ban đầu
        self.ui.otimkiem.clear()
        self.ui.cbkhoahoc.setCurrentIndex(0)
        self.ui.cbHDT.setCurrentIndex(0)
        self.ui.bangketqua.clear()

        main_app.show_loading_screen(self)

        def load_initial_data():
            try:
                all_students = database.get_all_students()
                self.populate_table(all_students)
            finally:
                main_app.hide_loading_screen()

        QtCore.QTimer.singleShot(200, load_initial_data)

    def populate_table(self, data):
        """Hàm hiển thị dữ liệu lên bảng."""
        self.ui.bang.setRowCount(0)
        for row_data in data:
            row_position = self.ui.bang.rowCount()
            self.ui.bang.insertRow(row_position)
            for col, cell_data in enumerate(row_data):
                self.ui.bang.setItem(row_position, col, QTableWidgetItem(str(cell_data)))

    def perform_search_action(self):
        """Thực hiện tìm kiếm trong CSDL và hiển thị kết quả."""
        term = self.ui.otimkiem.text().strip()
        course = self.ui.cbkhoahoc.currentText() if self.ui.cbkhoahoc.currentIndex() != 0 else ""
        program = self.ui.cbHDT.currentText() if self.ui.cbHDT.currentIndex() != 0 else ""

        main_app.show_loading_screen(self)

        def do_search():
            try:
                results = database.search_students(term, course, program)
                self.populate_table(results)
                if not results:
                    QMessageBox.information(self, "Kết quả", "Không tìm thấy học viên nào phù hợp.")
            finally:
                main_app.hide_loading_screen()

        QtCore.QTimer.singleShot(100, do_search)

    # ==================================================================
    def calculate_statistics_action(self):
        main_app.show_loading_screen(self)
        QtCore.QTimer.singleShot(100, self._process_calculate_statistics)

    def _process_calculate_statistics(self):
        try:
            current_table_data = []
            # Lấy dữ liệu từ bảng kết quả tìm kiếm hiện tại
            for row_idx in range(self.ui.bang.rowCount()):
                row_content = [self.ui.bang.item(row_idx, col_idx).text() if self.ui.bang.item(row_idx, col_idx) else ""
                               for col_idx in range(self.ui.bang.columnCount())]
                current_table_data.append(row_content)

            data_to_analyze = current_table_data
            selection = self.ui.cbthongke.currentText()

            if not data_to_analyze:
                self.ui.bangketqua.setPlainText("Không có dữ liệu học viên để thống kê (có thể do bộ lọc hiện tại).")
                return

            if self.ui.cbthongke.currentIndex() == 0 or selection == "Chọn loại thống kê":
                self.ui.bangketqua.setPlainText("Vui lòng chọn loại thống kê.")
                return

            today = datetime.today()
            total = len(data_to_analyze)
            genders = Counter(row[3] for row in data_to_analyze if len(row) > 3 and row[3])
            khoahoc_by_he_dt = defaultdict(lambda: Counter())
            age_buckets = Counter()

            def classify_age(age):
                if age < 10:
                    return "Dưới 10 tuổi"
                elif 10 <= age <= 15:
                    return "10–15 tuổi"
                elif 15 < age <= 25:
                    return "15–25 tuổi"
                elif 25 < age <= 45:
                    return "25–45 tuổi"
                else:
                    return "Trên 45 tuổi"

            for row in data_to_analyze:
                if len(row) < 7: continue
                try:
                    if row[2]:
                        birth_date = datetime.strptime(row[2], "%Y-%m-%d")
                        age = relativedelta(today, birth_date).years
                        age_buckets[classify_age(age)] += 1
                except (ValueError, TypeError):
                    pass
                he_dt_val = row[6] if len(row) > 6 and row[6] else "Không XĐ"
                khoa_hoc_val = row[5] if len(row) > 5 and row[5] else "Không XĐ"
                khoahoc_by_he_dt[he_dt_val][khoa_hoc_val] += 1

            lines = []
            if selection == "Chọn tất cả" or selection == "Tổng số lượng, tỉ lệ theo giới tính":
                lines.append(f"Tổng số lượng học viên (đang hiển thị): {total}")
                for gender_val in ["Nam", "Nữ"]:
                    count = genders.get(gender_val, 0)
                    percent = (count / total) * 100 if total > 0 else 0
                    lines.append(f"- {gender_val}: {count} ({percent:.1f}%)")
                other_genders_count = total - genders.get("Nam", 0) - genders.get("Nữ", 0)
                if other_genders_count > 0:
                    percent = (other_genders_count / total) * 100 if total > 0 else 0
                    lines.append(f"- Khác/Không XĐ: {other_genders_count} ({percent:.1f}%)")
                lines.append("-" * 20)

            if selection == "Chọn tất cả" or selection == "Tỉ lệ độ tuổi theo học":
                lines.append("Phân bố độ tuổi học viên (đang hiển thị):")
                if not age_buckets: lines.append("  Không có dữ liệu độ tuổi.")
                age_order = ['Dưới 10 tuổi', '10–15 tuổi', '15–25 tuổi', '25–45 tuổi', 'Trên 45 tuổi']
                sorted_age_items = sorted(age_buckets.items(),
                                          key=lambda x: age_order.index(x[0]) if x[0] in age_order else len(age_order))
                for bucket, count in sorted_age_items:
                    percent = (count / total) * 100 if total > 0 else 0
                    lines.append(f"- {bucket}: {count} học viên ({percent:.1f}%)")
                lines.append("-" * 20)

            if selection == "Chọn tất cả" or selection == "Số lượng theo hệ đào tạo và tỉ lệ khóa học":
                lines.append("Thống kê theo Hệ đào tạo và Khóa học (đang hiển thị):")
                if not khoahoc_by_he_dt: lines.append("  Không có dữ liệu.")
                for he, kh_counter in khoahoc_by_he_dt.items():
                    total_hv_in_he = sum(kh_counter.values())
                    lines.append(f"- Hệ {he if he else 'Không XĐ'} (Tổng: {total_hv_in_he} HV):")
                    if not kh_counter: lines.append("    Không có khóa học."); continue
                    sorted_kh = sorted(kh_counter.items(), key=lambda item: item[1], reverse=True)
                    for kh, count_kh in sorted_kh:
                        percent_kh = (count_kh / total_hv_in_he) * 100 if total_hv_in_he > 0 else 0
                        lines.append(f"    + {kh if kh else 'Không XĐ'}: {count_kh} HV ({percent_kh:.1f}%)")
                lines.append("-" * 20)

            if lines and lines[-1] == "-" * 20: lines.pop()
            self.ui.bangketqua.setPlainText("\n".join(lines).strip() if lines else "Không có kết quả cho lựa chọn này.")

        except Exception as e:
            self.ui.bangketqua.setPlainText(f"Lỗi khi tính toán thống kê: {e}")
        finally:
            main_app.hide_loading_screen()

    def export_to_excel_placeholder(self):
        QMessageBox.information(self, "Thông báo", "Chức năng Xuất Excel chưa được triển khai.")

    def go_back_to_qlhv_action(self):
        main_app.show_qlhv_window(self.main_window.current_user)

class MainApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.qlhv_window = None
        self.quenmk_window = None
        self.timkiem_window = None
        self.loading_widget = None
        self.loading_movie = None
        self._ensure_loading_widget_created()

    def _ensure_loading_widget_created(self):
        if self.loading_widget: return
        self.loading_widget = QtWidgets.QLabel()
        try:
            self.loading_movie = QtGui.QMovie("giaodien/load.gif")
            if not self.loading_movie.isValid(): self.loading_movie = None
        except Exception:
            self.loading_movie = None
        if self.loading_movie:
            self.loading_widget.setMovie(self.loading_movie)
            self.loading_widget.setFixedSize(QtCore.QSize(80, 80));
            self.loading_movie.setScaledSize(QtCore.QSize(80, 80))
            self.loading_widget.setStyleSheet("background-color: transparent;")
        else:
            self.loading_widget.setText("Đang tải...")
            self.loading_widget.setStyleSheet(
                "QLabel { color: white; background-color: rgba(0,0,0,180); padding: 20px; border-radius: 10px;}")
        self.loading_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_widget.setWindowFlags(
            QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.loading_widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

    def show_loading_screen(self, parent_window):
        if not parent_window or not parent_window.isVisible():
            active_win = self._get_current_visible_window() or self.app.primaryScreen()
        else:
            active_win = parent_window
        center_point = active_win.geometry().center()
        self.loading_widget.move(center_point.x() - self.loading_widget.width() // 2,
                                 center_point.y() - self.loading_widget.height() // 2)
        self.loading_widget.show()
        if self.loading_movie: self.loading_movie.start()
        QApplication.processEvents()

    def hide_loading_screen(self):
        if self.loading_widget:
            if self.loading_movie: self.loading_movie.stop()
            self.loading_widget.hide()

    def show_delayed_messagebox(self, parent, title, text, icon, delay_ms=200, on_close_action=None):
        def _execute():
            self.hide_loading_screen()
            msg_box = QMessageBox(parent)
            msg_box.setWindowTitle(title);
            msg_box.setText(text);
            msg_box.setIcon(icon)
            msg_box.exec_()
            if on_close_action:
                on_close_action()

        QtCore.QTimer.singleShot(delay_ms, _execute)

    def _get_current_visible_window(self):
        for window in [self.login_window, self.qlhv_window, self.quenmk_window, self.timkiem_window]:
            if window and window.isVisible():
                return window
        return None

    def start(self):
        database.initialize_database()
        self.login_window.show()
        sys.exit(self.app.exec_())

    def show_qlhv_window(self, username=""):
        current_win = self._get_current_visible_window()
        self.show_loading_screen(current_win)

        def setup_and_show():
            if not self.qlhv_window: self.qlhv_window = QLHVWindow()
            self.qlhv_window.set_current_user(username)
            self.qlhv_window.load_students_from_db()
            if current_win: current_win.hide()
            self.qlhv_window.show()
            self.hide_loading_screen()

        QtCore.QTimer.singleShot(500, setup_and_show)

    def show_login_window(self):
        current_win = self._get_current_visible_window()
        if current_win: current_win.hide()
        self.login_window.ui.nhapuser.clear();
        self.login_window.ui.nhapmk.clear()
        self.login_window.show()

    def show_quenmk_window(self):
        current_win = self._get_current_visible_window()
        self.show_loading_screen(current_win)

        def setup_and_show():
            if not self.quenmk_window:
                self.quenmk_window = ForgotPasswordWindow()
            if current_win:
                current_win.hide()
            self.quenmk_window.show()
            self.hide_loading_screen()

        QtCore.QTimer.singleShot(200, setup_and_show)

    def show_search_window(self, parent_window):
        if not self.timkiem_window:
            self.timkiem_window = TimKiemWindow(parent_window)
        parent_window.hide()
        self.timkiem_window.show()


if __name__ == '__main__':
    main_app = MainApplication()
    main_app.start()