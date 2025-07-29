import hashlib
import json
import os
from pathlib import Path

class FileScanner:
    def __init__(self, signatures_file=None):
        self.signatures_file = signatures_file or str(
            Path(__file__).parent.parent / 'rules' / 'signatures.json'
        )
        self.malware_signatures = self._load_signatures()
        
    def _load_signatures(self):
        """Load malware signatures from JSON file"""
        try:
            with open(self.signatures_file) as f:
                signatures = json.load(f)
                # Convert all hashes to lowercase for case-insensitive matching
                signatures["md5"] = [h.lower() for h in signatures.get("md5", [])]
                signatures["sha256"] = [h.lower() for h in signatures.get("sha256", [])]
                return signatures
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load signatures - {str(e)}")
            return {"md5": [], "sha256": []}
    
    def get_file_hash(self, file_path, hash_type="md5"):
        """Calculate file hash (MD5 or SHA256)"""
        hasher = hashlib.md5() if hash_type == "md5" else hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest().lower()  # Return lowercase for consistency
        except Exception as e:
            print(f"Error calculating hash: {str(e)}")
            return None
    
    def scan_file(self, file_path):
        """Scan a file for malware signatures"""
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            return False, None

        try:
            # Check MD5 first
            md5_hash = self.get_file_hash(file_path, "md5")
            if md5_hash and md5_hash in self.malware_signatures["md5"]:
                return True, md5_hash
            
            # Fallback to SHA256
            sha256_hash = self.get_file_hash(file_path, "sha256")
            if sha256_hash and sha256_hash in self.malware_signatures["sha256"]:
                return True, sha256_hash
            
            return False, None
        except Exception as e:
            print(f"Scan error: {str(e)}")
            return False, None

# Example test code (can be removed in production)
if __name__ == "__main__":
    scanner = FileScanner()
    test_file = "eicar.com.txt"
    is_malicious, file_hash = scanner.scan_file(test_file)
    print(f"Scan result for {test_file}:")
    print(f"Malicious: {is_malicious}")
    print(f"Hash: {file_hash}")
