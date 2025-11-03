# 🚀 GlobalExam Endless - Fast Mode

> **Language:** [🇬🇧 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

<div align="center">

![GlobalExam Endless](assets/5endless_logo.png)

**Ultra-fast automation for GlobalExam Activity 7 (Business > Building)**

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/)

**Fast Mode • No Pauses • Continuous Cycles**

</div>

---

## 🎯 What is GlobalExam Endless?

**GlobalExam Endless** is a professional GUI automation tool for GlobalExam Activity 7. It runs continuously without breaks, making it perfect for quick completions.

### ✨ Key Features

- ⚡ **Ultra-Fast Mode** - No pauses between cycles
- 🎨 **Beautiful GUI** - Modern dark theme with purple accents
- 📊 **Real-Time Statistics** - Track cycles and progress
- 🔐 **Password Protection** - Secure first-run authentication
- 📐 **Auto-Resolution Scaling** - Works on any screen size
- 🔍 **Browser Zoom Normalization** - Automatic 100% zoom reset
- 📝 **Live Activity Log** - See what's happening in real-time

---

## 📦 Installation

### Quick Start

1. **Clone or download** this repository
2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```powershell
   python 5endless_final_GUI.py
   ```

### Requirements

- **OS:** Windows 10/11
- **Python:** 3.13+ (or any Python 3.x)
- **Browser:** Chrome/Firefox at 100% zoom
- **Screen:** Any resolution (auto-adapts)

---

## 🚀 Usage

### Running the Application

```powershell
python 5endless_final_GUI.py
```

### First Launch

On first run, you'll be prompted for an access code:
- Enter the code when prompted (input is hidden)
- A `.first_run_ok` file is created after authentication
- You won't be asked again unless you delete this file

### Using the App

1. Open GlobalExam Activity 7 in your browser
2. Click **DÉMARRER** in the app
3. The app will:
   - Detect your screen resolution
   - Normalize browser zoom to 100%
   - Start continuous automation
4. Click **ARRÊTER** to stop anytime

---

## 📊 Features Overview

| Feature | Description |
|---------|-------------|
| **Continuous Mode** | Runs indefinitely without pauses |
| **Cycle Counter** | Tracks completed cycles |
| **Progress Bar** | Visual progress through questions |
| **Activity Log** | Timestamped event logging |
| **Error Handling** | Graceful error recovery |
| **Resolution Scaling** | Works on 1366x768 to 4K screens |

---

## 📂 Project Structure

```
GlobalExam_Endless/
├── 5endless_final_GUI.py    # Main application
├── final_test.py             # Helper functions
├── PNJ/                      # Image templates for recognition
├── assets/                   # Logos and icons
│   ├── 5endless_logo.png
│   └── 5endless_logo.ico
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── LICENSE                   # License file
└── README.md                 # This file
```

---

## ⚙️ Configuration

### Auto-Resolution Scaling

The app automatically scales coordinates based on a 1920x1080 baseline:
- Detects your current resolution
- Adjusts all click positions proportionally
- No manual configuration needed

### Browser Zoom

On startup, the app automatically:
- Presses `Ctrl+0` three times
- Ensures browser is at 100% zoom
- Prevents clicking misalignment

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Questions skipped** | Ensure browser zoom is at 100% |
| **Clicks miss targets** | Verify resolution scaling is working |
| **App won't start** | Check Python 3.13+ is installed |
| **Images not found** | Ensure PNJ folder exists with all .png files |

---

## ⚠️ Important Notes

- ✅ **Target Activity:** GlobalExam Activity 7 (Business > Building) only
- ✅ **Browser Zoom:** Must be at 100% (auto-normalized on start)
- ✅ **Screen Resolution:** Any resolution supported
- ⚠️ **Do not change zoom or resolution** during execution

---

## 📝 License

This project is provided for personal/educational automation purposes. Please respect the platform's terms of service.

---

<div align="center">

**Made with ❤️ for GlobalExam automation**

🚀 **GlobalExam Endless** - Fast Mode

</div>
