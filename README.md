# simple-port-scanner

Who: Created by you, as your first official project for the "Level 2: Applied Python & Security Tooling" roadmap.

What: A custom, automated TCP Port Scanner with banner-grabbing capabilities. It takes a target domain or IP address, scans a specified range of ports, and reports back which ones are open.

When: February 26, 2026.

Where: Built in VS Code. It is capable of scanning local networks (127.0.0.1) or external remote servers across the internet (like scanme.nmap.org).

Why: To automate the initial reconnaissance (information gathering) phase of a security assessment. Instead of manually checking network doors, this script finds the open ports and extracts the "Service Banner" to reveal exactly what software and operating system the target is running.

How: It uses Python's built-in socket library to establish IPv4 TCP connections (AF_INET, SOCK_STREAM). It loops through a given range of ports, uses connect_ex() to check for an open connection, and uses .recv(1024) to listen for and decode the server's welcome banner. The entire process is wrapped in try/except blocks so the script handles timeouts and closed ports gracefully without crashing.
