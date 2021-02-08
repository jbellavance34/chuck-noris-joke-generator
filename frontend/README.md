# Frontend

html/javascript frontend to get chuck norris jokes

# Configuration 

- create s3 bucket
    - name: chuck-norris-joke
    - static website hosting: enable
    - index document: index.html
- create cloudfront distribution
    - origin name: chuck-norris-joke
    - retrict bucket access: yes
    - origin access indentity: create new identity
    - grant read permission on bucke: Yes, Update bucket policy
    - viewer protocol policy: Redirect HTTP to HTTPS
    - allowed http methods: GET, HEAD
    - default root object: index.html


# Upload s3 bucket

```bash
aws s3 cp index.html s3://chuck-norris-joke/
aws s3 cp style.css s3://chuck-norris-joke/
```
