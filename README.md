# anaconda-web2cmd

Anaconda image with web2cmd script to run cmd via API

##  Usage

### ENV variables

* `PORT` port to listen
* `RUN_SCRIPT` script to run via API with params

### Call CMD

Run `curl` on URL with params in query string

```bash
curl http://localhost:8080/?param1=value1&param2=value2
```

will run following command

```
${RUN_SCRIPT} --param1 value1 --param2 value2
```
