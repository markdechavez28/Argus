import streamlit as st
import random
import time
from datetime import datetime

def generate_container_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "host_id": f"host_{random.randint(1, 100)}",
        "container_id": f"container_{random.randint(1, 1000)}",
        "container_image": f"image_{random.choice(['nginx', 'mysql', 'redis', 'flask'])}",
        "cpu_util_pct": round(random.uniform(0.0, 100.0), 2),
        "cpu_seconds": round(random.uniform(0.0, 10000.0), 2),
        "memory_rss_bytes": random.randint(0, 8 * 1024**2),
        "memory_limit_bytes": random.randint(8 * 1024**2, 16 * 1024**2),
        "disk_read_bytes": random.randint(0, 1024**3),
        "disk_write_bytes": random.randint(0, 1024**3),
        "io_ops": random.randint(0, 100),
        "network_rx_bytes": random.randint(0, 1024**3),
        "network_tx_bytes": random.randint(0, 1024**3),
        "process_count": random.randint(1, 50),
        "restart_count": random.randint(0, 10),
        "uptime_seconds": random.randint(0, 86400),
        "sensor_temp_c": round(random.uniform(0.0, 100.0), 2),
        "sensor_humidity_pct": round(random.uniform(0.0, 100.0), 2)
    }

def generate_vm_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "host_id": f"host_{random.randint(1, 100)}",
        "vm_cpu_pct": round(random.uniform(0.0, 100.0), 2),
        "cpu_seconds": round(random.uniform(0.0, 10000.0), 2),
        "vm_cpu_steal_pct": round(random.uniform(0.0, 100.0), 2),
        "memory_rss_bytes": random.randint(0, 8 * 1024**2),
        "memory_limit_bytes": random.randint(8 * 1024**2, 16 * 1024**2),
        "disk_iops": random.randint(0, 100),
        "disk_read_bytes": random.randint(0, 1024**3),
        "disk_write_bytes": random.randint(0, 1024**3),
        "network_rx_bytes": random.randint(0, 1024**3),
        "network_tx_bytes": random.randint(0, 1024**3),
        "host_power_estimate_w": round(random.uniform(0.0, 5000.0), 2),
        "hypervisor_overhead_pct": round(random.uniform(0.0, 100.0), 2),
        "uptime_seconds": random.randint(0, 86400)
    }

def generate_app_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "host_id": f"host_{random.randint(1, 100)}",
        "container_id": f"container_{random.randint(1, 1000)}",
        "request_rate_rps": round(random.uniform(0.0, 1000.0), 2),
        "latency_p95_ms": round(random.uniform(0.0, 1000.0), 2),
        "latency_p50_ms": round(random.uniform(0.0, 1000.0), 2),
        "latency_p99_ms": round(random.uniform(0.0, 1000.0), 2),
        "error_rate_pct": round(random.uniform(0.0, 100.0), 2),
        "db_connection_count": random.randint(0, 100),
        "cache_hit_ratio": round(random.uniform(0.0, 100.0), 2),
        "queue_length": random.randint(0, 100),
        "cpu_util_pct": round(random.uniform(0.0, 100.0), 2),
        "cpu_seconds": round(random.uniform(0.0, 10000.0), 2),
        "memory_rss_bytes": random.randint(0, 8 * 1024**2),
        "disk_read_bytes": random.randint(0, 1024**3),
        "disk_write_bytes": random.randint(0, 1024**3),
        "network_rx_bytes": random.randint(0, 1024**3),
        "network_tx_bytes": random.randint(0, 1024**3),
        "process_count": random.randint(1, 50),
        "restart_count": random.randint(0, 10),
        "sensor_temp_c": round(random.uniform(0.0, 100.0), 2),
        "sensor_humidity_pct": round(random.uniform(0.0, 100.0), 2)
    }

def generate_orchestrator_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "node_count": random.randint(1, 100),
        "pod_count": random.randint(1, 1000),
        "pod_status_pending": random.randint(0, 100),
        "pod_status_running": random.randint(0, 100),
        "pod_status_failed": random.randint(0, 100),
        "scheduler_evictions": random.randint(0, 50),
        "cluster_api_latency_ms": round(random.uniform(0.0, 1000.0), 2),
        "cluster_autoscaler_actions": random.randint(0, 50),
        "aggregated_cpu_util_pct": round(random.uniform(0.0, 100.0), 2),
        "aggregated_memory_rss_bytes": random.randint(0, 8 * 1024**2),
        "aggregated_network_bytes": random.randint(0, 1024**3),
        "restart_count": random.randint(0, 10),
        "uptime_seconds": random.randint(0, 86400)
    }

def generate_network_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "host_id": f"host_{random.randint(1, 100)}",
        "interface_throughput_bps": random.randint(0, 1000000),
        "network_rx_bytes": random.randint(0, 1024**3),
        "network_tx_bytes": random.randint(0, 1024**3),
        "packet_loss_pct": round(random.uniform(0.0, 100.0), 2),
        "rtt_ms": round(random.uniform(0.0, 1000.0), 2),
        "jitter_ms": round(random.uniform(0.0, 100.0), 2),
        "active_flows": random.randint(0, 100),
        "bgp_changes": random.randint(0, 10),
        "psu_efficiency_pct": round(random.uniform(0.0, 100.0), 2),
        "sensor_temp_c": round(random.uniform(0.0, 100.0), 2),
        "sensor_humidity_pct": round(random.uniform(0.0, 100.0), 2)
    }
#api naa

#app
def main():
    st.title("Telemetry Data Simulation")

    container_placeholder = st.empty()
    vm_placeholder = st.empty()
    app_placeholder = st.empty()
    orchestrator_placeholder = st.empty()
    network_placeholder = st.empty()

    while True:
        container_metrics = generate_container_metrics()
        vm_metrics = generate_vm_metrics()
        app_metrics = generate_app_metrics()
        orchestrator_metrics = generate_orchestrator_metrics()
        network_metrics = generate_network_metrics()

        container_placeholder.markdown(f"### Containers Metrics\n"
                                       f"**Timestamp:** {container_metrics['timestamp']}  \n"
                                       f"**Host ID:** {container_metrics['host_id']}  \n"
                                       f"**Container ID:** {container_metrics['container_id']}  \n"
                                       f"**Container Image:** {container_metrics['container_image']}  \n"
                                       f"**CPU Utilization (%):** {container_metrics['cpu_util_pct']}  \n"
                                       f"**CPU Seconds:** {container_metrics['cpu_seconds']}  \n"
                                       f"**Memory RSS (bytes):** {container_metrics['memory_rss_bytes']}  \n"
                                       f"**Memory Limit (bytes):** {container_metrics['memory_limit_bytes']}  \n"
                                       f"**Disk Read (bytes):** {container_metrics['disk_read_bytes']}  \n"
                                       f"**Disk Write (bytes):** {container_metrics['disk_write_bytes']}  \n"
                                       f"**I/O Operations:** {container_metrics['io_ops']}  \n"
                                       f"**Network RX (bytes):** {container_metrics['network_rx_bytes']}  \n"
                                       f"**Network TX (bytes):** {container_metrics['network_tx_bytes']}  \n"
                                       f"**Process Count:** {container_metrics['process_count']}  \n"
                                       f"**Restart Count:** {container_metrics['restart_count']}  \n"
                                       f"**Uptime (seconds):** {container_metrics['uptime_seconds']}  \n"
                                       f"**Sensor Temperature (°C):** {container_metrics['sensor_temp_c']}  \n"
                                       f"**Sensor Humidity (%):** {container_metrics['sensor_humidity_pct']}  \n")

        vm_placeholder.markdown(f"### Virtual Machines Metrics\n"
                                f"**Timestamp:** {vm_metrics['timestamp']}  \n"
                                f"**Host ID:** {vm_metrics['host_id']}  \n"
                                f"**VM CPU Utilization (%):** {vm_metrics['vm_cpu_pct']}  \n"
                                f"**CPU Seconds:** {vm_metrics['cpu_seconds']}  \n"
                                f"**VM CPU Steal (%):** {vm_metrics['vm_cpu_steal_pct']}  \n"
                                f"**Memory RSS (bytes):** {vm_metrics['memory_rss_bytes']}  \n"
                                f"**Memory Limit (bytes):** {vm_metrics['memory_limit_bytes']}  \n"
                                f"**Disk IOPS:** {vm_metrics['disk_iops']}  \n"
                                f"**Disk Read (bytes):** {vm_metrics['disk_read_bytes']}  \n"
                                f"**Disk Write (bytes):** {vm_metrics['disk_write_bytes']}  \n"
                                f"**Network RX (bytes):** {vm_metrics['network_rx_bytes']}  \n"
                                f"**Network TX (bytes):** {vm_metrics['network_tx_bytes']}  \n"
                                f"**Host Power Estimate (W):** {vm_metrics['host_power_estimate_w']}  \n"
                                f"**Hypervisor Overhead (%):** {vm_metrics['hypervisor_overhead_pct']}  \n"
                                f"**Uptime (seconds):** {vm_metrics['uptime_seconds']}  \n")

        app_placeholder.markdown(f"### Applications Metrics\n"
                                 f"**Timestamp:** {app_metrics['timestamp']}  \n"
                                 f"**Host ID:** {app_metrics['host_id']}  \n"
                                 f"**Container ID:** {app_metrics['container_id']}  \n"
                                 f"**Request Rate (RPS):** {app_metrics['request_rate_rps']}  \n"
                                 f"**Latency P95 (ms):** {app_metrics['latency_p95_ms']}  \n"
                                 f"**Latency P50 (ms):** {app_metrics['latency_p50_ms']}  \n"
                                 f"**Latency P99 (ms):** {app_metrics['latency_p99_ms']}  \n"
                                 f"**Error Rate (%):** {app_metrics['error_rate_pct']}  \n"
                                 f"**DB Connection Count:** {app_metrics['db_connection_count']}  \n"
                                 f"**Cache Hit Ratio (%):** {app_metrics['cache_hit_ratio']}  \n"
                                 f"**Queue Length:** {app_metrics['queue_length']}  \n"
                                 f"**CPU Utilization (%):** {app_metrics['cpu_util_pct']}  \n"
                                 f"**CPU Seconds:** {app_metrics['cpu_seconds']}  \n"
                                 f"**Memory RSS (bytes):** {app_metrics['memory_rss_bytes']}  \n"
                                 f"**Disk Read (bytes):** {app_metrics['disk_read_bytes']}  \n"
                                 f"**Disk Write (bytes):** {app_metrics['disk_write_bytes']}  \n"
                                 f"**Network RX (bytes):** {app_metrics['network_rx_bytes']}  \n"
                                 f"**Network TX (bytes):** {app_metrics['network_tx_bytes']}  \n"
                                 f"**Process Count:** {app_metrics['process_count']}  \n"
                                 f"**Restart Count:** {app_metrics['restart_count']}  \n"
                                 f"**Sensor Temperature (°C):** {app_metrics['sensor_temp_c']}  \n"
                                 f"**Sensor Humidity (%):** {app_metrics['sensor_humidity_pct']}  \n")

        orchestrator_placeholder.markdown(f"### Orchestrator Metrics\n"
                                           f"**Timestamp:** {orchestrator_metrics['timestamp']}  \n"
                                           f"**Node Count:** {orchestrator_metrics['node_count']}  \n"
                                           f"**Pod Count:** {orchestrator_metrics['pod_count']}  \n"
                                           f"**Pod Status Pending:** {orchestrator_metrics['pod_status_pending']}  \n"
                                           f"**Pod Status Running:** {orchestrator_metrics['pod_status_running']}  \n"
                                           f"**Pod Status Failed:** {orchestrator_metrics['pod_status_failed']}  \n"
                                           f"**Scheduler Evictions:** {orchestrator_metrics['scheduler_evictions']}  \n"
                                           f"**Cluster API Latency (ms):** {orchestrator_metrics['cluster_api_latency_ms']}  \n"
                                           f"**Cluster Autoscaler Actions:** {orchestrator_metrics['cluster_autoscaler_actions']}  \n"
                                           f"**Aggregated CPU Utilization (%):** {orchestrator_metrics['aggregated_cpu_util_pct']}  \n"
                                           f"**Aggregated Memory RSS (bytes):** {orchestrator_metrics['aggregated_memory_rss_bytes']}  \n"
                                           f"**Aggregated Network Bytes:** {orchestrator_metrics['aggregated_network_bytes']}  \n"
                                           f"**Restart Count:** {orchestrator_metrics['restart_count']}  \n"
                                           f"**Uptime (seconds):** {orchestrator_metrics['uptime_seconds']}  \n")

        network_placeholder.markdown(f"### Network Metrics\n"
                                      f"**Timestamp:** {network_metrics['timestamp']}  \n"
                                      f"**Host ID:** {network_metrics['host_id']}  \n"
                                      f"**Interface Throughput (bps):** {network_metrics['interface_throughput_bps']}  \n"
                                      f"**Network RX (bytes):** {network_metrics['network_rx_bytes']}  \n"
                                      f"**Network TX (bytes):** {network_metrics['network_tx_bytes']}  \n"
                                      f"**Packet Loss (%):** {network_metrics['packet_loss_pct']}  \n"
                                      f"**RTT (ms):** {network_metrics['rtt_ms']}  \n"
                                      f"**Jitter (ms):** {network_metrics['jitter_ms']}  \n"
                                      f"**Active Flows:** {network_metrics['active_flows']}  \n"
                                      f"**BGP Changes:** {network_metrics['bgp_changes']}  \n"
                                      f"**PSU Efficiency (%):** {network_metrics['psu_efficiency_pct']}  \n"
                                      f"**Sensor Temperature (°C):** {network_metrics['sensor_temp_c']}  \n"
                                      f"**Sensor Humidity (%):** {network_metrics['sensor_humidity_pct']}  \n")

        time.sleep(15) 

if __name__ == "__main__":
    main()