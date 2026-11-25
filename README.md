## What actually happens, step by step, when you type a URL into your browser and hit Enter?

The browser sends a URL to DNS server which generates IP address which is then passed to the AWS firewall(which checks if the request is allowed) and then it reaches a reverse proxy server (like NginX)
then NginX redirects it to the host server then after the request is processed, the response is relayed back to the browser via the same protocols

## What are the client and the server, and how do they talk to each other?
A client is a computer that generates request for some particular task, a Server is a computer that hosts websites, Apis, receives request, processes it and gives back a response along with the asked data(if allowed).
They talk to each over HTTP, in which TCP is used as transport protocol, HTTPS is a more secure version of HTTP as connection is encrypted on it.

## What is HTTP? What's inside a request and a response?

HTTP stands for Hyper Text Transfer Protocol, it is how communication is done b/w server and client
A request contains data about the HTTP protocol used( eg http 1.1) host, origin, http Method used, various headers abt authorization, caching method, data it accepts etc
A response contains data about the http protocol used, a response code , allowed websites, content it relays and a body. In case of a preflighted request it would also relay the method, and data type the site accepts

## What's the difference between GET and POST, and when would you use each?
GET is used to fetch data only, it does not modify data 
POST is used to send data for processing or saving new data , it is used when data needs to be updated server side
example to see a users post , GET method would be used whereas to like that post, POST method would be used

## What do status codes like 200, 302, 404 and 500 mean?
200 is a status code which says that the request was successful and action has been completed
302 is a redirection type response code which is relayed when the request is being redirected to another location temporarily, the original address cannot be accessed right now
404 is a error status code which is relayed when a resource is unavailable, or the requested resource cannot be found
500 is a server error response code which means that there is  a internal server error

## What jobs do HTML, CSS and JavaScript each do on a page?
HTML provides the structure and content of headings, paragraphs, images etc
CSS controls how the page looks that is it controls colors, fonts, layout , sizes etc
JavaScript controls the interaction of buttons, menus and content that is displayed.

## Why did the tutorial add {% csrf_token %} to the voting form?
That command is to include the CSRF template tag  ,it provides protection against Cross Site Request Forgeries.
This type of attacks occurs when a malicious website tricks us into clicking some button which does some unauthorized action using the users credentials in the browser.
This token is always used when using methods like PUT, DELETE, POST as it involves use of user's credentials while proving authorization while making a request.

## How does a website remember who you are between pages? 
Each page we open sends a new HTTP request. A cookie is a small piece of data that the browser stores and automatically sends back along with requests to the site. A session holds information the site wants to remember between requests.
Cookies prevent repeated sending of data through each request, and thus the page loads faster and uses lower bandwidth.
the session id is sent when we move to a new page if that session id is still valid, the user doesnt need to login again.

## In Django, how does a request travel through URLs, views, models and templates before a response comes back?
The browser send a HTTP request to django server, then it passes through URLs which tells it which view it should go to.
The view handles this request and passes it to model which interacts with database and modifies or saves the data depending on the request and passes it back to views.
The views passes the retrieved data to templates which combines the data with HTML layout and produces a webpage.
The response goes back to the browser and the browser displays the webpage.
