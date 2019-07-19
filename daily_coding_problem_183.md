## Describe what happens when you type a URL into your browser and press Enter.

1. Browser checks cache for a DNS record that maps the URL to a corresponding IP address
    
    * DNS (Domain Name System) is a database that maintains the name of the website/URL
    * Main purpose of DNS is for human friendly readable names
    * To find the right DNS record, the browser has four caches to look from
        
        * First it checks the browser cache
        * If that fails there is the OS cache to check
        * If that also doesn't work out the browser can check the router cache
        * Lastly if all else fails the browser moves on to check the ISP cache

    * If the request URL is not in the ISP's cache, the DNS server performs a DNS query to find the IP address of the server that hosts the URL
    * This is a recursive look up, because it continues to bounce form DNS server to DNS server to find the IP address or returns an error response that it was not found
    * The recursion floats up from lower level domains up to the top or root level domain during the search. Then the result is bubbled back down to the browser

2. Browser receives the IP address
3. Browser starts a TCP connection with the server
    
    * Browsers will use the internet protocol TCP 
        
        * Firstly it starts the TCP handshake:
        * Client machine (on browser) sends a SYN packet to server
        * If server accepts new connections, it response with an ACK, acknowledging receipt of the SYN
        * Client receive the SYN/ACK packet from server and then sends a new ACK
    * Now TCP connection is established

4. Browser sends and HTTP GET request to web server for website
5. Server receives request and sends back a response (usually in HTML format in this case)
    
    * Also sends an HTTP response with webpage, includes status code, content-type, and other meta data
6. Browser receives response and webpage then displays the HTML content
