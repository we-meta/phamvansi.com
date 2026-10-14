# Kiểm tra video

Bản dựng: 16 cảnh, 1920×1080, 30 fps, tổng 300,2 giây (5,00 phút). Chưa có giọng đọc.

| Mục kiểm tra | Đạt / Chưa đạt | Ghi chú |
| - | - | - |
| Báo cáo kết quả làm nguồn | Chưa đạt | Không có `07_synthesis/bao_cao_ket_qua.md`. Video giới thiệu **tài liệu khung**, mọi cảnh ghi rõ "không phải kết quả nghiên cứu" |
| Giọng đọc (TTS) | Chưa đạt | Mạng chặn edge-tts, gTTS và nơi tải giọng piper. Người dùng sẽ tạo giọng sau; văn bản TTS nằm ở `audio/canh_XX.txt` |
| Tổng thời lượng trong 5 phút ±15% | Đạt (ước tính) | 300,2 s, ước tính với tốc độ 3,6 âm tiết/giây. Cần đo lại sau khi có audio thật |
| Độ phân giải, fps | Đạt | ffprobe: h264 1920×1080, 30/1 ở cả hai bản |
| Có luồng âm thanh | Đạt (im lặng) | AAC 48 kHz stereo, hiện là âm thanh im lặng |
| Phụ đề mềm trong `video_ket_qua.mp4` | Đạt | Luồng mov_text, ngôn ngữ vie |
| Phụ đề in vào hình trong `video_ket_qua_phude.mp4` | Đạt | Font Be Vietnam Pro, nằm trên dòng nguồn, không đè nội dung (đã xem khung cảnh 5 và `kiem_tra_khung.png`) |
| Phụ đề ≤ 42 ký tự/dòng, ≤ 2 dòng/khung | Đạt | 93 khung, dòng dài nhất 42 ký tự |
| Lệch phụ đề so với audio | Chưa kiểm được | Chưa có audio. Hiện thời gian phụ đề được chia theo số ký tự trong thời lượng ước tính; sẽ tự căn lại theo audio thật khi chạy `build.py` |
| Dấu tiếng Việt, không có ô vuông thay ký tự | Đạt | Đã xem từng PNG trong `frames/` và khung giữa mỗi cảnh |
| Chữ không tràn khung | Đạt | `build.py` kiểm tự động: không phần tử nào vượt vùng nội dung (chừa 228 px cuối cho phụ đề) |
| Chữ trên màn hình ≤ 6 dòng, ≤ 60 ký tự | Đạt | `build.py` kiểm khi dựng |
| Cỡ chữ thân ≥ 36 px | Đạt một phần | Thân bài và danh sách ≥ 36 px. Nhãn trong sơ đồ dày (cảnh 4, 7, 9, 13) và dòng chú thích thuật ngữ dùng 26–32 px |
| Màu trạng thái claim thống nhất, có nhãn chữ | Đạt | Cảnh 10: Candidate xanh dương, Testing vàng, Supported xanh lá, Rejected đỏ, Inconclusive xám |
| Nguồn ghi ở góc dưới mỗi cảnh | Đạt | Ghi mục trong tài liệu và mã Sxx (cảnh 3, 16) |
| Cảnh giới hạn | Đạt | Cảnh 14, lấy từ mục 7.4, 0.5 và 13 |
| Cảnh nguồn chính | Đạt | Cảnh 16, S01–S16 |
| Đối chiếu số liệu với `nguon_so_lieu.md` | Đạt | Mọi con số đều có trong tài liệu (xem bảng nguồn) |
| An toàn: tấn công chỉ ở mức khái niệm | Đạt | Không có cảnh nào mô tả quy trình tấn công |
| Chuẩn hóa âm lượng (loudnorm) | Chưa áp dụng | Chỉ bật khi có audio thật |
