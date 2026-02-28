# PyThreadedScanner 🔍

A fast, concurrent TCP port scanner built in Python. This tool leverages multi-threading and queues to rapidly scan target IP addresses for open ports and attempts basic banner grabbing to identify running services.

## ✨ Features
* **High-Speed Scanning**: Utilizes Python's `threading` and `queue` modules to spawn 100 concurrent worker threads, drastically reducing scan times compared to sequential scanners.
* **Banner Grabbing**: Actively listens on open ports to capture and display service banners (e.g., SSH, HTTP server details) for immediate reconnaissance.
* **Timeout Handling**: Uses `socket.settimeout()` to prevent the scanner from hanging on unresponsive ports or filtered connections.

## ⚙️ Prerequisites
* Python 3.x (Built using entirely standard libraries, no `pip install` required)

## 🚀 How to Run

1. Open `port_scanner.py` and modify the `target_domain` variable to your authorized testing target (defaults to `scanme.nmap.org`).
2. Run the script in your terminal:
   ```bash
   python port_scanner.py
