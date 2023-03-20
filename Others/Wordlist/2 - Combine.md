--- ---

<h2>General</h2>

```Terminal
ubuntu@LXC:~$ python3 script.py

Please Type The File You Wanna Write Into: {YOUR FILE HERE}

Please Type All The Wordlists You Wanna Combine (One Space Seperated): {WORDLIST1} {WORDLIST2} {WORDLIST3} {ETC...}

Done Combining [WORDLISTS] into {THE MERGED WORDLISTS FILE.txt}
```

---

<h3>Other Possibility</h3>

Terminal
```
# Combine files together
cat file1.txt file2.txt file3.txt > combined_list.txt

# Sort and remove duplicate
sort combined_list.txt | uniq -u > cleaned_combined_list.txt