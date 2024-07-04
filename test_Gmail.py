import pytest
import selenium
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_gmail():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://www.gmail.com/#/login")

    #   login to gmail
    #   give username and click next
    user_name = driver.find_element(By.XPATH, "//input[@id='identifierId']")
    user_name.send_keys(os.getenv("EMAIL"))
    next_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
    next_btn.click()
    time.sleep(10)

    #   give password and click next
    password = driver.find_element(By.XPATH, "//input[@name='Passwd']")
    password.send_keys(os.getenv("PASSWORD"))
    next_btn1 = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
    next_btn1.click()
    time.sleep(20)

    #   click on compose mail
    compose = driver.find_element(By.XPATH, "//div[contains(text(),'Compose')]")
    compose.click()
    time.sleep(10)

    #   give email address,subject and message body
    to_fields = driver.find_element(By.XPATH, "//input[@class='agP aFw']")
    to_fields.send_keys(os.getenv("EMAIL"))
    subject_box = driver.find_element(By.XPATH, "//input[@name='subjectbox']")
    subject_box.send_keys("Test Mail")
    message_body = driver.find_element(By.XPATH, "//div [@aria-label='Message Body']")
    message_body.send_keys("Test Email Body")

    # Click on More options (three dots)
    more_button = driver.find_element(By.XPATH, "//div[@aria-label='More options']")
    more_button.click()

    # Click on Label as > Social
    label = driver.find_element(By.XPATH, "//div[text()='Label']")
    label.click()

    social = driver.find_element(By.XPATH, "//div[@class='J-LC-Jz'][normalize-space()='Social']")
    social.click()
    time.sleep(2)  # Wait for label to be applied

    more_button = driver.find_element(By.XPATH, "//div[@aria-label='More options']")
    more_button.click()
    label = driver.find_element(By.XPATH, "//div[text()='Label']")
    label.click()
    time.sleep(2)
    star = driver.find_element(By.XPATH, "//div[contains(text(),'Add star')]")
    star.click()
    time.sleep(2)
    #   send email and received in  inbox
    send_key = driver.find_element(By.XPATH, "//div[text()='Send']")
    send_key.click()
    time.sleep(20)

    inbox_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Inbox')]")
    inbox_btn.click()
    # Open the received email
    # inbox_email = driver.find_element(By.XPATH, "//span[text()='Test Mail']")
    inbox_email = driver.find_element(By.XPATH, "//tr[@class='zA zE'][1]")
    inbox_email.click()

    time.sleep(5)  # Wait for email to open

    # Verify the subject
    subject_received = driver.find_element(By.XPATH, "//h2[@class='hP']")
    assert subject_received.text == 'Test Mail'

    # Verify the body
    email_body = driver.find_element(By.XPATH, "//div[@class='a3s aiL ']")
    assert email_body.text == 'Test Email Body'

    """more_email_option_button = driver.find_element(By.XPATH, "//div[@aria-label='More email options']")
    more_email_option_button.click()
    # Verify the label "Social"
    labels = driver.find_elements(By.XPATH, "//div[@id=':1u5']//span[@class='J-Ph-hFsbo'][contains(text(),'►')]")
    """
    labels = driver.find_elements(By.XPATH, "//span[@class='J-J5-Ji']")
    for label in labels:
        print(label.text)
    assert (label.text == 'Social' for label in labels)

    time.sleep(5)
    driver.quit()
