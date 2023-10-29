import bs4
import csv

with open('fishing channel - YouTube.html', 'r', encoding='UTF-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('ytchannel.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'subscribers', 'video_num'])


    c = 0 
    for div in soup.find_all('div', id='info'):
        c += 1
        child_divs = div.find_all('div', id='text-container')
        if (len(child_divs) == 0):
            continue



        print("**********")
        print(div.text)
        print("*********INFO**********")
        print(child_divs[0].text.strip())

        sub_div = div.find_all('span', id='video-count')
        print(sub_div[0].text)
        if ('video' in sub_div[0].text):
            print(sub_div[0].text)
            writer.writerow([child_divs[0].text.strip(), 'n/a', sub_div[0].text])
        elif ('subscribers' in sub_div[0].text):
            print(sub_div[0].text)
            writer.writerow([child_divs[0].text.strip(), sub_div[0].text, 'n/a'])
        print("------------")

print('total: ' + str(c))


