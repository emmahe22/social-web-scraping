import bs4
import csv

with open('TikTok.html', 'r', encoding='UTF-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('tiktok.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['uid', 'follower', 'bio'])



    c = 0 
    for div in soup.find_all('div', class_="tiktok-1d5vh4i-DivLink e10wilco0"):
        print("**********")
        # print(div.text)

        uid = div.find_all('p', class_="tiktok-1ns35wh-PTitle e10wilco4")
   
        print(uid[0].text)
 
        userName = div.find_all('div', class_="tiktok-1n1o5vj-DivSubTitleWrapper e10wilco5")
        if (len(userName) > 0):
            section = userName[0].text
        else:
            section = 'N/A'

        userName2 = div.find_all('p', class_="tiktok-1n1o5vj-DivSubTitleWrapper e10wilco5")
        if (len(userName2) > 0):
            section = userName2[0].text


        print(section)

        strs = section.split("·")
        follower = strs[1].replace("Followers","").strip()
        print(follower)

        bio = 'N/A'
        bioNodes = div.find_all('p', class_="tiktok-1jq7d8a-PDesc e10wilco7")
        if (len(bioNodes) > 0):
            bio = bioNodes[0].text

        writer.writerow([uid[0].text,follower,bio])

        
print('total: ' + str(c))


