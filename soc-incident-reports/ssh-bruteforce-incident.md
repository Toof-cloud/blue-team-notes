# Incident: SSH Brute Force Attempt

## Summary
Multiple failed SSH login attempts were detected from a single source IP, indicating a potential SSH brute force attack against the system.

## Detection Time
Simulated log analysis during blue-team detection exercise.

## Data Source
- Log file: auth.log
- Log type: SSH authentication logs

## Evidence
The following indicators were observed:
- Repeated "Failed password" log entries
- Same source IP appearing multiple times
- Attempts targeting common usernames

Example log pattern:
Failed password for root from 10.0.0.5

Detection script output:
10.0.0.5 - 4 failed attempts

## Analysis
The volume and frequency of failed authentication attempts from a single IP exceed the defined threshold (≥3 attempts), which is consistent with brute force behavior rather than normal user error.

## Impact
If successful, this attack could result in:
- Unauthorized system access
- Privilege escalation
- Potential lateral movement within the network

## Detection Method
A Python-based detection script was used to parse SSH authentication logs and aggregate failed login attempts per source IP. Any IP exceeding a predefined threshold was flagged for investigation.

## Mitigation & Recommendations
- Block the offending IP using firewall rules
- Enable fail2ban to automatically mitigate brute force attempts
- Disable password-based SSH authentication
- Enforce SSH key-based authentication
- Monitor SSH logs continuously

## Lessons Learned
- Relative file paths can cause detection failures if not handled properly
- Threshold-based aggregation is effective for identifying brute force activity

## Questions
- What is the optimal failed-attempt threshold for alerting in a production environment?

## Answer 
- 3-5 attempts for small systems but 10+ attempts for enterprises of tuned systems.
