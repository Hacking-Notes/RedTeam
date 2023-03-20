--- ---

<h2>How To Prevent Directory Traversal Attacks</h2>

Avoid passing user-supplied input to filesystem APIs
- If this isn't possible, do the following:
	§ Application should validate user input before processing it by being compared to an allow list
	§ Append input to base directory and use platform filesystem API to canonicalize the path
 
- Sample code that does this:`
```
File file = new File(BASE_DIRECTORY,
userInput);
if
(file.getCanonicalPath().startsWith(BASE_DIRE
CTORY)) {
// process file
}
```