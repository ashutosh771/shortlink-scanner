<h1 align="center">
  <br>
  <br>
  ShortLink-Scanner
  <br>
</h1>

<h4 align="center">Find secrets from short URLs</h4>

### Introduction

ShortLink-Scanner is a powerful tool designed for expanding and analyzing shortened URLs. It provides insights into the final destination of shortened links, filters URLs with parameters, and specific HTTP response codes. 

### Features
<br>
URL Expansion: Converts shortened URLs to their full form, revealing the full path.

Parameter Detection: Identifies URLs that contain query parameters.

HTTP Status Filtering: Filters URLs based on specified HTTP status codes.

User-Agent Randomization: Option to use a random User-Agent for each request to mimic different browser types. (for stealth)

Multi-Threading Support: Speeds up the process by handling multiple URLs in parallel.

Request Delay and Timeout: Introduce delay between requests (for steealth) and a timeout feature to skip unresponsive URLs.

### Installation 

Ensure you have Python 3.x installed on your system.

Clone this repository or download the script directly.

Install the required dependencies: 

pip3 install -r requirements.txt

### Usage

python3 scanner.py -l <input_file> [options]

-l, --input_file (required): File containing the list of shortened URLs. <br>
-m, --http_status (optional): HTTP status code to filter the URLs. <br>
-t, --threads (optional): Number of threads (default is 10).<br>
-o, --output_file (optional): Output file name (default is out_long_urls.txt).<br>
-p, --params-only (optional): Filter for URLs that contain parameters.<br>
--random-agent (optional): Use a random user agent for each request.<br>
-d, --delay (optional): Delay between requests in seconds.<br>
--time-out (optional): Timeout in seconds for each request (default is 15 seconds).<br>


Examples -

python3 scanner.py -l targets.txt -m 200 -o out.txt (save only URLs with 200 response code to out.txt)

python3 scanner.py -l targets.txt -m 200 --params-only (save only URLs with parameters)

python3 scanner.py -l targets.txt -d 2 -t 30 --random-agents (add 2 second delay between each requests, threads=30, use random agents for each request) 


