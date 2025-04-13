import requests
from bs4 import BeautifulSoup

def get_image_from_web(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Поиск через Google Images
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        with open("test.txt","w", encoding="utf-8") as file:
            file.write(response.text)
        images = soup.find_all('img')
        for i in range(len(images)):
            if "src" in images[i].attrs.keys() and images[i].attrs["src"] != None and "alt" in images[i].attrs.keys() and images[i]["alt"] != "":
                image = images[i]
                print (f"alt = {images[i]["alt"]}")
                break
        return image
    return None

# Использование
image_url = get_image_from_web("Роза Хутор")
print(image_url)