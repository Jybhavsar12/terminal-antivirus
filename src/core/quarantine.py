import os
import shutil
import json
import hashlib
from datetime import datetime
from pathlib import Path

class QuarantineManager:
    def __init__(self, quarantine_dir=None):
        self.quarantine_dir = quarantine_dir or str(
            Path(__file__).parent.parent.parent / 'quarantine'
        )
        os.makedirs(self.quarantine_dir, exist_ok=True)
    
    def quarantine_file(self, file_path):
        if not os.path.exists(file_path):
            return False
        
        try:
            file_hash = self._calculate_hash(file_path)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            orig_path = os.path.abspath(file_path)
            file_name = os.path.basename(file_path)
            
            new_name = f"{timestamp}_{file_hash[:8]}_{file_name}"
            dest_path = os.path.join(self.quarantine_dir, new_name)
            
            shutil.move(file_path, dest_path)
            self._save_metadata({
                "original_path": orig_path,
                "quarantined_path": dest_path,
                "detection_time": timestamp,
                "file_hash": file_hash,
                "file_name": file_name
            })
            return True
        except Exception as e:
            print(f"Quarantine failed: {str(e)}")
            return False
    
    def _calculate_hash(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def _save_metadata(self, data):
        log_file = os.path.join(self.quarantine_dir, "quarantine.log")
        with open(log_file, "a") as f:
            f.write(json.dumps(data) + "\n")
