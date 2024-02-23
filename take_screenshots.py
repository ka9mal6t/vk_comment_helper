from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


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

    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Take screenshots
    driver.get_screenshot_as_png()
    driver.save_screenshot(f"screenshots/{url.split('https://vk.com/')[-1]}.png")

    # Close browser
    driver.quit()

