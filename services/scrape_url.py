from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re


def clean_amazon_image_url(url: str, size: str = "_SY606_") -> str:
    base_url = url.split("._", 1)[0]
    ext = url.split(".")[-1]
    return f"{base_url}._{size}.{ext}"


def scrape_product_page(url: str) -> dict:
    try:
        # Configure headless Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1280,1000")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/120.0.0.0 Safari/537.36")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        # Wait and extract key sections
        alt_images = driver.find_element(By.ID, "altImages").get_attribute("innerHTML")
        price_text = driver.find_element(By.ID, "apex_desktop").text
        feature_html = driver.find_element(By.ID, "feature-bullets").get_attribute("innerHTML")

        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, "lxml")
        image_soup = BeautifulSoup(alt_images, "lxml")
        feature_soup = BeautifulSoup(feature_html, "lxml")

        title = soup.title.string.strip() if soup.title else "No title found"

        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc['content'].strip() if meta_desc else "No meta description found"

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        bullet_points = []
        ul = feature_soup.find("ul")
        if ul:
            bullet_points = [li.get_text(strip=True) for li in ul.find_all("li")]

        image_urls = []
        # for img in image_soup.find_all("img"):
        #     src = img.get("src") or img.get("data-src")
        #     if src:
        #         full_url = urljoin(url, src)
        #         clean_url = clean_amazon_image_url(full_url, size="_SY606_")
        #         image_urls.append(clean_url)
        for li in image_soup.find_all("li"):
            li_class = li.get("class") or []
            print(li_class)
            # Skip if 'videoThumbnail' is in class list
            if any("imageThumbnail" in cls for cls in li_class):
                

                # Extract <img> inside the <li>
                img = li.find("img")
                if img:
                    src = img.get("src") or img.get("data-src")
                    if src:
                        full_url = urljoin(url, src)
                        clean_url = clean_amazon_image_url(full_url, size="_SY606_")
                        image_urls.append(clean_url)

        return {
            "error": None,
            "title": title,
            "description": description,
            "bullet_points": bullet_points,
            "price_data": price_text,
            "images": image_urls
        }

    except Exception as e:
        return {
            "error": str(e),
            "title": "",
            "description": "",
            "bullet_points": [],
            "price_data": "",
            "images": []
        }


def get_high_res_image(url: str) -> str:
    replacements = {
        "_SX38_SY50_": "_SL1500_",
        "_SX38_SY50_CR": "_SL1500_",
        "_SX300_SY300_": "_SL1500_",
    }

    for old, new in replacements.items():
        if old in url:
            return url.replace(old, new)

    base, _, ext = url.rpartition('.')
    if ext.lower() in ['jpg', 'jpeg', 'png']:
        return f"{base}_SL1500_.{ext}"
    return url
