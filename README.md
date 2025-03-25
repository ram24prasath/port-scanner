# port scanner

# Description
This is simple python based port scanner that allows users to check if specific port on the target IP/Domain is open or closed. It also integrates nmap scanning.

This step is a integral part of penetration testing.

# Features

*  Scan a single port or a range of ports.
*  Retrieve service information running on open ports.
*  Log scan results with timestamps.
*  Option to run an Nmap scan for detailed information.
*  Uses multithreading for faster scanning of multiple ports.

# Requirements

* Python 3.x
* Nmap (optional but recommended for detailed scanning)

# Installation

1. Clone this repository
   ```
   git clone https://github.com/your-username/port-scanner.git
   cd port-scanner
   ```
2. Install required dependencies
   ```
   pip install -r requirements.txt
   ```

# Usage

Run the script using:
  ```
  python port_scanner.py
  ```

# Single Port Scan Mode

  1. Enter the target IP/domain.
  2. Select "single" mode.
  3. Enter the port number to scan.
  4. The script will check if the port is open or closed.
  5. Optionally, run an Nmap scan for more details.

# Multiple port scan mode

  1. Enter the target IP/domain.
  2. Select "multiple" mode.
  3. Enter the start and end port range.
  4. The script will scan all ports in the specified range using multi-threading.
  5. Optionally, run an Nmap scan for more details.

# Logging

  * Scan results are saved in _scan_results.txt_.
  * Nmap scan results are saved in _nmap_results.txt_.

# Notes

  * Ensure Nmap is installed to use the Nmap scanning feature.
  * Run the script with proper permissions to avoid permission errors.

# Contributions

  Pull requests and issue reports are welcome!

Happy scanning! 🚀

