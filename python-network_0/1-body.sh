#!/bin/bash
# Sends a GET request to a URL, following redirects, and displays the body only on a 200 status
curl -sLf "$1"
