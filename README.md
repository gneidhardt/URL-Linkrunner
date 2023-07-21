# URL Linkrunner

This is an adapted version of (https://github.com/MrJeremyHobbs/A-Z-Linkrunner) modified to test URLs of open access portfolios exported from Alma. It uses a text file of URLs and Python via Windows Command Prompt. It checks the URLs for HTTP responses and generates a report.

# Getting Started

Search for URLs of "free" electronic portfolios in Alma [search string: (Is Local (Electronic Portfolio) equals "Yes" AND Library (Electronic Portfolio) equals (Galter Health Sciences Library & Learning Center) AND Free (Service) equals "Free") OR (Free (Electronic Collection) equals "Free" AND Is Local (Electronic Portfolio) equals "Yes" AND Library (Electronic Portfolio) equals (Galter Health Sciences Library & Learning Center))], also saved as set name "Free (Service) and Free (Electronic Collection) items at Galter"

Run job in Alma - export URLs on this set. Once complete, copy URLs column to document called "urls.txt" (make sure to delete column header). (Note - need to figure out how to add a random delay, OR split file up in order not to get blocked).

Adding random delays:
For especially polite crawlers, you can check a site’s robots.txt (this will be located at http://example.com/robots.txt or http://www.example.com/robots.txt), often they will have a line that says crawl-delay that will tell you how many seconds you should wait in between requests you send to the site so that you don’t cause any issues with heavy server traffic.
Internet Archive = crawl away
HathiTrust = 10 seconds
NIH = 2 seconds
OCLC = 2 seconds
NAP = none

Documentation on adding delays: https://stackoverflow.com/questions/4054254/how-to-add-random-delays-between-the-queries-sent-to-google-to-avoid-getting-blo

# Running the Scripts

### Run 1_get_urls_a_z_list.py. 

This script will search through the raw HTML and pull out the links. It will generate a file called urls.txt in the main script folder. (Note - loading URLs directly into .txt file makes this step unnecessary)

### Run 2_check_urls_a_z_list.py

This script makes an HTTP call to each URL in the urls.txt file. It will generate a log.txt file that is tabbed delimited and includes the Title, URL, HTTP status code, redirect location, and a blank note field for later use.

You can find a reference of HTTP status codes here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

To run, open Command Prompt, navigate to Python testing folder ([cd then drag folder path], then type [python 2_check_urls_a-z_list.py]

# Notes

You can use 2_check_urls_a-z_list.py to check any list of urls, including URLs from an Alma analytics report, an EZproxy config file, or similar source.

Keep in mind, though, that if your URL list includes hundreds of links from the same domain, this may cause the vendor to shut down access. In the case of an A-Z list, this is not a concern (single URL per resource), but with other uses, you'll want to add some code or pre-edit the URLs list to only show a single URL per domain source.
