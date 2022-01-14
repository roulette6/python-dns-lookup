# DNS lookups using python

Perform forward and reverse DNS lookups using the [`socket`](https://docs.python.org/3/library/socket.html) library.

## Forward lookups
By default, the script will read a file named _fqdn-list.txt_. There is a sample file in this repo. The script will perform a forward DNS lookup for each line, and save the results to a file named _fwd-results.csv_. If `socket.gethostbyname()` raises an exception, the script will write a line to the file stating that no FQDN was found.

## Reverse lookups
The same is true for reverse lookups, except that the script will read from a file named _ip-list.txt_ and save to a file named _rsv-results.csv_.