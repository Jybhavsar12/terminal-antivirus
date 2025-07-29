# Terminal Antivirus 🛡️

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python-based command line antivirus solution designed for cybersecurity professionals and enthusiasts. This project demonstrates core antivirus capabilities in a terminal environment, perfect for learning and portfolio development.
## Features 

- **Multi-engine scanning**
  - Signature-based detection (MD5/SHA256)
  - YARA rule support
  - Heuristic analysis (basic)
- **Real-time protection**
  - Filesystem monitoring with Watchdog
  - Instant quarantine of threats
- **Threat management**
  - Secure quarantine system with logging
  - VirusTotal API integration (optional)
- **Professional CLI**
  - Clean command line interface
  - Colorful output with emojis
  - Comprehensive help system

## Installation 

### Prerequisites
- Python 3.8+
- pip package manager

### Quick Start
```bash
# Clone the repository
git clone https://github.com/JYbhavsar12/terminal-antivirus.git
cd terminal-antivirus

# Install dependencies
pip install -r requirements.txt

# Run a test scan
python src/cli.py scan /path/to/scan
