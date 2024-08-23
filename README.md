🌐 Offline Site Generator
Web Crawler + Scraper + Parser

A Python-based multithreaded web crawler for scraping and saving web pages with support for different crawling strategies, proxies, and user agents. This web crawler leverages cloudscraper to bypass common anti-bot mechanisms and BeautifulSoup for HTML parsing. It ensures the accurate reconstruction of websites for offline access with intelligent link adjustments and robust error handling.
It's designed for comprehensive website crawling, scraping, and offline site generation. This powerful tool not only traverses and downloads entire websites but also bypasses advanced protections and restrictions including:

Cloudflare Protection
403 Forbidden errors
TLS
JA3
HTTP2 fingerprinting. 
   
🚀 Features

    Multi-Threaded Crawling: Efficiently handles multiple URLs concurrently.
    Content Scraping and Parsing: Extracts and saves HTML, images, scripts, and other resources.
    Offline Site Generation: Reconstructs the website structure for offline browsing, with adjusted internal links.
    Advanced Protection Bypass: Resistant to Cloudflare protection, 403 Forbidden errors, TLS, JA3, and HTTP2 fingerprinting.
    Rotating Proxies and User Agents: Utilizes rotating proxies and randomizes user agents to evade detection.
    Flexible Crawling Strategies: Supports breadth-first search (BFS) and depth-first search (DFS).
    Robust Error Handling: Retries failed requests and logs errors.

📦 Requirements

    Python 3.x
    cloudscraper - For bypassing anti-bot mechanisms.
    BeautifulSoup - For HTML parsing.
    requests - For making HTTP requests.
    urllib.parse - For handling URL parsing and joining.

📚 

-->   pip install cloudscraper beautifulsoup4 requests urllib.parse

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

🖇️ Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure your code follows PEP-8 standards.
📝 License

This project is licensed under the MIT License.
