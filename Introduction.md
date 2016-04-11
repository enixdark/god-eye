## [Project for internship 04/2016]
Hi, anh đang cần làm một hệ thống để monitor và visualize tình trạng của các tuyến kết nối internet quốc tế từ Datacenter. Project này sẽ lấy tên là God's Eye (ăn theo FF7)

*Đặt vấn đề:* VCCorp có rất nhiều dải mạng WAN khác nhau, và mỗi dải mạng này lại có đường đi ("đường đi" = một dãy các router/nút mạng) đến từng vùng trên thế giới khác nhau. Đường về của các gói tin từ từng vùng trên thế giới tới từng dải mạng của VCCorp cũng khác nhau. 
Với tình trạng như vậy hiện cho phương án monitor nào đủ tốt để nhanh chóng phát hiện nút mạng có vấn đề, dẫn đến việc có thể có một tập các user vào các site của công ty cũng như Cloud bị chậm hoặc thậm chí ko vào được mà chúng ta ko hề biết.

*Ý tưởng / Giải pháp:* Để cải thiện tình trạng này ta sẽ dùng N servers (là các VPS) nằm rải rác trên N dải mạng WAN của cty, và M servers (là các VPS) nằm rải rác ở các vùng trên thế giới (thuê của AWS, GoogleCloud, Rackspace, v.v...)

 Trên N+M servers này ta sẽ cài Webserver, host các file 100KB/1MB/10MB/100MB sẽ dùng để download test tốc độ; và cài thêm các Agent do chúng ta viết. 
Mỗi Agent này sẽ nhiệm vụ thực hiện các check khác nhau tới (N+M-1) servers còn lại để thu thập số liệu nhằm "vẽ" nên các loại bản đồ mà chúng ta mong muốn. Các check mà mỗi Agent có thể thực hiện bao gồm: 
Download file nằm tại (N+M-1) servers kia --> tính toán ra download-speed, độ biến động (Mean Deviation) của download-speed, và acceleration của download-speed. Và một số thông số khác như: TCP three-way-handshake time, Time-to-first-byte, v.v...
 Traceroute tới (N+M-1) servers kia để vẽ nên "bản đồ" mạng cũng như Latency từ Agent đó tới từng nút mạng nằm trên từng tuyến đường.  
v.v..

Sau khi các Agent đã thu thập đc số liệu thì việc tiếp theo sẽ là:
Visualize lên dasboard sao cho rõ ràng, có ý nghĩa và đẹp 
Gửi cảnh báo theo rules khi một thông số nào đó vượt ngưỡng
v.v..

Đây là một side-project hay và bọn em sẽ học được nhiều thứ khi tham gia làm. Ai muốn tham gia thì comment lại nhé.

*Happy Hacking! :D*
