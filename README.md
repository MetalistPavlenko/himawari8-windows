### **Description:**
#### **Sets a snapshot of the Earth to the desktop and lock screen.**

---

### **Support:**
#### **Only windows supported.**
#### **Tested on Windows 10 21H1 with Python 3.9x.**

---

### **Dependencies for work:**
```cmd
python -m pip install -U requests Pillow
```

---

### **Compilation:**
##### **Download:**
```cmd
curl -sSLO https://raw.githubusercontent.com/MetalistPavlenko/himawari8-windows/main/main.py
curl -sSLO https://raw.githubusercontent.com/MetalistPavlenko/himawari8-windows/main/icon.ico
```

---

#### **Compile with PyInstaller:**
##### **Dependency for compilation:**
```cmd
python -m pip install -U pyinstaller
```

##### **Compile:**
```cmd
python -m PyInstaller --onefile --noconsole --icon icon.ico main.py
```

---

#### **Compile with Nuitka:**
##### **Dependencies for compilation:**
```cmd
python -m pip install -U nuitka zstandard
```

##### **Compile:**
```cmd
python -m nuitka --mingw64 --remove-output --follow-imports --onefile --windows-disable-console --windows-icon-from-ico=icon.ico main.py
```

---

#### **Fix error some settings are managed by your organization:**
```cmd
REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" /v LockScreenImagePath /f
```