# 🔐 CrackSuite – Password Cracking & Audit Framework

CrackSuite is a Python-based, modular password auditing and cracking tool for cybersecurity researchers and enthusiasts. It supports hash-type detection, dictionary-based cracking, cracked password analysis, color-coded CLI output, auto-generated reports, and a web-based GUI built with Flask.

---

## 🚀 Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🔍 Hash Type Detection           | Automatically identifies MD5, SHA1, SHA256, and bcrypt formats              |
| 🧠 Dictionary-Based Cracking     | Uses wordlists like `rockyou.txt` to find matching passwords                |
| 📊 Password Strength Analysis    | Generates average length, longest, and weakest cracked passwords            |
| 📄 Auto Report Generation        | Saves results in organized `.txt` reports                                   |
| 🌈 Colorized CLI Output          | Green/Red display for cracked or not-found hashes                           |
| 🌐 Web GUI (Flask)               | Clean and fast interface for testing hashes via a browser                   |
| 🔌 Modular Code Design           | Easy to extend with your own crackers or hash analyzers                     |

---

## 📸 Screenshots

### 🖥️ Terminal Interface
![CLI Output](https://fakeimg.pl/600x180/282c34/61dafb/?text=CrackSuite+CLI&font=lobster)


[ WE STILL HAVE TO DO SOME WORK ON THE WEB GUI  DESIGN OF THE PROJECT WHEN TESTED ON THE KALI FIREFOX BROWSER. ]

### 🌐 Web GUI
![Web GUI](https://fakeimg.pl/600x180/282c34/fbfbfb/?text=Flask+Web+Interface&font=lobster)

---

## 🔧 Installation & Setup

### 🐍 1. Clone the repository
```bash
git clone https://github.com/yourusername/CrackSuite.git
cd CrackSuite




python3 -m venv venv
source venv/bin/activate


CrackSuite/
├── main.py                 # Main CLI interface
├── web_app.py              # Flask GUI app
├── samples/hashes.txt      # Input hash list
├── wordlists/rockyou.txt   # Dictionary file
├── reports/report.txt      # Auto-generated report
├── modules/
│   ├── cracker.py
│   ├── hash_detector.py
│   └── report_writer.py
└── README.md               # This file





python3 main.py
command to run CLI for viewing the CrackSuite 

python3 web_app.py
command to run the web GUI at localhost : http://127.0.0.1:5000

SAMPLE OUTPUT:-> 
+----------------------------------+-------------------------+
| Hash                             | Status                  |
+----------------------------------+-------------------------+
| 5f4dcc3b5aa765d61d8327deb882cf99 | ✅ Cracked: password     |
| 098f6bcd4621d373cade4e832627b4f6 | ✅ Cracked: test         |
| ab56b4d92b40713acc5af89985d4b786 | ❌ Not Found             |
+----------------------------------+-------------------------+




📁 WORDLISTS:
You can use any dictionary file:

Default: wordlists/rockyou.txt

Replace it or extend with your own

For large wordlists: use hashcat rules or Crunch patterns (future module)




🚧 ROADMAP:
 Add brute-force and hybrid attack modules

 Support NTLM, SHA-512, and custom salts

 Add export to CSV/HTML reports

 Password reuse and duplicate detection

 Docker container support

 Integration with Shodan/HaveIBeenPwned APIs
 
 
 

🧠 LEARNINGS / CONCEPTS COVERED:
Python file handling and hash operations

Dictionary attacks and basic cryptanalysis

Modular Python architecture (importable tools)

Virtual environments and pip packaging

Flask app routing, forms, and templating

Report generation and output formatting




📚 RESOURCES USED:
Kali Linux

RockYou Wordlist

Python Docs

Flask Framework

OWASP Top 10



⚠️ DISCLAIMER:
CrackSuite is intended only for educational and ethical purposes. Do NOT use this tool on real systems, networks, or data without explicit permission. Misuse can be illegal.



🧑‍💻 AUTHOR:
Mohit Nigote
CyberSec & Linux Enthusiast
📧 - mohitnigote461001@gmail.com (use real if public)
💻 GitHub:- ngmohit2003.
x-x 
MN.

