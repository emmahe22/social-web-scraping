import bs4
import csv

with open('Reddit Threads - fishing.html', 'r', encoding='UTF-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('reddit.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'memebers'])


    c = 0 
    for div in soup.find_all('faceplate-tracker', source='search'):
        
        c += 1
        rs = div.find_all('faceplate-tracker', source='search', action='click')
        if (len(rs) < 1):
            continue

        titlediv = div.find_all('faceplate-number') 
        if (len(titlediv) < 2):
            continue
        print("**********")
        print(div.text)
        print("*********INFO**********")
        for title in titlediv:
            print(title.text)
        print(rs[0].text.strip())
        writer.writerow([rs[0].text.strip(),titlediv[0].text])

print('total: ' + str(c))


