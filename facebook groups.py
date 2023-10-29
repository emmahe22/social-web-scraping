import bs4
import csv

with open('fbdata.html', 'r', encoding='UTF-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

with open('res3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'members', 'post_freq'])


    c = 0 
    for div in soup.find_all('div', class_='x78zum5 xdt5ytf xz62fqu x16ldp7u'):
        print(div.text)
        strs = div.text.split("·")
        if (len(strs) < 3 or 'member' not in strs[1]):
            continue

        strs[0] = strs[0].replace("Private","")
        strs[0] = strs[0].replace("Public","")
        strs[1] = strs[1].replace("members","")
        if ('posts a day' in strs[2]):
            strs[2] = strs[2][: strs[2].find("a day") + 5]
        if ('posts a week' in strs[2]):
            strs[2] = strs[2][: strs[2].find("a week") + 6]
        if ('posts a month' in strs[2]):
            strs[2] = strs[2][: strs[2].find("a month") + 7]
        print(strs[0])
        print(strs[1])
        print(strs[2])
        writer.writerow([strs[0], strs[1], strs[2]])
        c += 1

print('total: ' + str(c))


