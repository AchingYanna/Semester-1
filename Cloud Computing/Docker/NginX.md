<h1><b>NGINX</b></h1>
<img src="https://github.com/user-attachments/assets/9264ad95-7638-4890-9f4a-5f65c52a49c5" height="300" width="450"><br><Br>
NGINX is open-source web server software used for reverse proxy, load balancing, and caching. It provides HTTPS server capabilities and is mainly designed for maximum performance and stability. It also functions as a proxy server for email communications protocols, such as IMAP, POP3, and SMTP. 

<h1><b>Common nginx configuration tasks</b></h1>
<img src="https://github.com/user-attachments/assets/b14bd4bf-4f51-4adf-a9f1-d5f37492e78f" height="400" ><br><br>
<h3><b>- Server Block Configuration: </h3>Nginx uses server blocks to define how it handles incoming requests for different domains or IP addresses. Developers must configure server blocks to define the root directory, access permissions, SSL certificates, and other settings for each domain or IP address.
<br>
<h3><b>- Load Balancing:</b></h3>Nginx can be used as a load balancer to distribute incoming traffic across multiple backend servers. Developers should configure the load balancing algorithm, define backend server addresses, and set up health checks to ensure proper load distribution and failover.
<br>
<h3><b>- Reverse Proxying: </b></h3>Nginx can act as a reverse proxy, sitting in front of backend servers and handling client requests on their behalf.
<br>
<h3><b>- Caching: </b></h3>Nginx supports caching of static and dynamic content to improve performance. Developers can configure Nginx to cache certain types of content, set cache expiration rules, and control cache storage size.
<br>
<h3><b>- Logging and Monitoring: </b></h3>
Nginx provides extensive logging and monitoring capabilities. Developers can configure Nginx to log various types of information, such as access logs, error logs, or custom logs.

<h1><b>Advantages of NGINX</b></h1>
<img src="https://github.com/user-attachments/assets/850b68b5-ca7d-4dad-9cdc-78f5346b0ac7"><br><br>
<h3><b>- Performance: </b></h3> nginx is known for its high-performance capabilities. It is designed to handle a large number of concurrent connections efficiently.
<br>
<h3><b>- Scalability: </b></h3> nginx's architecture is event-driven and asynchronous, allowing it to handle many concurrent connections with minimal resource utilization. This makes it highly scalable, enabling developers to handle increasing traffic loads without additional hardware efficiently.
<br>
<h3><b>- Reverse proxy: </b></h3>nginx is often used as a reverse proxy server, which can improve performance and security. It can cache static content, reducing the load on the application servers and speeding up response times. Additionally, nginx can also act as a load balancer, distributing incoming requests across multiple backend servers ensuring efficient utilization of resources.
<br>
<h3><b>- Stability and reliability: </b></h3>nginx is known for its stability and reliability. It has a strong track record of powering high-traffic websites and has proven to be a reliable choice for many large-scale deployments. Its modular architecture and robust error-handling mechanisms contribute to its stability, ensuring it can handle high loads and function reliably even under challenging conditions.
<br>
<h3><b>- Security: </b></h3>nginx has built-in security features and is known for its ability to handle malicious traffic effectively. It includes IP and request rate limiting, SSL/TLS encryption support, and customizable access controls.

<h1><b>Installing Nginx</b></h1>
<img src="https://github.com/user-attachments/assets/1a3228ea-b206-4547-9b69-fc9c4913abbe"><br><br>
On your Linux Command line Run the following:

<h3><b>1. Update system packages</b></h3>

      sudo apt update

<h3><b>2. Intall NGINX</b></h3>

      sudo apt-get install nginx 

<h3><b>3. Setting up NGINX</b></h3>
     
      sudo systemctl start nginx
      sudo systemctl enable nginx

<h3><b>4. Allowing Firewall</b></h3>

       sudo ufw allow 'Nginx HTTP'

<h3><b>5. Verification</b></h3>

       sudo systemctl status nginx
      
