import requests
import os
import time

# clean-up
try:
    os.remove('log.txt')
except FileNotFoundError:
    pass

# MAIN
# take out def in jupyter notebook and move everything over
def main():
    with open('urls.txt', 'r', newline="", encoding="utf-8") as txtfile:
        lines = txtfile.read().splitlines()
        for line in lines:
            split = line.split('\t')
            title = split[0]
            url = split[0]
            
            # Loop through links checking for 404 responses, and append to list.
            _validate_url(title, url)


# Internal function for validating HTTP status code.
# take out def in jupyter notebook and move everything over
def _validate_url(title, url):
    note = ""
    
    try:
        r = requests.head(url)
    except Exception as e:
        status_code = ""
        redirect_location = ""
    
    try:
        redirect_location = r.headers['Location']
    except Exception as e:
        redirect_location = ""

    try:
        status_code = r.status_code
    except Exception as e:
        status_code = ""
        note = "No status code"
    
    # write to file
    with open('log.txt', 'a', encoding="utf-8") as writer:
        writer.write(f"{title}\t{url}\t{status_code}\t{redirect_location}\t{note}\n")
    
    time.sleep(10)
    
# maybe take this out if providing an error    
if __name__ == "__main__":
    main()
