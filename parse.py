from bs4 import BeautifulSoup
import csv

file_path = 'saved_page.html' # относительный путь
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')
table = soup.find("tbody")
trs = table.find_all("tr")
trs.pop() # последняя запись total (если не убрать выдаст исключение)
for tr in trs:
    name = tr.find("a", class_="symbol-word-break").text
    price = tr.find("td", class_="bold text-right").text
    with open("final_price.csv", "a", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file, delimiter=";", dialect="excel")
        writer.writerow([name,price])

    print(f'{name, price}')