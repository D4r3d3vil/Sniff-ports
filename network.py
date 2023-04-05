import urllib.request
ip = input("server: ")
start_scan = int(input("start scan at: "))
stop_scan = int(input("stop scan at: "))
if start_scan < 1024:
    print("starting at 1024 since rest are used.")
    start_scan = 1024
if stop_scan > 65535:
    print("stopping at 65535 since its the maximum.")
    stop_scan = 65535
open_ports = []
for port in range(start_scan, stop_scan+1):
    print(port)
    try:
        urllib.request.urlopen('http://' + ip + ":" + str(port))
        open_ports.append(port)
        print("\ndetected " + str(port) + " added to array")
    except:
        pass
print("\nDone!\n\nopen ports:\n", open_ports, "\n")