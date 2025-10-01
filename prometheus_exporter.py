from prometheus_client import start_http_server, Gauge
import time
import threading
from Agent import (
    generate_container_metrics, 
    generate_vm_metrics, 
    generate_app_metrics, 
    generate_orchestrator_metrics, 
    generate_network_metrics
)

# Create Prometheus metrics
container_cpu = Gauge('argus_container_cpu_percent', 'Container CPU usage', ['host_id', 'container_id'])
container_memory = Gauge('argus_container_memory_bytes', 'Container memory usage', ['host_id', 'container_id'])
vm_cpu = Gauge('argus_vm_cpu_percent', 'VM CPU usage', ['host_id'])
vm_power = Gauge('argus_vm_power_watts', 'VM power consumption', ['host_id'])
app_requests = Gauge('argus_app_requests_per_second', 'App request rate', ['host_id', 'container_id'])
app_latency = Gauge('argus_app_latency_p95_ms', 'App P95 latency', ['host_id', 'container_id'])

def update_metrics():
    while True:
        # Container metrics
        cm = generate_container_metrics()
        container_cpu.labels(host_id=cm['host_id'], container_id=cm['container_id']).set(cm['cpu_util_pct'])
        container_memory.labels(host_id=cm['host_id'], container_id=cm['container_id']).set(cm['memory_rss_bytes'])
        
        # VM metrics
        vm = generate_vm_metrics()
        vm_cpu.labels(host_id=vm['host_id']).set(vm['vm_cpu_pct'])
        vm_power.labels(host_id=vm['host_id']).set(vm['host_power_estimate_w'])
        
        # App metrics
        app = generate_app_metrics()
        app_requests.labels(host_id=app['host_id'], container_id=app['container_id']).set(app['request_rate_rps'])
        app_latency.labels(host_id=app['host_id'], container_id=app['container_id']).set(app['latency_p95_ms'])
        
        time.sleep(15)

if __name__ == '__main__':
    # Start metrics server
    start_http_server(8000)
    print("Prometheus metrics available at: http://localhost:8000/metrics")
    
    # Start updating metrics
    metrics_thread = threading.Thread(target=update_metrics, daemon=True)
    metrics_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")