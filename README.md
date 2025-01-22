# SQLi Detection

## Project Overview

This project aims to detect SQL injection attempts in captured packets by SIEM tools.  The core functionality is implemented in `main.py`.  The `test/` directory contains unit tests for the project.

## Features

* SQL injection vulnerability detection.
* (Further features would be added here)

## Installation

This project utilizes Python.  To install, please follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HaardikBhagtani/SQLi-Detection
   cd SQLi Detection
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:** 
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the SQLi detection tool, execute the main script:

```bash
python main.py <input_file> 
```


Example usage:
```bash
python main.py input_file.csv
```
