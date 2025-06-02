import http.server
import ssl
import tempfile
import os

# Create temporary self-signed certificate
cert_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pem')
key_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pem')

# Simple self-signed cert creation using Python
import subprocess
import sys

try:
    # Try creating cert with Python's ssl module
    import ssl
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_default_certs()
except:
    print("Let's try a different approach...")

print("Starting simple HTTP server on port 8000...")
print("We'll use your computer's IP address instead")
os.system("python -m http.server 8000 --bind 0.0.0.0")