# Python - Network #1

This directory contains Python scripts for fetching internet resources, sending `GET` and `POST` requests, handling HTTP errors, and consuming JSON APIs using `urllib` and `requests`.

## Files

* `0-hbtn_status.py`: Fetches a URL using `urllib.request` and displays the response body type and content.
* `1-hbtn_header.py`: Sends a request to a URL and displays the value of the `X-Request-Id` response header.
* `2-post_email.py`: Sends a `POST` request with an `email` parameter using `urllib` and displays the decoded response.
* `3-error_code.py`: Fetches a URL using `urllib` and handles `HTTPError` status codes.
* `4-hbtn_status.py`: Fetches a URL using the `requests` package and displays the response details.
* `5-hbtn_header.py`: Sends a request using `requests` and displays the `X-Request-Id` header variable.
* `6-post_email.py`: Sends a `POST` request with an `email` parameter using `requests`.
* `7-error_code.py`: Fetches a URL using `requests` and prints `Error code:` if the HTTP status code is `400` or higher.
* `8-json_api.py`: Sends a `POST` request with a letter parameter and parses the returned JSON payload.
* `10-my_github.py`: Authenticates with the GitHub API using Basic Authentication to display your user ID.
* `100-github_commits.py`: Retrieves and prints the 10 most recent commits from a GitHub repository.
