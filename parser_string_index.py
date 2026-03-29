print("Linux Auth parser Commencing!!!")
import sys

Auth_log = sys.argv[1]

count = 0

with open(Auth_log, 'r') as f:
    for line in f:
        if "Failed password" in line:
            try:
                count = count + 1
                parts = line.split()

                if "invalid" in parts:
                    user = parts[parts.index("user") + 1]
                else:
                    user = parts[parts.index("for") + 1]

                ip = parts[parts.index("from") + 1]

                print(f"Failed password attempt for user: {user} from IP: {ip}")

            except (ValueError, IndexError):
                pass

print(f"Failed password attempts: {count}")
