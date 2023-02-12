--- ---

<h2>General</h2>

Shodan is a search engine for Internet-connected devices. It allows users to search for specific types of devices (e.g. webcams, routers, servers, etc.) connected to the Internet using a variety of filters. To use Shodan in command line in Linux, you can install the "shodan" command-line interface (CLI) tool. This tool can be installed using the pip package manager by running the command "pip install shodan". Once installed, you can use the "shodan" command to perform various tasks, such as searching for specific devices, downloading data, and more. To use the tool, you will need to have an API key, which can be obtained by creating an account on the Shodan website.

---

<h2>Commands</h2>

The **shodan** CLI has a lot of commands, the most popular/ common ones are documented below. For the full list of commands just run the tool without any arguments:

<h3>Count</h3>
Returns the number of results for a search query.

- Example
```
$ shodan count microsoft iis 6.0
5310594
```

<h3>Download</h3>
Search Shodan and download the results into a file where each line is a JSON banner. For more information on what the banner contains check out:

[Banner Specification](https://developer.shodan.io/api/banner-specification)

By default it will only download 1,000 results, if you want to download more look at the **--limit** flag.

The **download** command is what you should be using most often when getting results from Shodan since it lets you save the results and process them afterwards using the **parse** command. Because paging through results uses query credits, it makes sense to always store searches that you're doing so you won't need to use query credits for a search you already did in the past.

- Example

![](https://cli.shodan.io/img/download.png)

<h3>Host</h3>
See information about the host such as where it's located, what ports are open and which organization owns the IP.

Example
```
$ shodan host 189.201.128.250
```

![](https://cli.shodan.io/img/host.png)

<h3>Myip</h3>
Returns your Internet-facing IP address.

- Example
```
$ shodan myip
199.30.49.210
```
<h3>Parse</h3>
Use **parse** to analyze a file that was generated using the **download** command. It lets you filter out the fields that you're interested in, convert the JSON to a CSV and is friendly for pipe-ing to other scripts.

- Example

The following command outputs the IP address, port and organization in CSV format for the previously downloaded Microsoft-IIS data:
```
$ shodan parse --fields ip_str,port,org --separator , microsoft-data.json.gz
```

![](https://cli.shodan.io/img/parse.png)


<h3>Search</h3>
This command lets you search Shodan and view the results in a terminal-friendly way. By default it will display the IP, port, hostnames and data. You can use the **--fields** parameter to print whichever banner fields you're interested in.

- Example

To search Microsoft IIS 6.0 and print out their IP, port, organization and hostnames use the following command:
```
$ shodan search --fields ip_str,port,org,hostnames microsoft iis 6.0
```

![](https://cli.shodan.io/img/search.png)