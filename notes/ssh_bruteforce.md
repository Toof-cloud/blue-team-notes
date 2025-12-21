Attack: SSH brute force

What happens:
Repeated login attempts over SSH using many passwords or usernames.

Logs involved:
- /var/log/auth.log

Key indicators:
- "Failed password"
- Same source IP
- Multiple attempts in short time

Why it matters:
If successful → full system access.
