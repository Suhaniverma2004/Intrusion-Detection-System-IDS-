
import socket
import ssl
import random
import time

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("cert.pem")

server_address = ("localhost", 9999)
patterns = ["attack", "scan", "malicious"]
ips = [f"10.0.0.{i}" for i in range(1, 10)]

while True:
    pattern = random.choice(patterns)
    ip = random.choice(ips)
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    alert = f"{timestamp} [ALERT] Pattern '{pattern}' detected from {ip}"

    with socket.create_connection(server_address) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as ssock:
            ssock.sendall(alert.encode())

    print("✅ Sent:", alert)
    time.sleep(random.randint(2, 4))
