from collections import defaultdict

log_file = "auth.log"
failures = defaultdict(int)

with open(log_file, "r") as logs:
    for line in logs:
        if "Failed password" in line:
            ip = line.split("from")[1].split()[0]
            failures[ip] += 1

print("Potential SSH Brute Force Sources:")
for ip, count in failures.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")
