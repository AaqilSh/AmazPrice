from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_amazon_price(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)  # Loading time for page

        # Get product title
        title = driver.find_element(By.ID, "productTitle").text.strip()

        # Get product price
        price = driver.find_element(By.CLASS_NAME, "a-offscreen").text.strip()

        return {
            "title": title,
            "price": price
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()
