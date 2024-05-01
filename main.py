import os
from datetime import date

try:
    from selenium import webdriver
except ImportError:
    os.system("pip install selenium")
    from selenium import webdriver

try:
    import discord
except ImportError:
    os.system("pip install discord")
    import discord

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


url = 'https://longap.com/product/longap-one/'


def by_ref_click(enterloc, enterref):
    found = False
    while not found:
        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((enterloc, enterref))
            )
            found = True
        except NoSuchElementException:
            time.sleep(0.5)
        finally:
            found1 = False
            while not found1 and found == True:
                try:
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    element.click()
                    found1 = True
                except ElementNotVisibleException:
                    time.sleep(0.5)
                except StaleElementReferenceException:
                    time.sleep(0.5)
                except TimeoutException:
                    time.sleep(0.5)


def worker():
    error = False
    while error is False:
        try:
            driver.delete_all_cookies()
            driver.get(url)
            by_ref_click(By.XPATH, '//*[@id="power-adapter"]')
            select = Select(driver.find_element_by_xpath(
                '//*[@id="power-adapter"]'))
            time.sleep(0.5)
            select.select_by_value('UK')
            error = True
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        ".//*[contains(text(),'Out of stock')]"))
            )
            print("Out of Stock")
            error = False
        except NoSuchElementException:
            time.sleep(0.5)
        except ElementNotVisibleException:
            time.sleep(0.5)
        except StaleElementReferenceException:
            time.sleep(0.5)
        except TimeoutException:
            time.sleep(0.5)

        finally:
            if error is True:
                print("In Stock")
                DM_BOT()


def DM_BOT():
    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        channel = client.get_channel(839668365311082547)
        for i in range(100):
            await channel.send('Final Testing')

    client.run('ODM5MzgwMzAyMTk5NjUyMzUy.YJIz0g.2rNP_WN8_g_HjUBP3F_2A4Xvf9g')


if __name__ == '__main__':
    print("------------Created By SNIPER-------------")
    options = Options()
    # options.add_experimental_option(
    #     'excludeSwitches', ['enable-automation', 'ignore-certificate-errors'])
    # options.add_experimental_option(
    #     "prefs", {"profile.managed_default_content_settings.images": 2})
    # options.add_argument('no-sandbox')
    # options.add_argument('--disable-shm-usage')
    options.headless = True
    driver = webdriver.Chrome(options=options)
    worker()