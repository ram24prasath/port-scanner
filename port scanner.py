import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime  #import datetime for timestamp of the port scanning.
import subprocess #import subprocess for running nmap.

#Function that retrives the service running for a given port.
def get_service(port):
    try:
        return socket.getservbyport(port)    #Lookup service by port number.
    except OSError:
        return "Unknown Service"             #If service not found, return unknown service.

#Check if the port is open or closed.
def check_connection(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Create a TCP socket.
    sock.settimeout(2)                                         #set timeout for conenction attempt.
    
    status = "unknown"
    service = "unknown service"
    try:
        result = sock.connect_ex((target, port))               #try connecting to the target on the given port.

        if result == 0:
            service = get_service(port)
            status = "open"
            print(f"[+] Port {port} is Open ({service})")
        else:
            status = "closed"
            print(f"[-] Port {port} is Closed")
        
        #log scan results to a file.
        log_results(target,port,status,service)

    except socket.timeout:
        print(f"Connection to {target} on port {port} timed out.")
    
    except socket.gaierror:
        print(f"Hostname {target} could not be resolved. Please check domain name or IP address ")
    
    except socket.error as err:
        print(f"Error connection to {target} on port {port}: {err}")    
    
    finally:
        sock.close()

#Function to log scan results to a file, captures timestamp, status, service.
def log_results(target, port, status, service):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("scan_"
    "results.txt", "a") as f:
        f.write(f"[{timestamp:}]{target}:{port} - {status} ({service})\n")

#def scan_port_thread(target, port):
#    thread = threading.Thread(target=check_connection, args=(target, port))
#    thread.start()
#    return thread

#function to run nmap as a subprocess
def nmap_scan(target):
    print("\nRunning nmap scan...")
    try:
        nmap_result = subprocess.run(["nmap","-sV", target], capture_output=True, text=True)
        nmap_output = nmap_result.stdout

        print(nmap_output)
        #Save nmap results to a file.
        with open("nmap_results.txt","w") as file:
            file.write(f"Nmap scan results for {target}:\n\n{nmap_output}")
        
        print("\nNmap scan completed! Results saved in nmap_results.txt")
    
    except FileNotFoundError:
        print("[!] nmap is not installed. please install nmap and try again.")

#Main function to handle user inputs and run port scan.
if __name__ == "__main__":
    target = input("Enter the target website IP/ Domain you wish to scan: ").strip()
    scan_mode = input("Do you want scan a single port or multiple ports, please enter (single/multiple): ").strip().lower()
    
    #Single port scan mode
    if scan_mode == "single":
        port = int(input("Enter the port number to scan: "))
        check_connection(target, port)

        # Ask the user if they want to run an Nmap scan
        run_nmap = input("\n Would you like to run nmap for detailed scan? (yes/no): ").strip().lower()
        if run_nmap == "yes":
            nmap_scan(target)
    elif scan_mode == "multiple": 
        start_port = int(input("Enter the starting port number to scan: "))
        fin_port = int(input("Enter the end port number to scan: "))
    
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(check_connection, [target] * (fin_port - start_port +1), range(start_port, fin_port + 1))
        #for port in range (start_port, fin_port +1):
        #   scan_port_thread(target, port)

        run_nmap = input("\n Would you like to run nmap for detailed scan? (yes/no): ").strip().lower()
        if run_nmap == "yes":
            nmap_scan(target)

    else:
        print("please enter valid scan mode (single/multiple).")
