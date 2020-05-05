# speech_processing

Sử dụng phần mềm bằng cách chọn tên article trùng với tên folder data. 

# Assignment2 

* Tạo thêm thư mục output_data để lưu kết quả
* Tải toàn bộ data về bằng cách chạy load_assignment1.py, giải nén ra và xóa file zip đi, các mã số sinh viên dùng được vào 5/5 là 17020616, 17021184, 17021186, 17021187, 17020709, 17021194, 17021200, 17020039, 17021059, 17020042, 16022494, 17021311
* Vào file CSVReader thay đổi tham số đầu vào CSVReader là list các mã số sinh viên đã tải được dữ liệu, mã số sinh viên được lưu dưới dạng string, ví dụ ['17020035'] chứ không phải [17020035]
* Chọn từ cần bắt đầu cắt bằng cách thay đổi tham số khi gọi hàm reader.recordWord, tham số chính là từ cần dùng
* Vào folder ouput_data, tạo folder mới có tên là từ cần dùng, folder này dùng để chứa các file ghi âm đầu ra của từ này
* Mỗi bước chương trình sẽ in ra câu có chứa từ đó, câu được phát với tốc độ chậm hơn bình thường, người dùng nghe và khi nào cần record thì giữ phím SHIFT, chương trình sẽ record toàn bộ khoảng thời gian phím được giữ và lưu ra 1 file mới.
* Sau khi câu đã được đọc hết, nếu như cảm giác mình record còn chưa đúng thì có thể vào thư mục vừa tạo bên trên xóa những file vừa được tạo ra (lưu ý mỗi lần ghi âm xong nên vào folder xem đã ghi đến file bao nhiêu để lần sau nếu ghi lại còn biết file nào là file mới được ghi để xóa) bấm phím ESC chương trình sẽ đọc và cho phép record lại.
* Nếu đã ghi xong thì bấm phím mũi tên '->' để đến câu tiếp theo
