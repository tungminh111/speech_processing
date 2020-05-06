# speech_processing

Sử dụng phần mềm bằng cách chọn tên article trùng với tên folder data. 

# Assignment2 

* Tạo thêm thư mục output_data để lưu kết quả
* Tải toàn bộ data về bằng cách chạy load_assignment1.py, giải nén ra và xóa file zip đi, các mã số sinh viên dùng được vào 5/5 là 17020616, 17021184, 17021186, 17021187, 17020709, 17021194, 17021200, 17020039, 17021059, 17020042, 16022494, 17021311

* Chọn từ cần bắt đầu cắt bằng cách thay đổi tham số khi gọi hàm reader.recordWord trong file CSVReader.py, tham số chính là từ cần dùng
* Vào folder ouput_data, tạo folder mới có tên là từ cần dùng, folder này dùng để chứa các file ghi âm đầu ra của từ này
* Chạy file CSVReader.py để tìm các file audio chứa từ cần ghi
* Mỗi bước chương trình in ra câu mà file đó chứa và đường dẫn của file
* Vào audacity mở file lên, view bằng spectrogram (xem hướng dẫn https://www.youtube.com/watch?v=7WYw3qoTdU4), mỗi từ khi được phát âm thì thanh đỏ sẽ cao lên, khi kết thúc thì nó thấp dần, dùng đặc tính này để căn đoạn cắt từ mình cần, nên nghe qua trước khi cắt. (Hướng dẫn cắt audio https://www.youtube.com/watch?v=x8Mxnc4F-EU)
* Cắt xong muốn chuyển sang câu khác thì quay lại chương trình CSVReader.py
