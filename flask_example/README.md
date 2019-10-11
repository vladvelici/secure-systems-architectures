# Flask example

## Run the server:

    ./server.py

or

    python server.py

or

    python3 server.py



## Using HTTP server without written clients

After you run `server.py` you can use it without necessarily implementing the clients, since it's served via HTTP.

With a browser, command line tool like `curl` or a browser extension like `Postman`.

CURL example to send message **hi there, how are you?** from **john** to **jane**:


    curl \
        -d '{"auth_data": "john", "message": "hi there, how are you?", "recipient": "jane"}' \
        -H "Content-Type: application/json" \
        http://localhost:8000/send-message


The data is encoded in [JSON](https://www.json.org).

CURL example to read Jane's inbox:

    curl http://localhost:8000/get-inbox?auth_data=jane


The second example is much simpler, since it is a simple GET request as opposed to a POST request. All data needed to be sent is the authentication data, which in this case we pass as a [*query string*](https://en.wikipedia.org/wiki/Query_string).

[Read more about HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods). For this coursework it is sufficient to use POST and GET requests. POST for when you WRITE something (e.g. send a message) and GET for when you READ data (e.g. read inbox).
