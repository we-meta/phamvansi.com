**Phân cấp toàn diện Research và Deep Research về Hardware Security**

Bản mở rộng chi tiết: bản đồ lĩnh vực, phân cấp chủ đề, quy trình khảo
cứu có truy vết bằng chứng và bộ mẫu hồ sơ

*Ngày đối chiếu nguồn: 14 tháng 10 năm 2026 · Bản mở rộng từ khung tổng
hợp gốc · Dùng cho nghiên cứu cá nhân và nhóm*

> *Tài liệu là khung tổng hợp đề xuất, không phải taxonomy chính thức
> của một tổ chức. Các nhánh giao nhau; dùng cây phân cấp để đọc và định
> hướng, dùng nhiều nhãn (multi-label) để quản lý tài liệu và bằng
> chứng. Việc đánh giá một thiết kế cụ thể vẫn cần dữ liệu, phép thử và
> phạm vi của chính thiết kế đó.*

**Mục lục**

0 Cách dùng tài liệu

0.1 Mục đích của bản mở rộng

Bản gốc đã đưa ra khung chín lớp (L0--L8), sáu mức research (R1--R6),
mười sáu nhánh chủ đề, mười trục khảo sát và quy trình deep research
mười hai bước. Bản này mở rộng khung đó theo ba hướng:

-   **Theo chiều sâu:** mỗi nhánh chủ đề được tách xuống ba đến bốn cấp,
    từ lĩnh vực tới chủ đề con có thể đặt thành câu hỏi nghiên cứu.

-   **Theo chiều vận hành:** mỗi lớp, mỗi mức research và mỗi bước quy
    trình có đầu vào, hoạt động, đầu ra và cổng chất lượng (quality
    gate).

-   **Theo chiều kiểm soát bằng chứng:** bổ sung hồ sơ nhánh, ma trận
    đối chiếu, thang trạng thái và các mẫu hồ sơ để mọi kết luận đều
    truy vết được về nguồn hoặc dữ liệu.

0.2 Quy ước mã phân cấp

  --------------------------------------------------------------------------
  **Mã**      **Ý nghĩa**                       **Ví dụ**
  ----------- --------------------------------- ----------------------------
  L0--L8      Lớp của bản phân cấp, từ mục đích L5 = literature research và
              tới chuyển giao                   deep research

  R1--R6      Mức độ sâu của research thông     R4 = systematic hoặc scoping
              thường                            review

  D1--D4      Mức độ sâu của deep research      D3 = kiểm tra artifact

  HS-01 ...   Nhánh chủ đề cấp 1                HS-06 = side-channel
  HS-16                                         

  HS-06.2     Nhánh con cấp 2                   HS-06.2 = cách khai thác và
                                                phân tích

  HS-06.2.3   Chủ đề cấp 3                      HS-06.2.3 = profiling và
                                                template attack

  A01--A10    Trục khảo sát                     A04 = tầng kỹ thuật

  P01--P12    Bước của quy trình deep research  P07 = đối chiếu và giải
                                                quyết mâu thuẫn

  T01--T14    Mẫu hồ sơ (template)              T04 = claim card

  S01--S16    Nguồn tham chiếu gốc              S07 = NIST SP 800-90B
  --------------------------------------------------------------------------

Cấp 4 trở xuống được trình bày dạng danh sách lồng nhau. Khi gắn nhãn
cho một paper, ghi mã ở cấp sâu nhất có căn cứ; không gắn cấp sâu hơn
mức nội dung nguồn thực sự hỗ trợ.

0.3 Ba lối đọc theo nhu cầu

  ------------------------------------------------------------------------
  **Người đọc**    **Mục tiêu**  **Lối đọc đề xuất**
  ---------------- ------------- -----------------------------------------
  Người mới vào    Nắm từ vựng   Phần 1 → HS-01, HS-02 → lướt hồ sơ nhánh
  lĩnh vực         và bản đồ     của 16 nhánh → Phụ lục A (glossary) → Phụ
                                 lục D (lộ trình đọc)

  Người đang chọn  Thu hẹp thành Phần 3 (nhánh quan tâm) → Phần 4 (trục và
  đề tài           câu hỏi khả   mẫu câu hỏi) → Phần 12 → mẫu T01, T13
                   thi           

  Người làm review Tạo hồ sơ có  Phần 2 → Phần 6 → Phần 7, 8 → Phần 10, 11
  hoặc deep        truy vết      
  research                       
  ------------------------------------------------------------------------

0.4 Thang trạng thái dùng thống nhất

  ------------------------------------------------------------------------
  **Đối      **Trạng thái**                **Ý nghĩa**
  tượng**                                  
  ---------- ----------------------------- -------------------------------
  Tổ hợp     Covered / Partial / Not       Trạng thái tìm kiếm và bằng
  trong      searched / Evidence missing / chứng của một ô trong ma trận
  coverage   Not applicable                trục; Not applicable phải có lý
  ledger                                   do

  Claim      Candidate / Testing /         Trạng thái của một mệnh đề cụ
             Supported / Rejected /        thể trong phạm vi đã nêu
             Inconclusive                  

  Nguồn      Identified / Screened / Full  Mức xử lý của một công trình
             text read / Extracted /       trong corpus
             Excluded                      

  Artifact   Accessible / Executable /     Mức kiểm tra reproducibility
             Reproduced / Robust under     
             change / Independently        
             replicated                    

  Gap        Retrieval gap / Evidence gap  Phân biệt "chưa tìm thấy" với
             đã xác minh / Đề tài khả thi  "đã có căn cứ là còn thiếu"
  ------------------------------------------------------------------------

0.5 Những điều tài liệu không làm

-   Không đưa ra hướng dẫn tấn công chi tiết lên thiết bị của người
    khác. Các nhánh tấn công được mô tả ở mức khái niệm, phương pháp
    đánh giá và điều kiện phòng thí nghiệm được phép.

-   Không thay thế một systematic corpus đã sàng lọc. Danh sách nguồn là
    đầu mối, cần kiểm tra version, trạng thái và errata trực tiếp.

-   Không gán điểm bảo mật tổng hợp cho cơ chế hay sản phẩm.

-   Không khẳng định một nhánh "chưa ai nghiên cứu"; mọi gap phải gắn
    với phạm vi tìm kiếm.

1 Phạm vi và cấu trúc tổng thể

1.1 Ba hướng nghiên cứu

  -----------------------------------------------------------------------
  **Hướng**     **Đối tượng**             **Câu hỏi trung tâm**
  ------------- ------------------------- -------------------------------
  Security of   Chip, IP, board, package, Phần cứng bị đọc bí mật, thay
  hardware      firmware gắn với phần     đổi hành vi, giả mạo hoặc phá
                cứng                      vỡ tin cậy bằng cách nào?

  Hardware for  Root of Trust, TPM,       Phần cứng cung cấp căn cứ tin
  security      secure element, HSM,      cậy và dịch vụ bảo mật gì cho
                enclave, bộ tăng tốc mật  hệ thống?
                mã                        

  Security      CPU, bộ nhớ, firmware,    Một thuộc tính bảo mật còn đúng
  across        OS, compiler, driver,     khi các tầng được tích hợp và
  hardware and  cloud workload            vận hành không?
  software                                
  -----------------------------------------------------------------------

NIST IR 8320 mô tả hardware-enabled security trong cloud và edge, với
nền tảng vật lý là một lớp của bảo vệ hệ thống. \[S01\]

1.1.1 Security of hardware --- các vùng con

-   Rò rỉ thông tin vật lý: side-channel (HS-06), rò rỉ qua test/debug
    (HS-10).

-   Thay đổi hành vi: fault injection (HS-07), Trojan và sửa đổi trong
    chuỗi cung ứng (HS-11).

-   Lỗi thiết kế và tích hợp: access control trên SoC (HS-09), luồng
    boot (HS-05), cấu hình lifecycle (HS-10).

-   Giả mạo và sao chép: counterfeit, overproduction, reverse
    engineering (HS-11).

-   Ảnh hưởng của hiện thực vật lý: placement, routing, power delivery
    (HS-13), package và chiplet (HS-14).

1.1.2 Hardware for security --- các vùng con

-   Neo tin cậy: boot ROM, OTP/eFuse, Root of Trust, TPM, DICE (HS-05).

-   Nguồn ngẫu nhiên và định danh vật lý: TRNG, PUF (HS-04).

-   Tăng tốc và bảo vệ mật mã: accelerator, key storage, masking
    (HS-03).

-   Cách ly và tính toán bảo mật: TEE, enclave, confidential computing
    (HS-08).

-   Thiết bị chuyên dụng: HSM, secure element, smartcard (HS-15).

1.1.3 Security across hardware and software --- các vùng con

-   Hợp đồng phần cứng/phần mềm: constant-time, ISA contract, leakage
    contract (HS-08, HS-12).

-   Chuỗi tin cậy qua firmware, OS và hypervisor (HS-05, HS-08).

-   Tác động của compiler, toolchain và EDA tới thuộc tính bảo mật
    (HS-11, HS-12, HS-13).

-   Bảo mật khi vận hành: update, recovery, attestation, quản lý vòng
    đời (HS-05, HS-10, HS-16).

1.2 Ranh giới với các lĩnh vực lân cận

  -----------------------------------------------------------------------------
  **Lĩnh vực**   **Giao với Hardware  **Khác biệt cần giữ**
                 Security ở đâu**     
  -------------- -------------------- -----------------------------------------
  Functional     Fault detection,     Safety giả định lỗi ngẫu nhiên; security
  safety         redundancy,          giả định đối thủ chọn thời điểm và vị trí
                 fail-safe            lỗi

  Reliability và PUF reliability,     Reliability đo xác suất hỏng tự nhiên;
  aging          entropy drift, fault security hỏi đối thủ có khai thác được
                 model                hay không

  Software       Constant-time code,  Phần mềm có thể vá; hành vi silicon
  security       firmware bug, driver thường không vá được sau khi chế tạo

  Network        Attestation, device  Network security thường giả định endpoint
  security       identity, secure     đáng tin; hardware security xét chính
                 channel              endpoint

  IC test và DFT Scan chain, JTAG,    Test tối đa hóa khả năng quan sát;
                 test mode            security giới hạn khả năng quan sát với
                                      người không được phép

  Cryptography   Primitive, protocol, Mật mã lý thuyết xét thuật toán; hardware
                 tham số              security xét hiện thực và môi trường vật
                                      lý

  Computer       Cache, speculation,  Kiến trúc tối ưu hiệu năng; bảo mật hỏi
  architecture   isolation            trạng thái chia sẻ nào làm lộ thông tin
  -----------------------------------------------------------------------------

1.3 Các lớp của bản phân cấp --- mở rộng

  -----------------------------------------------------------------------------------
  **Lớp**      **Câu hỏi chủ  **Đầu vào** **Hoạt động    **Sản       **Cổng chất
               đạo**                      chính**        phẩm**      lượng**
  ------------ -------------- ----------- -------------- ----------- ----------------
  L0 Mục đích  Nghiên cứu     Nhu cầu,    Viết research  Research    Quyết định và
               phục vụ quyết  bối cảnh,   brief, xác     brief (T01) tiêu chí dừng
               định gì?       ràng buộc   định người                 được ghi rõ
                                          dùng kết quả               

  L1 Từ vựng   Các khái niệm  Nguồn nền   Glossary,      Glossary    Phân biệt đúng
               có bị nhầm     tảng, chuẩn prerequisite   song ngữ,   các cặp khái
               không?                     map            bản đồ kiến niệm dễ nhầm
                                                         thức        

  L2 Chủ đề    Câu hỏi thuộc  Glossary,   Gắn nhãn       Taxonomy đã Mỗi nhãn có lý
               nhánh nào?     survey      HS-xx, xác     gắn nhãn    do
                                          định nhánh                 
                                          giao                       

  L3 Tầng và   Ở tầng nào,    Taxonomy,   Ma trận tầng × Ma trận     Ô ngoài phạm vi
  vòng đời     giai đoạn nào? threat      vòng đời       phạm vi     có lý do
                              model                                  

  L4 Câu hỏi   Câu hỏi nào có Ma trận     Dựng câu hỏi   Question    Mỗi câu hỏi có
               thể bác bỏ?    phạm vi     theo mẫu trục  register    điều kiện bác bỏ

  L5           Bằng chứng     Question    Protocol, tìm  Corpus,     Search log và
  Literature   hiện có nói    register    kiếm, sàng     evidence    exclusion log
  và deep      gì?                        lọc,           matrix      đầy đủ
  research                                extraction                 

  L6 Chứng     Kết quả có lặp Claim cần   Proof,         Notebook,   Experiment
  minh và thực lại hoặc chứng kiểm tra    simulation,    proof,      manifest khớp
  nghiệm       minh được                  đo,            trace, test với dữ liệu thô
               không?                     reproduction   report      

  L7 Tổng hợp  Đóng góp mới   Evidence    SoK,           Bản tổng    Tách finding,
               là gì?         matrix, kết guideline, bài hợp         interpretation
                              quả L6      báo                        và hypothesis

  L8 Chuyển    Kết quả dùng   Bản tổng    Checklist,     Sản phẩm    Được kiểm tra
  giao         vào công việc  hợp         công cụ, giáo  thực tế     với người dùng
               thế nào?                   trình                      mục tiêu
  -----------------------------------------------------------------------------------

Một review có hệ thống có thể dừng ở L5 và L7. Nghiên cứu thực nghiệm đi
sâu vào L6. Không cần chế tạo chip để mọi nghiên cứu đều có giá trị.

1.4 Quan hệ giữa các lớp

-   **Luồng chính:** L0 → L1 → L2 → L3 → L4 → L5 → (L6) → L7 → L8.

-   **Vòng lặp hẹp:** L4 ↔ L5. Kết quả tìm kiếm thường buộc phải sửa câu
    hỏi; ghi lại mọi lần sửa trong protocol (P02).

-   **Vòng lặp kiểm chứng:** L5 ↔ L6. Một claim mâu thuẫn trong
    literature có thể cần reproduction nhỏ trước khi tổng hợp.

-   **Vòng lặp phản hồi:** L8 → L0. Phản hồi từ người dùng thực tế tạo
    câu hỏi mới.

-   **Điểm dừng hợp lệ:** sau L5 (review), sau L6 (reproduction report),
    sau L7 (SoK, bài báo), sau L8 (công cụ, giáo trình).

1.5 Cây phân cấp và hệ đa nhãn

Cùng một thiết kế RISC-V có thể thuộc SoC isolation (HS-09), secure boot
(HS-05), side-channel (HS-06) và formal verification (HS-12). Vì vậy:

-   Dùng cây để điều hướng và đọc.

-   Dùng đa nhãn để quản lý paper: một nhãn chính (nhánh đóng góp chủ
    yếu) và các nhãn phụ.

-   Dùng trục A01--A10 (Phần 4) để định vị câu hỏi trong không gian
    nhiều chiều.

-   Dùng knowledge graph (Phần 9) khi số paper đủ lớn để truy vấn quan
    hệ thay vì duyệt cây.

2 Phân cấp theo độ sâu nghiên cứu

2.1 Research thông thường (R1--R6)

Research giải quyết nhu cầu hiểu hoặc ra quyết định trong phạm vi xác
định: tìm tài liệu, đọc tiêu chuẩn, xem thiết kế, so sánh phương pháp và
viết nhận định. Độ dài báo cáo không quyết định chất lượng.

  -------------------------------------------------------------------------
  **Mức**        **Mục tiêu**    **Công việc**       **Điều kiện hoàn
                                                     thành**
  -------------- --------------- ------------------- ----------------------
  R1 Orientation Hiểu ngôn ngữ   Đọc nguồn nền tảng, Giải thích đúng các
                 và ranh giới    tạo glossary        khái niệm dễ nhầm
                 lĩnh vực                            

  R2 Landscape   Biết các trường Tìm survey, tiêu    Có bản đồ chủ đề và
  mapping        phái và nhánh   chuẩn, paper mốc    nguồn cho từng nhánh

  R3 Focused     Hỗ trợ một lựa  So sánh các phương  Có bảng điều kiện, lợi
  comparative    chọn            án trong cùng       ích, chi phí và điểm
  research                       threat model        chưa rõ

  R4 Systematic  Tổng hợp có thể Protocol tìm kiếm,  Có search log,
  hoặc scoping   kiểm tra        sàng lọc,           exclusion log,
  review                         extraction          evidence matrix

  R5             Kiểm tra một    Chạy artifact, đo   Có dữ liệu, môi trường
  Reproduction   kết quả         lại, thử biến thể   và kết quả có thể lặp
  và validation                                      lại

  R6 Original    Tạo đóng góp    Đề xuất, đo, phân   Có novelty cụ thể,
  research       mới có căn cứ   tích hoặc chứng     baseline và giới hạn
                                 minh                kết luận
  -------------------------------------------------------------------------

2.1.1 R1 Orientation

-   **Hoạt động chi tiết:**

    -   Đọc một survey tổng quan và một chuẩn nền tảng của nhánh quan
        tâm.

    -   Lập glossary song ngữ với định nghĩa ngắn và nguồn.

    -   Liệt kê các cặp khái niệm dễ nhầm (ví dụ secure boot / measured
        boot; leakage detection / key recovery; TRNG / DRBG).

-   **Đầu ra:** glossary, danh sách prerequisite, ba đến năm câu hỏi mở.

-   **Cổng chất lượng:** giải thích được mỗi cặp khái niệm dễ nhầm bằng
    lời của mình, kèm nguồn.

-   **Sai lầm thường gặp:** học thuật ngữ từ blog hoặc slide mà không
    đối chiếu định nghĩa trong chuẩn hoặc paper gốc.

2.1.2 R2 Landscape mapping

-   **Hoạt động chi tiết:**

    -   Xác định venue chính, chuẩn và nhóm nghiên cứu của nhánh.

    -   Tìm survey, SoK và paper mốc; ghi năm, đóng góp, phương pháp.

    -   Vẽ bản đồ nhánh con và quan hệ giữa các trường phái.

-   **Đầu ra:** bản đồ chủ đề, danh sách paper candidate, coverage
    ledger sơ bộ.

-   **Cổng chất lượng:** mỗi nhánh con có ít nhất một nguồn gốc đã đọc,
    không chỉ survey.

-   **Sai lầm thường gặp:** coi taxonomy của một survey là taxonomy duy
    nhất; không phân biệt taxonomy đề xuất của mình với taxonomy từ
    nguồn.

2.1.3 R3 Focused comparative research

-   **Hoạt động chi tiết:**

    -   Cố định threat model, target và metric trước khi so sánh.

    -   Lập bảng phương án × điều kiện × lợi ích × chi phí × điểm chưa
        rõ.

    -   Đánh dấu các so sánh không công bằng (khác setup, khác metric,
        khác số thiết bị).

-   **Đầu ra:** bảng so sánh có điều kiện, khuyến nghị có phạm vi.

-   **Cổng chất lượng:** không xếp hạng các phương án được đánh giá dưới
    threat model khác nhau.

-   **Sai lầm thường gặp:** so sánh con số throughput hoặc số trace giữa
    các paper mà bỏ qua khác biệt setup.

2.1.4 R4 Systematic hoặc scoping review

-   **Hoạt động chi tiết:**

    -   Viết protocol trước (P02), chạy query families, deduplicate,
        sàng lọc hai vòng.

    -   Extraction theo schema cố định; đánh giá evidence profile của
        từng nguồn.

    -   Báo cáo theo nguyên tắc minh bạch (vận dụng PRISMA-ScR cho
        scoping review). \[S14\]

-   **Đầu ra:** search log, exclusion log, evidence matrix, flow diagram
    số lượng nguồn qua từng bước.

-   **Cổng chất lượng:** người khác chạy lại protocol thu được corpus
    tương đương.

-   **Sai lầm thường gặp:** sửa tiêu chí inclusion sau khi thấy kết quả
    mà không ghi lý do.

2.1.5 R5 Reproduction và validation

-   **Hoạt động chi tiết:**

    -   Kiểm tra artifact theo bậc: accessible → executable → reproduced
        → robust under change → independently replicated.

    -   Ghi môi trường, version, seed, thiết bị, điều kiện đo.

    -   Thử ít nhất một biến thể có ý nghĩa (thiết bị khác, session
        khác, seed khác).

-   **Đầu ra:** reproduction report (T12), dữ liệu thô, so sánh với kết
    quả gốc.

-   **Cổng chất lượng:** sai khác với kết quả gốc được giải thích hoặc
    ghi là chưa phân giải.

-   **Sai lầm thường gặp:** coi download hoặc build thành công là
    reproduction thành công.

2.1.6 R6 Original research

-   **Hoạt động chi tiết:**

    -   Xác định novelty cụ thể so với công trình gần nhất (closest
        work).

    -   Thiết kế baseline công bằng và phép thử có thể bác bỏ.

    -   Báo cáo giới hạn, negative result và điều kiện không bao phủ.

-   **Đầu ra:** bài báo, artifact, dataset, proof hoặc công cụ.

-   **Cổng chất lượng:** claim chính có evidence trực tiếp; phần suy
    rộng được ghi là hypothesis.

-   **Sai lầm thường gặp:** novelty dựa trên "chưa thấy trong lần tìm
    kiếm này" thay vì gap đã xác minh.

2.2 Deep research

Deep research ở đây là phương pháp khảo cứu sâu với truy vết bằng chứng.
Một vòng có giá trị cần:

-   Câu hỏi cụ thể và ranh giới rõ.

-   Tìm kiếm nhiều tuyến, gồm công trình nền tảng và kết quả mới.

-   Đọc phần phương pháp và giới hạn của nguồn gốc.

-   Đối chiếu bằng chứng thuận, nghịch và các điều kiện khác nhau.

-   Kiểm tra artifact hoặc thiết kế phép kiểm tra khi câu hỏi cần thực
    nghiệm.

-   Kết luận đúng phạm vi, nêu điểm chưa phân giải và quyết định tiếp
    theo.

Không bắt buộc mọi deep research đều chạy phần cứng. Một SoK có thể đóng
góp bằng cách chuẩn hóa khái niệm, chỉ ra benchmark không so sánh được
hoặc bác bỏ một giả định phổ biến. CHES/TCHES có hạng mục SoK và yêu cầu
giá trị bổ sung ngoài việc tổng hợp tài liệu. \[S02\]

2.2.1 Bốn mức độ sâu của deep research

  ---------------------------------------------------------------------------
  **Mức**   **Tên**    **Yêu cầu tối thiểu**               **Bằng chứng tạo
                                                           ra**
  --------- ---------- ----------------------------------- ------------------
  D1        Truy vết   Mọi claim trọng tâm truy về nguồn   Evidence matrix có
            nguồn gốc  gốc đã đọc full text; có source     locator
                       locator                             

  D2        Đối chiếu  D1 + evidence thuận/nghịch, phân    Claim register có
            có hệ      loại mâu thuẫn, kiểm tra điều kiện  trạng thái và lý
            thống      tương đương                         do

  D3        Kiểm tra   D2 + chạy hoặc kiểm tra artifact    Reproduction
            artifact   của ít nhất một kết quả then chốt   report

  D4        Thực       D3 + phép thử mới được thiết kế để  Experiment
            nghiệm độc bác bỏ hoặc mở rộng claim           manifest, dữ liệu
            lập                                            thô, kết quả
  ---------------------------------------------------------------------------

2.2.2 Dấu hiệu một vòng deep research chưa đạt

-   Kết luận dựa trên abstract hoặc tóm tắt thứ cấp.

-   Không có bằng chứng nghịch nào được tìm hoặc ghi nhận.

-   So sánh các kết quả khác threat model mà không ghi chú.

-   Gọi kết quả tìm kiếm trên web là exhaustive.

-   Gap được khẳng định mà không gắn với corpus và query.

2.3 Quan hệ giữa R và D

  ----------------------------------------------------------------------------
  **Mức        **Mức deep research thường đi **Ghi chú**
  research**   kèm**                         
  ------------ ----------------------------- ---------------------------------
  R1--R2       Chưa cần D; có thể D1 cho vài Ưu tiên rộng hơn sâu
               claim trọng tâm               

  R3           D1--D2                        So sánh cần điều kiện tương đương

  R4           D2                            Protocol và extraction bắt buộc

  R5           D3                            Artifact là trọng tâm

  R6           D2--D4                        Cần D2 để xác định gap, D4 cho
                                             đóng góp thực nghiệm
  ----------------------------------------------------------------------------

2.4 Chọn mức phù hợp

-   Cần hiểu để trao đổi với chuyên gia → R1--R2.

-   Cần chọn giữa hai hoặc ba phương án cho một dự án → R3 với D1--D2.

-   Cần một bản tổng hợp người khác kiểm tra được → R4 với D2.

-   Nghi ngờ một kết quả công bố → R5 với D3.

-   Muốn đóng góp mới → bắt đầu R4 thu hẹp, sau đó R5 trên công trình
    gần nhất, rồi R6.

-   Thời gian hoặc nguồn lực giới hạn → chọn mức thấp hơn nhưng ghi rõ
    phạm vi và trạng thái chưa phân giải.

3 Phân cấp chủ đề Hardware Security (HS-01 ... HS-16)

3.0 Cách đọc mỗi nhánh

Mỗi nhánh gồm: phạm vi; các nhánh con cấp 2 (HS-xx.y) với chủ đề cấp 3
và cấp 4 dạng danh sách lồng nhau; và một **hồ sơ nhánh** gồm câu hỏi
nghiên cứu theo mức (R1--R2, R3--R4, R5--R6), phương pháp, chỉ số và
bằng chứng, đầu ra, khái niệm dễ nhầm, bẫy và giới hạn, liên kết sang
nhánh khác và đầu mối nguồn.

  -------------------------------------------------------------------------
  **Mã**   **Nhánh**                        **Hướng       **Tầng trọng
                                            chính**       tâm**
  -------- -------------------------------- ------------- -----------------
  HS-01    Nền tảng liên ngành              Cả ba         Mọi tầng

  HS-02    Threat model và kiến trúc bảo    Cả ba         Specification,
           mật                                            system

  HS-03    Mật mã trong phần cứng           Hardware for  RTL, netlist
                                            security      

  HS-04    Entropy, TRNG và PUF             Hardware for  Transistor,
                                            security      layout, silicon

  HS-05    Root of Trust, boot, firmware và Hardware for  Firmware, system
           attestation                      security      

  HS-06    Side-channel                     Security of   Netlist, layout,
                                            hardware      silicon

  HS-07    Fault injection, tamper và       Security of   Silicon, package
           physical attack                  hardware      

  HS-08    Processor, microarchitecture và  Across HW/SW  RTL, system
           memory                                         

  HS-09    SoC, IP, interconnect và         Security of   RTL, SoC
           isolation                        hardware      

  HS-10    DFT, debug và lifecycle          Security of   RTL, netlist, vận
                                            hardware      hành

  HS-11    Supply chain, Trojan,            Security of   Toàn vòng đời
           counterfeit và IP protection     hardware      

  HS-12    Formal methods, security         Across HW/SW  Specification,
           verification và CAD                            RTL, netlist

  HS-13    Physical Design và đánh đổi      Security of   Netlist, layout
           Security--PPA                    hardware      

  HS-14    PCB, packaging, chiplet và       Security of   Package, PCB
           heterogeneous integration        hardware      

  HS-15    Hệ thống và lĩnh vực ứng dụng    Cả ba         System

  HS-16    Tiêu chuẩn, evaluation và        Cả ba         Mọi tầng
           assurance                                      
  -------------------------------------------------------------------------

HS-01 Nền tảng liên ngành

**Phạm vi:** kiến thức nền giúp hiểu vì sao một thuộc tính bảo mật có
thể đúng ở mô hình trừu tượng nhưng sai ở hiện thực.

HS-01.1 Điện tử và vật lý

-   CMOS và chuyển mạch

    -   Dynamic power, short-circuit current, leakage current

    -   Quan hệ giữa dữ liệu xử lý và năng lượng tiêu thụ

-   Delay và glitch

    -   Delay phụ thuộc dữ liệu, glitch trong mạch tổ hợp

    -   Ảnh hưởng của glitch tới các countermeasure giả định giá trị ổn
        định

-   Parasitic và coupling

    -   Capacitive coupling, crosstalk, EM coupling

-   Power distribution

    -   IR drop, decoupling, power grid và khả năng quan sát

-   Process variation và PVT

    -   Biến thiên giữa die, giữa wafer; nhiệt độ, điện áp, lão hóa

HS-01.2 Thiết kế số

-   RTL và FSM: encoding, trạng thái không hợp lệ, reset behavior

-   Synthesis và STA: tối ưu có thể làm mất cấu trúc bảo vệ

-   CDC và reset-domain crossing: trạng thái trung gian khi chuyển miền

-   Memory: SRAM, register file, retention

-   DFT: scan insertion, BIST

-   Physical design: floorplan, placement, CTS, routing, signoff

HS-01.3 Kiến trúc máy tính

-   Pipeline, cache, predictor, speculative execution

-   Privilege level, virtual memory, MMU, IOMMU

-   Bus, interconnect, DMA

-   Interrupt và exception

HS-01.4 Firmware và hệ thống

-   Bootloader, driver, interrupt handler

-   Linker, compiler và tác động của tối ưu hóa

-   Binary analysis và firmware image

HS-01.5 Mật mã

-   Primitive và protocol; security parameter

-   Key lifecycle: sinh, lưu, dùng, xoay vòng, hủy

-   Implementation security: khoảng cách giữa thuật toán và hiện thực

HS-01.6 Toán và đo lường

-   Xác suất và thống kê: kiểm định giả thuyết, khoảng tin cậy, multiple
    comparisons

-   Signal processing: lọc, căn chỉnh (alignment), biến đổi tần số

-   Information theory: entropy, min-entropy, mutual information

-   Experimental design: biến kiểm soát, lặp lại, randomization

Hồ sơ nhánh HS-01

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Những hiện tượng vật lý nào làm mô hình logic không mô tả
  R1--R2       đủ hành vi bảo mật?

  Câu hỏi      Từ một thuộc tính mật mã tới hiện thực RTL và silicon, cần
  R3--R4       giữ những giả định nào ở mỗi tầng?

  Câu hỏi      Mô hình trừu tượng nào đang bỏ qua hành vi có ý nghĩa đối
  R5--R6       với bảo mật, và có thể đo được sai khác đó không?

  Phương pháp  Đọc chuẩn và giáo trình; lập bản đồ giả định theo tầng; mô
               phỏng đơn giản để minh họa

  Chỉ số và    Không có metric riêng; bằng chứng là độ chính xác của định
  bằng chứng   nghĩa và giả định

  Đầu ra       Glossary song ngữ; prerequisite map; danh sách giả định
               theo tầng

  Khái niệm dễ Entropy và min-entropy; delay và glitch; correctness và
  nhầm         security

  Bẫy và giới  Coi kiến thức nền là "xong một lần"; thực tế mỗi nhánh cần
  hạn          quay lại nền tảng tương ứng

  Liên kết     Mọi nhánh; đặc biệt HS-06, HS-07, HS-13

  Đầu mối      Giáo trình thiết kế số và kiến trúc; chuẩn NIST liên quan
  nguồn        \[S07\] \[S13\]
  -----------------------------------------------------------------------

HS-02 Threat model và kiến trúc bảo mật

**Phạm vi:** xác định cái cần bảo vệ, khỏi ai, với năng lực nào và trong
ranh giới nào. Mọi nhánh khác phụ thuộc vào threat model.

HS-02.1 Asset

-   Bí mật: key, seed, credential

-   Mã và cấu hình: firmware, bitstream, fuse configuration

-   Dữ liệu người dùng và dữ liệu mô hình

-   Danh tính thiết bị

-   Design IP

-   Availability của dịch vụ

HS-02.2 Thuộc tính bảo mật

-   Confidentiality, integrity, authenticity

-   Isolation giữa các miền

-   Freshness và chống replay/rollback

-   Recovery sau khi bị xâm phạm

-   Non-repudiation và auditability (khi có liên quan)

HS-02.3 Đối thủ

-   Remote: chỉ qua giao diện mạng

-   Local software: chạy mã không đặc quyền trên cùng nền tảng

-   Privileged software: OS hoặc hypervisor không đáng tin

-   Physical access: ngắn hạn, dài hạn, có thiết bị đo

-   Insider: nhân sự thiết kế, sản xuất, bảo trì

-   Bên cung ứng không tin cậy: foundry, test house, IP vendor

HS-02.4 Năng lực đối thủ

-   Số lần quan sát và số lần thử

-   Quyền chọn input (known, chosen, adaptive)

-   Quyền chạy mã và mức đặc quyền

-   Độ chính xác đo: băng thông, độ phân giải thời gian, vị trí đầu dò

-   Loại tiếp cận vật lý: non-invasive, semi-invasive, invasive

-   Ngân sách: thời gian, thiết bị, chuyên môn

HS-02.5 Trust boundary và TCB

-   Trust anchor và chuỗi phụ thuộc

-   Trusted Computing Base và cách thu nhỏ TCB

-   Giả định về nhà sản xuất, chủ thiết bị, người vận hành

HS-02.6 Attack surface và ngoài phạm vi

-   Giao diện: bus, debug, test, clock/power/reset, cảm biến

-   Liệt kê điều kiện nằm ngoài phạm vi và lý do

OpenTitan trình bày threat model theo asset, attacker profile, attack
surface và attack method, bao gồm cả test/debug và clock/power/reset.
\[S03\]

Hồ sơ nhánh HS-02

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các thành phần chuẩn của threat model phần cứng là gì và
  R1--R2       được trình bày ra sao trong các thiết kế mở?

  Câu hỏi      Đối thủ có thể quan sát hoặc kiểm soát chính xác những
  R3--R4       thành phần nào; các paper trong nhánh X có nêu đủ năng lực
               đối thủ không?

  Câu hỏi      Điều gì thay đổi nếu nhà sản xuất, chủ thiết bị hoặc hệ
  R5--R6       điều hành không còn được tin cậy?

  Phương pháp  Threat modeling có cấu trúc; attack tree; phân tích trust
               boundary

  Chỉ số và    Độ đầy đủ của bảng asset--threat--control--evidence; số
  bằng chứng   giả định được nêu tường minh

  Đầu ra       Sơ đồ trust boundary; threat-model card (T02); bảng
               asset--threat--control--evidence

  Khái niệm dễ Trust và trustworthiness; TCB và Root of Trust; attack
  nhầm         surface và attack vector

  Bẫy và giới  Threat model quá rộng không kiểm tra được; quá hẹp loại bỏ
  hạn          đối thủ thực tế

  Liên kết     Mọi nhánh

  Đầu mối      \[S03\] \[S01\] \[S11\]
  nguồn        
  -----------------------------------------------------------------------

HS-03 Mật mã trong phần cứng

**Phạm vi:** hiện thực thuật toán mật mã trên phần cứng và các yêu cầu
bảo mật gắn với hiện thực đó.

HS-03.1 Symmetric crypto

-   Block cipher (AES): S-box, key schedule, mode of operation

-   Authenticated encryption

-   Hash và MAC

-   Lightweight crypto cho thiết bị hạn chế

HS-03.2 Public-key crypto

-   RSA: modular exponentiation, Montgomery multiplication

-   ECC: scalar multiplication, coordinate system, ladder

-   Arithmetic accelerator dùng chung

HS-03.3 Post-quantum crypto

-   KEM (ML-KEM, FIPS 203) và chữ ký (ML-DSA FIPS 204, SLH-DSA FIPS 205)
    \[S04\] \[S05\] \[S06\]

-   Lattice: NTT, polynomial multiplication, sampling

-   Hash-based: hash tree, nhiều lần gọi hash

-   Memory access pattern và băng thông

-   Bảo mật hiện thực của PQC: masking, fault resistance

HS-03.4 Microarchitecture của bộ tăng tốc

-   Iterative, unrolled, pipelined

-   Shared datapath giữa nhiều thuật toán

-   Trade-off area--throughput--latency--energy

HS-03.5 Hardware/software co-design

-   Phân chia phần cứng và phần mềm

-   Giao diện accelerator: register, DMA, interrupt

-   Key storage, key loading, key scheduling

HS-03.6 Yêu cầu bảo mật của hiện thực

-   Constant-time behavior

-   Masking và yêu cầu randomness

-   Fault resistance

-   Zeroization và xóa trạng thái

Hồ sơ nhánh HS-03

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các kiến trúc accelerator cho AES, ECC và PQC khác nhau ra
  R1--R2       sao về cấu trúc và chi phí?

  Câu hỏi      Với cùng thuật toán và mức tham số, kiến trúc nào đáp ứng
  R3--R4       throughput, energy và điều kiện bảo mật?

  Câu hỏi      Tối ưu arithmetic hoặc memory có thay đổi leakage, fault
  R5--R6       behavior hoặc randomness consumption không?

  Phương pháp  Functional validation với test vectors; synthesis và đo
               PPA; đánh giá leakage/fault kèm theo

  Chỉ số và    Throughput, latency, area, energy per operation,
  bằng chứng   randomness per operation, kết quả leakage/fault

  Đầu ra       Bảng kiến trúc; kết quả functional validation; benchmark
               có security context

  Khái niệm dễ Thuật toán an toàn và hiện thực an toàn; constant-time
  nhầm         phần mềm và phần cứng

  Bẫy và giới  Benchmark PPA không kèm điều kiện bảo mật; đổi sang PQC
  hạn          không tự động bảo đảm hiện thực an toàn

  Liên kết     HS-04 (randomness), HS-06, HS-07, HS-13

  Đầu mối      \[S04\] \[S05\] \[S06\] \[S02\]
  nguồn        
  -----------------------------------------------------------------------

HS-04 Entropy, TRNG và PUF

**Phạm vi:** nguồn ngẫu nhiên vật lý và định danh dựa trên biến thiên
vật lý.

HS-04.1 Entropy source

-   Noise source: jitter, metastability, thermal noise

-   Entropy estimate và min-entropy

-   Conditioning

-   Startup test và continuous health test

HS-04.2 Cấu trúc nguồn ngẫu nhiên

-   Ring oscillator và các biến thể

-   Ảnh hưởng PVT và nhiễu nguồn

-   TRNG, DRBG và cấu trúc Random Bit Generator

HS-04.3 PUF

-   SRAM PUF

-   Delay-based PUF: arbiter, ring-oscillator

-   Các cấu trúc dựa trên biến thiên vật lý khác

-   Weak PUF (sinh key) và strong PUF (challenge--response)

HS-04.4 Sinh và tái tạo key từ PUF

-   Enrollment

-   Reconstruction, fuzzy extractor, error-correcting code

-   Helper data và rò rỉ qua helper data

HS-04.5 Chất lượng PUF

-   Reliability theo PVT và aging

-   Uniqueness, bias, uniformity

-   Modelability bởi học máy

SP 800-90B quy định nguyên tắc và yêu cầu đối với entropy source cùng
các phép đánh giá liên quan. \[S07\]

Hồ sơ nhánh HS-04

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Entropy source, TRNG, DRBG và PUF khác nhau về chức năng
  R1--R2       và giả định bảo mật như thế nào?

  Câu hỏi      Entropy hoặc khả năng tái tạo key thay đổi thế nào theo
  R3--R4       nhiệt độ, điện áp và lão hóa?

  Câu hỏi      Helper data hoặc mô hình học máy làm thay đổi giả định bảo
  R5--R6       mật của PUF như thế nào?

  Phương pháp  Noise-source characterization; entropy assessment theo SP
               800-90B; đo nhiều điều kiện; thử modeling attack trên dữ
               liệu được phép

  Chỉ số và    Min-entropy estimate; health-test behavior; reliability
  bằng chứng   (intra-distance); uniqueness (inter-distance); bias; tỷ lệ
               reconstruction failure

  Đầu ra       Entropy dossier; dataset nhiều điều kiện; reliability
               report

  Khái niệm dễ Statistical randomness test và entropy assessment;
  nhầm         uniqueness và khả năng chống modeling

  Bẫy và giới  Statistical randomness tests đơn lẻ không chứng minh chất
  hạn          lượng entropy source; uniqueness đơn lẻ không chứng minh
               PUF chống được mô hình hóa

  Liên kết     HS-03, HS-05 (key provisioning), HS-13 (layout ảnh hưởng
               tới oscillator)

  Đầu mối      \[S07\] \[S16\]
  nguồn        
  -----------------------------------------------------------------------

HS-05 Root of Trust, boot, firmware và attestation

**Phạm vi:** thành phần phần cứng và firmware tạo căn cứ tin cậy cho
toàn hệ thống.

HS-05.1 Trust anchor

-   Immutable (boot ROM) và updateable trust anchor

-   OTP/eFuse và chính sách ghi

-   Key provisioning trong sản xuất

HS-05.2 Chuỗi boot

-   Secure boot: xác minh chữ ký trước khi chạy

-   Measured boot: đo và ghi trạng thái

-   Verified update và anti-rollback

-   Xử lý lỗi xác minh và đường fallback

HS-05.3 Firmware resiliency

-   Protect: bảo vệ vùng firmware

-   Detect: phát hiện thay đổi trái phép

-   Recover: khôi phục về trạng thái tốt

HS-05.4 Danh tính thiết bị

-   Device identity, certificate, endorsement

-   Ownership transfer

-   Layered identity (ví dụ DICE)

HS-05.5 Remote attestation

-   Evidence, freshness (nonce)

-   Verifier policy và reference values

-   Thời điểm đo và khoảng cách time-of-check/time-of-use

HS-05.6 Thành phần chuyên dụng

-   TPM, secure element, HSM

-   Root of Trust tích hợp trong SoC

NIST SP 800-193 tổ chức firmware resiliency quanh bảo vệ, phát hiện thay
đổi trái phép và phục hồi an toàn. TCG cung cấp đặc tả TPM 2.0 để nghiên
cứu các chức năng của TPM. \[S08\] \[S09\]

Hồ sơ nhánh HS-05

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Secure boot, measured boot và attestation khác nhau ở chức
  R1--R2       năng, bằng chứng và người kiểm tra như thế nào?

  Câu hỏi      Boot chain được kiểm chứng và khôi phục thế nào khi một
  R3--R4       thành phần bị thay đổi?

  Câu hỏi      Attestation xác nhận trạng thái nào, tại thời điểm nào và
  R5--R6       với giả định tin cậy nào?

  Phương pháp  State-machine modeling; negative-path testing; review
               policy; formal model của protocol khi cần

  Chỉ số và    Hành vi reject/accept; xử lý rollback; bằng chứng
  bằng chứng   recovery; độ phủ trạng thái

  Đầu ra       Boot-state diagram; update/recovery test matrix;
               attestation policy

  Khái niệm dễ Secure boot và measured boot; integrity và freshness;
  nhầm         identity và attestation

  Bẫy và giới  Chỉ test đường thành công; bỏ qua fault injection vào bước
  hạn          xác minh (giao với HS-07)

  Liên kết     HS-04, HS-07, HS-10, HS-16

  Đầu mối      \[S08\] \[S09\] \[S03\]
  nguồn        
  -----------------------------------------------------------------------

HS-06 Side-channel

**Phạm vi:** thông tin bí mật rò rỉ qua tín hiệu phụ thuộc hiện thực, và
cách đánh giá, giảm rò rỉ đó.

HS-06.1 Kênh quan sát

-   Timing

-   Power

-   Electromagnetic emission

-   Các tín hiệu phụ thuộc hiện thực khác (âm thanh, nhiệt, quang) ---
    ghi rõ khi thuộc phạm vi

HS-06.2 Cách khai thác và phân tích

-   Non-profiling: phân tích thống kê không cần thiết bị mẫu

-   Profiling: dựng mô hình trên thiết bị tương tự

-   Template attack

-   ML/DL-based analysis

-   Higher-order analysis cho hiện thực có masking

HS-06.3 Leakage model

-   Hamming weight, Hamming distance

-   Transition và glitch-aware model

-   Multivariate và higher-order

HS-06.4 Countermeasure

-   Masking (Boolean, arithmetic; glitch-robust masking)

-   Hiding: balancing, noise, shuffling

-   Constant-time cho timing

-   Giảm khả năng quan sát ở mức vật lý

HS-06.5 Điều kiện đo

-   Bandwidth, sampling rate, alignment, triggering

-   Preprocessing

-   Biến thiên giữa session, giữa thiết bị, theo PVT

HS-06.6 Đánh giá

-   Leakage detection (ví dụ TVLA)

-   Attack-based evaluation

-   Liên hệ giữa phát hiện rò rỉ và mức độ khai thác được

Hồ sơ nhánh HS-06

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các họ kênh quan sát, mô hình rò rỉ và countermeasure
  R1--R2       chính là gì?

  Câu hỏi      Tín hiệu nào chứa thông tin về secret dưới năng lực quan
  R3--R4       sát đã chọn?

  Câu hỏi      Countermeasure còn hiệu quả khi đổi thiết bị, session hoặc
  R5--R6       điều kiện PVT không?

  Phương pháp  Measurement protocol; leakage detection; attack-based
               evaluation trong lab được phép; cross-device validation

  Chỉ số và    Test statistic; SNR; success rate; guessing entropy hoặc
  bằng chứng   key rank theo protocol; số trace cần thiết

  Đầu ra       Measurement protocol; leakage-assessment report; raw trace
               và metadata

  Khái niệm dễ Leakage detected và key recoverable; masking order lý
  nhầm         thuyết và bảo vệ thực tế khi có glitch

  Bẫy và giới  TVLA với Welch's t-test có giới hạn khi dùng độc lập để
  hạn          suy ra mức an toàn \[S10\]; trace cùng thiết bị hoặc
               session tạo shortcut cho mô hình ML

  Liên kết     HS-03, HS-08 (timing microarchitecture), HS-13, HS-12

  Đầu mối      \[S10\] \[S02\] \[S15\]
  nguồn        
  -----------------------------------------------------------------------

HS-07 Fault injection, tamper và physical attack

**Phạm vi:** đối thủ chủ động làm sai hành vi phần cứng hoặc tiếp cận
vật lý trực tiếp.

HS-07.1 Nguồn lỗi

-   Electrical disturbance (điện áp)

-   Clock disturbance

-   Electromagnetic

-   Optical/laser

-   Điều kiện vật lý khác (nhiệt độ)

HS-07.2 Fault model

-   Bit flip, stuck-at

-   Instruction skip, corruption nhiều bit

-   Transient và persistent

-   Độ chính xác không gian và thời gian

HS-07.3 Tác động

-   Integrity của tính toán

-   Bỏ qua authentication hoặc kiểm tra chữ ký

-   Availability

-   Lộ key qua phân tích kết quả sai

HS-07.4 Countermeasure

-   Redundancy (thời gian, không gian)

-   Consistency check, error-detecting code

-   Sensor: glitch, clock, voltage, light, temperature

-   Fail-safe behavior và xử lý khi phát hiện

HS-07.5 Tamper

-   Tamper resistance, tamper evidence, tamper response

-   Shield, mesh, sensor bao bọc

HS-07.6 Mức tiếp cận

-   Non-invasive, semi-invasive, invasive

-   Reverse engineering vật lý (giao với HS-11)

Hồ sơ nhánh HS-07

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các nguồn lỗi, fault model và họ countermeasure được phân
  R1--R2       loại ra sao?

  Câu hỏi      Fault model trong mô phỏng có đại diện cho lỗi quan sát
  R3--R4       được trên mục tiêu vật lý không?

  Câu hỏi      Thiết kế phát hiện sai lệch và xử lý thế nào trước khi
  R5--R6       secret hoặc kết quả bị phát hành?

  Phương pháp  Fault simulation; injection campaign trên thiết bị được
               phép; outcome classification

  Chỉ số và    Detection rate; escape rate; false alarm; silent
  bằng chứng   corruption; phân bố kết quả theo tham số injection

  Đầu ra       Fault-model taxonomy; campaign report; detection/escape
               report

  Khái niệm dễ Lỗi ngẫu nhiên (reliability) và lỗi do đối thủ chọn
  nhầm         (security)

  Bẫy và giới  Fault model mô phỏng quá lý tưởng; chỉ báo cáo injection
  hạn          thành công mà không báo tổng số lần thử

  Liên kết     HS-03, HS-05, HS-12, HS-13, HS-14

  Đầu mối      \[S02\] \[S03\] \[S15\]
  nguồn        
  -----------------------------------------------------------------------

HS-08 Processor, microarchitecture và memory

**Phạm vi:** trạng thái chia sẻ trong vi kiến trúc và bộ nhớ có thể phá
vỡ cách ly giữa các miền phần mềm.

HS-08.1 Trạng thái vi kiến trúc

-   Cache, TLB, predictor

-   Speculative và transient execution

-   Resource sharing: port, buffer, SMT

HS-08.2 Kênh thời gian

-   Timing channel, contention

-   Covert channel và side channel trong vi kiến trúc

HS-08.3 Cách ly theo đặc quyền

-   Privilege transition, interrupt, context switch

-   Xóa trạng thái khi chuyển miền

HS-08.4 Bộ nhớ

-   DRAM disturbance

-   Retention và memory remanence

-   Memory encryption và integrity

HS-08.5 TEE và confidential computing

-   Enclave, VM-based TEE

-   TCB của TEE và giả định về OS/hypervisor

HS-08.6 Truy cập bộ nhớ ngoài CPU

-   DMA, IOMMU

-   Thiết bị ngoại vi có quyền truy cập bộ nhớ

Hồ sơ nhánh HS-08

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Những loại trạng thái nào trong vi kiến trúc có thể chia
  R1--R2       sẻ giữa các miền?

  Câu hỏi      Trạng thái nào còn chia sẻ khi phần mềm tưởng rằng các
  R3--R4       miền đã được cách ly?

  Câu hỏi      Một mitigation bảo vệ thuộc tính nào và gây chi phí nào ở
  R5--R6       workload thực tế?

  Phương pháp  State-sharing modeling; isolation test; benchmark có
               threat model; formal contract

  Chỉ số và    Channel capacity hoặc tỷ lệ lỗi bit; overhead hiệu năng
  bằng chứng   theo workload; số trạng thái được xóa

  Đầu ra       State-sharing model; threat-conditioned benchmark;
               isolation test; residual-risk table

  Khái niệm dễ Covert channel và side channel; mitigation và fix
  nhầm         

  Bẫy và giới  Đánh giá overhead trên microbenchmark không đại diện
  hạn          workload

  Liên kết     HS-06, HS-09, HS-12, HS-15

  Đầu mối      \[S01\] \[S11\]
  nguồn        
  -----------------------------------------------------------------------

HS-09 SoC, IP, interconnect và isolation

**Phạm vi:** chính sách truy cập và hợp đồng bảo mật giữa các block khi
tích hợp thành SoC.

HS-09.1 Access control trên interconnect

-   Bus/NoC access control

-   Address decode và alias

-   Privilege và security attribute propagation

HS-09.2 Cấu hình bảo mật

-   Memory map, security register

-   Lock bit và configuration ordering

-   Trạng thái mặc định khi reset

HS-09.3 Miền và master

-   Secure/non-secure domain

-   CPU, peripheral, accelerator, DMA master

-   Firewall cho peripheral

HS-09.4 Đường đi của secret

-   Key movement giữa block

-   Secret buffer và xóa sau khi dùng

-   Sideband và debug path

HS-09.5 Trạng thái bất thường

-   Reset một phần, error response

-   Power transition, clock gating

-   Cấu hình chưa hoàn tất

HS-09.6 Tích hợp IP

-   Hợp đồng bảo mật giữa block (security contract)

-   Giả định của IP vendor và trách nhiệm của integrator

MITRE Hardware Design view phân loại các lỗi về boot/security flow, IP
integration và privilege/access control. View 1194 là bản đồ điều hướng;
mapping một vulnerability cần CWE cụ thể phù hợp. \[S11\]

Hồ sơ nhánh HS-09

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các lớp weakness phổ biến trong tích hợp SoC là gì?
  R1--R2       

  Câu hỏi      Access policy có được áp dụng cho tất cả master và tất cả
  R3--R4       đường đọc/ghi không?

  Câu hỏi      Policy có bị phá vỡ ở reset, lỗi giao thức, power
  R5--R6       transition hoặc cấu hình chưa hoàn tất không?

  Phương pháp  Access-control matrix; assertion-based verification;
               integration test theo trạng thái; information-flow
               tracking

  Chỉ số và    Policy coverage; counterexample; số tổ hợp master × vùng ×
  bằng chứng   trạng thái đã kiểm tra

  Đầu ra       Access-control matrix; integration assertions; test matrix
               theo trạng thái

  Khái niệm dễ Policy được đặc tả và policy được thực thi
  nhầm         

  Bẫy và giới  Chỉ kiểm tra CPU master; bỏ qua DMA và debug
  hạn          

  Liên kết     HS-05, HS-08, HS-10, HS-12

  Đầu mối      \[S11\] \[S03\]
  nguồn        
  -----------------------------------------------------------------------

HS-10 DFT, debug và lifecycle

**Phạm vi:** cơ chế test và debug cần thiết cho sản xuất và bảo trì, và
cách giới hạn chúng theo vòng đời.

HS-10.1 Hạ tầng test

-   Scan chain, scan compression

-   Boundary scan, JTAG

-   BIST cho memory và logic

HS-10.2 Debug

-   Debug interface và trace

-   Debug authentication, secure debug

-   Quyền của người bảo trì

HS-10.3 Lifecycle states

-   Manufacturing, provisioning, development, production

-   RMA và sửa chữa

-   Retirement và hủy

HS-10.4 Key và fuse theo lifecycle

-   Test key, field key

-   Fuse policy và irreversible transition

HS-10.5 Rò rỉ qua test/debug

-   Memory dump

-   Scan visibility của register chứa secret

-   Debug state retention sau khi chuyển trạng thái

HS-10.6 Đánh đổi testability--security

-   Test coverage khi khóa debug

-   Khả năng chẩn đoán sau khi đưa vào production

Hồ sơ nhánh HS-10

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các kỹ thuật secure scan và secure debug chính là gì?
  R1--R2       

  Câu hỏi      Có đường test/debug nào đọc được secret trong một trạng
  R3--R4       thái không được phép?

  Câu hỏi      RMA và sửa chữa có thể thực hiện mà giữ được chính sách
  R5--R6       key và ownership không?

  Phương pháp  Lifecycle state machine; formal property cho chuyển trạng
               thái; test theo từng state

  Chỉ số và    Số đường quan sát secret theo state; test coverage; kết
  bằng chứng   quả chuyển trạng thái âm

  Đầu ra       Lifecycle state machine; debug-permission table; DFT
               security checklist; state-transition tests

  Khái niệm dễ Khóa debug và xóa secret; lifecycle state và privilege
  nhầm         level

  Bẫy và giới  Bỏ qua trạng thái RMA; giả định fuse không thể bị tác động
  hạn          

  Liên kết     HS-05, HS-09, HS-11, HS-13

  Đầu mối      \[S03\] \[S11\]
  nguồn        
  -----------------------------------------------------------------------

HS-11 Supply chain, Trojan, counterfeit và IP protection

**Phạm vi:** tin cậy xuyên các bên tham gia từ thiết kế tới triển khai,
và bảo vệ IP thiết kế.

HS-11.1 Design provenance

-   Third-party IP

-   EDA/tool flow integrity

-   Build và tape-out integrity

HS-11.2 Hardware Trojan

-   Trigger: điều kiện kích hoạt hiếm

-   Payload: rò rỉ, sai chức năng, từ chối dịch vụ

-   Insertion stage: RTL, netlist, layout, fabrication

-   Detection: logic testing, side-channel fingerprint, formal,
    inspection

HS-11.3 Các bên trong chuỗi

-   Foundry, test house, packaging, provisioning

-   Phân bổ tin cậy cho từng bên

HS-11.4 Counterfeit

-   Recycled components

-   Remarked components

-   Unauthorized overproduction

HS-11.5 IP protection

-   Logic locking

-   Watermarking

-   Obfuscation và chống reverse engineering

-   Split manufacturing

HS-11.6 Traceability

-   Evidence chain xuyên vòng đời

-   Provenance record

Hồ sơ nhánh HS-11

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các giai đoạn và bên tham gia nào trong chuỗi cung ứng có
  R1--R2       thể đưa vào thay đổi trái phép?

  Câu hỏi      Điều kiện nào giúp phát hiện thay đổi độc hại khi không có
  R3--R4       golden chip đáng tin?

  Câu hỏi      Biện pháp bảo vệ IP chống được lớp đối thủ nào và đã được
  R5--R6       đánh giá bằng chứng nào?

  Phương pháp  Supply-chain mapping; detection benchmark; đánh giá logic
               locking dưới các mô hình tấn công đã công bố

  Chỉ số và    Detection rate và false positive trên benchmark; chi phí
  bằng chứng   overhead; mô hình đối thủ được kiểm tra

  Đầu ra       Supply-chain trust map; provenance record; detection
               benchmark

  Khái niệm dễ Trojan và bug; counterfeit và overproduction; logic
  nhầm         locking và obfuscation

  Bẫy và giới  Không mặc định logic locking, watermarking hay một
  hạn          detector cung cấp bảo đảm cho mọi mô hình đối thủ;
               benchmark Trojan có thể không đại diện Trojan thực

  Liên kết     HS-06, HS-12, HS-13, HS-14

  Đầu mối      \[S12\] \[S16\]
  nguồn        
  -----------------------------------------------------------------------

HS-12 Formal methods, security verification và CAD

**Phạm vi:** phát biểu và kiểm chứng thuộc tính bảo mật trên mô hình
thiết kế, và công cụ hỗ trợ.

HS-12.1 Đặc tả thuộc tính

-   Security property specification

-   Assertion-based verification

-   Phân loại: confidentiality, integrity, isolation, liveness của cơ
    chế bảo vệ

HS-12.2 Information flow

-   Information-flow tracking ở mức gate và RTL

-   Taint analysis

-   Noninterference

HS-12.3 Kỹ thuật chứng minh

-   Model checking

-   SMT-based reasoning

-   Theorem proving

HS-12.4 Hợp đồng và lập luận hợp thành

-   Hardware/software contract

-   Compositional reasoning

HS-12.5 Kiểm tra động

-   Security fuzzing cho phần cứng

-   Fault simulation

-   Coverage

HS-12.6 Tính nhất quán qua tầng

-   Equivalence giữa các phiên bản

-   Kiểm tra giả định sau synthesis

-   Verification cho masking ở mức netlist

Hồ sơ nhánh HS-12

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Những loại thuộc tính bảo mật nào có thể được kiểm chứng
  R1--R2       hình thức trên phần cứng?

  Câu hỏi      Thuộc tính cần bảo vệ đã được phát biểu chính xác và có
  R3--R4       tránh vacuous proof không?

  Câu hỏi      Proof bao phủ mô hình và assumption nào; hành vi vật lý
  R5--R6       nào nằm ngoài mô hình?

  Phương pháp  Property set; assumption register; formal tool; fuzzing;
               fault simulation

  Chỉ số và    Proof result; counterexample trace; property coverage;
  bằng chứng   vacuity check

  Đầu ra       Property set; assumption register; counterexample trace;
               proof/test coverage report

  Khái niệm dễ Functional equivalence và security equivalence; proof và
  nhầm         test

  Bẫy và giới  Formal proof có giá trị trong mô hình đã nêu; cần phép đo
  hạn          bổ sung nếu claim liên quan leakage vật lý

  Liên kết     HS-06, HS-07, HS-09, HS-10, HS-13

  Đầu mối      \[S11\] \[S02\]
  nguồn        
  -----------------------------------------------------------------------

HS-13 Physical Design và đánh đổi Security--PPA

**Phạm vi:** ảnh hưởng của hiện thực vật lý (floorplan tới signoff) tới
thuộc tính bảo mật, và chi phí của countermeasure ở mức vật lý.

HS-13.1 Placement

-   Khoảng cách giữa vùng xử lý dữ liệu nhạy cảm

-   Tách miền mask share

-   Floorplan và vị trí sensor

HS-13.2 Routing

-   Glitch propagation và coupling giữa share

-   Symmetry constraints cho logic cân bằng

-   Routing của tín hiệu nhạy cảm

HS-13.3 Clock và reset

-   Clock tree và độ nhạy với glitch

-   Reset tree

HS-13.4 Power

-   Power domain, DVFS, sleep/wakeup

-   Power delivery network, local switching, decoupling

-   Khả năng quan sát qua mạng nguồn

HS-13.5 Phân tích sau triển khai

-   Parasitic extraction

-   Gate-level simulation có timing

-   MCMM, IR/EM, thermal

HS-13.6 Overhead của countermeasure

-   Area, delay, energy, routing congestion, testability

HS-13.7 Tính nhất quán qua tầng

-   RTL → netlist → post-route → silicon

-   Leakage proxy và quan hệ với đo trên silicon

Hồ sơ nhánh HS-13

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Bước nào trong luồng physical design có thể ảnh hưởng tới
  R1--R2       leakage hoặc fault sensitivity?

  Câu hỏi      Placement/routing có thay đổi leakage hoặc fault
  R3--R4       sensitivity với RTL giữ nguyên không?

  Câu hỏi      Ràng buộc thiết kế nào cải thiện chỉ số bảo mật đã chọn
  R5--R6       với chi phí PPA chấp nhận được?

  Phương pháp  Nhiều implementation seed; post-layout simulation; leakage
               proxy; đối chiếu với đo vật lý khi có

  Chỉ số và    Area, WNS/TNS, power; leakage proxy; phân bố theo seed;
  bằng chứng   mức tương quan proxy--đo

  Đầu ra       Security-related implementation constraints; PPA--security
               comparison; phép thử sau triển khai

  Khái niệm dễ Timing closure và security closure; power estimate và
  nhầm         power trace

  Bẫy và giới  Timing closure và IR/EM signoff cung cấp bằng chứng kỹ
  hạn          thuật riêng; không thay thế security evaluation; proxy
               chưa xác nhận trên silicon

  Liên kết     HS-03, HS-06, HS-07, HS-12

  Đầu mối      \[S02\] \[S12\]
  nguồn        
  -----------------------------------------------------------------------

HS-14 PCB, packaging, chiplet và heterogeneous integration

**Phạm vi:** bảo mật ở mức board, package và khi nhiều die từ nhiều nhà
cung ứng được tích hợp.

HS-14.1 Board level

-   Trust boundary trên board

-   External memory, link, service interface

-   Test pad, connector, power/clock exposure

HS-14.2 Chiplet

-   Chiplet identity

-   Authenticated die-to-die link

-   Trust giữa các die

HS-14.3 Advanced packaging

-   Interposer, 2.5D/3D integration

-   Die-to-die communication

HS-14.4 Hiệu ứng vật lý ở package

-   Thermal/power coupling giữa die

-   Fault propagation

-   Package-level observation

HS-14.5 Chuỗi cung ứng nhiều bên

-   Multi-vendor supply chain

-   Package provenance

-   Secure provisioning qua nhiều die

HOST 2026 liệt kê advanced packaging, chiplet security, AI for hardware
security và security of AI chips trong nhóm chủ đề nghiên cứu. \[S12\]

Hồ sơ nhánh HS-14

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Bề mặt tấn công mới nào xuất hiện khi chuyển từ monolithic
  R1--R2       SoC sang chiplet?

  Câu hỏi      Những giả định nào của monolithic SoC không còn đúng khi
  R3--R4       die đến từ nhiều nhà cung ứng?

  Câu hỏi      Thông tin nhạy cảm hoặc trạng thái xác thực được bảo vệ
  R5--R6       thế nào khi đi qua package boundary?

  Phương pháp  Threat modeling die-to-die; protocol analysis; mô phỏng
               coupling

  Chỉ số và    Requirement coverage; overhead của
  bằng chứng   authentication/encryption trên link

  Đầu ra       Die-to-die threat model; authentication/isolation
               requirements; package evidence matrix

  Khái niệm dễ Package boundary và trust boundary
  nhầm         

  Bẫy và giới  Chuyển nguyên threat model SoC sang chiplet; thiếu dữ liệu
  hạn          đo cho package thực

  Liên kết     HS-02, HS-05, HS-07, HS-11

  Đầu mối      \[S12\]
  nguồn        
  -----------------------------------------------------------------------

HS-15 Hệ thống và lĩnh vực ứng dụng

**Phạm vi:** cách asset, đối thủ và chi phí chấp nhận được thay đổi theo
lĩnh vực triển khai.

HS-15.1 FPGA

-   Bitstream protection và configuration

-   Shared fabric trong môi trường đa người dùng

-   IP ownership

HS-15.2 IoT và edge

-   Thiết bị hạn chế tài nguyên

-   Onboarding, update

-   Tiếp cận vật lý dễ dàng

HS-15.3 Automotive, CPS, industrial

-   Authenticity và availability

-   Liên hệ với safety

HS-15.4 Medical và thiết bị bảo mật

-   Lifecycle dài

-   Update và dữ liệu nhạy cảm

HS-15.5 Cloud

-   Attestation, workload isolation

-   Confidential computing

HS-15.6 AI hardware

-   Accelerator

-   Bảo vệ model, key, dữ liệu

-   Isolation và workload-induced observation

HS-15.7 Thiết bị xác thực và lưu trữ

-   Smartcard, wallet

-   Storage, authentication device

Hồ sơ nhánh HS-15

  -----------------------------------------------------------------------
  **Mục**       **Nội dung**
  ------------- ---------------------------------------------------------
  Câu hỏi       Mỗi lĩnh vực ưu tiên asset và thuộc tính nào?
  R1--R2        

  Câu hỏi       Asset, đối thủ và chi phí chấp nhận được khác nhau như
  R3--R4        thế nào giữa các lĩnh vực?

  Câu hỏi       Một cơ chế ở block level giữ được thuộc tính nào khi tích
  R5--R6        hợp vào toàn hệ thống?

  Phương pháp   Domain profiling; deployment threat model; workload
                benchmark

  Chỉ số và     Phụ thuộc lĩnh vực; luôn kèm workload và điều kiện vận
  bằng chứng    hành

  Đầu ra        Domain profile; deployment threat model; workload
                benchmark; operational requirements

  Khái niệm dễ  HSM, TPM, secure element và TEE có chức năng, giao diện
  nhầm          và ranh giới tin cậy riêng

  Bẫy và giới   Suy rộng kết quả lĩnh vực này sang lĩnh vực khác mà không
  hạn           xét lại threat model

  Liên kết      Mọi nhánh

  Đầu mối nguồn \[S01\] \[S12\]
  -----------------------------------------------------------------------

HS-16 Tiêu chuẩn, evaluation và assurance

**Phạm vi:** cách chứng minh với bên thứ ba rằng thiết kế đáp ứng yêu
cầu, và phạm vi thực sự của chứng nhận.

HS-16.1 Cryptographic module validation

-   Phạm vi module (boundary)

-   Mức bảo mật định tính

HS-16.2 Yêu cầu theo nhóm

-   Physical security và non-invasive security

-   Key management

-   Self-test

-   Lifecycle assurance

HS-16.3 Đánh giá theo security target

-   Security target, protection profile

-   Evaluation evidence

HS-16.4 Kiểm thử theo mối đe dọa

-   Threat-specific test plan

-   Penetration testing

-   Vulnerability handling và disclosure

HS-16.5 Chứng cứ theo giai đoạn

-   Design, implementation, integration, operation

HS-16.6 Quản lý phiên bản

-   Version, configuration, errata

-   Trạng thái validation

FIPS 140-3 xác định các yêu cầu bảo mật cho cryptographic module, với
bốn mức bảo mật định tính. Phạm vi của một validation cần được đọc theo
module và cấu hình tương ứng. \[S13\]

Hồ sơ nhánh HS-16

  -----------------------------------------------------------------------
  **Mục**      **Nội dung**
  ------------ ----------------------------------------------------------
  Câu hỏi      Các khung chứng nhận chính khác nhau về đối tượng, phạm vi
  R1--R2       và bằng chứng yêu cầu như thế nào?

  Câu hỏi      Chứng nhận hoặc test report bao phủ đúng module, phiên bản
  R3--R4       và operating mode nào?

  Câu hỏi      Những giả định, countermeasure hoặc integration property
  R5--R6       nào vẫn cần kiểm tra riêng?

  Phương pháp  Requirement-to-evidence review; assurance case; gap
               analysis

  Chỉ số và    Requirement coverage; configuration; exclusions
  bằng chứng   

  Đầu ra       Requirement-to-evidence matrix; assurance case; evaluation
               scope; versioned security report

  Khái niệm dễ Compliance và security; validated module và validated
  nhầm         system

  Bẫy và giới  Compliance có phạm vi riêng; integration và operation vẫn
  hạn          cần evidence tương ứng

  Liên kết     HS-03, HS-04, HS-05, HS-07

  Đầu mối      \[S13\] \[S07\] \[S08\]
  nguồn        
  -----------------------------------------------------------------------

4 Các trục giúp khảo sát có hệ thống

Một chủ đề được nhận diện bằng nhiều trục. Chọn tổ hợp có ý nghĩa kỹ
thuật thay vì nhân tất cả các nhãn thành hàng nghìn câu hỏi trùng nhau.

4.1 Mười trục và giá trị

  ---------------------------------------------------------------------------
  **Mã**   **Trục**   **Các giá trị điển hình**
  -------- ---------- -------------------------------------------------------
  A01      Asset      key, data, firmware, identity, design IP, availability

  A02      Thuộc tính confidentiality, integrity, authenticity, isolation,
                      freshness, recovery

  A03      Đối thủ    remote, local, privileged, physical, insider, supply
                      chain

  A04      Tầng       specification, RTL, netlist, transistor, layout,
                      die/package, PCB, firmware, system

  A05      Vòng đời   design, fabrication, test, provisioning, deployment,
                      maintenance/RMA, retirement

  A06      Cơ chế     leakage, fault, misuse, tamper, Trojan, counterfeit,
                      shared-state interference

  A07      Biện pháp  prevention, detection, containment, recovery

  A08      Phương     proof, simulation, emulation, FPGA, silicon
           pháp       measurement, field evidence

  A09      Điều kiện  process, voltage, temperature, aging, tool version,
                      workload, implementation seed

  A10      Đầu ra     finding, taxonomy, benchmark, proof, dataset,
                      countermeasure, design guideline
  ---------------------------------------------------------------------------

4.2 Giá trị chi tiết theo cấp

A01 Asset

-   Bí mật: symmetric key, private key, seed, PUF response, credential

-   Mã: boot ROM code, firmware, bitstream, microcode

-   Cấu hình: fuse, lock bit, lifecycle state, policy

-   Dữ liệu: dữ liệu người dùng, dữ liệu mô hình AI, log

-   Danh tính: device identity, certificate

-   Design IP: netlist, layout, thuật toán độc quyền

-   Availability: dịch vụ, tuổi thọ thiết bị

A04 Tầng

-   Specification và kiến trúc

-   RTL

-   Gate-level netlist (pre-layout, post-layout)

-   Transistor và cell

-   Layout và parasitic

-   Die, package, chiplet

-   PCB và hệ thống vật lý

-   Firmware, OS, hypervisor

-   Hệ thống phân tán, cloud

A05 Vòng đời

-   Thiết kế: specification, RTL, verification, physical design

-   Chế tạo: foundry, mask

-   Test: wafer test, package test

-   Provisioning: nạp key, identity, cấu hình

-   Triển khai và vận hành

-   Bảo trì: update, RMA, sửa chữa

-   Kết thúc: retirement, zeroization, hủy

A08 Phương pháp

-   Phân tích: threat modeling, proof, mô hình toán

-   Mô phỏng: RTL, gate-level, transistor, fault simulation

-   Emulation và FPGA prototype

-   Đo trên silicon: power, EM, timing, fault injection

-   Bằng chứng thực địa: sự cố, advisory, field return

4.3 Quy tắc tổ hợp trục

-   **Bắt đầu từ asset và thuộc tính:** đây là cặp xác định "cái gì quan
    trọng".

-   **Cố định đối thủ trước khi chọn phương pháp:** phương pháp phải phù
    hợp năng lực đối thủ.

-   **Tầng và phương pháp phải tương thích:** claim ở tầng silicon cần
    bằng chứng ở tầng silicon hoặc giải thích chuyển giao.

-   **Điều kiện là trục bắt buộc ghi:** một kết quả không ghi điều kiện
    không so sánh được.

-   **Loại tổ hợp vô nghĩa:** ví dụ đối thủ remote với cơ chế invasive;
    ghi là Not applicable kèm lý do.

-   **Ưu tiên tổ hợp theo cặp:** khi số trục lớn, xét các cặp trục quan
    trọng (asset × đối thủ, tầng × phương pháp, cơ chế × biện pháp) thay
    vì tích Đề-các đầy đủ.

4.4 Mẫu dựng câu hỏi

Với \[asset\] trong \[target/layer/lifecycle\], đối thủ có
\[capability\] có thể phá \[property\] qua \[mechanism\] không;
\[control\] được đánh giá bằng \[method/metric\] trong \[conditions\]
như thế nào?

**Ví dụ từ bản gốc**

-   Confidentiality của AES key trong một block FPGA thay đổi thế nào
    giữa các placement seed dưới power-observation model đã xác định?

-   Quyền đọc vùng key có còn bị chặn cho DMA master trong mọi
    reset/lifecycle state đã liệt kê không?

-   Health test của entropy source phát hiện được những lớp suy giảm nào
    trong khoảng PVT của ứng dụng?

-   Chiplet chưa xác thực có thể truy cập resource nào trước khi link
    policy được thiết lập?

-   Một mitigation transient-execution giảm channel nào và có tác động
    performance ra sao với workload đã chọn?

**Ví dụ bổ sung theo nhánh**

-   HS-03: Lượng randomness tiêu thụ trên mỗi phép toán của các hiện
    thực ML-KEM có masking được báo cáo ra sao, và có so sánh được giữa
    các paper không?

-   HS-05: Bootloader có từ chối image có chữ ký hợp lệ nhưng version
    thấp hơn trong mọi đường update đã liệt kê không?

-   HS-07: Tỷ lệ escape của countermeasure redundancy thời gian thay đổi
    thế nào khi fault model chuyển từ single-bit sang multi-bit?

-   HS-10: Register chứa key có nằm trong scan chain ở trạng thái
    production không, và nếu có thì có bị xóa trước khi vào test mode
    không?

-   HS-12: Property noninterference đã chứng minh ở RTL có còn đúng trên
    netlist sau synthesis với các tối ưu mặc định không?

4.5 Coverage ledger

Mỗi tổ hợp có trạng thái Covered, Partial, Not searched, Evidence
missing hoặc Not applicable. Ghi lý do Not applicable. Coverage theo
trục giúp phát hiện khoảng trống; không tạo một tỷ lệ phần trăm bao phủ
nếu chưa có tập tham chiếu và mẫu số rõ ràng.

  -----------------------------------------------------------------------------
  **Tổ hợp (ví dụ)**   **Trạng      **Nguồn hoặc lý do**      **Bước tiếp
                       thái**                                 theo**
  -------------------- ------------ ------------------------- -----------------
  AES key × power      Partial      Hai paper có đánh giá sau Tìm forward
  observation ×                     triển khai; chưa có đo    snowball
  post-route netlist                silicon                   

  AES key × power      Not searched Chưa chạy query family    Thêm query vào
  observation ×                     tương ứng                 protocol
  silicon × nhiều seed                                        

  PUF response ×       Evidence     Đã tìm theo protocol,     Ghi gap card,
  modeling × aging     missing      chưa thấy dữ liệu aging   kiểm tra lại với
                                    cho cấu trúc này          query mở rộng

  Bitstream × remote × Not          Đối thủ remote không có   ---
  invasive             applicable   tiếp cận invasive         
  -----------------------------------------------------------------------------

5 Phân cấp hình thức research

5.1 Literature và knowledge research

  -------------------------------------------------------------------------------
  **Hình thức**  **Khi dùng**     **Đầu ra**   **Tiêu chí chất **Bẫy**
                                               lượng**         
  -------------- ---------------- ------------ --------------- ------------------
  Conceptual     Thuật ngữ đang   Định nghĩa,  Phân biệt rõ,   Định nghĩa mới
  research       bị dùng không    mô hình khái có ví dụ và     không dựa trên
                 thống nhất       niệm         phản ví dụ      nguồn

  Narrative      Cần diễn giải    Bài tổng     Công khai phạm  Thiên lệch chọn
  review         một dòng nghiên  quan         vi lựa chọn     nguồn
                 cứu                                           

  Scoping review Cần bản đồ phạm  Bản đồ,      Protocol và log Coi bản đồ là câu
                 vi và khoảng     evidence map đầy đủ          trả lời
                 trống                                         

  Systematic     Câu hỏi hẹp cần  Tổng hợp có  Protocol trước, Câu hỏi quá rộng
  review         trả lời          thể lặp lại  sàng lọc hai    
                                               vòng            

  SoK            Cần tổ chức lại  Taxonomy,    Giá trị bổ sung Chỉ là survey dài
                 tri thức         insight, hệ  ngoài tóm tắt   
                                  đánh giá     \[S02\]         

  Bibliometric   Cần xem quan hệ  Mạng trích   Nêu rõ cơ sở dữ Dùng citation
  analysis       công trình, tác  dẫn, cụm chủ liệu và giới    count thay chất
                 giả              đề           hạn             lượng kỹ thuật
  -------------------------------------------------------------------------------

PRISMA-ScR hỗ trợ cách báo cáo scoping review và việc đánh giá phạm vi
literature. Có thể vận dụng các nguyên tắc minh bạch về tìm kiếm và sàng
lọc cho Hardware Security; đó là điều chỉnh phương pháp, không phải một
chuẩn chứng nhận bảo mật phần cứng. \[S14\]

5.2 Analytical research

-   **Threat modeling và attack-tree analysis**

    -   Đầu ra: cây tấn công, bảng điều kiện tiên quyết

-   **Mô hình hóa**

    -   Complexity model, leakage model, fault model, adversary model

-   **Security proof dưới assumption đã chỉ định**

    -   Proof trong mô hình probing, mô hình hình thức của protocol

-   **Tính hợp thành**

    -   Thuộc tính của từng block có giữ khi ghép không

-   **Trade-off và giới hạn**

    -   Phân tích chi phí--lợi ích, giới hạn lý thuyết

-   **Counterexample hoặc impossibility**

    -   Chỉ ra một mô hình cụ thể không thể đạt thuộc tính

5.3 Empirical research

-   Simulation, emulation, FPGA và ASIC/silicon experiments

-   Trace capture, observation và statistical analysis

-   Controlled fault campaign và outcome classification

-   Cross-device, cross-session, cross-condition validation

-   Benchmark, dataset và reproduction study

-   Negative results khi thiết kế phép thử đủ thông tin

  -----------------------------------------------------------------------
  **Nền tảng**                 **Điểm mạnh**       **Giới hạn chuyển
                                                   giao**
  ---------------------------- ------------------- ----------------------
  RTL simulation               Nhanh, quan sát đầy Không có hiệu ứng vật
                               đủ                  lý

  Gate-level/post-layout       Có delay, glitch    Mô hình power là ước
  simulation                                       lượng

  FPGA                         Đo thật, chi phí    Cấu trúc khác ASIC
                               thấp                

  ASIC/silicon                 Đại diện sản phẩm   Chi phí cao, số mẫu ít

  Field evidence               Điều kiện thực tế   Khó kiểm soát biến
  -----------------------------------------------------------------------

5.4 Design research

-   Primitive, accelerator, protocol hoặc secure subsystem mới

-   Countermeasure, verification method hoặc CAD workflow

-   Hardware/software co-design

-   Tool hoặc measurement infrastructure

-   Evaluation suite và artifact

-   Security-aware physical implementation

5.5 Translational research

-   Design guideline và engineering checklist

-   Lộ trình tích hợp, provisioning và operation

-   Giáo trình, lab và skill assessment

-   Công cụ triage/evidence retrieval

-   Đánh giá nhu cầu kỹ thuật hoặc sản phẩm với người dùng thực tế

5.6 Kết hợp các hình thức

Một nghiên cứu có thể kết hợp nhiều hình thức. Các chuỗi điển hình:

-   Scoping review → tìm điều kiện đo còn thiếu → reproduction study
    kiểm tra một mitigation trên nhiều thiết bị.

-   Conceptual research → chuẩn hóa định nghĩa → SoK đề xuất hệ đánh
    giá.

-   Threat modeling → formal property → design research cho
    countermeasure → empirical validation.

-   Design research → translational research thành checklist và lab.

6 Quy trình deep research có truy vết bằng chứng

6.0 Tổng quan mười hai bước

  -------------------------------------------------------------------------------
  **Bước**   **Tên**           **Đầu vào** **Đầu ra**       **Cổng chất lượng**
  ---------- ----------------- ----------- ---------------- ---------------------
  P01        Định khung câu    Nhu cầu,    Question card    Câu hỏi có điều kiện
             hỏi               quyết định  (T01)            bác bỏ

  P02        Viết protocol     Question    Search protocol  Protocol có ngày và
                               card                         version

  P03        Tìm nhiều tuyến   Protocol    Search log       Mỗi query ghi nguyên
                                                            văn, ngày, bộ lọc

  P04        Deduplicate và    Kết quả tìm Corpus register, Mỗi loại trừ có lý do
             sàng lọc                      exclusion log    

  P05        Đọc nguồn gốc     Corpus      Paper cards      Ghi rõ đã đọc full
                                           (T03)            text hay chưa

  P06        Lập evidence      Paper cards Evidence matrix  Trường thiếu ghi
             matrix                                         Missing

  P07        Đối chiếu mâu     Evidence    Claim register   Mâu thuẫn được phân
             thuẫn             matrix      (T04)            loại

  P08        Đánh giá          Artifact    Reproduction     Phân biệt các bậc
             reproducibility               status           reproducibility

  P09        Thiết kế phép thử Claim chưa  Experiment       Tiêu chí hỗ trợ/bác
                               phân giải   manifest (T05)   bỏ đặt trước

  P10        Tổng hợp và xác   Mọi hồ sơ   Gap cards (T06)  Gap gắn với phạm vi
             định gap                                       tìm kiếm

  P11        Chốt research     Tổng hợp    Research memo    Có quyết định và next
             memo                          (T10)            check

  P12        Điều kiện dừng    Memo        Decision log     Lý do dừng được ghi
  -------------------------------------------------------------------------------

6.1 P01 Định khung câu hỏi

Ghi mục đích, quyết định cần hỗ trợ, target, asset, property, attacker
capability, thời gian literature và loại đầu ra. Dùng câu hỏi mà một kết
quả có thể bác bỏ.

-   **Kiểm tra câu hỏi:**

    -   Có nêu target và tầng không?

    -   Có nêu đối thủ và năng lực không?

    -   Có kết quả nào bác bỏ được câu hỏi không?

    -   Có giới hạn thời gian literature không?

-   **Ví dụ tốt:** Trong các hiện thực AES masked được đánh giá trên
    FPGA, các paper xử lý glitch và placement như thế nào, và bằng chứng
    được lấy trước hay sau triển khai?

-   **Ví dụ cần sửa:** "Side-channel trên AES hiện nay ra sao?" --- quá
    rộng, không có điều kiện bác bỏ.

6.2 P02 Viết protocol trước khi tìm rộng

Protocol gồm database/venue, query families, khoảng thời gian, ngôn ngữ,
inclusion/exclusion criteria, phương pháp deduplicate, extraction schema
và cách đánh giá bằng chứng.

Giữ protocol gốc; ghi ngày và lý do khi sửa. Điều này giúp phân biệt
thay đổi hợp lý với việc chọn tiêu chí sau khi đã thấy kết quả mong
muốn.

-   **Thành phần protocol:**

    -   Câu hỏi và phạm vi (copy từ question card)

    -   Nguồn tìm: database, venue, kho chuẩn, kho artifact

    -   Query families và từ đồng nghĩa

    -   Khoảng thời gian và ngôn ngữ

    -   Inclusion criteria (ví dụ: có threat model, có đánh giá thực
        nghiệm)

    -   Exclusion criteria (ví dụ: chỉ có abstract, khác target)

    -   Quy tắc deduplicate và chọn version

    -   Extraction schema (trường của evidence matrix)

    -   Evidence profile (Phần 8.3)

    -   Lịch sửa đổi protocol

6.3 P03 Tìm theo nhiều tuyến

-   **Tuyến chuẩn và đặc tả:** NIST, TCG, MITRE, tài liệu kiến trúc và
    tiêu chuẩn liên quan.

-   **Tuyến công trình gốc:** paper mô tả cơ chế, thực nghiệm, proof
    hoặc dataset.

-   **Tuyến survey/SoK:** dựng từ vựng và tìm paper mốc.

-   **Tuyến backward snowball:** đọc reference của paper phù hợp.

-   **Tuyến forward snowball:** tìm paper trích dẫn, phản biện, sửa hoặc
    mở rộng.

-   **Tuyến artifact:** repository, release, test vectors, datasets,
    errata và replication.

Query families cần có thuật ngữ đồng nghĩa, target và countermeasure. Ví
dụ:

> (\"hardware security\" OR \"secure hardware\") AND (\"physical
> design\" OR placement OR routing)
>
> (\"side-channel\" OR \"power leakage\") AND masking AND (FPGA OR ASIC)
>
> (\"fault injection\" OR \"fault attack\") AND (\"root of trust\" OR
> \"secure boot\")
>
> (\"secure scan\" OR \"scan-chain security\" OR \"debug
> authentication\")
>
> (chiplet OR \"die-to-die\" OR \"advanced packaging\") AND (security OR
> attestation)
>
> (\"hardware trojan\" OR \"malicious circuit\") AND (detection OR
> verification)
>
> (\"entropy source\" OR TRNG) AND (\"health test\" OR \"min-entropy\")
> AND (PVT OR temperature OR aging)
>
> (PUF) AND (\"modeling attack\" OR \"machine learning\") AND
> (reliability OR \"helper data\")
>
> (\"information flow\" OR noninterference) AND (RTL OR netlist) AND
> (verification OR proof)
>
> (\"transient execution\" OR \"speculative execution\") AND (mitigation
> OR defense) AND (overhead OR performance)

Điều chỉnh cú pháp theo database. Ghi nguyên văn query, ngày chạy và bộ
lọc; không suy ra một query bao phủ toàn lĩnh vực.

6.4 P04 Deduplicate và sàng lọc

-   Ghép DOI, title, author và version.

-   Phân biệt preprint, camera-ready, extended version và artifact.

-   Một công trình xuất hiện trên nhiều website vẫn là một nguồn bằng
    chứng.

-   Sàng lọc title/abstract rồi full text.

-   Ghi lý do loại: sai target, thiếu threat model, thiếu dữ liệu cần
    thiết, outside scope hoặc duplicate.

-   Ghi nguồn chưa truy cập full text và hạ phạm vi sử dụng của nguồn
    đó.

  ------------------------------------------------------------------------
  **Mã lý do **Ý nghĩa**
  loại**     
  ---------- -------------------------------------------------------------
  EX-TGT     Sai target hoặc tầng

  EX-TM      Thiếu threat model cần thiết cho câu hỏi

  EX-DATA    Thiếu dữ liệu cần thiết để trích xuất

  EX-SCOPE   Ngoài phạm vi thời gian, ngôn ngữ hoặc chủ đề

  EX-DUP     Trùng với công trình đã có (ghi ID bản giữ lại)

  EX-ACC     Không truy cập được full text (giữ ở trạng thái hạn chế,
             không loại hẳn nếu quan trọng)
  ------------------------------------------------------------------------

6.5 P05 Đọc nguồn gốc ở độ sâu phù hợp

Trích riêng:

-   Claim và novelty.

-   Threat model, assumption, exclusions.

-   Target, implementation và setup.

-   Baseline và fairness của so sánh.

-   Dataset, number of trials/devices, metric.

-   Method, result, uncertainty.

-   Artifact và khả năng tái tạo.

-   Limitations, errata và negative results.

Abstract có thể hỗ trợ việc tìm và phân loại nguồn; đánh giá phương pháp
cần nội dung phương pháp, bảng và artifact tương ứng.

  ------------------------------------------------------------------------
  **Độ sâu  **Phần cần đọc**                         **Dùng cho**
  đọc**                                              
  --------- ---------------------------------------- ---------------------
  Lướt      Title, abstract, figure chính            Sàng lọc vòng 1

  Có trọng  Introduction, threat model, kết quả      Phân loại và gắn nhãn
  tâm       chính, limitation                        

  Đầy đủ    Toàn bộ, gồm setup, bảng, phụ lục        Evidence matrix

  Kiểm      Đầy đủ + artifact + errata               Claim trọng tâm,
  chứng                                              reproduction
  ------------------------------------------------------------------------

6.6 P06 Lập evidence matrix

  -----------------------------------------------------------------------
  **Trường**         **Nội dung phải giữ**
  ------------------ ----------------------------------------------------
  Work ID            Một ID cho một công trình, kèm version

  Claim              Mệnh đề cụ thể

  Scope              Target, layer, lifecycle

  Adversary          Năng lực và giới hạn

  Method             Proof, simulation, measurement

  Conditions         PVT, setup, tool, workload

  Baseline           Phương án và điều kiện so sánh

  Metric             Định nghĩa, đơn vị, mẫu số

  Result             Giá trị hoặc kết luận được báo cáo

  Reproduction       Artifact, access và trạng thái kiểm tra

  Limit              Điều kiện không bao phủ

  Source locator     DOI/URL và section/page/figure
  -----------------------------------------------------------------------

Tạo cột Missing thay vì tự điền thông tin không được báo cáo.

6.7 P07 Đối chiếu và giải quyết mâu thuẫn

Trước khi nói hai kết quả mâu thuẫn, kiểm tra chúng có cùng target,
adversary, implementation, condition và metric hay không. Phân loại:

-   Mâu thuẫn thực sự trong phạm vi tương đương.

-   Khác điều kiện nên chưa so sánh trực tiếp.

-   Khác định nghĩa hoặc unit.

-   Một kết quả chỉ là estimate/proxy.

-   Chưa đủ thông tin để phân giải.

Ghi evidence thuận và nghịch cho từng claim, không lấy đa số paper làm
phép chứng minh.

-   **Quy trình xử lý một cặp kết quả trái chiều:**

    -   So khớp năm trường: target, adversary, implementation,
        condition, metric.

    -   Nếu khác ít nhất một trường → phân loại "khác điều kiện" hoặc
        "khác định nghĩa".

    -   Nếu khớp cả năm → mâu thuẫn thực sự; tìm errata, forward
        snowball, artifact.

    -   Nếu không đủ thông tin để so khớp → "chưa đủ thông tin"; ghi
        trường Missing.

    -   Cập nhật claim card và đề xuất phép kiểm tra phân giải.

6.8 P08 Đánh giá reproducibility

Kiểm tra code, data, dependency, target, bitstream/firmware, tool
version, setup, seeds và quyền dùng dataset. Phân biệt:

-   Artifact accessible.

-   Artifact executable.

-   Kết quả tái tạo được trong môi trường đã chạy.

-   Kết quả giữ được khi đổi điều kiện.

-   Replication độc lập.

Download thành công không đồng nghĩa với reproduction thành công.

6.9 P09 Thiết kế phép thử khi cần

Chọn baseline, biến độc lập, biến kiểm soát, metric, số lần lặp có lý
do, calibration và tiêu chí dừng. Xác định trước kết quả nào hỗ trợ, bác
bỏ hoặc chưa phân giải giả thuyết.

Với side-channel/ML, giữ tập đánh giá độc lập; tránh để trace cùng thiết
bị hoặc cùng session vô tình tạo shortcut cho mô hình khi claim hướng
tới generalization.

-   **Ba kết quả phải định nghĩa trước:**

    -   Hỗ trợ: kết quả nào, vượt ngưỡng nào, trong điều kiện nào.

    -   Bác bỏ: kết quả nào cho thấy giả thuyết sai.

    -   Inconclusive: khi nào dữ liệu không đủ phân biệt (ví dụ nhiễu đo
        lớn hơn hiệu ứng cần phát hiện).

6.10 P10 Tổng hợp và xác định gap

Một gap cần có phạm vi, corpus và bằng chứng về điều còn thiếu. Các
loại:

  --------------------------------------------------------------------------------
  **Loại gap**            **Mô tả**                  **Ví dụ dạng câu**
  ----------------------- -------------------------- -----------------------------
  Model gap               Mô hình không bao phủ hành Leakage model không xét
                          vi quan trọng              glitch sau routing

  Measurement gap         Thiếu phép đo ở điều kiện  Chưa có dữ liệu ở nhiệt độ
                          cần                        thấp

  Evaluation gap          Phương pháp đánh giá không Chỉ dùng leakage detection
                          phù hợp claim              cho claim về key recovery

  Reproducibility gap     Không có artifact hoặc     Kết quả quan trọng không có
                          không chạy được            code hoặc dữ liệu

  Integration gap         Đánh giá block nhưng không Countermeasure chưa xét DMA
                          đánh giá khi tích hợp      master

  Physical implementation Đánh giá trước triển khai, Proof ở RTL, chưa kiểm tra
  gap                     chưa sau                   netlist

  Lifecycle/operational   Thiếu xét giai đoạn vòng   Chưa xét RMA
  gap                     đời                        

  Data/benchmark gap      Thiếu dataset hoặc         Các paper dùng setup không so
                          benchmark so sánh được     sánh được
  --------------------------------------------------------------------------------

"Chưa thấy trong lần tìm kiếm này" là trạng thái retrieval, chưa phải
kết luận "chưa ai nghiên cứu".

6.11 P11 Chốt research memo

Memo kết thúc với câu trả lời, supporting evidence, conflicting
evidence, assumption, residual uncertainty, một quyết định và bước kiểm
tra có giá trị nhất. Nếu câu hỏi chưa phân giải, chốt Inconclusive cùng
nguyên nhân.

6.12 P12 Điều kiện dừng

Dừng khi câu hỏi đã được trả lời ở mức bằng chứng cần cho quyết định,
hoặc giới hạn ngân sách/thời gian đã tới và phần chưa rõ được ghi đầy
đủ. Search saturation chỉ có nghĩa trong corpus, query và phạm vi đã
định.

-   **Dấu hiệu có thể dừng:**

    -   Forward và backward snowball không đưa thêm công trình đạt
        inclusion criteria trong phạm vi.

    -   Claim trọng tâm đã có trạng thái với lý do.

    -   Quyết định cần hỗ trợ đã đưa ra được.

-   **Dấu hiệu chưa nên dừng:**

    -   Claim trọng tâm chỉ có evidence thuận.

    -   Có mâu thuẫn chưa phân loại.

    -   Nguồn then chốt chưa đọc full text.

7 Phương pháp đánh giá và chỉ số

7.1 Chọn phép kiểm tra theo claim

  ----------------------------------------------------------------------------------
  **Claim cần đánh giá** **Phương pháp phù hợp**       **Chỉ số hoặc bằng chứng**
  ---------------------- ----------------------------- -----------------------------
  Functional correctness Test vectors, simulation,     Mismatch, assertion result,
                         formal equivalence theo phạm  coverage
                         vi                            

  Access isolation       Information-flow reasoning,   Counterexample, policy
                         formal property, integration  coverage, assumption
                         test                          

  Side-channel leakage   Leakage detection và          Test statistic, SNR, success
                         attack-based evaluation       rate, key rank theo protocol

  Fault resistance       Campaign với fault model rõ   Detection, escape, false
                                                       alarm, silent corruption

  Entropy                Noise-source characterization Min-entropy estimate,
                         và entropy assessment         health-test behavior

  PUF behavior           Cross-device và               Reliability, uniqueness,
                         repeated-condition tests      bias, reconstruction failure

  Physical-design        So sánh implementation ở điều Area, timing, energy,
  overhead               kiện tương đương              congestion và security metric
                                                       riêng

  Boot/update/recovery   State và negative-path tests  Reject/accept behavior,
                                                       rollback handling, recovery
                                                       evidence

  Generalization của ML  Independent                   Performance theo nhóm,
                         device/session/condition      uncertainty và failure cases
                         evaluation                    

  Assurance scope        Requirement-to-evidence       Coverage, configuration,
                         review                        exclusions
  ----------------------------------------------------------------------------------

7.2 Từ điển chỉ số

  ---------------------------------------------------------------------------
  **Chỉ số**       **Định nghĩa ngắn**              **Lưu ý khi báo cáo**
  ---------------- -------------------------------- -------------------------
  SNR              Tỷ lệ phương sai của phần tín    Ghi điểm thời gian, biến
  (side-channel)   hiệu phụ thuộc dữ liệu trên      trung gian, cách ước
                   phương sai nhiễu                 lượng

  Test statistic   Thống kê kiểm định khác biệt     Ngưỡng là tiêu chí phát
  (ví dụ t-value)  giữa các nhóm trace              hiện, không phải mức an
                                                    toàn \[S10\]

  Success rate     Xác suất khôi phục đúng secret   Ghi số lần lặp thực
                   theo số trace                    nghiệm để ước lượng

  Guessing entropy Vị trí kỳ vọng hoặc thực tế của  Ghi cách ước lượng rank
  / key rank       key đúng trong danh sách ứng     cho key đầy đủ
                   viên                             

  Min-entropy      Entropy theo xác suất của kết    Gắn với mô hình nguồn và
                   quả có khả năng cao nhất         phương pháp ước lượng
                                                    \[S07\]

  Reliability      Mức ổn định của response trên    Ghi điều kiện PVT và thời
  (PUF)            cùng thiết bị qua lần đo, điều   gian
                   kiện                             

  Uniqueness (PUF) Mức khác biệt response giữa các  Ghi số thiết bị và cách
                   thiết bị                         ghép cặp

  Bias /           Tỷ lệ bit 0 và 1                 Đánh giá theo thiết bị và
  uniformity                                        toàn bộ

  Detection rate   Tỷ lệ lỗi được phát hiện trong   Ghi mẫu số: lỗi có tác
                   số lỗi có tác động               động hay mọi lần
                                                    injection

  Escape rate      Tỷ lệ lỗi có tác động không bị   Báo cáo cùng với silent
                   phát hiện                        corruption

  False alarm      Tỷ lệ cảnh báo khi không có lỗi  Quan trọng cho
                   có tác động                      availability

  Policy coverage  Tỷ lệ tổ hợp policy đã kiểm tra  Mẫu số là tập liệt kê,
                   trên tập đã liệt kê              ghi rõ

  Overhead PPA     Chênh lệch area, delay, power so Cùng tool, cùng thư viện,
                   với baseline tương đương         cùng ràng buộc
  ---------------------------------------------------------------------------

7.3 Thiết kế thực nghiệm

-   Ghi target, hardware revision và số thiết bị.

-   Giữ version của RTL, netlist, firmware, software và tool.

-   Ghi measurement setup, calibration, sensor placement và
    environmental conditions.

-   Giữ raw data và preprocessing recipe.

-   Chọn repetition và statistical procedure phù hợp câu hỏi.

-   Báo cáo unit, denominator, dispersion và confidence interval khi có
    ý nghĩa.

-   Giữ failed runs, null results và missing values.

-   So sánh mitigation với baseline tương đương; báo cả security và
    performance.

Không cộng các metric khác đơn vị thành một "security score" chung nếu
chưa định nghĩa mô hình, trọng số và cách kiểm chứng.

7.4 Giới hạn bằng chứng cần giữ

-   Không phát hiện trong test đã chạy chỉ hỗ trợ phạm vi test đó.

-   Leakage detected chưa tự động định lượng khả năng khôi phục key.

-   FPGA measurement không tự động đại diện ASIC implementation.

-   Switching activity hoặc power estimate không tự động đại diện power
    trace trên silicon.

-   Proof thuộc tính logic không tự động bao phủ leakage hoặc fault vật
    lý.

-   Randomness test không thay cho entropy-source assessment.

-   Kết quả trên một chip không tự động tổng quát qua process, device và
    aging.

-   Compliance có phạm vi riêng; integration và operation vẫn cần
    evidence tương ứng.

8 Nguồn nghiên cứu và cách đánh giá evidence

8.1 Phân nguồn theo công dụng

  ------------------------------------------------------------------------
  **Loại nguồn**      **Công dụng**                 **Điều cần đọc**
  ------------------- ----------------------------- ----------------------
  Chuẩn và đặc tả     Định nghĩa requirement,       Version, status,
  chính thức          protocol, interface           errata, scope

  Paper gốc có peer   Cơ chế, phương pháp, thực     Threat model, setup,
  review              nghiệm                        baseline, limitations

  Preprint của tác    Theo dõi kết quả trước hoặc   Version và trạng thái
  giả                 ngoài venue                   review

  Artifact của tác    Reproduction và inspection    Release, commit,
  giả                                               dependency, data

  Tài liệu            Hiểu thiết kế cụ thể          Hardware/firmware
  implementation                                    revision và cấu hình
  chính thức                                        

  Survey/SoK          Dựng landscape và tìm nguồn   Search scope và cách
                      gốc                           lựa chọn paper

  Security advisory   Lỗi đã công bố và biện pháp   Sản phẩm, version bị
  và errata của                                     ảnh hưởng, phạm vi fix
  vendor                                            

  Luận án             Chi tiết setup và kết quả âm  Version, trạng thái
                      thường không có trong paper   bảo vệ
  ------------------------------------------------------------------------

Ưu tiên nguồn gốc cho claim kỹ thuật. Tài liệu vendor là nguồn tốt về
chức năng được công bố, nhưng một claim hiệu quả cần được đánh giá theo
phép thử và điều kiện của nó.

8.2 Đầu mối theo nhánh

-   CHES/TCHES: cryptographic implementation, side-channel, fault,
    primitives, formal tools và SoK.

-   HOST: hardware-oriented security, architecture, supply chain, CAD,
    integration và ứng dụng.

-   NIST: cryptographic module, entropy, firmware resiliency và
    hardware-enabled security.

-   TCG: TPM, identity và trusted-computing specifications.

-   MITRE CWE Hardware Design view: vocabulary cho các lớp design
    weakness.

-   OpenTitan: thiết kế mở, security requirements, threat model và
    implementation context.

-   ChipWhisperer documentation: môi trường capture/analysis phục vụ các
    bài lab side-channel và fault trên target phù hợp. \[S15\]

-   NIST Hardware Security Program: các hướng nghiên cứu và measurement
    trong hardware security. \[S16\]

8.2.1 Venue bổ sung theo nhánh (đầu mối tìm kiếm)

  -----------------------------------------------------------------------
  **Nhánh**        **Venue và kênh nên đưa vào protocol**
  ---------------- ------------------------------------------------------
  HS-03, HS-06,    CHES/TCHES, COSADE, CARDIS, FDTC, Journal of
  HS-07            Cryptographic Engineering

  HS-08            IEEE S&P, USENIX Security, ACM CCS, NDSS, ISCA, MICRO

  HS-09, HS-10,    DAC, ICCAD, DATE, ITC, IEEE TCAD, IEEE TVLSI, ACM
  HS-12, HS-13     TODAES

  HS-11, HS-14     HOST, DAC, ICCAD, IEEE TIFS

  HS-04            CHES/TCHES, HOST, IEEE TIFS

  HS-05, HS-16     NIST, TCG, tài liệu kiến trúc chính thức; USENIX
                   Security, ACM CCS cho phần đánh giá
  -----------------------------------------------------------------------

Danh sách venue là đầu mối tìm kiếm, không phải đánh giá chất lượng của
từng paper.

8.3 Evidence profile

Đánh giá từng nguồn theo các chiều, không gán điểm chỉ vì venue:

1.  Claim rõ và đủ hẹp.

2.  Threat model đầy đủ.

3.  Method phù hợp với claim.

4.  Setup và baseline có thể kiểm tra.

5.  Data/proof/artifact truy cập được.

6.  Uncertainty và limitations được ghi.

7.  Independent validation hoặc reproduction.

8.  Phạm vi chuyển giao sang target đang quan tâm.

  ----------------------------------------------------------------------------
  **Chiều**        **Đạt**                    **Một phần**         **Thiếu**
  ---------------- -------------------------- -------------------- -----------
  Claim            Mệnh đề hẹp, có điều kiện  Rõ nhưng rộng        Mơ hồ

  Threat model     Nêu asset, năng lực, ngoài Nêu một phần         Không nêu
                   phạm vi                                         

  Method--claim    Phương pháp trực tiếp kiểm Kiểm tra qua proxy   Không phù
  fit              tra claim                                       hợp

  Setup/baseline   Đủ để người khác lặp lại   Thiếu chi tiết       Không có

  Artifact         Public, chạy được          Có nhưng thiếu phần  Không có

  Uncertainty      Có dispersion, limitation  Chỉ có limitation    Không có

  Validation độc   Có replication độc lập     Có replication của   Chưa có
  lập                                         cùng nhóm            

  Chuyển giao      Target tương đương         Khác một phần        Khác cơ bản
  ----------------------------------------------------------------------------

Ghi từng chiều riêng, không cộng thành điểm tổng. Một proof và một
silicon measurement cung cấp các loại evidence khác nhau. Phân loại theo
claim trước khi cân nhắc độ tin cậy.

9 Tổ chức tri thức và dùng AI trong nghiên cứu

9.1 Phân cấp biểu diễn tri thức

  -------------------------------------------------------------------------
  **Tầng**     **Nội dung**                            **Vai trò**
  ------------ --------------------------------------- --------------------
  Vocabulary   Thuật ngữ, acronym, synonym, định nghĩa Tránh nhầm từ và hỗ
                                                       trợ retrieval

  Taxonomy     Chủ đề, subtopic, lớp attack/control    Điều hướng
                                                       literature

  Ontology     Entity type và relation có nghĩa        Biểu diễn các câu
                                                       hỏi và chứng cứ

  Knowledge    Paper, claim, target, measurement,      Truy vấn nguồn và
  graph        countermeasure được liên kết            mâu thuẫn

  Evidence     Claim, status, phạm vi và locator       Kiểm soát kết luận
  register                                             

  Research     Task, corpus, extraction, experiment,   Vận hành vòng nghiên
  workflow     decision                                cứu
  -------------------------------------------------------------------------

9.2 Ontology tối thiểu

**Entity:** Asset, Property, ThreatModel, AdversaryCapability,
HardwareTarget, LifecycleState, AttackMechanism, Countermeasure,
Requirement, Experiment, Metric, Result, Claim, Paper, Artifact,
ResearchGap.

**Relation:**

-   Claim được hỗ trợ bởi Result.

-   Result sinh ra từ Experiment.

-   Experiment đánh giá HardwareTarget.

-   Experiment dùng ThreatModel và đo Metric.

-   AttackMechanism đe dọa Property của Asset.

-   Countermeasure giảm AttackMechanism dưới những Condition nhất định.

-   Paper mô tả Claim, Experiment hoặc Artifact.

-   ResearchGap là thiếu evidence của một câu hỏi có phạm vi.

Quan hệ "mitigates" phải có condition; một cạnh trống điều kiện dễ biến
biện pháp có giới hạn thành bảo đảm tuyệt đối.

9.2.1 Thuộc tính tối thiểu của entity

  ---------------------------------------------------------------------------
  **Entity**       **Thuộc tính bắt buộc**
  ---------------- ----------------------------------------------------------
  Paper            work_id, version, title, year, venue, doi_or_url,
                   full_text_read

  Claim            claim_id, proposition, scope, status, status_reason

  Experiment       target, method, conditions, n_devices, n_trials,
                   artifact_link

  Result           value, unit, denominator, uncertainty, source_locator

  Countermeasure   name, mechanism_addressed, layer, overhead_reported

  ThreatModel      assets, capabilities, out_of_scope

  ResearchGap      gap_type, scope, search_coverage, evidence
  ---------------------------------------------------------------------------

9.2.2 Ràng buộc quan hệ

-   Mọi cạnh Claim--Result phải có source_locator.

-   Mọi cạnh Countermeasure--AttackMechanism phải có Condition và
    Experiment.

-   ResearchGap phải liên kết tới ít nhất một search log entry.

-   Claim ở trạng thái Supported phải có ít nhất một Result trực tiếp;
    Rejected phải có Result trái chiều trong phạm vi tương đương.

9.3 Vai trò AI trong workflow

-   **Framer:** chuyển nhu cầu thành question và scope.

-   **Retriever:** tạo query families và tìm candidate sources.

-   **Extractor:** điền evidence matrix từ nội dung đã đọc.

-   **Critic:** tìm assumption, phản chứng và so sánh không công bằng.

-   **Experiment assistant:** soạn testbench, notebook hoặc analysis
    code.

-   **Synthesizer:** kết nối bằng chứng thành memo.

-   **Recorder:** giữ version, source locator, missing fields và status.

Đây là các vai trò chức năng; có thể thực hiện lần lượt trong một phiên.
Không cần triển khai nhiều agent để dùng workflow này.

  ------------------------------------------------------------------------
  **Vai trò**         **Bước quy    **Đầu ra cần người kiểm tra**
                      trình**       
  ------------------- ------------- --------------------------------------
  Framer              P01           Question card

  Retriever           P02--P03      Query families, candidate list

  Extractor           P05--P06      Evidence matrix (đối chiếu locator)

  Critic              P07           Danh sách mâu thuẫn và assumption

  Experiment          P09           Manifest, code chưa chạy được tách
  assistant                         riêng

  Synthesizer         P10--P11      Memo, gap cards

  Recorder            Mọi bước      Log, version, trạng thái
  ------------------------------------------------------------------------

9.4 Quy tắc kiểm soát AI

-   Mỗi factual claim cần nguồn hoặc dữ liệu tương ứng.

-   Không suy diễn rằng mô hình đã đọc full text khi chỉ có abstract.

-   Nhiều câu trả lời AI không tạo nhiều nguồn evidence độc lập.

-   Giữ file gốc và kết quả đã thực sự chạy; tách code sinh ra khỏi code
    đã kiểm tra.

-   Đưa phản chứng và failure case vào extraction, không chỉ kết quả
    thuận.

-   Không để suy luận AI tự biến hypothesis thành finding.

-   Người nghiên cứu kiểm tra claim trọng tâm, assumption và kết luận.

-   Kiểm tra ngẫu nhiên một phần evidence matrix do AI điền với nguồn
    gốc; ghi tỷ lệ sai lệch phát hiện được trong mẫu đã kiểm tra.

9.5 Các câu hỏi graph có ích

-   Countermeasure này được đánh giá với adversary capability nào?

-   Kết quả nào chỉ có simulation, kết quả nào có silicon measurement?

-   Paper nào đánh giá post-route leakage và lưu artifact?

-   Claim nào đang có evidence trái chiều?

-   Source nào cần cập nhật vì version, errata hoặc target thay đổi?

-   Gap nào đã có đủ evidence để thành đề tài khả thi?

Ví dụ truy vấn dạng giả mã:

> MATCH (c:Countermeasure)-\[m:MITIGATES\]-\>(a:AttackMechanism
> {name:\"power side-channel\"})
>
> WHERE m.layer = \"post-route\" AND m.experiment.method = \"silicon
> measurement\"
>
> RETURN c.name, m.condition, m.experiment.n_devices, m.source_locator

10 Bộ artifact và mẫu hồ sơ

10.1 Bộ đầu ra tối thiểu

1.  Research brief.

2.  Threat-model card.

3.  Search protocol và search log.

4.  Corpus register cùng exclusion log.

5.  Paper cards và evidence matrix.

6.  Claim register.

7.  Reproduction hoặc experiment package khi cần.

8.  Research memo và decision log.

10.2 Cấu trúc workspace đề xuất

> hardware-security-research/
>
> 00_brief/ research_brief, question_cards
>
> 01_threat_model/ threat_model_card, trust_boundary
>
> 02_search/ search_protocol (có version), search_log, coverage_ledger
>
> 03_corpus/ corpus_register, exclusion_log, fulltext/ (theo quyền truy
> cập)
>
> 04_extraction/ paper_cards/, evidence_matrix
>
> 05_claims/ claim_register, claim_cards/
>
> 06_experiments/ experiment_manifest, raw_data/, analysis/,
> reproduction_reports/
>
> 07_synthesis/ gap_cards/, research_memo, sok_outline
>
> 08_decisions/ decision_log

Đây là cấu trúc đề xuất cho một workspace nghiên cứu; tên file có thể
đổi theo nhu cầu.

10.3 Danh mục mẫu

  ------------------------------------------------------------------------
  **Mã**         **Mẫu**                                  **Bước dùng**
  -------------- ---------------------------------------- ----------------
  T01            Research question card                   P01

  T02            Threat-model card                        P01, L3

  T03            Paper card                               P05

  T04            Claim card                               P07

  T05            Experiment manifest                      P09

  T06            Research gap card                        P10

  T07            Search log entry                         P03

  T08            Exclusion log entry                      P04

  T09            Coverage ledger row                      P03, P10

  T10            Research memo                            P11

  T11            Decision log entry                       P12

  T12            Reproduction report                      P08

  T13            Research brief                           L0

  T14            Protocol amendment                       P02
  ------------------------------------------------------------------------

10.4 T01 Research question card

> Question:
>
> Decision supported:
>
> Target and layer:
>
> Asset and property:
>
> Adversary capability:
>
> Lifecycle and operating conditions:
>
> Included literature:
>
> Excluded scope:
>
> Evidence required:
>
> What result would reject the hypothesis:
>
> Output and stopping condition:

10.5 T02 Threat-model card

> Target and version:
>
> Assets (với thuộc tính cần bảo vệ):
>
> Trust anchors and TCB:
>
> Trusted parties / untrusted parties:
>
> Adversary profiles and capabilities:
>
> Attack surfaces (interfaces, test/debug, clock/power/reset):
>
> Lifecycle states in scope:
>
> Out of scope and why:
>
> Assumptions:
>
> Controls and the evidence expected for each:

10.6 T03 Paper card

> Work ID and version:
>
> Title and authors:
>
> Year and venue:
>
> DOI or canonical URL:
>
> Full text read:
>
> Research question:
>
> Claim and novelty:
>
> Threat model and assumptions:
>
> Target and implementation:
>
> Method and baseline:
>
> Data and metrics:
>
> Results:
>
> Artifact and reproduction status:
>
> Limitations and counterevidence:
>
> Relevant section/page/figure:
>
> Labels (HS-xx.y, axes):

10.7 T04 Claim card

> Claim ID:
>
> Exact proposition:
>
> Scope and assumptions:
>
> Supporting evidence:
>
> Conflicting evidence:
>
> Missing evidence:
>
> Status: Candidate / Testing / Supported / Rejected / Inconclusive
>
> Why this status:
>
> Next most informative check:

10.8 T05 Experiment manifest

> Question and hypothesis:
>
> Target and hardware revision:
>
> RTL/netlist/firmware/software versions:
>
> Threat model:
>
> Setup and calibration:
>
> Independent variables:
>
> Controlled variables:
>
> Baseline:
>
> Dataset and split policy:
>
> Metric definitions and units:
>
> Trials and repetition rationale:
>
> Analysis recipe:
>
> Acceptance/rejection criteria:
>
> Raw data and output locations:
>
> Observed result and limitations:

10.9 T06 Research gap card

> Gap:
>
> Gap type
> (model/measurement/evaluation/reproducibility/integration/physical/lifecycle/data):
>
> Scope:
>
> Search coverage:
>
> Evidence showing the gap:
>
> Closest existing work:
>
> Why the difference matters:
>
> Candidate method:
>
> Resources and constraints:
>
> Measurable outcome:
>
> What would make the gap disappear:

10.10 T07--T09 Mẫu log

> \[T07 Search log entry\]
>
> Date / database or venue / exact query / filters / hits / exported to
> / notes
>
> \[T08 Exclusion log entry\]
>
> Work ID / screening stage (title-abstract or full text) / reason code
> / note / reviewer
>
> \[T09 Coverage ledger row\]
>
> Axis combination / status / sources or reason / next step / last
> updated

10.11 T10 Research memo

> Question (copy từ T01):
>
> Short answer and scope:
>
> Supporting evidence (claim IDs, locators):
>
> Conflicting evidence:
>
> Assumptions:
>
> Residual uncertainty:
>
> Decision:
>
> Most informative next check:
>
> Status if unresolved: Inconclusive because \...

10.12 T11--T14

> \[T11 Decision log entry\]
>
> Date / decision / based on (memo, claim IDs) / alternatives considered
> / revisit condition
>
> \[T12 Reproduction report\]
>
> Original work and version / artifact source and commit / environment /
> steps run /
>
> reproducibility level reached / differences from original /
> explanation or unresolved
>
> \[T13 Research brief\]
>
> Purpose / decision to support / audience / scope / constraints (time,
> tools, data) /
>
> expected outputs / research level (R) and depth (D) / stopping
> condition
>
> \[T14 Protocol amendment\]
>
> Date / protocol version before-after / what changed / reason / was it
> decided before seeing results?

11 Prompt phục vụ từng bước

11.1 Prompt dựng scope (P01)

> Định khung nghiên cứu Hardware Security cho \[chủ đề\].
>
> Tạo question card gồm target, asset, property, adversary capability,
>
> layer, lifecycle, conditions, evidence required và stopping condition.
>
> Phân biệt phần đã biết, giả thuyết và thông tin còn thiếu.
>
> Thu hẹp thành tối đa ba câu hỏi có thể kiểm chứng.

11.2 Prompt làm landscape research (R2)

> Lập landscape cho \[câu hỏi\] trong \[phạm vi thời gian\].
>
> Tạo nhóm từ khóa, nguồn chính thức, venue và paper mốc cần tìm.
>
> Mỗi nguồn phải có URL/DOI thật và trạng thái đã đọc.
>
> Phân biệt taxonomy đề xuất của bạn với taxonomy từ nguồn.
>
> Kết quả gồm bản đồ nhánh, paper candidates và coverage ledger.

11.3 Prompt viết protocol (P02)

> Viết search protocol cho \[question card\].
>
> Gồm nguồn tìm, query families với từ đồng nghĩa, khoảng thời gian,
>
> inclusion/exclusion criteria có mã lý do, quy tắc deduplicate và chọn
> version,
>
> extraction schema theo evidence matrix và evidence profile.
>
> Đánh dấu version 1.0 và ngày; không chạy tìm kiếm trong bước này.

11.4 Prompt deep research (P03--P11)

> Thực hiện khảo cứu sâu cho \[research question\].
>
> Viết protocol và tiêu chí inclusion/exclusion trước khi tổng hợp.
>
> Tìm nguồn gốc theo chuẩn/đặc tả, paper, backward/forward snowball và
> artifact.
>
> Deduplicate các phiên bản của cùng công trình.
>
> Đọc threat model, method, baseline, result, artifact và limitations.
>
> Tạo evidence matrix; để Missing cho dữ kiện không có.
>
> So sánh chỉ các kết quả có điều kiện tương đương.
>
> Tìm evidence thuận và nghịch.
>
> Chốt câu trả lời có phạm vi, uncertainty, gap có căn cứ và next check.
>
> Không gọi việc tìm trên web là exhaustive nếu corpus và coverage chưa
> được chứng minh.

11.5 Prompt extraction (P05--P06)

> Từ full text của \[paper\] (đã cung cấp), điền paper card và một dòng
> evidence matrix.
>
> Mỗi trường kèm section/page/figure. Trường không được báo cáo ghi
> Missing.
>
> Tách claim của tác giả với nhận xét của bạn.
>
> Liệt kê limitation do tác giả nêu và limitation bạn nhận thấy riêng.

11.6 Prompt phản biện (P07)

> Phản biện claim \[claim\] dựa trên \[evidence matrix\].
>
> Kiểm tra assumption, scope mismatch, confounder, baseline fairness,
>
> data leakage, proxy metric và reproducibility.
>
> Nêu counterevidence thật; đánh dấu giả thuyết nếu chưa có nguồn.
>
> Đề xuất một phép kiểm tra có thể bác bỏ claim.

11.7 Prompt kiểm tra coverage (P10)

> Từ coverage ledger \[ledger\] và search log \[log\], liệt kê các tổ
> hợp trục
>
> ở trạng thái Not searched và Evidence missing.
>
> Với mỗi tổ hợp Evidence missing, kiểm tra query đã chạy có đủ từ đồng
> nghĩa không.
>
> Đề xuất query bổ sung; không kết luận gap trước khi chạy chúng.

11.8 Prompt thiết kế experiment (P09)

> Thiết kế experiment kiểm tra \[hypothesis\] trên \[target\].
>
> Nêu baseline, biến độc lập, biến kiểm soát, calibration,
>
> metrics/units, repetition rationale, data-split policy,
>
> tiêu chí hỗ trợ/bác bỏ và outcome inconclusive.
>
> Giữ rõ giới hạn của simulation, FPGA hoặc silicon.
>
> Xuất experiment manifest; không tuyên bố đã chạy phép thử.

11.9 Prompt kế hoạch reproduction (P08)

> Lập kế hoạch reproduction cho \[paper và artifact\].
>
> Liệt kê dependency, tool version, target, dữ liệu, quyền sử dụng.
>
> Xác định bậc reproducibility mục tiêu và tiêu chí đạt từng bậc.
>
> Đề xuất một biến thể điều kiện có ý nghĩa để kiểm tra độ bền kết quả.

11.10 Prompt viết SoK (L7)

> Từ corpus \[corpus\] và evidence matrix \[matrix\], xây đề cương SoK.
>
> Chỉ ra taxonomy, assumption, inconsistency và comparability problems.
>
> Nêu giá trị bổ sung ngoài việc tóm tắt các paper.
>
> Mỗi gap phải có phạm vi và evidence tương ứng.
>
> Tách findings, interpretation và hypotheses.

12 Các hướng khởi đầu phù hợp với nền Physical Design

Đây là các lựa chọn đề xuất dựa trên kinh nghiệm Physical Design của Sĩ.
Mức khả thi thực tế phụ thuộc vào quyền sử dụng tool, dữ liệu, thời gian
và cộng tác viên.

12.1 Bốn hướng

  ------------------------------------------------------------------------------
  **Hướng**        **Câu hỏi đầu tiên**       **Artifact đầu   **Giới hạn cần
                                              tiên**           giữ**
  ---------------- -------------------------- ---------------- -----------------
  Security-aware   Leakage proxy thay đổi ra  Reproduction     Proxy chưa xác
  Physical Design  sao giữa implementation    notebook và bảng nhận chống tấn
                   seeds của một block giữ    PPA/proxy        công trên silicon
                   nguyên RTL?                                 

  DFT và lifecycle Secret có còn đi tới       Threat model,    Cần mô hình
  security         scan/debug output trong    policy matrix và debug/lifecycle
                   các state không được phép? assertions       đầy đủ

  Post-route       Có property hoặc leakage   RTL-to-netlist   Equivalence chức
  security         assumption nào mất hiệu    comparison và    năng không đủ cho
  verification     lực sau synthesis/PnR?     assumption       mọi security
                                              register         claim

  Hardware         Có thể truy vết claim về   Corpus nhỏ đã    Chất lượng
  Security         countermeasure tới method, đọc và           retrieval không
  evidence         target và result không?    claim-evidence   thay cho security
  retrieval                                   graph            evaluation
  ------------------------------------------------------------------------------

12.2 Kỹ năng sẵn có và kỹ năng cần bổ sung

  ------------------------------------------------------------------------
  **Kỹ năng Physical    **Dùng vào đâu**        **Cần bổ sung**
  Design sẵn có**                               
  --------------------- ----------------------- --------------------------
  Floorplan, placement, HS-13.1, HS-13.2        Leakage model, masking và
  routing                                       yêu cầu tách share

  CTS, power planning,  HS-13.3, HS-13.4, HS-07 Fault model liên quan
  IR/EM                                         clock/power

  STA, MCMM, signoff    HS-13.5                 Phân biệt timing closure
                                                và security closure

  Parasitic extraction, HS-13.5, HS-06          Ước lượng power theo chu
  gate-level sim                                kỳ, leakage proxy

  Scan insertion, DFT   HS-10                   Secure scan, lifecycle
  flow                                          state machine

  Scripting flow (Tcl,  Tự động hóa nhiều seed, Thống kê và experimental
  Python)               thu thập dữ liệu        design
  ------------------------------------------------------------------------

12.3 Lộ trình theo giai đoạn cho hướng Security-aware Physical Design

  ----------------------------------------------------------------------------------
  **Giai đoạn**  **Mục tiêu** **Hoạt động**       **Đầu ra**     **Điều kiện chuyển
                                                                 giai đoạn**
  -------------- ------------ ------------------- -------------- -------------------
  G0 Orientation Nắm HS-06,   R1 cho              Glossary, danh Giải thích được vì
                 HS-13        side-channel,       sách giả định  sao glitch ảnh
                              masking, glitch     theo tầng      hưởng masking

  G1 Scoping     Biết phần đã R4 thu hẹp:         Evidence       Có ít nhất một gap
                 làm          placement/routing   matrix,        card đã xác minh
                              và leakage          coverage       
                                                  ledger         

  G2             Kiểm tra     R5 với artifact có  Reproduction   Đạt bậc Executable
  Reproduction   công trình   sẵn                 report         trở lên hoặc ghi lý
                 gần nhất                                        do

  G3 Thử nghiệm  Kiểm tra giả Nhiều seed, đo PPA  Experiment     Kết quả Supported,
  nhỏ            thuyết trên  và leakage proxy    manifest, dữ   Rejected hoặc
                 block mở                         liệu, notebook Inconclusive có lý
                                                                 do

  G4 Chuyển giao Xác nhận     Cộng tác đo vật lý  Bài viết,      Claim khớp với tầng
                 proxy hoặc   hoặc giới hạn claim guideline có   của bằng chứng
                 thu hẹp      ở proxy             phạm vi        
                 claim                                           
  ----------------------------------------------------------------------------------

12.4 Lộ trình rút gọn cho ba hướng còn lại

-   **DFT và lifecycle security**

    -   G0: đọc HS-10, threat model của một thiết kế mở có lifecycle
        \[S03\].

    -   G1: liệt kê register chứa secret và đường scan/debug; dựng
        lifecycle state machine.

    -   G2: viết assertion cho quan hệ state → quyền quan sát.

    -   G3: chạy formal hoặc simulation theo từng state; ghi
        counterexample.

-   **Post-route security verification**

    -   G0: đọc HS-12; chọn một property đã chứng minh ở RTL.

    -   G1: liệt kê bước synthesis/PnR có thể thay đổi cấu trúc liên
        quan.

    -   G2: so sánh RTL và netlist theo property và assumption register.

    -   G3: báo cáo property nào còn giữ, property nào cần kiểm chứng
        lại.

-   **Hardware Security evidence retrieval**

    -   G0: chọn một nhánh hẹp (ví dụ HS-06.4 masking).

    -   G1: dựng corpus nhỏ đã đọc full text, điền evidence matrix.

    -   G2: dựng claim-evidence graph theo ontology Phần 9.

    -   G3: kiểm tra với người nghiên cứu hoặc kỹ sư mục tiêu xem graph
        trả lời được câu hỏi nào.

12.5 Đề tài mẫu

"Đánh giá ảnh hưởng của placement và routing tới leakage proxy của một
block mật mã, kèm chi phí PPA và kiểm tra khả năng chuyển giao sang phép
đo vật lý."

Bắt đầu bằng một block mở có baseline rõ, một countermeasure, một
property, một threat model và một cách đánh giá. Khảo cứu tài liệu trước
để xác định phần nào đã được làm và phần nào còn thiếu evidence.

-   **Biến độc lập gợi ý:** implementation seed; ràng buộc placement
    (có/không tách vùng share); utilization.

-   **Biến kiểm soát:** RTL, thư viện cell, tool version, ràng buộc
    timing, corner.

-   **Chỉ số:** PPA (area, WNS, power) và một leakage proxy được định
    nghĩa trước.

-   **Tiêu chí bác bỏ đặt trước:** biến thiên proxy giữa seed không vượt
    biến thiên do nhiễu ước lượng.

-   **Giới hạn cần ghi:** proxy chưa phải phép đo silicon; kết quả gắn
    với một block, một thư viện.

12.6 Một vòng kiểm chứng đầu tiên

-   Chọn một câu hỏi trong bảng 12.1.

-   Đọc kỹ một công trình gốc có artifact, một công trình phản biện hoặc
    mở rộng và một nguồn requirement/threat model.

-   Điền evidence matrix và một claim card.

-   Chạy một reproduction nhỏ nếu có môi trường phù hợp.

-   Ghi kết quả Supported, Rejected hoặc Inconclusive trong đúng phạm
    vi; chọn bước tiếp theo từ kết quả đó.

Nếu dùng hướng này cho we-meta.ai, artifact hữu ích ban đầu là một bộ
research cards có nguồn và điều kiện rõ. Nhu cầu sử dụng bộ đó cần được
kiểm tra với người nghiên cứu hoặc kỹ sư mục tiêu.

13 Nguồn tham chiếu gốc

-   \[S01\] NIST IR 8320 Hardware-Enabled Security ---
    https://csrc.nist.gov/pubs/ir/8320/final --- hardware-enabled
    platform security cho cloud và edge.

-   \[S02\] CHES 2026 Call for Papers ---
    https://ches.iacr.org/2026/cfp_ches2026.pdf --- phạm vi
    cryptographic hardware/embedded security và yêu cầu SoK.

-   \[S03\] OpenTitan Lightweight Threat Model ---
    https://opentitan.org/book/doc/security/threat_model/ --- asset,
    attacker profile, attack surface và attack methods của một thiết kế
    cụ thể.

-   \[S04\] NIST FIPS 203 --- https://csrc.nist.gov/pubs/fips/203/final
    --- ML-KEM.

-   \[S05\] NIST FIPS 204 --- https://csrc.nist.gov/pubs/fips/204/final
    --- ML-DSA.

-   \[S06\] NIST FIPS 205 --- https://csrc.nist.gov/pubs/fips/205/final
    --- SLH-DSA.

-   \[S07\] NIST SP 800-90B ---
    https://csrc.nist.gov/pubs/sp/800/90/b/final --- entropy-source
    requirements và assessment.

-   \[S08\] NIST SP 800-193 ---
    https://csrc.nist.gov/pubs/sp/800/193/final --- platform firmware
    resiliency.

-   \[S09\] TCG TPM 2.0 Library ---
    https://trustedcomputinggroup.org/resource/tpm-library-specification/
    --- đặc tả TPM; giữ version của tài liệu cụ thể khi triển khai.

-   \[S10\] François-Xavier Standaert, How (not) to Use Welch's T-test
    in Side-Channel Security Evaluations ---
    https://eprint.iacr.org/2017/138 --- giới hạn diễn giải TVLA khi
    dùng độc lập.

-   \[S11\] MITRE CWE Hardware Design View 1194 ---
    https://cwe.mitre.org/data/definitions/1194.html --- taxonomy điều
    hướng các lớp hardware weakness.

-   \[S12\] IEEE HOST 2026 Call for Papers ---
    https://www.ieee-security.org/Calendar/cfps/cfp-HOST2026.html ---
    phạm vi hardware-oriented security, gồm chiplet, packaging và AI
    hardware.

-   \[S13\] NIST FIPS 140-3 ---
    https://csrc.nist.gov/pubs/fips/140-3/final --- yêu cầu
    cryptographic module và mức bảo mật.

-   \[S14\] PRISMA Scoping Reviews ---
    https://www.prisma-statement.org/scoping --- hướng dẫn báo cáo
    scoping review.

-   \[S15\] ChipWhisperer Documentation ---
    https://chipwhisperer.readthedocs.io/en/latest/ --- documentation
    của môi trường lab capture/analysis.

-   \[S16\] NIST Hardware Security Program ---
    https://csrc.nist.gov/Projects/hardware-security --- các hướng
    nghiên cứu và measurement trong hardware security.

Khi thực hiện một nghiên cứu cụ thể, kiểm tra version, trạng thái và
errata trực tiếp trên nguồn. Danh sách này là đầu mối nghiên cứu; không
phải một systematic corpus đã sàng lọc cho mọi nhánh.

Phụ lục A Glossary song ngữ

  --------------------------------------------------------------------------------
  **Thuật ngữ**     **Tiếng Việt**   **Định nghĩa ngắn**               **Nhánh**
  ----------------- ---------------- --------------------------------- -----------
  Asset             Tài sản cần bảo  Thứ có giá trị mà thuộc tính bảo  HS-02
                    vệ               mật hướng tới                     

  Threat model      Mô hình mối đe   Mô tả asset, đối thủ, năng lực,   HS-02
                    dọa              ranh giới và ngoài phạm vi        

  Trusted Computing Nền tính toán    Tập thành phần mà bảo mật của hệ  HS-02,
  Base (TCB)        tin cậy          thống phụ thuộc vào               HS-08

  Root of Trust     Gốc tin cậy      Thành phần được tin cậy mặc định, HS-05
                                     làm điểm khởi đầu cho chuỗi tin   
                                     cậy                               

  Secure boot       Khởi động an     Chỉ chạy mã đã được xác minh      HS-05
                    toàn                                               

  Measured boot     Khởi động có đo  Đo và ghi lại trạng thái các      HS-05
                                     thành phần được nạp               

  Attestation       Chứng thực       Cung cấp bằng chứng về trạng thái HS-05
                                     cho bên kiểm tra                  

  Anti-rollback     Chống hạ phiên   Ngăn chạy phiên bản cũ có lỗ hổng HS-05
                    bản                                                

  Entropy source    Nguồn entropy    Thành phần vật lý tạo ra tính     HS-04
                                     không đoán trước                  

  Min-entropy       Entropy tối      Thước đo dựa trên xác suất kết    HS-04
                    thiểu            quả có khả năng nhất              

  TRNG / DRBG       Bộ sinh số ngẫu  Nguồn vật lý / thuật toán sinh    HS-04
                    nhiên thực / xác bit từ seed                       
                    định                                               

  PUF               Hàm không thể    Ánh xạ challenge--response dựa    HS-04
                    sao chép vật lý  trên biến thiên chế tạo           

  Helper data       Dữ liệu hỗ trợ   Dữ liệu công khai giúp tái tạo    HS-04
                                     key từ response nhiễu             

  Side-channel      Kênh phụ         Thông tin rò rỉ qua đặc tính vật  HS-06
                                     lý của hiện thực                  

  Leakage model     Mô hình rò rỉ    Hàm liên hệ dữ liệu trung gian và HS-06
                                     tín hiệu quan sát                 

  Masking           Che giấu bằng    Chia biến nhạy cảm thành nhiều    HS-06
                    chia sẻ          share ngẫu nhiên                  

  Hiding            Ẩn tín hiệu      Giảm tương quan giữa dữ liệu và   HS-06
                                     tín hiệu (cân bằng, nhiễu, xáo    
                                     trộn)                             

  Profiling attack  Tấn công có lập  Dựng mô hình trên thiết bị tương  HS-06
                    hồ sơ            tự trước khi phân tích            

  TVLA              Đánh giá rò rỉ   Phát hiện rò rỉ bằng kiểm định    HS-06
                    theo kiểm định   thống kê giữa các nhóm trace      

  Fault injection   Tiêm lỗi         Cố ý gây sai lệch hoạt động phần  HS-07
                                     cứng                              

  Fault model       Mô hình lỗi      Mô tả loại, vị trí, thời điểm của HS-07
                                     lỗi                               

  Escape            Lỗi lọt          Lỗi có tác động nhưng không bị    HS-07
                                     phát hiện                         

  Tamper evidence / Dấu hiệu can     Để lại dấu vết / hành động khi    HS-07
  response          thiệp / phản ứng phát hiện can thiệp               
                    can thiệp                                          

  Transient         Thực thi tạm     Lệnh thực thi rồi bị hủy nhưng để HS-08
  execution         thời             lại dấu vết vi kiến trúc          

  Covert channel    Kênh bí mật      Kênh truyền tin chủ đích qua cơ   HS-08
                                     chế không thiết kế để truyền tin  

  TEE / enclave     Môi trường thực  Miền cách ly bảo vệ mã và dữ liệu HS-08
                    thi tin cậy      khỏi phần mềm khác                

  IOMMU             Đơn vị quản lý   Dịch và kiểm soát truy cập bộ nhớ HS-08,
                    bộ nhớ cho I/O   của thiết bị ngoại vi             HS-09

  Access control    Ma trận kiểm     Bảng quyền của từng master với    HS-09
  matrix            soát truy cập    từng vùng                         

  Lifecycle state   Trạng thái vòng  Giai đoạn của thiết bị quyết định HS-10
                    đời              quyền test/debug và key           

  Secure scan       Scan an toàn     Cơ chế giới hạn quan sát qua scan HS-10
                                     chain                             

  RMA               Trả hàng để sửa  Quy trình đưa thiết bị về phân    HS-10
                                     tích lỗi                          

  Hardware Trojan   Trojan phần cứng Sửa đổi độc hại trong thiết kế    HS-11
                                     hoặc chế tạo                      

  Logic locking     Khóa logic       Thêm key vào mạch để chức năng    HS-11
                                     đúng chỉ khi có key               

  Counterfeit       Linh kiện giả    Linh kiện tái chế, đánh dấu lại   HS-11
                                     hoặc sản xuất trái phép           

  Noninterference   Không can thiệp  Đầu vào bí mật không ảnh hưởng    HS-12
                                     tới đầu ra quan sát được          

  Vacuous proof     Chứng minh rỗng  Property đúng vì điều kiện không  HS-12
                                     bao giờ xảy ra                    

  Leakage proxy     Đại lượng thay   Ước lượng rò rỉ từ mô phỏng thay  HS-13
                    thế rò rỉ        cho đo thực                       

  PPA               Công suất, hiệu  Ba chỉ số chi phí chính của thiết HS-13
                    năng, diện tích  kế                                

  Chiplet           Die chức năng    Die nhỏ ghép trong cùng package   HS-14

  Cryptographic     Module mật mã    Tập phần cứng/firmware/phần mềm   HS-16
  module                             thực hiện chức năng mật mã trong  
                                     một ranh giới                     

  Assurance case    Lập luận bảo đảm Lập luận có cấu trúc nối yêu cầu  HS-16
                                     với bằng chứng                    

  SoK               Hệ thống hóa tri Bài tổ chức lại tri thức của một  Phần 5
                    thức             lĩnh vực với giá trị bổ sung      
  --------------------------------------------------------------------------------

Phụ lục B Ma trận nhánh × phương pháp

Ký hiệu: ● phương pháp chính; ○ dùng bổ trợ; để trống khi ít dùng.

  -----------------------------------------------------------------------------------------------
  **Nhánh**             **Proof/formal**   **Simulation**   **FPGA**   **Silicon**   **Review
                                                                                     chuẩn**
  --------------------- ------------------ ---------------- ---------- ------------- ------------
  HS-02 Threat model    ○                                                            ●

  HS-03 Crypto HW       ○                  ●                ●          ○             ●

  HS-04 TRNG/PUF        ○                  ○                ●          ●             ●

  HS-05 RoT/boot        ●                  ●                ○          ○             ●

  HS-06 Side-channel    ○                  ●                ●          ●             ○

  HS-07 Fault           ○                  ●                ●          ●             ○

  HS-08 Microarch       ●                  ●                ○          ●             

  HS-09 SoC isolation   ●                  ●                ○                        ○

  HS-10 DFT/lifecycle   ●                  ●                ○          ○             ○

  HS-11 Supply chain    ○                  ●                ○          ●             ○

  HS-12 Formal/CAD      ●                  ●                                         

  HS-13 Physical Design ○                  ●                ○          ●             

  HS-14 Chiplet/package ○                  ●                           ○             ○

  HS-15 Ứng dụng        ○                  ○                ○          ○             ●

  HS-16 Assurance                                                      ○             ●
  -----------------------------------------------------------------------------------------------

Ma trận là gợi ý định hướng, không phải thống kê từ corpus.

Phụ lục C Ma trận nhánh × vòng đời

  -----------------------------------------------------------------------------------
  **Nhánh**   **Thiết   **Chế        **Provisioning**   **Vận    **Bảo       **Kết
              kế**      tạo/test**                      hành**   trì/RMA**   thúc**
  ----------- --------- ------------ ------------------ -------- ----------- --------
  HS-03       ●                                         ●                    ○

  HS-04       ●         ○            ●                  ●                    

  HS-05       ●                      ●                  ●        ●           ○

  HS-06       ●                                         ●                    

  HS-07       ●                                         ●        ○           

  HS-08       ●                                         ●                    

  HS-09       ●                                         ●                    

  HS-10       ●         ●            ●                  ○        ●           ●

  HS-11       ●         ●            ●                  ○        ○           ○

  HS-13       ●         ○                                                    

  HS-14       ●         ●            ●                  ●                    

  HS-16       ●         ○            ○                  ●        ○           ○
  -----------------------------------------------------------------------------------

Phụ lục D Lộ trình đọc theo bậc

  ------------------------------------------------------------------------
  **Bậc**   **Mục tiêu**         **Nhánh trọng   **Sản phẩm kiểm tra**
                                 tâm**           
  --------- -------------------- --------------- -------------------------
  Bậc 1 Nền Từ vựng, threat      HS-01, HS-02    Glossary; threat-model
            model                                card cho một thiết kế mở

  Bậc 2 Cơ  Hiểu các họ tấn công HS-03, HS-04,   Một trang tóm tắt mỗi
  chế       và bảo vệ            HS-05, HS-06,   nhánh với nguồn gốc
                                 HS-07           

  Bậc 3     Hiểu thuộc tính khi  HS-08, HS-09,   Access-control matrix và
  Tích hợp  ghép hệ thống        HS-10           lifecycle state machine
                                                 mẫu

  Bậc 4     Kiểm chứng và hiện   HS-12, HS-13    Property set; bảng giả
  Phương    thực                                 định theo tầng
  pháp                                           

  Bậc 5 Hệ  Chuỗi cung ứng,      HS-11, HS-14,   Supply-chain trust map;
  sinh thái package, ứng dụng,   HS-15, HS-16    requirement-to-evidence
            assurance                            matrix

  Bậc 6     Một nhánh hẹp        Theo đề tài     Evidence matrix và gap
  Chuyên                                         card đã xác minh
  sâu                                            
  ------------------------------------------------------------------------

Phụ lục E Đầu mối bổ sung cần đối chiếu

Các tên dưới đây là đầu mối tìm kiếm thường gặp trong lĩnh vực. Bản này
chưa đối chiếu version, trạng thái hay URL của chúng; cần kiểm tra trực
tiếp trước khi dùng làm nguồn.

  ---------------------------------------------------------------------------
  **Nhánh**   **Đầu mối**
  ----------- ---------------------------------------------------------------
  HS-04       NIST SP 800-90A (DRBG), NIST SP 800-90C (RBG constructions)

  HS-05       TCG DICE; DMTF SPDM; dự án Root of Trust mở (ví dụ Caliptra của
              CHIPS Alliance)

  HS-06       ISO/IEC 17825 (kiểm thử biện pháp giảm thiểu tấn công
              non-invasive); dataset công khai cho side-channel (ví dụ ASCAD)

  HS-08       Tài liệu kiến trúc TEE của các nhà cung cấp CPU; dự án nghiên
              cứu như CHERI, Keystone

  HS-09       Đặc tả bảo vệ bộ nhớ của RISC-V (PMP/ePMP); tài liệu TrustZone

  HS-13       OpenROAD và các PDK mở (ví dụ SkyWater SKY130) cho thử nghiệm
              có thể tái tạo; cần kiểm tra license và mức phù hợp

  HS-14       Đặc tả UCIe và các tài liệu bảo mật liên quan chiplet

  HS-16       Common Criteria (ISO/IEC 15408); ISO/IEC 19790 và 24759;
              GlobalPlatform SESIP
  ---------------------------------------------------------------------------

Phụ lục F Checklist rà soát trước khi chốt memo

-   Câu hỏi có target, tầng, đối thủ và điều kiện bác bỏ.

-   Protocol có version; mọi sửa đổi có ngày và lý do.

-   Search log ghi nguyên văn query, ngày và bộ lọc.

-   Exclusion log có mã lý do cho mọi công trình bị loại.

-   Claim trọng tâm truy về nguồn gốc đã đọc full text, kèm locator.

-   Mọi trường không được báo cáo ghi Missing.

-   Có evidence nghịch được tìm và ghi nhận cho mỗi claim trọng tâm.

-   Mâu thuẫn được phân loại; không so sánh kết quả khác điều kiện.

-   Bậc reproducibility được ghi đúng; không đồng nhất download với
    reproduction.

-   Mọi gap gắn với phạm vi tìm kiếm và corpus.

-   Không cộng metric khác đơn vị thành điểm tổng.

-   Giới hạn bằng chứng (Phần 7.4) được kiểm tra với từng kết luận.

-   Phần AI hỗ trợ được người nghiên cứu kiểm tra ở claim trọng tâm.

-   Memo có quyết định và bước kiểm tra tiếp theo; nếu chưa phân giải,
    ghi Inconclusive cùng nguyên nhân.
