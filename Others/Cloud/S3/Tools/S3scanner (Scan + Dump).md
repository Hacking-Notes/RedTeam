--- ---

<h2>Top Commands</h2>

```
s3scanner scan --bucket my-bucket(Bucket Name)
s3scanner dump --bucket my-bucket(Bucket Name) --dump-dir ~/Desktop/...(pc location)/
```


Other Commands
```
usage: s3scanner [-h] [--version] [--threads n] [--endpoint-url ENDPOINT_URL] [--endpoint-address-style {path,vhost}] [--insecure] {scan,dump} ...

s3scanner: Audit unsecured S3 buckets
           by Dan Salmon - github.com/sa7mon, @bltjetpack

optional arguments:
  -h, --help            show this help message and exit
  --version             Display the current version of this tool
  --threads n, -t n     Number of threads to use. Default: 4
  --endpoint-url ENDPOINT_URL, -u ENDPOINT_URL
                        URL of S3-compliant API. Default: https://s3.amazonaws.com
  --endpoint-address-style {path,vhost}, -s {path,vhost}
                        Address style to use for the endpoint. Default: path
  --insecure, -i        Do not verify SSL

mode:
  {scan,dump}           (Must choose one)
    scan                Scan bucket permissions
    dump                Dump the contents of buckets
```


---

<h2>What is S3Scanner</h2>

A tool to find open S3 buckets and dump their contents!

More information ---> https://github.com/sa7mon/S3Scanner

<iframe src="https://github.com/sa7mon/S3Scanner" width="100%" height="1300"></iframe>