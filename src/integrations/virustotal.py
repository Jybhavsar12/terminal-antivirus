import requests
import os
from pathlib import Path

class VirusTotalClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('VT_API_KEY')
        self.base_url = "https://www.virustotal.com/api/v3"
    
    def scan_file(self, file_path):
        if not self.api_key:
            raise ValueError("VirusTotal API key not configured")
            
        url = f"{self.base_url}/files"
        headers = {"x-apikey": self.api_key}
        
        try:
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f)}
                response = requests.post(url, headers=headers, files=files)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"VirusTotal scan failed: {str(e)}")
            return None
