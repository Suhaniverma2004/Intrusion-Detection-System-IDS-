
import socket
import ssl

log_file = "logs.txt"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 9999))
server_socket.listen(5)

print("🔐 SSL IDS Server is running on port 9999...")

with context.wrap_socket(server_socket, server_side=True) as secure_socket:
    while True:
        conn, addr = secure_socket.accept()
        print(f"📥 Connected from {addr}")
        data = conn.recv(1024).decode()
        if data:
            print("🔍 Received:", data)
            with open(log_file, "a") as f:
                f.write(data + "\n")
        conn.close()
