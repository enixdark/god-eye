# Overview
## Scope
# Archietecture
## Use Cases
### 1. Check Networking:
Agent run checks namely:
> Note: Run lần lượt `check_jobs` đối với mỗi Node. `check_jobs` bao
 gồm nhiều check song song( đồng thời chạy).

- ping
- download:
    + 100KB
    + 1MB
    + 10MB
    + 100MB
    
Then, analyze some term like:
> Chỗ này em chưa hỏi anh. Phần tính toàn nào dưới đấy là đc đo từ agent,
phần nào thuộc MetricsDB?

- download-speed
- Mean Deviation(độ biến động) of download-speed
- acceleration của download-speed
- TCP three-way-handshake time
- Time-to-first-byte

### 2. Check Timeout:
Mỗi check phải có time out.

### 3. Use APScheduler to manage check jobs

### 4. Upload Result:
After run checks, agent send each result to MetricsDB.


### 5. Dynamic Plugins Patterns:
> Chỗ này có cần design kỹ không?
Có thể dễ dàng enable các check một cách tùy ý.
Và dễ dàng config các tham số của một check.

### 6. Get Lists of Node:
Agent lấy danh sách các node từ rpc_server.

## Config:
Dựa vào use case ta có các option:

- `rpc_server_url`: địa chỉ rpc_server
- `db_url`: địa chỉ của MetricDB
- `enable_check_plugin`: danh sách các check ví dụ:

```python
[
    {
        'name': 'ping',
        'path': 'agent.check_plugins.ping.Ping' # đường dẫn tới check_plugin
    }
]
```

- `check_timeout`: đơn vị `second`
- `upload_timeout`: đơn vị `second` timeout of sending result to DB
- `check_interval`: đơn vị `second` option which APScheduler need

## Components

```
└── Agent
    ├── requirements.txt
    ├── dev-requirements.text
    ├── Makefile
    ├── setup.py
    ├── middleware.py
    ├── Agent
    │   ├── agent.py
    │   ├── config.py
    │   ├── webservercontroller.py
    │   ├── listnodemanager.py
    │   ├── __init__.py
    │   ├── webservercontroller.py
    │   ├── listnodemanager.py
    │   ├── networkchecker.py
    │   ├── sendresult.py
    │   ├── check_plugin
    │   │   ├── __init__.py
    │   │   ├── ping.py
    │   │   ├── download.py
    │   │   └── abcdef.py
    ├── tests
    │   ├── test_load_config.py
    │   ├── test_.....py
```


