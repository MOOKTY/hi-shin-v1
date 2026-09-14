import os
import platform
import psutil
from pathlib import Path
import socket
#----------------------------------
def Get_System_Information():
    while True:
        print("select number : ")
        print("0-exit:")
        print("1-system:")
        print("2-release:")
        print("3-version:")
        print("4-Every things:")
        try:
            select  = int(input())
        except ValueError:
            print("plz just number input: ")
            continue
        if select  == 0:
            break
        elif select  == 1:
            print(platform.system())
        elif select == 2:
            print(platform.release())
        elif select == 3:
            print(platform.version())
        elif select == 4:
            print(platform.system())
            print(platform.release())
            print(platform.version())
        else:
            print("select correct  number : ")
#----------------------------------
def osmodule():
    while True:
        print("select number :")
        print("0- exit : ")
        print("1- Display all file in my dir : ")
        print("2- file detals : ")
        print("3- FileExists : ")
        print("4- Check Running Processes : ")
        print("5- get my pwd : ")
        try:
            select = int(input())
        except ValueError:
            print("plz just number input: ")
            continue
        if select == 0:
            break
        elif select == 1:
            lisdir()
        elif select == 2:
            filedet()
        elif select == 3:
            FileExists()
        elif select == 4:
            Check_Running_Processes()
        elif select == 5:
            print(os.getcwd())
        else:
            print("select correct number : ")
#----------------------------------
def filedet():
    fileN = input("Enter File Name : ")
    try:
        info = os.stat(fileN)
        print(info.st_size, "bytes")
        print(info.st_mtime)
    except FileNotFoundError:
        print("plz write correct Name: ")
#----------------------------------
def FileExists():
    fileEx = input("Enter File Name : ")
    file_exists = Path(fileEx)
    if file_exists.exists():
        print("file exists")
    else:
        print("No File")
#----------------------------------
def lisdir():
    files = os.listdir(".")
    print(files)
#----------------------------------
def Check_Running_Processes():
    for process in psutil.process_iter(['pid', 'name', 'username']):
        print(process.info)
#----------------------------------
def FileAna():
    ipf = {}
    fileNmae=input("Enter file name: ")
    try:
        with open(fileNmae, "r") as file:
            for i in file:
                if "login_failed" in i:
                    try:
                        fileddip = i.split()[3].split("=")[1]
                    #------------------
                        if fileddip in ipf:
                             ipf[fileddip] += 1
                        else:
                            ipf[fileddip] = 1
                    except (IndexError, ValueError):
                        continue
                    # ------------------
    except FileNotFoundError:
        print("File not found")
        return
    except PermissionError:
        print("Permission denied")
        return
    for ip, FN in ipf.items():
        if FN >= 3:
            print("the SUS ip = ", ip)
#----------------------------------
def getDomin():
    dominin=input("Enter Domin : ")
    try:
        add=socket.gethostbyname_ex(dominin)
        print(add)
    except socket.gaierror:
        print("Invalid domain or DNS error")
#----------------------------------
def gethostbyaddr():
    ipin = input("Enter IP : ")
    try:
        ip=socket.gethostbyaddr(ipin)
        print(ip)
    except socket.herror:
        print("No reverse DNS found for this IP")
    except socket.gaierror:
        print("Invalid IP address")
#----------------------------------
def getservbyport():
    try:
        portin = int(input("Enter Port : "))
    except ValueError:
            print("Enter a valid number")
            return
    try:
        port=socket.getservbyport(portin,'tcp')
        print(port)
    except OSError:
        print("Unknown port")
#----------------------------------
def scanport():
    while True:
        print("0- Exit ")
        print("1- Famas ports: ")
        print("2- Custom range: ")
        try:
            select=int(input("select one: "))
        except ValueError:
            print("plz just number input: ")
            continue
        if select ==0:
            break
        elif select == 1:
            famasport()
        elif select ==2:
            castemport()
        else:
            print("woorng")
#----------------------------------
def famasport():
    target = input("Enter target: ")
    port={
        "FTP":21,
        "SSH":22,
        "DNS":53,
        "HTTP":80,
        "HTTPS":443,
        "HTTP-ALT":8080,
        "HTTP-ALT 1": 8180,
        "SMB":445,
        "SMTP":25
    }
    for name, number in port.items():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, number))
                if result == 0:
                    print(f"{name} (port {number}) is open")
        except socket.error:
            print(f"Error: {number}")
#----------------------------------
def castemport():
    target = input("Enter target: ")
    start = int(input("Enter Start Port"))
    end = int(input("Enter End Port"))
    for port in range(start, end + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("port" + str(port) + "is open")
            s.close()
        except socket.error:
            print("Error occurred")
#----------------------------------
def active_connections():
    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        if conn.laddr:
            local_addr = str(conn.laddr.ip) + ":" + str(conn.laddr.port)
        else:
            local_addr = "N/A"

        if conn.raddr:
            remote_addr = str(conn.raddr.ip) + ":" + str(conn.raddr.port)
        else:
            remote_addr = "N/A"
        print(f"Local Address : {local_addr}")
        print(f"Remote Address: {remote_addr}")
        print(f"Status        : {conn.status}")
        print(f"PID           : {conn.pid}")
        print("-" * 40)
#----------------------------------
def network_menu():
    while True:
        print("select number :")
        print("0- exit : ")
        print("1- get domain : ")
        print("2- reverse DNS : ")
        print("3- get service by port : ")
        print("4- scan ports : ")
        try:
            select = int(input())
        except ValueError:
            print("plz just number input: ")
            continue
        if select == 0:
            break
        elif select == 1:
            getDomin()
        elif select == 2:
            gethostbyaddr()
        elif select == 3:
            getservbyport()
        elif select == 4:
            scanport()
        else:
            print("select correct number : ")
def main_menu():
    while True:
        print("===== Main Menu =====")
        print("1- System Information")
        print("2- OS Module")
        print("3- Network Tools")
        print("4- File Analyzer")
        print("5- Active Connections")
        print("0- Exit")
        try:
            select = int(input("Select: "))
        except ValueError:
            print("plz just number input: ")
            continue
        if select == 0:
            print("Bye")
            break
        elif select == 1:
            Get_System_Information()
        elif select == 2:
            osmodule()
        elif select == 3:
            network_menu()
        elif select == 4:
            FileAna()
        elif select == 5:
            active_connections()
        else:
            print("select correct number : ")


if __name__ == "__main__":
    main_menu()
