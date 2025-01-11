import webbrowser
from datetime import datetime

# list of URLs you want to open in your browser everyday
urls = [
    "https://twitter.com",
]

#Monday
if datetime.today().weekday() == 0:
    urls.append("https://twitter.com") #Twitter
    
#Tuesday
elif datetime.today().weekday() == 1:
	urls.append("https://twitter.com")
    
#Wednesday
elif datetime.today().weekday() == 2:
    urls.append("https://twitter.com")
    
#Thursday
elif datetime.today().weekday() == 3:
    urls.append("https://twitter.com")
    
#Friday
elif datetime.today().weekday() == 4:
    urls.append("https://twitter.com")
    
#Saturday
elif datetime.today().weekday() == 5:
    urls.append("https://twitter.com")
    
#Sunday
elif datetime.today().weekday() == 6:
    urls.append("https://twitter.com")


# Set Firefox as the browser
firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each URL in a new tab
for url in urls:
    webbrowser.get('chrome').open_new_tab(url)
