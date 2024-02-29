from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def take_screenshots(url: str):
    create_directory_if_not_exists("screenshots")
    options = webdriver.ChromeOptions()

    options.headless = True  # disable headless mode
    options.add_argument(f"user-agent=Mozilla/5.0")
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Web driver (Chrome)
    driver = webdriver.Chrome()

    # Upload page
    driver.get(url)

    # Scroll
    elements = driver.find_elements(By.CSS_SELECTOR, ".reply.reply_dived.clear._post")
    driver.execute_script("arguments[0].scrollIntoView(false);", elements[0])

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of(elements[0]))

    # JavaScript код для скрытия элемента с заданным классом
    js_code = """
    var element = document.querySelector('.PageBottomBanner');
    if (element) {
        element.style.display = 'none';
    }
    """

    # Выполнение JavaScript кода
    driver.execute_script(js_code)

    # Take screenshots
    driver.get_screenshot_as_png()
    driver.save_screenshot(f"screenshots/{url.split('https://vk.com/')[-1]}.png")

    # Close browser
    driver.quit()
