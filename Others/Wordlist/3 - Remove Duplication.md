--- ---

<h2>General</h2>

This tool can be very useful to cleanup a wordlist containing duplicate entries.Might be handy for CTF challenges where wordlists are intentionally made large and contain lots of duplicate entries.

---

<h2>Command</h2>

Tool
```Terminal
>$ ./dup-rem.py input-file output-file {Optional arguments: asc, dsc}
```

- asc - dsc                            ---> Sorts the output in a Ascending or descending order

---

<h3>Other Possibility</h3>

Terminal
```
# Combine files together
cat file1.txt file2.txt file3.txt > combined_list.txt

# Sort and remove duplicate
sort combined_list.txt | uniq -u > cleaned_combined_list.txt