--- ---
<h3>What is John the Ripper?</h3>
John the Ripper is a popular, free, and open-source password cracking tool that can be used for auditing and testing the strength of passwords. It is a command-line tool that uses various password cracking techniques to identify weak passwords.

John the Ripper can work with many different operating systems and can crack passwords for a wide range of applications, such as Unix, Windows, and databases. The tool is highly customizable and can be used to simulate various types of attacks, including dictionary attacks, brute-force attacks, and hybrid attacks.

---
<h3>Common Uses and Commands</h3>
John the Ripper is primarily used for password cracking and testing. Some common use cases include testing the strength of passwords on a system, auditing password-protected files, and identifying weak passwords that need to be strengthened.

To use John the Ripper, users must first download and install the software on their system. Once installed, they can run it from the command line and specify the target file or system and the attack method to be used. Some common command line options for John the Ripper include:

```Terminal
# Brute Force
john [options] --wordlist=[path to wordlist] [path to file]
john [options] --wordlist=[path to wordlist] [path to file] --show passwd

# Wordlist Creation
cat /etc/john/john.conf|grep "List.Rules:" | cut -d"." -f3 | cut -d":" -f2 | cut -d"]" -f1 | awk NF                                                      ---> List the rules
john --wordlist=single-password-list.txt --rules=best64 --stdout | wc -l
john --wordlist=single-password-list.txt --rules=KoreLogic --stdout

	# Create a Rule
	sudo nano /etc/john/john.conf
	ADD THIS LINE --> [List.Rules:Password-Attacks] 
	ADD THIS LINE --> Az"[0-9]" ^[!@#$]
	
	john --wordlist=single-password-list.txt --rules=Password-Attacks --stdout
```

- `[options]`               ---> Hashing option
- --wordlist               ---> Wordlist
- `[path to file]`     ---> The file containing the hash you're trying to crack, if it's in the same directory you won't need to name a path, just the file.
- --show passwd     ---> Display password dehashed

- --rules                   ---> To specify which rule or rules to use.
- --stdout                ---> To print the output to the terminal.
- |wc -l                     ---> To count how many lines John produced.

---
<h3>More Information</h3>
John the Ripper is widely used in the field of password security and cracking. It has a large community of users who contribute to its development and improvement. The tool is constantly evolving to keep up with new security threats and password cracking techniques. Users can find more information and documentation on the tool's official website.

Check [[Red Team/3 - Web Hacking/2 - Cryptography/1 - Cracking Tools/John The Ripper/• Informations]]
- Cracking NTML Hashes
- Cracking Shadow Hashes
- Cracking Single Mode Hashes
- Cracking Cracking Hashes
- Cracking Zip Hashes
- Cracking Rar Hashes
- Cracking SSH Hashes

