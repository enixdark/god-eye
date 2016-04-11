rpc_server_url = None # địa chỉ rpc_server
db_url = None #địa chỉ của MetricDB
check_timeout = 5
upload_timeout = None # timeout of sending result to DB
check_interval = 10 # option which APScheduler need


enable_plugin = [
    {
        'name': 'ping',
        'path': 'agent.check_plugins.ping.Ping'
    }
]