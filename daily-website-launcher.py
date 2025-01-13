import webbrowser
from datetime import datetime

urls = []

# Update this to the path of your chosen browser
browser_path = "C:/Program Files/Mozilla Firefox/firefox.exe"



# list of URLs you want to open in your browser every day
urls.append("https://github.com/ProgrammerTerra")
urls.append("https://google.com")

#Monday
if datetime.today().weekday() == 0:
    urls.append("https://wikipedia.org")
    urls.append("https://coursera.org")
    
#Tuesday
elif datetime.today().weekday() == 1:
    urls.append("https://stackoverflow.com")
    urls.append("https://www.theodinproject.com/")
    
#Wednesday
elif datetime.today().weekday() == 2:
    urls.append("https://www.khanacademy.org/")
    urls.append("https://brilliant.org")
    
#Thursday
elif datetime.today().weekday() == 3:
    urls.append("https://leetcode.com/explore/")
    urls.append("https://www.skillshare.com/en/")
    
#Friday
elif datetime.today().weekday() == 4:
    urls.append("https://www.npr.org/")
    urls.append("https://www.goodreads.com/")
    
#Saturday
elif datetime.today().weekday() == 5:
    urls.append("https://netflix.com")
    urls.append("ed.ted.com")
    
#Sunday
elif datetime.today().weekday() == 6:
    urls.append("https://duolingo.com")
    urls.append("https://www.headspace.com/")



# Open each URL in a new tab
webbrowser.register('browser', None, webbrowser.BackgroundBrowser(browser_path))
for url in urls:
    webbrowser.get('browser').open_new_tab(url)
