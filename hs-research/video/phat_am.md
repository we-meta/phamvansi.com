# Bảng phát âm

Lời đọc trong `storyboard.json` dùng cú pháp `[hiển thị|cách đọc]`. Phụ đề lấy phần hiển thị,
file đưa vào TTS (`audio/canh_XX.txt`) lấy phần cách đọc. Trên màn hình vẫn giữ thuật ngữ gốc.

| Trên màn hình | Trong lời đọc | Ghi chú |
| - | - | - |
| L0, L5, L8 | lớp L không, lớp L năm, lớp L tám | |
| R1 … R6 | mức R một … mức R sáu | |
| D1 … D4 | mức D một … mức D bốn | |
| HS-01, HS-06, HS-13, HS-16 | H S không một, nhánh H S không sáu, nhánh H S mười ba, H S mười sáu | |
| TPM | tê pê em | |
| FPGA | ép pê giê a | |
| ASIC | a xích | |
| NIST | nít | |
| MITRE | mai tơ | |
| CHES | chét | |
| HOST | hốt | |
| Research / Deep Research | nghiên cứu / nghiên cứu chuyên sâu | Thay bằng từ tiếng Việt |
| Hardware Security | bảo mật phần cứng | Thay bằng từ tiếng Việt |
| claim | mệnh đề | Thay bằng từ tiếng Việt |
| side-channel | kênh phụ | Theo glossary, Phụ lục A |
| protocol | đề cương | |
| evidence matrix | ma trận bằng chứng | |
| artifact | mã và dữ liệu | |
| reproducibility | khả năng tái lập | |
| gap | khoảng trống | |
| Physical Design, PPA | thiết kế vật lý; công suất, hiệu năng, diện tích | |
| 2026 | hai nghìn không trăm hai mươi sáu | Viết thành chữ để TTS đọc đúng |

**Cần nghe lại sau khi tạo giọng:** tê pê em, ép pê giê a, a xích, nít, mai tơ, chét, hốt.
Nếu giọng TTS đọc các từ viết tắt tiếng Anh tốt hơn, sửa phần sau dấu `|` trong
`storyboard.json` rồi chạy lại `python3 build.py`.
