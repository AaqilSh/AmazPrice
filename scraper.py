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
        price = driver.find_element(By.XPATH, "//span[@class='a-price-whole']").text.strip()

        return {
            "title": title,
            "price": price
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()

if __name__ == "__main__":
    product_url = "https://www.amazon.co.uk/Google-Fitbit-tracking-management-features/dp/B0CGX9JPWY/ref=pd_ci_mcx_mh_pe_im_d1_hxwPPE_sspa_dk_det_cao_p_0_0?pd_rd_i=B0CGX9JPWY&pd_rd_w=lKb7Z&content-id=amzn1.sym.7d048aad-7058-4131-afb2-93865dd4fb90&pf_rd_p=7d048aad-7058-4131-afb2-93865dd4fb90&pf_rd_r=05PXCQMG00DBQPRKND5G&pd_rd_wg=99gvb&pd_rd_r=898d69d5-0f5d-4519-aa60-5a5e6a1cb1f5&th=1"  
    data = get_amazon_price(product_url)
    print(data)
