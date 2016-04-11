rpc_server_url = None # địa chỉ rpc_server
db_url = None #địa chỉ của MetricDB
check_timeout = 3
upload_timeout = None # timeout of sending result to DB
check_interval = 5 # option which APScheduler need


enable_plugin = [
    {
        'name': 'Ping',
        'path': 'check_plugins.ping'
    }
]