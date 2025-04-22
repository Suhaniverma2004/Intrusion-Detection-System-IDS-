
from collections import defaultdict

def parse_logs(logfile, patterns):
    threat_counts = defaultdict(int)
    try:
        with open(logfile, "r") as f:
            for line in f:
                for pattern in patterns:
                    if pattern in line:
                        threat_counts[pattern] += 1
    except FileNotFoundError:
        pass
    return threat_counts
