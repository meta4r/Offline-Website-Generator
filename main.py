import threading
import os
import random
import logging
from urllib.parse import urljoin, urlparse
import cloudscraper
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

START_URL = "https://selfdefinition.org/index.htm"
OUTPUT_DIR = "output"
PROXIES = [
    "184.174.44.238:6664",
    "103.51.21.165:8080",
    "148.113.162.23:54931",
    "67.43.228.251:3343",
    "190.128.241.102:80",
    "72.10.164.178:30085",
    "125.87.82.86:3256",
    "139.180.140.254:1080",
    "202.162.105.202:80",
    "43.202.154.212:80",
    "170.78.92.98:5678",
    "67.43.227.227:18141",
    "67.43.236.20:11205",
    "202.51.190.202:8080",
    "123.30.154.171:7777",
    "3.24.58.156:3128",
    "190.94.213.81:999",
    "72.10.164.178:17561",
    "202.40.179.18:4145",
    "38.242.251.177:15357",
    "201.20.118.146:27234",
    "103.95.97.53:4153",
    "104.207.36.163:3128",
    "109.122.195.16:80",
    "138.128.153.51:5085",
    "192.3.28.239:8080",
    "182.52.161.125:8080",
    "103.165.43.140:8080",
    "167.172.109.12:37355",
    "50.207.44.142:3355",
    "106.1.94.48:8888",
    "103.172.23.82:8080",
    "64.227.134.208:80",
    "112.198.129.234:8085",
    "4.155.2.13:9480",
    "104.165.127.37:3128",
    "101.109.245.200:4153",
    "188.125.167.71:8080",
    "13.36.113.81:3128",
    "104.207.46.145:3128",
    "174.138.176.78:16500",
    "27.75.150.180:1080",
    "125.141.151.83:80",
    "156.250.119.137:7001",
    "161.34.40.117:3128",
    "103.84.208.170:8080",
    "81.163.56.104:23500",
    "185.109.184.150:55019",
    "203.150.128.74:8080",
    "45.65.113.71:80",
    "103.48.71.6:83",
    "190.14.249.217:999",
    "3.127.121.101:3128",
    "103.177.9.120:8181",
    "125.26.165.245:8080",
    "185.38.111.1:8080",
    "203.150.172.151:8080",
    "182.253.17.173:8080",
    "72.10.164.178:15597",
    "116.203.27.109:80",
    "189.250.135.40:80",
    "37.52.50.28:5678",
    "31.128.69.121:8080",
    "67.43.227.227:31505",
    "202.62.67.209:53281",
    "201.71.3.62:999",
    "138.201.21.218:13478",
    "94.232.145.158:5678",
    "79.110.200.148:8081",
    "72.10.164.178:29327",
    "45.166.26.81:53695",
    "190.71.60.195:999",
    "5.58.33.187:55507",
    "116.107.232.189:10013",
    "49.51.93.222:443",
    "217.69.126.196:6066",
    "103.188.136.44:32650",
    "191.97.16.126:999",
    "188.132.222.6:8080",
    "47.250.11.111:8081",
    "20.204.214.23:3129",
    "141.145.214.176:80",
    "181.204.39.202:26312",
    "103.159.188.250:80",
    "207.244.254.27:1212",
    "45.43.84.62:6687",
    "189.50.9.33:8080",
    "181.215.134.105:80",
    "31.207.38.66:80",
    "77.37.41.168:80",
    "72.10.164.178:10867",
    "103.156.249.43:1080",
    "8.148.23.165:9098",
    "88.84.62.5:4153",
    "50.174.7.162:80",
    "80.13.39.65:80",
    "46.51.249.135:3128",
    "124.156.100.83:8118",
    "13.38.176.104:3128",
    "111.68.127.170:4153",
    "47.91.109.17:8008",
    "202.57.2.19:8080",
    "213.171.214.19:8001",
    "156.67.217.159:80",
    "183.100.14.134:8000",
    "146.70.80.76:80",
    "104.252.131.208:3128",
    "182.66.93.218:80",
    "103.144.209.104:3629",
    "41.207.187.178:80",
    "14.241.241.185:4145",
    "115.223.11.212:8103",
    "43.134.121.40:3128",
    "181.15.156.170:8080",
    "186.24.9.116:999",
    "122.52.196.36:8080",
    "103.83.97.46:7777",
    "223.100.178.167:9091",
    "181.212.45.228:8080",
    "103.14.232.46:5678",
    "47.128.243.200:8888",
    "45.159.150.23:3128",
    "101.101.217.36:80",
    "200.215.160.210:5678",
    "112.198.150.11:8082",
    "45.230.51.13:999",
    "213.212.204.206:1976",
    "103.228.118.85:60606",
    "133.232.89.179:80",
    "84.17.51.235:3128",
    "148.72.140.24:30127",
    "34.87.84.105:80",
    "138.91.159.185:80",
    "103.199.117.115:8080",
    "103.155.197.193:8080",
    "188.255.247.50:8088",
    "50.173.22.16:80",
    "104.252.131.182:3128",
    "36.94.47.59:4480",
    "183.196.80.217:8060",
    "200.6.175.10:59341",
    "104.249.29.170:5863",
    "103.137.218.166:83",
    "155.50.208.37:3128",
    "89.35.237.187:999",
    "58.20.248.139:9002",
    "213.160.150.237:8080",
    "45.230.47.133:60606",
    "102.0.5.152:8080",
    "185.53.129.141:3128",
    "165.154.236.214:80",
    "184.174.24.92:6668",
    "49.0.34.194:8080",
    "5.61.205.217:4153",
    "20.205.61.143:8123",
    "50.218.224.32:80",
    "67.43.227.227:1785",
    "41.33.179.195:8080",
    "46.10.229.58:60606",
    "209.121.164.50:31147",
    "194.190.169.197:3701",
    "161.34.39.54:9999",
    "102.68.139.247:8080",
    "114.130.153.58:58080",
    "189.22.142.29:8091",
    "202.40.187.126:60606",
    "152.26.229.52:9443",
    "103.27.22.65:32650",
    "178.255.44.62:48545",
    "182.72.203.246:80",
    "151.236.14.178:18080",
    "211.43.214.205:80",
    "103.24.107.186:8080",
    "14.207.24.176:8080",
    "104.143.226.149:5752",
    "190.110.99.189:999",
    "185.43.189.182:3629",
    "138.117.63.102:3629",
    "103.177.9.104:8080",
    "27.77.234.88:1080",
    "8.213.195.191:8008",
    "183.134.101.186:3128",
    "27.112.70.155:8083",
    "219.79.71.33:8080"
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.2 Safari/605.1.15"
]
MAX_RETRIES = 42  # Number of retries before giving up
TIMEOUT = 50  # Timeout for HTTP requests in seconds

class WebCrawler:
    def __init__(self, start_url, output_dir, proxies, max_depth=137, max_threads=17, strategy='dfs'):
        self.start_url = start_url
        self.output_dir = output_dir
        self.proxies = proxies
        self.max_depth = max_depth
        self.max_threads = max_threads
        self.visited = set()
        self.lock = threading.Lock()
        self.scraper = cloudscraper.create_scraper(ssl_context=False)  # Disable SSL verification
        self.proxy_index = 0
        self.strategy = strategy  # 'bfs' or 'dfs'
        
    def get_proxy(self):
        with self.lock:
            proxy = {"http": random.choice(self.proxies)}
        return proxy

    def crawl(self, url, depth=0):
        if depth > self.max_depth or url in self.visited:
            return

        logging.info(f"Crawling URL: {url} at depth: {depth}")
        with self.lock:
            self.visited.add(url)

        for attempt in range(MAX_RETRIES):
            try:
                headers = {'User-Agent': random.choice(USER_AGENTS)}
                response = self.scraper.get(url, headers=headers, proxies=self.get_proxy(), timeout=TIMEOUT)
                if response.status_code == 200:
                    content_type = response.headers.get('Content-Type')
                    if 'text/html' in content_type:
                        html_content = response.text
                        parsed_html = self.parse_html(html_content, url)
                        file_path = self.get_local_path(url)
                        self.save_file(parsed_html.encode(), file_path)
                        links = self.extract_links(html_content, url)
                        
                        if self.strategy == 'bfs':
                            self.bfs_crawl(links, depth)
                        else:
                            self.dfs_crawl(links, depth)

                    else:
                        self.save_content(url, response.content, content_type)
                    break  # Exit the retry loop on success
                else:
                    logging.warning(f"Failed to fetch {url}: {response.status_code}")
                    break  # No point in retrying if we get a non-200 status code
            except RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    logging.error(f"Giving up on {url} after {MAX_RETRIES} attempts")

    def bfs_crawl(self, links, depth):
        threads = []
        for link in links:
            thread = threading.Thread(target=self.crawl, args=(link, depth + 1))
            threads.append(thread)
            thread.start()
            if len(threads) >= self.max_threads:
                for t in threads:
                    t.join()
                threads = []
        for t in threads:
            t.join()

    def dfs_crawl(self, links, depth):
        for link in links:
            self.crawl(link, depth + 1)

    def save_content(self, url, content, content_type):
        file_path = self.get_local_path(url)
        self.save_file(content, file_path)

    def save_file(self, content, path):
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        with open(path, 'wb') as file:
            file.write(content)

    def parse_html(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.find_all(['link', 'script', 'img', 'a']):
            if tag.name == 'link' and tag.get('href'):
                self.handle_link_tag(tag, base_url)
            elif tag.name == 'script' and tag.get('src'):
                self.handle_script_tag(tag, base_url)
            elif tag.name == 'img' and tag.get('src'):
                self.handle_img_tag(tag, base_url)
            elif tag.name == 'a' and tag.get('href'):
                self.handle_a_tag(tag, base_url)

        return soup.prettify()

    def handle_link_tag(self, tag, base_url):
        file_url = urljoin(base_url, tag['href'])
        file_path = self.get_local_path(file_url)
        self.save_file(self.download_content(file_url), file_path)
        tag['href'] = os.path.relpath(file_path, os.path.dirname(self.get_local_path(base_url)))

    def handle_script_tag(self, tag, base_url):
        file_url = urljoin(base_url, tag['src'])
        file_path = self.get_local_path(file_url)
        self.save_file(self.download_content(file_url), file_path)
        tag['src'] = os.path.relpath(file_path, os.path.dirname(self.get_local_path(base_url)))

    def handle_img_tag(self, tag, base_url):
        file_url = urljoin(base_url, tag['src'])
        file_path = self.get_local_path(file_url)
        self.save_file(self.download_content(file_url), file_path)
        tag['src'] = os.path.relpath(file_path, os.path.dirname(self.get_local_path(base_url)))

    def handle_a_tag(self, tag, base_url):
        href = tag['href']
        file_url = urljoin(base_url, href)
        file_path = self.get_local_path(file_url)

        # Ensure that links to directories point to the index.htm within that directory
        if not href.endswith('.htm') and not href.endswith('.pdf') and not href.endswith('.jpg') and not href.endswith('.png'):
            if not href.endswith('/'):
                href += '/'
            href += 'index.htm'
            file_path = self.get_local_path(href)

        tag['href'] = os.path.relpath(file_path, os.path.dirname(self.get_local_path(base_url)))

    def download_content(self, url):
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        response = self.scraper.get(url, headers=headers, proxies=self.get_proxy(), timeout=TIMEOUT)
        return response.content

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if not href.startswith(('http://', 'https://')):
                href = urljoin(base_url, href)
            if urlparse(href).netloc == urlparse(base_url).netloc:
                links.add(href)
        return links

    def get_local_path(self, url):
        parsed_url = urlparse(url)
        path = parsed_url.path

        # Treat directories as index.htm files
        if path.endswith('/'):
            path += "index.htm"
        elif not os.path.splitext(path)[1]:  # If no extension, assume it's a directory
            path += "/index.htm"
        return os.path.join(self.output_dir, path.lstrip('/'))

    # No need for a separate create_index_file method as each directory itself is treated as an index.htm page

# Start the web crawler
crawler = WebCrawler(START_URL, OUTPUT_DIR, PROXIES, strategy='bfs')  # Switch strategy to 'dfs' for depth-first search
crawler.crawl(START_URL)
