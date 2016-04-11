## Tóm tắt thiết kế của God's Eye
1. Dùng [Serf](https://www.serfdom.io/) để quản lý membership khi các node join/leave hệ thống (một lý do chọn Serf là do nó là một [distributed-system loại AP](https://dzone.com/articles/better-explaining-cap-theorem) + nhẹ, đơn giản)
2. Dùng Ansible (với [dynamic-inventory](http://docs.ansible.com/ansible/intro_dynamic_inventory.html) lấy [từ Serf](https://github.com/ansible/ansible/blob/stable-2.0/contrib/inventory/serf.py)) để manage service (serf, nginx,..) và deploy code (agent,..) tới các node trong hệ thống. (Sẽ cân nhắc dùng Docker để chạy agent nếu có ích) 
3. Có 1 node làm *bootstrap-node* vừa chạy Serf vừa chạy Ansible, các node mới khi được khởi tạo sẽ join vào cụm bằng địa chỉ (domain) của *bootstrap-node*.
4. Agent được viết python khi cần get node-list hoặc gửi event gì tới các node sẽ gọi đến rpc-server (của Serf daemon) chạy trên chính node đó.
5. Agent có config file ([dạng INI](https://docs.python.org/2/library/configparser.html)) để quản lý các thông tin như: 
    + các action+handler ở local (ví dụ check local-webserver, restart nếu die), 
    + các check mà agent sẽ thực hiện kèm theo các tham số (ví dụ URL-download, check-interval,..), 
    + thông tin về Metrics DB host 
    + v.v...
6. Các funtion check phải có timeout (ví dụ dùng Signal & Contextmanager)
7. [Optional] Dùng [APScheduler](https://pypi.python.org/pypi/APScheduler/3.0.5) hoặc tương tự để quản lý các jobs check.
8. [Optional] Để xử lý trường hợp khi network không thông giữa Agent và MetricsDB host có thể dùng Queue (của Python hoặc dùng ZeroMQ) hoặc dùng Python's retry decoration.
9. MetricsDB dùng InfluxDB; cảnh báo theo metrics bằng Kapacitor
10. [Admin Dashboard] Các bạn thực tập Ruby/Rails sẽ bắt đầu làm khi Backend đã xong tương đối.
