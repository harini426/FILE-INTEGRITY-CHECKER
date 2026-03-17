# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS
**NAME**: S. HARINI
**INTERN ID**: CTIS6595
**DOMAIN**: CYBER SECURITY & ETHICAL HACKING
**DURATION**: 4 WEEKS
**MENTOR**: NEELA SANTHOSH

---

## 📌 Introduction
During my Cybersecurity internship at **CodTech IT Solutions**, I developed a robust **File Integrity Checker** using Python. In the digital world, ensuring that data remains unchanged from its original state is a critical challenge. This project addresses that by using cryptographic hashing to verify whether a file has been tampered with or corrupted.

## 🛡️ Core Concept: Data Integrity
Data Integrity is one of the three pillars of the **CIA Triad** (Confidentiality, Integrity, and Availability). My tool acts as a "watchdog" for files, providing a way to detect unauthorized modifications immediately.

## ⚙️ Technical Deep Dive
The project is built on the **SHA-256 (Secure Hash Algorithm 256-bit)**. 
- **Unique Fingerprint**: Every file has a unique hash. Even a single bit change (like adding a space or a full stop) results in a completely different hash.
- **Irreversibility**: You cannot recreate the original file from the hash, making it a secure way to store "identity."

## 🛠️ Development Stack & Tools
- **Python 3.12.6**: Core programming language.
- **Visual Studio Code (VS Code)**: Primary IDE.
- **Command Prompt (CMD)**: For executing scripts.
- **Hashlib Library**: Built-in Python module for SHA-256 algorithm.

## 🚀 Workflow Involved
1. **Environment Setup**: Configuring Python path in Windows system.
2. **Scripting**: Writing `checker.py` to read files in binary mode (`rb`).
3. **Baseline Generation**: Running the tool on `sample.txt` to get its original hash.
4. **Verification**: Modifying the file and re-running the tool to detect the hash change.

## 🌍 Real-World Applications
- **Software Security**: Verifying ISO files or software installers.
- **Digital Forensics**: Proving evidence has not been altered.
- **Malware Analysis**: Identifying known virus signatures.
- **Blockchain**: Securing transactions.
-
