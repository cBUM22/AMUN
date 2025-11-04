helpTable = r"""
-pS        Port scanner
             Enumerates open network ports on a target host to identify active services.
             Legitimate uses: network inventory, diagnosing connectivity/service issues,
             and authorised security assessments. Always scan only systems you own or
             have explicit permission to test.

  -osint     OSINT (public DNS footprint discovery)
             Gathers public, non-sensitive DNS and internet-exposed footprint information
             (e.g., public DNS records, subdomains, WHOIS). Legitimate uses: asset discovery,
             threat hunting, and reconnaissance for authorised assessments. Do not use to
             collect private data or to stalk/harass.

             type "-osint" than a follow up input that says "Target Domain:" than input your
             target website domain to carry out this attack/DNS Service discovery

  -bF        Brute force (credential guessing)
             Attempts repeated authentication attempts to discover valid credentials.
             NOTE: brute forcing credentials is highly intrusive and illegal without
             explicit authorization. Use only in controlled, permitted penetration tests
             with strict rate-limiting and logging, or better: use approved password
             auditing tools and policies that don’t rely on guessing.

  -vS        Vulnerability scanner (web)
             Scans web applications/sites to detect known vulnerabilities and misconfigurations.
             Legitimate uses: vulnerability management, remediation prioritization, and
             authorised penetration testing. Do not scan third‑party sites without permission.

  -wC        Web crawler
             Automatically crawls a website to index reachable pages and resources.
             Legitimate uses: site mapping, content audits, SEO analysis, and authorised
             security discovery. Respect robots.txt, rate limits and terms of service.

  -kL        Key logger
             Captures keystrokes entered on a device.
             WARNING: keylogging records highly sensitive personal data (passwords, PII).
             Deployment without explicit, informed consent is illegal and unethical. Use
             only for accepted, transparent monitoring in environments governed by law
             (e.g., corporate endpoint monitoring with employee consent) and prefer
             privacy-respecting alternatives.

  -aM        Mail sending
             Sends email messages (single or bulk).
             Legitimate uses: notifications, alerts, marketing (with consent), and system
             messages. Must follow anti-spam laws (e.g., CAN-SPAM, GDPR where applicable),
             and never be used to deliver malware or spam.

  -sms       SMS sending
             Sends SMS messages to phone numbers.
             Legitimate uses: multi-factor authentication, alerts, transactional messages.
             Must comply with telecommunications and privacy regulations and obtain consent
             from recipients. Avoid high-frequency or unsolicited messaging.

  -mIP       Mask IP address (IP obfuscation / proxying)
             Routes traffic through intermediaries to hide the original source IP.
             Legitimate uses: privacy protection for lawful activity, geo-testing, and
             protecting services from casual fingerprinting. Do not use to evade law
             enforcement or to assist in committing crimes. Use reputable, legal services
             and follow terms of service.

    WARNING: 1-) Rooms that has been created will be destroyed within 2 days if there are no active chats
             2-) Rooms have rate-limits password can only be tried up to 10 times if you get blocked room
                 admin needs to clear your ip from the black list
             3-) Rooms can only be deleted by ROOM OWNER to use commands you need to be AUTHORISED BY ROOM OWNER

    ROOM COMMANDS:
        /kick: "Username"   -Kicks user with given username they cannot join for a day
        /clear              -Clear chat history
        /allow: "IP address"-Unbans users IP from black list (due to rate-limits)
        /ban: "Username"    -Ban user with given username they can never join unless they are unbanned
        /unban: "IP address"-Unbans user who got banned by "/ban" command
        /deleteR            -Deletes Room (ONLY ROOM ADMIN CAN USE)
        /checkIP: "Username"-Check IP of user with username
        /addCo: "IP Address"-Adds another user who can use commands except /ban /deleteR /kick /checkIP /allow
        /noChat             -Block sending messages for everyone except the ROOM ADMIN (ONLY ROOM ADMIN CAN USE IT)
        /doghnut            -Doghnut and spin
"""