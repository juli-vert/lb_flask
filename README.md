# Load Balancer using flask(?)
This is crazy stuff, creating a load balancer-ish using flask with auto-generated routes just for fun.  
We do expose routes on our frontend flask-app which actually request the content to the backend servers with different balancing algorithms.  

Create the backend container  
> docker build -t mybackhurts backend/.  

Edit the config file with your vips (match the backends with what you bring up)  
> docker run --name back{n} mybackhurts {port}  

Bring up the frontend app which will generate the routes on the fly:  
> python lbmanager.py
