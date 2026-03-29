print("Linux Auth parser Commencing!!!")
import sys
import re

Auth_log = sys.argv[1]

Failed_Password_Pattern = r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"

count = 0

with open(Auth_log, 'r') as f:
    for line in f:
        match = re.search(Failed_Password_Pattern, line)
        if match:
            count = count + 1
            user = match.group("user")
            ip = match.group("ip")
            print(f"Failed password attempt for user: {user} from IP: {ip}")

print(f"Failed password attempts: {count}")
