#!/bin/bash
# Sends a GET request to a URL with a custom header variable
curl -s -H "X-School-User-Id: 98" "$1"
