import argparse
import requests
import time
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import concurrent.futures
from urllib.parse import urlparse, parse_qs
from tqdm import tqdm

def print_ascii_art():
    print(r"""\    
         __              ______   __    _       __               _____                                 
   _____/ /_  ____  ____/_  __/  / /   (_)___  / /__            / ___/_________ _____  ____  ___  _____
  / ___/ __ \/ __ \/ ___// /    / /   / / __ \/ //_/  ______    \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/  [ v1.1 ] | ashutoshbarot.com
 (__  ) / / / /_/ / /   / /    / /___/ / / / / ,<    /_____/   ___/ / /__/ /_/ / / / / / / /  __/ /    
/____/_/ /_/\____/_/   /_/    /_____/_/_/ /_/_/|_|            /____/\___/\__,_/_/ /_/_/ /_/\___/_/     by Ashutosh Barot [ Follow me on X - @ashu_barot ] 


""")


# List of User-Agents
USER_AGENTS = [
    # Add more user agents here, especially mobile user agents ;)


	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
	"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
	"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
	"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
	"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
	"Mozilla/5.0 (Linux; U; Android 2.1-update1; es-mx; SonyEricssonE10a Build/2.0.A.0.504) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
	"Mozilla/5.0 (Linux; U; Android 1.6; ar-us; SonyEricssonX10i Build/R2BA026) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 ",


    # ... more user agents ...
]

# Create a session object to persist parameters and reuse TCP connections
session = requests.Session()

# Disable SSL verification in the session
session.verify = False

# Disable InsecureRequestWarning for the session
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Argument parsing setup
parser = argparse.ArgumentParser(description="Expand shortened URLs and filter by HTTP status code.")
parser.add_argument('-l', '--input_file', required=True, help="File containing the list of shortened URLs.")
parser.add_argument('-m', '--http_status', type=int, help="HTTP status code to filter the URLs (optional).")
parser.add_argument('-t', '--threads', type=int, default=10, help="Number of threads (default is 10, max is 40).")
parser.add_argument('-o', '--output_file', default='out_long_urls.txt', help="Output file name (default is out_long_urls.txt).")
parser.add_argument('-p', '--params-only', action='store_true', help="Filter for URLs that contain parameters.")
parser.add_argument('--random-agents', action='store_true', help="Use a random user agent for each request.")
parser.add_argument('-d', '--delay', type=int, default=0, help="Delay between requests in seconds.")
parser.add_argument('--time-out', type=int, default=15, help="Timeout in seconds for each request (default is 15 seconds).")
args = parser.parse_args()

def get_random_user_agents():
    return random.choice(USER_AGENTS)

def expand_url(short_url):
    urls_to_try = [short_url]
    if not short_url.startswith('http://') and not short_url.startswith('https://'):
        urls_to_try = [f'https://{short_url}', f'http://{short_url}'] + urls_to_try
    elif short_url.startswith('http://'):
        urls_to_try = [short_url.replace('http://', 'https://', 1)] + urls_to_try

    headers = {'User-Agent': get_random_user_agent()} if args.random_agents else {}

    for url in urls_to_try:
        try:
            response = session.head(url, headers=headers, allow_redirects=True, timeout=args.time_out)
            time.sleep(args.delay)
            return short_url, response.url, response.status_code
        except requests.exceptions.Timeout:
            print(f"Request timed out for {url}")
        except Exception as e:
            print(f"Error for {url}: {e}")
            continue
    return short_url, None, None

def main():
    print_ascii_art()
    with open(args.input_file, 'r') as file:
        short_urls = [line.strip() for line in file]

    valid_urls_count = sum(1 for url in short_urls if url)
    print(f"Number of valid URLs in the target file: {valid_urls_count}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(expand_url, short_url): short_url for short_url in short_urls if short_url}
        expanded_urls = []
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), unit="URL", desc="Expanding URLs"):
            short_url = futures[future]
            expanded_urls.append(future.result())

    if args.params_only:
        expanded_urls = [(short_url, url, code) for short_url, url, code in expanded_urls if url and parse_qs(urlparse(url).query)]

    with open(args.output_file, 'w') as file:
        for _, url, _ in expanded_urls:
            if url:
                file.write(f"{url}\n")

    total_expanded = len(expanded_urls)
    status_200_count = sum(1 for _, _, code in expanded_urls if code == 200)
    status_403_count = sum(1 for _, _, code in expanded_urls if code == 403)
    urls_with_params_count = sum(1 for _, url, _ in expanded_urls if parse_qs(urlparse(url).query))
    print(f"\nOutput file: {args.output_file}")
    print("Summary of expanded URLs:")
    print(f"1. Number of total expanded URLs: {total_expanded}")
    print(f"2. Number of expanded URLs with 200 HTTP response code: {status_200_count}")
    print(f"3. Number of URLs with 403 response code: {status_403_count}")
    print(f"4. Number of URLs with parameters: {urls_with_params_count}")

if __name__ == "__main__":
    main()
