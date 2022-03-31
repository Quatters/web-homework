```
server {
	listen 80;
	root /usr/share/nginx/html/nginx-config-demo/app1;
}

server {
	listen 7777;
	root /usr/share/nginx/html/nginx-config-demo/app1;

	location /docs {
		alias /usr/share/nginx/html/nginx-config-demo/app2;
	}
}
```

![Alt text](app1.png 'app1')
![Alt text](app2.png 'app2')
