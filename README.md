🌐 Offline Site Generator
Web Crawler + Scraper + Parser

A Python-based multithreaded web crawler for scraping and saving web pages with support for different crawling strategies, proxies, and user agents. This web crawler leverages cloudscraper to bypass common anti-bot mechanisms and BeautifulSoup for HTML parsing ensureing accurate reconstruction of websites for offline access.

Bypasses advanced protections and restrictions including:

Anti - [Cloudflare Protection,
403 Forbidden errors,
TLS,
JA3,
HTTP2 fingerprinting]
   
🚀 Features

    Multi-Threading
    Parsing HTML, CSS, images, PDF's and other resources.
    Offline Site Generation
    Advanced Protection Bypass: Resistant to Cloudflare protection, 403 Forbidden errors, TLS, JA3, and HTTP2 fingerprinting.
    Rotating Proxies and User Agents on every request.
    Breadth-first search (BFS) and Depth-first search (DFS).
    Retries failed requests and logs errors.

📦 Requirements

    Python 3.x
    cloudscraper - For bypassing anti-bot mechanisms.
    BeautifulSoup - For HTML parsing.
    requests - For making HTTP requests.
    urllib.parse - For handling URL parsing and joining.


🛠️ Configuration

Before running the crawler, configure the following variables as needed:

    START_URL: The starting URL for the crawler.
    OUTPUT_DIR: The directory where crawled content will be saved.
    PROXIES: A list of proxies to use during crawling. You can get proxies from here --> https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt.
    USER_AGENTS: A list of user agents to randomize requests.
    MAX_RETRIES: Maximum number of retries for each URL.
    TIMEOUT: Timeout for HTTP requests in seconds.

🔄 Customization

    Max Depth: The maximum depth to crawl can be adjusted by changing the max_depth parameter in the WebCrawler class instantiation.
    Max Threads: The number of threads used for crawling can be set by adjusting the max_threads parameter.

📜 Logging

The crawler uses Python's built-in logging module to log events. Logs are printed to the console with timestamps and log levels (INFO, WARNING, ERROR).

🔒 Error Handling

    Script etries with a maximum of MAX_RETRIES attempts for each URL.
    Uses exception handling to catch and log HTTP-related errors.


📝 License

This project is licensed under the MIT License.
