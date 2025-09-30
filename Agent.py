import streamlit as st
import random
import time
import uuid
import math
from datetime import datetime

def human_bytes(n: int) -> str:
    step_unit = 1024.0
    if n < step_unit:
        return f"{n} B"
    for unit in ["KB", "MB", "GB", "TB"]:
        n /= step_unit
        if n < step_unit:
            return f"{n:,.2f} {unit}"
    return f"{n:,.2f} PB"

def human_seconds(s: int) -> str:
    if s < 60:
        return f"{s} s"
    m, s = divmod(s, 60)
    if m < 60:
        return f"{m}m {s}s"
    h, m = divmod(m, 60)
    return f"{h}h {m}m"

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

INTERVAL = 15  
SLEEP_STEP = 1  
MAX_FEED = 10   

def main():
    st.set_page_config(page_title="Argus Agent", layout="wide", initial_sidebar_state="expanded")

    if "agent_log" not in st.session_state:
        st.session_state.agent_log = []
    if "instance_id" not in st.session_state:
        st.session_state.instance_id = str(uuid.uuid4())[:8]
    if "emit_seq" not in st.session_state:
        st.session_state.emit_seq = 0
    if "last_emit" not in st.session_state:
        st.session_state.last_emit = time.monotonic() - INTERVAL  
    if "last_metrics" not in st.session_state:
        st.session_state.last_metrics = {
            "containers": generate_container_metrics(),
            "vms": generate_vm_metrics(),
            "apps": generate_app_metrics(),
            "orchestrator": generate_orchestrator_metrics(),
            "network": generate_network_metrics()
        }

# Need help in designing the agent's UI
    st.markdown(
        """
    <style>
    .agent-card {background: linear-gradient(90deg, #0f172a 0%, #071034 100%); padding: 14px; border-radius: 10px; color: #E6F0FF;}
    .agent-metric {background: rgba(255,255,255,0.03); padding:8px; border-radius:8px; margin-bottom:6px}
    .agent-small {color:#AFC6FF; font-size:12px}
    .status-pill {display:inline-block; padding:6px 10px; border-radius:999px; font-weight:700;}
    .status-online {background: #10b981; color: white}
    .status-offline {background: #ef4444; color: white}
    .muted {color:#9aa7c7}
    pre {
        background-color: #021026 !important;
        color: #dbeafe !important;
        padding: 8px !important;
        border-radius: 6px !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col_logo, col_text = st.columns([0.10, 0.90])

    with col_logo:
        st.image("Assets/Argus Logo.png", width=60)

    with col_text:
        st.markdown(
            """
            <div>
            <div style='font-size:20px;font-weight:700'>Argus Agent</div>
            <div class='agent-small'>Telemetry ingestion preview</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.sidebar:
        st.markdown("# Argus Agent")
        st.markdown(f"**Instance ID:** `{st.session_state.instance_id}`")
        st.markdown("**Location:** edge-site-01")
        st.markdown("---")
        st.markdown("Agent fetches new telemetry data every **15 seconds**")
        show_raw = st.checkbox("Show global raw JSON", value=False)
        st.markdown("---")
        st.caption("Argus Agent by PiUEneer")

    main_area = st.container()
    sidebar_right = st.empty()

    with main_area:
        panels = st.container()
        left, right = panels.columns([2, 1])

        cont_placeholder = left.empty()
        vm_placeholder = left.empty()
        app_placeholder = left.empty()
        orch_placeholder = left.empty()
        net_placeholder = left.empty()

        with right:
            st.markdown("### Agent Feed")
            feed_box = st.empty()
            st.markdown("### Controls")
            st.markdown("(Presentation only)")

    countdown_placeholder = sidebar_right.empty()

    try:
        while True:
            now_mon = time.monotonic()
            elapsed = now_mon - st.session_state.last_emit
            remaining = max(0.0, INTERVAL - elapsed)
            remaining_ceil = math.ceil(remaining)

            if elapsed >= INTERVAL:
                st.session_state.last_metrics = {
                    "containers": generate_container_metrics(),
                    "vms": generate_vm_metrics(),
                    "apps": generate_app_metrics(),
                    "orchestrator": generate_orchestrator_metrics(),
                    "network": generate_network_metrics()
                }
                st.session_state.emit_seq += 1
                st.session_state.last_emit = now_mon

                entry = (
                    f"{datetime.now().strftime('%H:%M:%S')} - Update #{st.session_state.emit_seq} - "
                    f"Snapshot captured and ready for storage (instance: {st.session_state.instance_id})  | "
                    f"container: {st.session_state.last_metrics['containers']['container_id']}  | "
                    f"vm: {st.session_state.last_metrics['vms']['host_id']}  | "
                    f"app: {st.session_state.last_metrics['apps']['container_id']}"
                )
                st.session_state.agent_log.insert(0, entry)
                st.session_state.agent_log = st.session_state.agent_log[:MAX_FEED]

            m = st.session_state.last_metrics

            countdown_placeholder.markdown(f"**Next update in:** {remaining_ceil} s")

            cm = m["containers"]
            with cont_placeholder.container():
                st.markdown("<div class='agent-card'>", unsafe_allow_html=True)
                st.markdown(
                    f"<div style='display:flex; justify-content:space-between; align-items:center'>"
                    f"<div><strong>Containers</strong> <span class='agent-small'>| {cm['container_image']} - {cm['container_id']}</span></div>"
                    f"<div class='agent-small muted'>Host: {cm['host_id']}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
                k1, k2, k3, k4 = st.columns([1, 1, 1, 1])
                k1.metric("CPU %", f"{cm['cpu_util_pct']}%")
                k2.metric("Memory", f"{human_bytes(cm['memory_rss_bytes'])}")
                k3.metric("Net RX", f"{human_bytes(cm['network_rx_bytes'])}")
                k4.metric("Uptime", f"{human_seconds(cm['uptime_seconds'])}")
                st.progress(min(max(cm['cpu_util_pct'] / 100.0, 0.0), 1.0))
                st.markdown(f"<div class='agent-small muted'>Next update in: {remaining_ceil} s</div>", unsafe_allow_html=True)
                with st.expander("All telemetry - container", expanded=False):
                    st.json(cm)
                st.markdown("</div>", unsafe_allow_html=True)

            vm = m["vms"]
            with vm_placeholder.container():
                st.markdown("<div class='agent-card' style='margin-top:10px'>", unsafe_allow_html=True)
                st.markdown(f"<strong>Virtual Machine</strong> <span class='agent-small muted'>| {vm['host_id']}</span>", unsafe_allow_html=True)
                v1, v2, v3, v4 = st.columns([1, 1, 1, 1])
                v1.metric("CPU %", f"{vm['vm_cpu_pct']}%")
                v2.metric("Memory", f"{human_bytes(vm['memory_rss_bytes'])}")
                v3.metric("Disk IOPS", f"{vm['disk_iops']}")
                v4.metric("Power Est.", f"{vm['host_power_estimate_w']} W")
                st.progress(min(max(vm['vm_cpu_pct'] / 100.0, 0.0), 1.0))
                st.markdown(f"<div class='agent-small muted'>Next update in: {remaining_ceil} s</div>", unsafe_allow_html=True)
                with st.expander("All telemetry - vm", expanded=False):
                    st.json(vm)
                st.markdown("</div>", unsafe_allow_html=True)

            ap = m["apps"]
            with app_placeholder.container():
                st.markdown("<div class='agent-card' style='margin-top:10px'>", unsafe_allow_html=True)
                st.markdown(f"<strong>Application</strong> <span class='agent-small muted'>| {ap['container_id']} on {ap['host_id']}</span>", unsafe_allow_html=True)
                a1, a2, a3 = st.columns([1, 1, 1])
                a1.metric("Req/s", f"{ap['request_rate_rps']}")
                a2.metric("P95 (ms)", f"{ap['latency_p95_ms']}")
                a3.metric("Errors %", f"{ap['error_rate_pct']}%")
                st.progress(min(max(ap['cpu_util_pct'] / 100.0, 0.0), 1.0))
                st.markdown(f"<div class='agent-small muted'>Next update in: {remaining_ceil} s</div>", unsafe_allow_html=True)
                with st.expander("All telemetry - app", expanded=False):
                    st.json(ap)
                st.markdown("</div>", unsafe_allow_html=True)

            orc = m["orchestrator"]
            with orch_placeholder.container():
                st.markdown("<div class='agent-card' style='margin-top:10px'>", unsafe_allow_html=True)
                st.markdown(f"<strong>Orchestrator</strong> <span class='agent-small muted'>| nodes: {orc['node_count']}</span>", unsafe_allow_html=True)
                o1, o2 = st.columns([1, 1])
                o1.metric("Pods", f"{orc['pod_count']}")
                o2.metric("API Latency ms", f"{orc['cluster_api_latency_ms']}")
                st.markdown(f"<div class='agent-small muted'>Next update in: {remaining_ceil} s</div>", unsafe_allow_html=True)
                with st.expander("All telemetry - orchestrator", expanded=False):
                    st.json(orc)
                st.markdown("</div>", unsafe_allow_html=True)

            net = m["network"]
            with net_placeholder.container():
                st.markdown("<div class='agent-card' style='margin-top:10px'>", unsafe_allow_html=True)
                st.markdown(f"<strong>Network</strong> <span class='agent-small muted'>| {net['host_id']}</span>", unsafe_allow_html=True)
                n1, n2, n3 = st.columns([1, 1, 1])
                n1.metric("Throughput bps", f"{net['interface_throughput_bps']}")
                n2.metric("RTT ms", f"{net['rtt_ms']}")
                n3.metric("Packet Loss %", f"{net['packet_loss_pct']}%")
                st.markdown(f"<div class='agent-small muted'>Next update in: {remaining_ceil} s</div>", unsafe_allow_html=True)
                with st.expander("All telemetry - network", expanded=False):
                    st.json(net)
                st.markdown("</div>", unsafe_allow_html=True)

            feed_box.markdown("""
            <div style='background:#021026;padding:8px;border-radius:8px;min-height:220px;'>
            <pre style='white-space:pre-wrap'>
            """ + "\n".join(st.session_state.agent_log) + """
            </pre>
            </div>
            """, unsafe_allow_html=True)

            if show_raw:
                st.sidebar.markdown("### Latest raw telemetry")
                st.sidebar.json(st.session_state.last_metrics)

            time.sleep(SLEEP_STEP)

    except Exception as e:
        err_entry = f"[{datetime.now().isoformat()}] instance={st.session_state.instance_id} encountered error: {e}"
        st.session_state.agent_log.insert(0, err_entry)
        st.session_state.agent_log = st.session_state.agent_log[:MAX_FEED]
        feed_box.markdown(
            "<div style='background:#021026;padding:8px;border-radius:8px;min-height:220px;'><pre style='white-space:pre-wrap'>"
            + "\n".join(st.session_state.agent_log)
            + "</pre></div>",
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()
