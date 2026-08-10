# 🛡️ GlexGC | Security Toolkit

<p align="center">
  <b>An all-in-one GUI-based penetration testing and cybersecurity utility tool.</b><br>
  <i>Designed for beginners, students, and security enthusiasts.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-000000?style=flat-square&logo=gtk&logoColor=white" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/OS-Windows%2011-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/Version-1.0-success?style=flat-square" alt="Version">
</p>

---

## 📖 About the Project

**GlexGC** is a comprehensive dashboard that bundles essential network, cryptography, and web security tools into a modern user interface. It was designed to make complex terminal commands visually and easily accessible for beginners without requiring deep programming knowledge to operate the tools. I created it a few years ago once i started in Cybersecurity, So dont blame me if the Tool is bad.  Thanks.

> [!TIP]
> **Compatibility:** The tool is primarily optimized for **Windows 11**.

---

## ⚠️ Important Disclaimer

> [!CAUTION]
> **FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY!**
> This tool was developed to promote the understanding of networks and security. The developer (**Glitch**) assumes **no liability** for misuse, damages, or illegal activities conducted with this software. Scanning or attacking systems without explicit, written permission is a criminal offense. **Always act legally and ethically!**
> ⚠️ Use only against systems you own or have explicit permission to test.

---

## ✨ Features

### 🛜 1. Network Tools
Tools for analyzing networks, ports, and domains.
*   **Port Scanner:** Multi-threaded TCP scan (Ports 0-1024) with start/stop capabilities.
*   **Ping Test:** Quick host reachability testing via native ICMP requests.
*   **DNS Lookup:** Resolves domain names to their corresponding IPv4 addresses.
*   **Reverse DNS Lookup:** Identifies hostnames and aliases associated with a specific IP.
*   **WHOIS Lookup:** Retrieves domain registration and ownership data.
*   **Dirb Discovery:** Brute-force search for hidden web directories and files (requires `dirb.txt`).

### 📍 2. IP Tools
Analysis and tracking of IP addresses.
*   **IP Geolocation:** Tracks the physical location, ISP, and timezone of a target IP via `ip-api.com`.
*   **Public IP Fetcher:** Instantly displays your own external public IP address.

### 🔐 3. Cryptography Tools
Tools for encryption, hashing, and password generation.
*   **File Encryption/Decryption:** Securely encrypts and decrypts files using Fernet symmetric encryption.
*   **Text Hashing:** Generates hashes (MD5, SHA-1, SHA-256, SHA-384, SHA-512) for text strings.
*   **Password Generator:** Creates strong, randomized 20-character passwords with alphanumeric and symbolic characters.

### 🌐 4. Web Security
Automated vulnerability scanning in web applications.
*   **Automated Web Fuzzer:** Tests target URLs against built-in payloads on common GET parameters for:
    *   Cross-Site Scripting (XSS)
    *   SQL Injection (SQLi)
    *   Local File Inclusion (LFI)
    *   Remote Code Execution (RCE) vectors

---

## 🛠️ Tech Stack & Dependencies

| Category | Technology / Library | Purpose in Project |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core logic and scripting |
| **GUI** | `customtkinter` | Modern, dark-themed user interface |
| **Networking** | `requests`, `socket` | HTTP requests, port scanning, DNS resolution |
| **Security** | `cryptography` | Fernet encryption for file handling |
| **Data** | `python-whois` | WHOIS queries for domain analysis |
| **System** | `subprocess`, `platform` | Ping tests, OS information gathering |

---

## 🚀 Installation & Getting Started

### 1. Prerequisites
Ensure that **Python (version 3.8 or higher)** is installed on your system and added to your system PATH.

### 2. Clone the Repository
```bash
git clone https://github.com/glitch-402/First-CyberSecurity-project
cd First-CyberSecurity-project
