import pandas as pd
import re

def analyze_csv(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)
    
    attacker_ip = "NULL"
    sql_injection_attempts = []

    # Regular expression to detect SQL injection patterns
    sql_injection_patterns = [
        r"\bUNION\b", r"\bSELECT\b", r"\bINSERT\b", r"\bDELETE\b", r"\bUPDATE\b", r"\bDROP\b", r"\bOR\b.*=", r"\bAND\b.*=", r"\b--\b", r";", r"'"
        ]

    for index, row in data.iterrows():
        info = row['Info']

        # Check if the packet contains SQL injection patterns
        if any(re.search(pattern, info, re.IGNORECASE) for pattern in sql_injection_patterns):
            sql_injection_attempts.append(row)

    if sql_injection_attempts:
        # Extract the attacker's IP address (source IP of the first attempt)
        attacker_ip = sql_injection_attempts[0]['Source']

        # Extract the first and last payload URIs
        first_payload = extract_uri(sql_injection_attempts[0]['Info'])
        last_payload = extract_uri(sql_injection_attempts[-1]['Info'])
    else:
        first_payload = "NULL"
        last_payload = "NULL"

    # Output results
    print(f"Attacker IP: {attacker_ip}")
    print(f"Number of SQLi Attempts: {len(sql_injection_attempts)}")
    print(f"First Payload: {first_payload}")
    print(f"Last Payload: {last_payload}")

def extract_uri(info):
    # Extract URI from the Info column (Assuming it's in the format "GET /path?query HTTP/1.1")
    match = re.search(r"(?:GET|POST)\s+(.*?)\s+HTTP/", str(info))
    return match.group(1) if match else "NULL"
    
analyze_csv('test/file1.csv')