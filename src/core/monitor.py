import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from core.scanner import FileScanner
from core.quarantine import QuarantineManager

class FileMonitor(FileSystemEventHandler):
    def __init__(self, scanner, quarantine):
        self.scanner = scanner
        self.quarantine = quarantine
    
    def on_created(self, event):
        if not event.is_directory:
            self._process_file(event.src_path)
    
    def on_modified(self, event):
        if not event.is_directory:
            self._process_file(event.src_path)
    
    def _process_file(self, file_path):
        try:
            malicious, hash_val = self.scanner.scan_file(file_path)
            if malicious:
                print(f"🚨 Malware detected: {file_path}")
                self.quarantine.quarantine_file(file_path)
        except Exception as e:
            print(f"Monitoring error: {str(e)}")

def start_monitoring(path='.'):
    scanner = FileScanner()
    quarantine = QuarantineManager()
    event_handler = FileMonitor(scanner, quarantine)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
