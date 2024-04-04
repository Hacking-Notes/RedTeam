--- ---

<h3>General</h3>

Examine the small selection of tools provided here and identify the one that is most relevant to your requirements.

- CUPP
- Mentalist
- Cewl
- Crunch

---
<h2>CUPP</h2>
- command
```Terminal
python3 cupp.py -h

python3 cupp.py -i (Interactive mod, Ask you question about your target)

puthon4 cupp.py -l (Download Pre-created wordlists to your machine)
```

![cupp-example](https://github.com/Mebus/cupp/raw/master/screenshots/cupp-example.gif)

---
<h2>Mentalist</h2>
Mentalist is a graphical tool for custom wordlist generation. It utilizes common human paradigms for constructing passwords and can output the full wordlist as well as rules compatible with [Hashcat](https://hashcat.net/hashcat) and [John the Ripper](http://www.openwall.com/john).  


![Mentalist GUI](https://camo.githubusercontent.com/4eb268cbdaf7e2a09a3be4b1c7a2a32b47e9f6e568a9b34d549bfbfb512b684a/68747470733a2f2f73633074667265652e73717561726573706163652e636f6d2f732f6d656e74616c6973742d726561646d652d6775692e676966)

---
<h3>Cewl (Only work for english website)</h3>
Tools such as Cewl can be used to effectively crawl a website and extract strings or keywords. Cewl is a powerful tool to generate a wordlist specific to a given company or target. Consider the following example below:

```
cewl -w list.txt -d 5 -m 5 http://example.com
```
-w         ---> Will write the contents to a file. In this case, list.txt.
-m 5     ---> Gathers strings (words) that are 5 characters or more
-d 5      ---> Is the depth level of web crawling/spidering (default 2)

---
<h3>Username Generator</h3>
Gathering employees' names in the enumeration stage is essential. We can generate username lists from the target's website. For the following example, we'll assume we have a {first name} {last name} (ex: John Smith) and a method of generating usernames.

**This can be usefull to generate username list for Acive Directory**

Example
```
-   **{first name}:** john
-   **{last name}:** smith
-   **{first name}{last name}:  johnsmith** 
-   **{last name}{first name}:  smithjohn**  
-   first letter of the **{first name}{last name}: jsmith** 
-   first letter of the **{last name}{first name}: sjohn**  
-   first letter of the **{first name}.{last name}: j.smith** 
-   first letter of the **{first name}-{last name}: j-smith** 
-   and so on
```

```
git clone https://github.com/therodri2/username_generator.git

cd username_generator

python3 username_generator.py -h

echo "John Smith" > users.lst

python3 username_generator.py -w users.lst
```

---
<h3>Crunch</h3>
Crunch allow you to create custom brute force worlist (related to characters lengh)

Simple
```
crunch 2 2 01234abcd -o crunch.txt
```
- The following example creates a wordlist containing all possible combinations of 2 characters, including 0-4 and a-d. We can use the -o argument and specify a file to save the output to.

Include a know variable (Example: We want that all password start with pass)
```
crunch 6 6 -t "pass%%" -o crunch.txt
```
- We can use the % symbol from above to match the numbers. Here we generate a wordlist that contains pass followed by 2 numbers.
 
![[Pasted image 20230317202043.png]]