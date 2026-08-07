# 🛡️ GlexGC | Skids Toolkit

<p align="center">
  <b>Ein All-in-One GUI-basiertes Pentesting- und Cybersecurity-Utility-Tool.</b><br>
  <i>Entwickelt für Einsteiger, Studenten und Security-Enthusiasten.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-000000?style=flat-square&logo=gtk&logoColor=white" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/OS-Windows%2011-0078D6?style=flat-square&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/Version-1.0-success?style=flat-square" alt="Version">
</p>

---

## 📖 Über das Projekt

**GlexGC** (auch bekannt als *Skids Toolkit*) ist ein umfassendes Dashboard, das essentielle Netzwerk-, Kryptographie- und Web-Security-Tools in einer modernen Benutzeroberfläche bündelt. Es wurde entwickelt, um komplexe Terminal-Befehle für Einsteiger (in der Szene oft "Skids" genannt) visuell und einfach zugänglich zu machen, ohne dass tiefgreifende Programmierkenntnisse für die Bedienung nötig sind.

> [!TIP]
> **Kompatibilität:** Das Tool ist primär für **Windows 11** optimiert, kann aber mit kleinen Anpassungen (z.B. beim Ping-Befehl) auch auf Linux/macOS ausgeführt werden.

---

## ⚠️ Wichtiger Haftungsausschluss (Disclaimer)

> [!CAUTION]
> **NUR FÜR BILDUNGSZWECKE UND AUTORISIERTE TESTS!**
> Dieses Tool wurde entwickelt, um das Verständnis für Netzwerke und Sicherheit zu fördern. Der Entwickler (**Glitch**) übernimmt **keine Haftung** für Missbrauch, Schäden oder illegale Aktivitäten, die mit dieser Software durchgeführt werden. Das Scannen oder Angreifen von Systemen ohne ausdrückliche, schriftliche Erlaubnis ist strafbar. **Handeln Sie stets legal und ethisch!**

---

## ✨ Funktionsumfang (Features)

### 🛜 1. Netzwerk-Tools (Network Tools)
Werkzeuge zur Analyse von Netzwerken, Ports und Domains.
*   **Port Scanner:** Multithreading TCP-Scan (Ports 0-1024) mit Start/Stop-Funktion.
*   **Ping Test:** Schnelle Erreichbarkeitsprüfung von Hosts via ICMP.
*   **DNS Lookup:** Auflösen von Domainnamen zu IPv4-Adressen.
*   **Reverse DNS Lookup:** Ermittlung von Hostnamen und Aliase für eine gegebene IP.
*   **WHOIS Lookup:** Abrufen von Domain-Registrierungs- und Eigentümerdaten.
*   **Dirb Discovery:** Brute-Force-Suche nach versteckten Web-Verzeichnissen (benötigt `dirb.txt`).

### 📍 2. IP-Tools
Analyse und Tracking von IP-Adressen.
*   **IP Geolocation:** Ortung des physischen Standorts, ISPs und der Zeitzone via `ip-api.com`.
*   **Public IP Fetcher:** Zeigt sofort Ihre eigene externe, öffentliche IP-Adresse an.

### 🔐 3. Kryptographie-Tools (Cryptography)
Werkzeuge für Verschlüsselung, Hashing und Passwortgenerierung.
*   **File Encryption/Decryption:** Sichere Ver- und Entschlüsselung von Dateien mittels Fernet (symmetrische Verschlüsselung).
*   **Text Hashing:** Generierung von Hashes (MD5, SHA-1, SHA-256, SHA-384, SHA-512) für Textstrings.
*   **Password Generator:** Erstellt starke, zufällige 20-Zeichen-Passwörter mit Sonderzeichen.

### 🌐 4. Web-Security
Automatisierte Schwachstellensuche in Webanwendungen.
*   **Automated Web Fuzzer:** Testet Ziel-URLs mit integrierten Payloads gegen häufige GET-Parameter auf:
    *   Cross-Site Scripting (XSS)
    *   SQL Injection (SQLi)
    *   Local File Inclusion (LFI)
    *   Remote Code Execution (RCE) Vektoren

---

## 🛠️ Tech-Stack & Abhängigkeiten

| Kategorie | Technologie / Bibliothek | Zweck im Projekt |
| :--- | :--- | :--- |
| **Sprache** | Python 3.8+ | Kernlogik und Skripting |
| **GUI** | `customtkinter` | Moderne, dunkle Benutzeroberfläche |
| **Netzwerk** | `requests`, `socket` | HTTP-Requests, Port-Scans, DNS |
| **Security** | `cryptography` | Fernet-Verschlüsselung für Dateien |
| **Daten** | `python-whois` | WHOIS-Abfragen für Domains |
| **System** | `subprocess`, `platform` | Ping-Tests, OS-Informationen |

---

## 🚀 Installation & Start (Getting Started)

### 1. Voraussetzungen (Prerequisites)
Stellen Sie sicher, dass **Python (Version 3.8 oder höher)** auf Ihrem System installiert ist und im System-Pfad (PATH) hinterlegt ist.

### 2. Repository klonen
```bash
git clone https://github.com/DEIN-USERNAME/glexgc-toolkit.git
cd glexgc-toolkit
