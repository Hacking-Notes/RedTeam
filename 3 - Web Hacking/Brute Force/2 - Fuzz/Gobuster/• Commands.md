--- ---
<h2>Top Commands</h2>

#DIR
```Terminal 
gobuster dir -u WEBSITE -w WORDLIST -x "html,txt,php,zip,..." -t 25 --timeout Xs  --exclude-length X
```
- -u = URL
- -w = Wordlist
- -x = Append at the end of the directory
- -t = treats
- --timeout = Add some time between respond
- --exclude-lenght = Exclude result that has X bytes of data

---

<h2>All Commands (Modes)</h2>

#DIR ---> Uses directory/file enumeration mode

```
Usage:
  gobuster dir [flags]

Flags:
  -f, --add-slash                       Append / to each request
  -c, --cookies string                  Cookies to use for the requests
  -d, --discover-backup                 Also search for backup files by appending multiple backup extensions
      --exclude-length ints             exclude the following content length (completely ignores the status). Supply multiple times to exclude multiple sizes.
  -e, --expanded                        Expanded mode, print full URLs
  -x, --extensions string               File extension(s) to search for
  -r, --follow-redirect                 Follow redirects
  -H, --headers stringArray             Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                            help for dir
      --hide-length                     Hide the length of the body in the output
  -m, --method string                   Use the following HTTP method (default "GET")
  -n, --no-status                       Don't print status codes
  -k, --no-tls-validation               Skip TLS certificate verification
  -P, --password string                 Password for Basic Auth
      --proxy string                    Proxy to use for requests [http(s)://host:port]
      --random-agent                    Use a random User-Agent string
      --retry                           Should retry on request timeout
      --retry-attempts int              Times to retry on request timeout (default 3)
  -s, --status-codes string             Positive status codes (will be overwritten with status-codes-blacklist if set)
  -b, --status-codes-blacklist string   Negative status codes (will override status-codes if set) (default "404")
      --timeout duration                HTTP Timeout (default 10s)
  -u, --url string                      The target URL
  -a, --useragent string                Set the User-Agent string (default "gobuster/3.2.0")
  -U, --username string                 Username for Basic Auth

Global Flags:
      --delay duration    Time each thread waits between requests (e.g. 1500ms)
      --no-color          Disable color output
      --no-error          Don't display errors
  -z, --no-progress       Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -p, --pattern string    File containing replacement patterns
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist
```

#DNS ---> Uses DNS subdomain enumeration mode

```
Usage:
  gobuster dns [flags]

Flags:
  -d, --domain string      The target domain
  -h, --help               help for dns
  -r, --resolver string    Use custom DNS server (format server.com or server.com:port)
  -c, --show-cname         Show CNAME records (cannot be used with '-i' option)
  -i, --show-ips           Show IP addresses
      --timeout duration   DNS resolver timeout (default 1s)
      --wildcard           Force continued operation when wildcard found

Global Flags:
      --delay duration    Time each thread waits between requests (e.g. 1500ms)
      --no-color          Disable color output
      --no-error          Don't display errors
  -z, --no-progress       Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -p, --pattern string    File containing replacement patterns
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist
```

#Fuzz ---> Uses fuzzing mode

```
Usage:
  gobuster fuzz [flags]

Flags:
  -c, --cookies string              Cookies to use for the requests
      --exclude-length ints         exclude the following content length (completely ignores the status). Supply multiple times to exclude multiple sizes.
  -b, --excludestatuscodes string   Negative status codes (will override statuscodes if set)
  -r, --follow-redirect             Follow redirects
  -H, --headers stringArray         Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                        help for fuzz
  -m, --method string               Use the following HTTP method (default "GET")
  -k, --no-tls-validation           Skip TLS certificate verification
  -P, --password string             Password for Basic Auth
      --proxy string                Proxy to use for requests [http(s)://host:port]
      --random-agent                Use a random User-Agent string
      --retry                       Should retry on request timeout
      --retry-attempts int          Times to retry on request timeout (default 3)
      --timeout duration            HTTP Timeout (default 10s)
  -u, --url string                  The target URL
  -a, --useragent string            Set the User-Agent string (default "gobuster/3.2.0")
  -U, --username string             Username for Basic Auth

Global Flags:
      --delay duration    Time each thread waits between requests (e.g. 1500ms)
      --no-color          Disable color output
      --no-error          Don't display errors
  -z, --no-progress       Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -p, --pattern string    File containing replacement patterns
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist
```

#Vhost ---> Uses VHOST enumeration mode (use the IP address as the URL parameter)

```


Usage:
  gobuster vhost [flags]

Flags:
      --append-domain         Append main domain from URL to words from wordlist. Otherwise the fully qualified domains need to be specified in the wordlist.
  -c, --cookies string        Cookies to use for the requests
      --domain string         the domain to append when using an IP address as URL. If left empty and you specify a domain based URL the hostname from the URL is extracted
      --exclude-length ints   exclude the following content length (completely ignores the status). Supply multiple times to exclude multiple sizes.
  -r, --follow-redirect       Follow redirects
  -H, --headers stringArray   Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                  help for vhost
  -m, --method string         Use the following HTTP method (default "GET")
  -k, --no-tls-validation     Skip TLS certificate verification
  -P, --password string       Password for Basic Auth
      --proxy string          Proxy to use for requests [http(s)://host:port]
      --random-agent          Use a random User-Agent string
      --retry                 Should retry on request timeout
      --retry-attempts int    Times to retry on request timeout (default 3)
      --timeout duration      HTTP Timeout (default 10s)
  -u, --url string            The target URL
  -a, --useragent string      Set the User-Agent string (default "gobuster/3.2.0")
  -U, --username string       Username for Basic Auth

Global Flags:
      --delay duration    Time each thread waits between requests (e.g. 1500ms)
      --no-color          Disable color output
      --no-error          Don't display errors
  -z, --no-progress       Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -p, --pattern string    File containing replacement patterns
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist
```

#others ---> https://github.com/OJ/gobuster