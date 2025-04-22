
import time
import random

log_file = "logs.txt"
patterns = ["malicious", "attack", "scan"]
ips = [f"192.168.0.{i}" for i in range(1, 20)]

while True:
    pattern = random.choice(patterns)
    ip = random.choice(ips)
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    log_line = f"{timestamp} [ALERT] Pattern '{pattern}' detected from {ip}\n"

    with open(log_file, "a") as f:
        f.write(log_line)

    print("Logged:", log_line.strip())
    time.sleep(random.randint(2, 5))
