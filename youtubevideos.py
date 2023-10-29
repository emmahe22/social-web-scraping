import bs4
import csv

with open('fishing - YouTube.html', 'r', encoding='UTF-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('ytvideo.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'channel', 'views', 'timestamp'])


    c = 0 
    for div in soup.find_all('div', class_='style-scope ytd-video-renderer'):
        c += 1

        print("**********")
        print(div.text)
        print("*********INFO**********")

        child_divs = div.find_all('yt-formatted-string', class_='style-scope ytd-channel-name', id="text")
        if (len(child_divs) == 0):
            continue

        #channel name
        channelName = child_divs[0].text.strip()

        child_divs = div.find_all('span', class_='inline-metadata-item style-scope ytd-video-meta-block')
        if (len(child_divs) < 2):
            continue

        viewC = child_divs[0].text
        timeStamp = child_divs[1].text

        titlediv = div.find_all('div', class_='style-scope ytd-video-renderer', id="title-wrapper")
        # titlestr = titlediv.find_all('yt-formatted-string', class_='style-scope ytd-video-renderer')
         
        print(titlediv[0].text.strip())
        print(channelName)
        print(viewC)
        print(timeStamp)
      
        writer.writerow([titlediv[0].text.strip(), channelName, viewC, timeStamp])
        print("------------")

print('total: ' + str(c))


