#!/usr/bin/env python3
import click
from pathlib import Path
from core.scanner import FileScanner
from core.quarantine import QuarantineManager
from core.monitor import start_monitoring
from core.updater import SignatureUpdater

@click.group()
def cli():
    """Terminal Antivirus - A Python-based command line antivirus solution"""
    pass

@cli.command()
@click.argument('path')
def scan(path):
    """Scan a file or directory"""
    scanner = FileScanner()
    quarantine = QuarantineManager()
    
    if Path(path).is_file():
        malicious, hash_val = scanner.scan_file(path)
        if malicious:
            click.echo(f"🚨 Malware detected! Quarantining {path}")
            quarantine.quarantine_file(path)
        else:
            click.echo(f"✅ File is clean: {path}")

@cli.command()
@click.argument('path')
def monitor(path):
    """Monitor a directory in real-time"""
    click.echo(f"👀 Starting monitoring on {path} (Press Ctrl+C to stop)")
    start_monitoring(path)

@cli.command()
def update():
    """Update malware signatures"""
    updater = SignatureUpdater()
    updater.update_signatures()
    click.echo("🔄 Signature database updated")

if __name__ == "__main__":
    cli()
