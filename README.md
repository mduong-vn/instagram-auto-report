# instagram-auto-report
#### dev by: duong
#### date: 2025-06-17
#### x (twitter) version: coming soon :d

### description
this script automatically logs into instagram accounts and reports specific accounts from a list.

### files
- login_report.py → main script
- login.txt → list of instagram accounts (username and password)
- report.txt → list of instagram profile links to report

### how to use
1. **install python**
- download from: https://www.python.org/downloads/
- run the .exe file and check "add to path"
- verify installation:
  - open command prompt as administrator
  - type `python --version` and press enter

2. **install selenium**
- open command prompt as administrator
- install with: `pip install selenium` (recommended: `pip install selenium==4.2.0` for compatibility with this script)
- verify installation:
  - type `pip show selenium` and check the version

3. **set up chromedriver**
- **option 1: manual setup**
  - download chromedriver matching your chrome version from: https://googlechromelabs.github.io/chrome-for-testing/
  - extract zip to a folder
  - add to system path:
    - search "environment variables" on your pc
    - click "edit the system environment variables"
    - click "environment variables"
    - find "path" under system variables, click "edit"
    - add the folder path containing `chromedriver.exe`
    - click ok to save
- **option 2: automatic setup (easier)**
  - install `webdriver-manager`: `pip install webdriver-manager`
  - the script will automatically download the correct chromedriver if this package is installed (no manual path setup needed)

4. **prepare login.txt**
- write username on one line, password on the next line
- example:
  username1
  password1
  username2
  password2
  ...

5. **prepare report.txt**
- list the instagram profile links to report, one per line
- example:
  https://www.instagram.com/target1
	https://www.instagram.com/target2
  ...

6. **run the script**
- open command prompt
- navigate to the folder: `cd path\to\folder` (e.g., `cd c:\user\documents\code\instagramreporter`)
- run: `python login_report.py`

### notes
- each account runs in a separate thread with its own chrome browser window.
- ensure chrome is installed and updated.
- using `webdriver-manager` eliminates the need for manual chromedriver setup.
- automated reporting may violate instagram's terms of service—use cautiously to avoid account bans.
- high resource usage is possible with multiple threads; monitor your system.
- if errors occur (e.g., "chromedriver not found"), verify chromedriver version or install `webdriver-manager`.
