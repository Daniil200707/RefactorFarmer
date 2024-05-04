import requests
from bs4 import BeautifulSoup

def get_image_urls(query, num_images=10):
    url = f"https://www.google.com/search?q={query}&tbm=isch&num={num_images}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    image_urls = []
    for img in soup.find_all("img"):
        try:
            image_urls.append(img["src"])
        except KeyError:
            return image_urls

    return image_urls

# Пример использования функции
if __name__ == "__main__":
    query = "landscape"  # Ваш запрос
    num_images = 5  # Количество изображений

    image_urls = get_image_urls(query, num_images)
    print("URL изображений:")
    for url in image_urls:
        print(url)
        try:
            p = requests.get(url)
            out = open(f"images\img{url}.jpg", "wb")
            out.write(p.content)
            out.close()
        except requests.exceptions.MissingSchema:
            print("error")
