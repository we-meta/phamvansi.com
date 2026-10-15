# Kiểm tra video

Bản dựng: 16 cảnh, 1920×1080, 30 fps, tổng 266,4 giây (4:26).
Giọng: Piper `vi_VN-vais1000-medium`, giọng nữ tổng hợp, chạy offline qua sherpa-onnx, tốc độ 0.9.

| Mục kiểm tra | Đạt / Chưa đạt | Ghi chú |
| - | - | - |
| Báo cáo kết quả làm nguồn | Chưa đạt | Không có `07_synthesis/bao_cao_ket_qua.md`. Video giới thiệu **tài liệu khung**, mọi cảnh ghi rõ "không phải kết quả nghiên cứu" |
| Giọng đọc (TTS) | Đạt | edge-tts, gTTS và HuggingFace bị chặn mạng, nên dùng Piper offline với model tải từ GitHub Releases. Đo cao độ trung vị khoảng 240 Hz, khớp tham số `giong=nu` |
| Tổng thời lượng trong 5 phút ±15% (4:15–5:45) | Đạt | 266,4 s. Giọng Piper đọc nhanh hơn ước tính, kể cả khi đã giảm tốc độ còn 0.9 |
| Độ phân giải, fps | Đạt | ffprobe: h264 1920×1080, 30/1 ở cả hai bản |
| Có luồng âm thanh | Đạt | AAC 48 kHz stereo |
| Âm lượng đều, chuẩn hóa | Đạt | loudnorm, tích hợp −16,0 LUFS; mức trung bình từng cảnh từ −18 đến −20 dB |
| Phát âm thuật ngữ | Đạt một phần | Kiểm bằng nhận dạng giọng nói offline, WER trung bình khoảng 5%; xem `phat_am.md`. Chưa nghe lại bằng tai |
| Phụ đề mềm trong `video_ket_qua.mp4` | Đạt | Luồng mov_text, ngôn ngữ vie |
| Phụ đề in vào hình trong `video_ket_qua_phude.mp4` | Đạt | Font Be Vietnam Pro, nằm trên dòng nguồn, không đè nội dung |
| Phụ đề ≤ 42 ký tự/dòng, ≤ 2 dòng/khung | Đạt | 93 khung, dòng dài nhất 42 ký tự |
| Lệch phụ đề so với audio | Đạt | Mỗi câu được tổng hợp riêng nên có mốc thật (`audio/canh_XX.json`). So 81 điểm đầu câu với điểm bắt đầu tiếng (silencedetect): lệch TB 0,06 s, tối đa 0,15 s. Đầu video 0,15 s / giữa 129,45 s / cuối 264,34 s đều khớp |
| Dấu tiếng Việt, không có ô vuông thay ký tự | Đạt | Đã xem từng PNG trong `frames/` và `kiem_tra_khung.png` |
| Chữ không tràn khung | Đạt | `build.py` kiểm tự động: không phần tử nào vượt vùng nội dung (chừa 228 px cuối cho phụ đề) |
| Chữ trên màn hình ≤ 6 dòng, ≤ 60 ký tự | Đạt | `build.py` kiểm khi dựng |
| Cỡ chữ thân ≥ 36 px | Đạt một phần | Thân bài và danh sách ≥ 36 px. Nhãn trong sơ đồ dày (cảnh 4, 7, 9, 13) và dòng chú thích thuật ngữ dùng 26–32 px |
| Màu trạng thái claim thống nhất, có nhãn chữ | Đạt | Cảnh 10: Candidate xanh dương, Testing vàng, Supported xanh lá, Rejected đỏ, Inconclusive xám |
| Nguồn ghi ở góc dưới mỗi cảnh | Đạt | Ghi mục trong tài liệu và mã Sxx (cảnh 3, 16) |
| Cảnh giới hạn | Đạt | Cảnh 14, lấy từ mục 7.4, 0.5 và 13 |
| Cảnh nguồn chính | Đạt | Cảnh 16, S01–S16 |
| Đối chiếu số liệu với `nguon_so_lieu.md` | Đạt | Mọi con số đều có trong tài liệu |
| An toàn: tấn công chỉ ở mức khái niệm | Đạt | Không có cảnh nào mô tả quy trình tấn công |
| Giọng không mô phỏng người thật | Đạt | Giọng tổng hợp có sẵn của Piper |
