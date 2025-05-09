# Hệ Thống Quản Lý Sinh Viên

Đây là một ứng dụng quản lý sinh viên được xây dựng bằng Python với giao diện đồ họa sử dụng PyQt6 và cơ sở dữ liệu MySQL. Ứng dụng cho phép quản lý thông tin sinh viên, bao gồm thêm, sửa, xóa và tìm kiếm sinh viên.

## Tính Năng

- **Thêm Sinh Viên**: Thêm sinh viên chính quy hoặc tại chức với các thông tin như mã sinh viên, tên, ngày sinh, khoa và loại sinh viên.
- **Sửa Sinh Viên**: Chỉnh sửa thông tin của sinh viên hiện có.
- **Xóa Sinh Viên**: Xóa sinh viên khỏi cơ sở dữ liệu.
- **Tìm Kiếm Sinh Viên**: Tìm kiếm sinh viên theo mã, tên, khoa hoặc kết hợp khoa và tên.
- **Lọc Sinh Viên**: Lọc danh sách sinh viên theo loại (Tất cả, Chính quy, Tại chức).
- **Tích Hợp Cơ Sở Dữ Liệu**: Sử dụng MySQL để lưu trữ và quản lý dữ liệu sinh viên.

## Yêu Cầu

- Python 3.10 hoặc mới hơn
- MySQL Server
- Các thư viện Python cần thiết (xem bên dưới)

## Cài Đặt

1. Cài đặt các thư viện cần thiết:
   pip install PyQt6 mysql-connector-python
2. Thiết lập cơ sở dữ liệu MySQL:

Import tệp SQL db/db_ltudkt.sql vào MySQL Server của bạn.
Cập nhật thông tin kết nối cơ sở dữ liệu trong tệp db/dbconnect.py nếu cần.

3. Chạy ứng dụng
   python main.py

## Hướng dẫn sử dụng
Thêm Sinh Viên: Nhấn nút "Add" để mở form thêm sinh viên mới.
Sửa Sinh Viên: Chọn một sinh viên trong bảng và nhấn nút "Edit" để chỉnh sửa thông tin.
Xóa Sinh Viên: Chọn một sinh viên trong bảng và nhấn nút "Delete" để xóa.
Tìm Kiếm Sinh Viên: Sử dụng các trường tìm kiếm để tìm sinh viên theo mã, tên hoặc khoa.
Lọc Sinh Viên: Sử dụng menu thả xuống để lọc danh sách sinh viên theo loại.

## Cơ sở dữ liệu
Cơ sở dữ liệu bao gồm các bảng:

student: Lưu thông tin chung của sinh viên.
regularstudent: Lưu thông tin chi tiết của sinh viên chính quy.
inservicestudent: Lưu thông tin chi tiết của sinh viên tại chức.

## Đóng góp
Mọi đóng góp đều được hoan nghênh! Vui lòng fork dự án và gửi pull request.

## Liên hệ
Nếu có bất kỳ câu hỏi hoặc vấn đề nào, vui lòng liên hệ:

Tên: Nguyễn Trường Duy
Email: ntduy279@gmail.com
