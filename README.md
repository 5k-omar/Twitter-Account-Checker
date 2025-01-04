# **Twitter Account Checker**

  [![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://opensource.org/licenses/MIT)
  <p align="center"> <img src="https://komarev.com/ghpvc/?username=5k-omar&label=Repo%20views&color=0e75b6&style=flat" alt="Repo Views" /> </p>

  **My Discord Server**: [Join Here](https://discord.gg/tcnksFMCR9)

  **My Discord Open Src Server (Soon)**: [Join Here](https://discord.gg/323wKvBb45)

  A powerful and user-friendly tool to check Twitter account credentials (username and password) either from a file or as a single input. This tool is designed to help you validate accounts efficiently and save the results for further analysis.

  ---

  ## 🌟 **Features**

  - **Bulk Checking**: Check multiple accounts from a file (format: `username:password`).
  - **Single Account Check**: Input a single username and password for validation.
  - **Detailed Results**:
    - Separate lists for **Worked** and **Unworked** accounts.
    - Save results to `Worked.txt`, `Unworked.txt`, and a detailed `results.json` file.
  - **Error Handling**:
    - Detects invalid usernames, wrong passwords, and other errors.
    - Provides clear error messages for failed accounts.
  - **Save Results**:
    - Optionally save results to files for later use.

  ---

  ## 📦 **Installation**

  1. Clone the repository:
     ```bash
     git clone https://github.com/5k-omar/Twitter-Account-Checker.git
     cd Twitter-Account-Checker
     ```

  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

  3. Run the script:
     ```bash
     python twitter_checker.py
     ```

  ---

  ## 🚀 **Usage**

  ### **Option 1: Check Credentials from a File**
  1. Prepare a file containing Twitter account credentials in the following format:
     ```
     username1:password1
     username2:password2
     username3:password3
     ```

  2. Run the script:
     ```bash
     python twitter_checker.py
     ```

  3. Choose **Option 1** and provide the path to your credentials file when prompted.

  ### **Option 2: Check a Single Account**
  1. Run the script:
     ```bash
     python twitter_checker.py
     ```

  2. Choose **Option 2** and enter the **username** and **password** when prompted.
Last updated: 2025-01-04 02:59:14
