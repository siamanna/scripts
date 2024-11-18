# Instagram Story Viewer Checker

This Python bot checks if a specific Instagram user has viewed your story. It automates the process using Selenium, allowing you to avoid manually searching for a particular user in the story viewers list.

# Features

Logs into Instagram automatically.
Opens your story and checks if the specified user has viewed it.
Notifies you if the user has or hasn't seen your story.

# Prerequisites

1. Python (3.6 or higher) - Download and install Python from python.org.
2. Selenium (Python library) - Install Selenium via pip:

```bash
pip install selenium
```

3. Chrome Browser - Ensure you have Google Chrome installed.
4. ChromeDriver -

Download the version of ChromeDriver matching your Chrome version from chromedriver.chromium.org.
Add the ChromeDriver executable to your system's PATH or place it in the project directory.

5. Instagram Account - Use a secondary/disposable Instagram account to avoid risking your primary account.

# Setup

1. Clone or download the project files to your local machine.

2. Create a file named igloginfo.py in the same directory as igstoryviewer.py, and add your Instagram login credentials:

```python

# igloginfo.py
username = 'your_instagram_username'
pw = 'your_instagram_password'

```

3. Verify that ChromeDriver is correctly installed and accessible.

# How to Run

1. Open a terminal and navigate to the project directory:

```bash
cd /path/to/the/project
```
2. Run the script with the target username as an argument:

```bash
python igstoryviewer.py <target_username>
```

Replace <target_username> with the Instagram username of the person you want to check.

3. The bot will:

Open Chrome,
Log in to your Instagram account,
Open your active story,
Scroll through the viewer list,
Notify you in the terminal if the target user has seen your story.

# Notes

Legal and Ethical Disclaimer:

Automating Instagram actions violates Instagram’s terms of service. Use this script responsibly.
Avoid running this script frequently to prevent your account from being flagged or banned.

# Troubleshooting:

If the script fails to locate elements, ensure that your Chrome and ChromeDriver versions match.
Slow internet connections may require you to increase the timeout values in the script.

# Improvements:

You can enhance the script to handle multiple target usernames or provide a graphical user interface.

# License

This project is for educational purposes only. The author assumes no responsibility for any misuse of the code.

