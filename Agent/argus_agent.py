import streamlit as st
import random
import time
import uuid
import math
import random
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

    st.markdown(
        """
    <style>
    .agent-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0c4a6e 100%); 
        padding: 18px; 
        border-radius: 12px; 
        color: #E6F0FF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 4px solid #10b981;
        margin-bottom: 16px;
    }
    .agent-card.critical {
        border-left-color: #ef4444;
        background: linear-gradient(135deg, #1f1f23 0%, #2d1b20 50%, #3f1825 100%);
    }
    .agent-card.warning {
        border-left-color: #f59e0b;
        background: linear-gradient(135deg, #1f1f23 0%, #2d2520 50%, #3f2f1a 100%);
    }
    .agent-metric {
        background: rgba(255,255,255,0.05); 
        padding: 12px; 
        border-radius: 8px; 
        margin-bottom: 8px;
        transition: all 0.2s ease;
    }
    .agent-metric:hover {
        background: rgba(255,255,255,0.08);
        transform: translateY(-1px);
    }
    .agent-small {
        color: #94a3b8; 
        font-size: 13px;
        font-weight: 500;
    }
    .status-pill {
        display: inline-block; 
        padding: 4px 12px; 
        border-radius: 20px; 
        font-weight: 600;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .status-online {background: linear-gradient(90deg, #10b981, #059669); color: white; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);}
    .status-offline {background: linear-gradient(90deg, #ef4444, #dc2626); color: white; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);}
    .status-warning {background: linear-gradient(90deg, #f59e0b, #d97706); color: white; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);}
    .muted {color: #64748b;}
    .env-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 12px;
        font-weight: 600;
    }
    .env-good {color: #10b981;}
    .env-moderate {color: #f59e0b;}
    .env-poor {color: #ef4444;}
    .header-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid rgba(148, 163, 184, 0.1);
    }
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 12px;
        margin: 12px 0;
    }
    .metric-card {
        background: rgba(255,255,255,0.03);
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        transition: all 0.2s ease;
    }
    .metric-card:hover {
        background: rgba(255,255,255,0.06);
        transform: translateY(-2px);
    }
    .metric-value {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .metric-label {
        font-size: 12px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    pre {
        background-color: #0f172a !important;
        color: #e2e8f0 !important;
        padding: 12px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(148, 163, 184, 0.1);
        font-family: 'Monaco', 'Consolas', monospace;
    }
    .agent-feed {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 8px;
        padding: 12px;
        min-height: 280px;
        max-height: 400px;
        overflow-y: auto;
    }
    .countdown-box {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin: 8px 0;
        color: white;
        font-weight: 600;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class='header-section'>
        <div style='display: flex; align-items: center; gap: 16px;'>
            <div style='font-size: 24px; font-weight: 700; color: #e2e8f0;'>
                🛡️ Argus Environmental Monitoring Agent
            </div>
            <div class='status-pill status-online'>ACTIVE</div>
        </div>
        <div style='margin-top: 8px; color: #94a3b8; font-size: 14px;'>
            Data-Driven Observability Infrastructure for Environmental Standards Compliance
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("# 🛡️ Argus Agent")
        st.markdown(f"**Instance ID:** `{st.session_state.instance_id}`")
        st.markdown("**Location:** edge-site-01")
        st.markdown("**ESG Compliance:** Active")
        
        st.markdown("---")
        st.markdown("### 🌱 Environmental Status")
        st.markdown("""
        <div class='env-indicator env-good'>🟢 Carbon Footprint: Normal</div><br>
        <div class='env-indicator env-moderate'>🟡 Heat Stress: Moderate</div><br>
        <div class='env-indicator env-good'>🟢 Air Quality: Good</div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("**Update Frequency:** 15 seconds")
        st.markdown("**ESG Frameworks:** GRI, TCFD")
        show_raw = st.checkbox("Show global raw JSON", value=False)
        st.markdown("---")
        st.caption("🏆 Argus Platform by PiUEneer")

    main_area = st.container()
    sidebar_right = st.empty()

    with main_area:
        panels = st.container()
        left, right = panels.columns([2.5, 1])

        cont_placeholder = left.empty()
        vm_placeholder = left.empty()
        app_placeholder = left.empty()
        orch_placeholder = left.empty()
        net_placeholder = left.empty()

        with right:
            st.markdown("### 📊 Agent Feed")
            feed_box = st.empty()
            st.markdown("### 🎛️ Controls")
            st.markdown("""
            <div style='background: rgba(255,255,255,0.03); padding: 12px; border-radius: 8px;'>
                <div style='color: #94a3b8; font-size: 12px;'>SIMULATION MODE</div>
                <div style='margin-top: 8px;'>
                    🔄 Auto-refresh: ON<br>
                    📈 ESG Calculation: Active<br>
                    📋 Report Generation: Ready
                </div>
            </div>
            """, unsafe_allow_html=True)

    countdown_placeholder = sidebar_right.empty()

    def get_environmental_status(metrics):
        """Determine environmental status based on metrics"""
        cm = metrics["containers"]
        vm = metrics["vms"]
        
        if cm['cpu_util_pct'] > 80 or vm['vm_cpu_pct'] > 80:
            return "warning"
        elif cm['cpu_util_pct'] > 90 or vm['vm_cpu_pct'] > 90:
            return "critical"
        return "normal"

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
                    f"🕐 {datetime.now().strftime('%H:%M:%S')} | Update #{st.session_state.emit_seq} | "
                    f"ESG snapshot captured | Instance: {st.session_state.instance_id} | "
                    f"CO₂ Impact: Calculated | Environmental Indices: Updated"
                )
                st.session_state.agent_log.insert(0, entry)
                st.session_state.agent_log = st.session_state.agent_log[:MAX_FEED]

            m = st.session_state.last_metrics
            env_status = get_environmental_status(m)

            countdown_placeholder.markdown(f"""
            <div class='countdown-box'>
                <div style='font-size: 14px;'>Next ESG Update</div>
                <div style='font-size: 20px; margin: 4px 0;'>{remaining_ceil}s</div>
                <div style='font-size: 11px; opacity: 0.8;'>Environmental indices refreshing...</div>
            </div>
            """, unsafe_allow_html=True)

            cm = m["containers"]
            card_class = "agent-card"
            if cm['cpu_util_pct'] > 80:
                card_class += " warning" if cm['cpu_util_pct'] <= 90 else " critical"
                
            with cont_placeholder.container():
                st.markdown(f"<div class='{card_class}'>", unsafe_allow_html=True)
                st.markdown(f"""
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px;'>
                    <div>
                        <div style='font-size: 16px; font-weight: 700;'>🐳 Container Infrastructure</div>
                        <div class='agent-small'>{cm['container_image']} • {cm['container_id']} • Host: {cm['host_id']}</div>
                    </div>
                    <div class='env-indicator env-good'>🌱 ESG: Active</div>
                </div>
                """, unsafe_allow_html=True)
                
                k1, k2, k3, k4 = st.columns([1, 1, 1, 1])
                k1.metric("CPU Usage", f"{cm['cpu_util_pct']:.1f}%", delta=f"{random.uniform(-5, 5):.1f}%")
                k2.metric("Memory", f"{human_bytes(cm['memory_rss_bytes'])}", delta=f"{random.choice(['+', '-'])}{human_bytes(random.randint(1000, 50000))}")
                k3.metric("Network RX", f"{human_bytes(cm['network_rx_bytes'])}")
                k4.metric("Uptime", f"{human_seconds(cm['uptime_seconds'])}")
                
                co2_impact = cm['cpu_util_pct'] * 0.12  # Simulated CO₂ calculation
                st.markdown(f"""
                <div style='margin: 12px 0; padding: 8px; background: rgba(16, 185, 129, 0.1); border-radius: 6px; border-left: 3px solid #10b981;'>
                    <div style='font-size: 12px; color: #10b981; font-weight: 600;'>ENVIRONMENTAL IMPACT</div>
                    <div style='color: #e2e8f0;'>Estimated CO₂: {co2_impact:.2f} kg/h • Heat Generation: {cm['sensor_temp_c']:.1f}°C</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.progress(min(max(cm['cpu_util_pct'] / 100.0, 0.0), 1.0))
                
                with st.expander("🔍 Full Telemetry - Container", expanded=False):
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

            feed_box.markdown(f"""
            <div class='agent-feed'>
                <div style='font-weight: 600; margin-bottom: 8px; color: #e2e8f0;'>🔄 Real-time ESG Monitoring Feed</div>
                <pre style='white-space: pre-wrap; margin: 0; font-size: 12px;'>{"<br>".join(st.session_state.agent_log)}</pre>
            </div>
            """, unsafe_allow_html=True)

            if show_raw:
                st.sidebar.markdown("### 📋 Latest Raw Telemetry")
                st.sidebar.json(st.session_state.last_metrics)

            time.sleep(SLEEP_STEP)

    except Exception as e:
        err_entry = f"❌ [{datetime.now().isoformat()}] ERROR | instance={st.session_state.instance_id} | {str(e)}"
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