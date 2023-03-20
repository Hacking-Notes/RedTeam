--- ---
<h3>What is Hashcat?</h3>
Hashcat is a popular, free, and open-source password cracking tool that is used to recover lost or forgotten passwords. It uses various cracking techniques to crack passwords, including brute-force attacks, dictionary attacks, and mask attacks.

Hashcat is a command-line tool that can work with a variety of different password hash types and can be used on a range of platforms, including Windows, Linux, and macOS. The tool is highly customizable, allowing users to specify attack methods, rules, and other parameters.

---
<h3>Common Uses and Commands</h3>
Hashcat is primarily used for password cracking and recovery. Some common use cases include recovering forgotten passwords for personal accounts, testing the strength of passwords on a system, and auditing password-protected files.

To use Hashcat, users must first download and install the software on their system. Once installed, they can run it from the command line and specify the target hash type and the attack method to be used. Some common command line options for Hashcat include:
```Terminal
hashcat -m HASH-MODE HASH.FILE PASSWORD.TXT             ---> Crack Hash
hashcat -m HASH-MODE HASH.FILE PASSWORD.TXT --show      ---> Show Cracked Hash
hashcat -a 3 "?d?d?d?d" --stdout                        ---> Brute Force Mode
hashcat -b                                              ---> Benchmark
```

- -m HASH-MODE          ---> The hash mode found from identifing the hash type (Form tools section)
- --show                          ---> Show the Cracked Hash
- -b                                  ---> Benchmark (Used to test GPU)
- -a 3                               ---> Sets the attacking mode as a brute-force attack
- --stdout                        ---> Print the result to the terminal
- ?d?d?d?d                      ---> Tells hashcat to use a digit. In our case, ?d?d?d?d for four digits starting with 0000 and ending at 9999

---
<h3>More Information</h3>
Hashcat is a widely used and respected tool in the field of password cracking and recovery. It has a large community of users who contribute to its development and improvement. The tool is constantly evolving to keep up with new security threats and password cracking techniques. Users can find more information and documentation on the tool's official website.

More information ---> https://hashcat.net/hashcat/

<iframe src="https://hashcat.net/hashcat/" width="100%" height="1300"></iframe>