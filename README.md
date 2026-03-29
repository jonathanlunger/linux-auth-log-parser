# Auth Log Parser

## Overview

This is a Python script that parses Linux authentication logs to detect failed password attempts.

The script reads a log file, searches for failed login attempts, extracts the username and source IP address, and counts how many failed attempts occurred.

## How I Built It

I started this project using string indexing. I wanted to understand how the log format worked at a basic level, so I split each line and manually pulled out values like the username and IP address.

This worked, but it was not very reliable. The parsing depended on the exact format of the log, and small changes could break the script.

After that, I learned how to use the regex module in Python. Using regex allowed me to match patterns in the log instead of relying on fixed positions. This made the parser more consistent and easier to work with.

## What the Script Does

- takes a log file as input from the command line
- searches for lines containing failed password attempts
- extracts the username from each match
- extracts the source IP address from each match
- prints each failed login attempt
- counts the total number of failed password attempts

## Example Output

Failed password attempt for user: admin from IP: 192.168.1.10  
Failed password attempt for user: root from IP: 192.168.1.20  

Failed password attempts: 2

## Limitations

Right now the script:
- does not count failed attempts per IP
- does not extract timestamps
- does not analyze behavior over time

## Next Steps

- track failed login attempts per IP address
- extract timestamps from each log entry
- detect repeated login attempts from the same source

## Usage

Run:

python parser_regex.py test.log

or:

python parser_string_index.py test.log
