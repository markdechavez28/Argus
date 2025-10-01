Argus Agent Monitoring

Requirements:

1. Python 3.9
2. Prometheus
3. Windows PowerShell

Setup Instructions:

1. Run Argus Agent (VS Terminal)
   python Agent/argus_agent.py
   Note: It should run at http://localhost:8000/metrics
2. Run Prometheus (PowerShell)  
   .\prometheus.exe --config.file=prometheus.yml
   Note: It should run at: http://localhost:9090

P.S. Updated on Sep 30
