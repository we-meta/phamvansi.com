# Bảng phát âm

Lời đọc trong `storyboard.json` dùng cú pháp `[hiển thị|cách đọc]`. Phụ đề lấy phần hiển thị,
file đưa vào TTS (`audio/canh_XX.txt`) lấy phần cách đọc. Trên màn hình vẫn giữ thuật ngữ gốc.

Giọng đang dùng: Piper `vi_VN-vais1000-medium`. Giọng này đọc kém chuỗi chữ cái Latin
(R, L, TPM, FPGA, MITRE…). Mỗi cách đọc dưới đây đã được kiểm bằng cách cho TTS đọc, rồi
dùng model nhận dạng tiếng Việt `sherpa-onnx-zipformer-vi-2025-04-20` nghe lại.

| Trên màn hình | Trong lời đọc | Kết quả nhận dạng / lý do |
| - | - | - |
| D1 … D4 | mức đê một … mức đê bốn | Nhận đúng thành "d một" |
| HS-06, HS-13 | nhánh hát ét không sáu, nhánh hát ét mười ba | Nhận đúng thành "hs" |
| R1 … R6 | mức thứ nhất … mức thứ sáu | "e rờ", "a rờ", "rờ" đều bị nghe thành "e", "a", "giờ" |
| L0, L5, L8 | lớp không, lớp năm, lớp tám | "e lờ", "lờ" bị nghe thành "e", "l" |
| TPM (cảnh 3) | bộ tăng tốc mật mã | Cảnh 3 nêu một ví dụ khác cùng danh sách trong mục 1.1; "tê pê em" bị nghe thành "tt m" |
| TPM (cảnh 16) | mô đun nền tảng tin cậy | Viết không gạch nối; "mô-đun" bị nghe thành "môn" |
| FPGA | mạch lập trình được | "ép pê giê a" bị nghe thành "fpcia" |
| ASIC | chíp chuyên dụng | "a xích" bị nghe thành "axit" |
| NIST | nít | Nhận thành "nit" |
| MITRE, CHES, HOST (cảnh 16) | danh mục điểm yếu phần cứng; hai hội nghị chuyên ngành | "mai tơ", "chét", "hốt" bị nghe thành "mi", "chết", "hút"; tên vẫn hiện trên màn hình |
| Research / Deep Research | nghiên cứu / nghiên cứu chuyên sâu | Thay bằng từ tiếng Việt |
| claim | mệnh đề | |
| side-channel | kênh phụ | Theo glossary, Phụ lục A |
| protocol | đề cương | |
| evidence matrix | ma trận bằng chứng | |
| artifact | mã và dữ liệu | |
| reproducibility | khả năng tái lập | |
| gap | khoảng trống | |
| Physical Design, PPA | thiết kế vật lý; công suất, hiệu năng, diện tích | |
| 2026 | hai nghìn không trăm hai mươi sáu | Viết thành chữ để TTS đọc đúng |

Tỷ lệ lỗi từ (WER) khi model nhận dạng nghe lại cả 16 cảnh trước lần sửa cuối là khoảng 5%
trung bình. Phần lớn số lỗi đó là do model ghi "đê" thành "d" và "hát ét" thành "hs", không
phải lỗi đọc. Lỗi còn sót: "truy vết mệnh đề" đôi khi bị nghe mất chữ "mệnh". Đây là đánh giá
bằng máy; vẫn nên nghe lại bằng tai.

Đổi cách đọc: sửa phần sau dấu `|` trong `storyboard.json`, rồi chạy `python3 tao_giong.py --toc-do 0.9`.
