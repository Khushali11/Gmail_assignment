from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Function to login to Gmail
def login_to_gmail(driver, username, password):
    driver.get("https://mail.google.com")
    driver.find_element(By.NAME, "identifier").send_keys(username)
    driver.find_element(By.ID, "identifierNext").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()


# Function to compose and send an email
def compose_email(driver, to_email, subject, body):
    driver.find_element(By.CSS_SELECTOR, "div.T-I.T-I-KE.L3").click()  # Click on Compose button
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "to"))).send_keys(to_email)
    driver.find_element(By.NAME, "subjectbox").send_keys(subject)
    driver.find_element(By.CSS_SELECTOR, "div.Am.Al.editable.LW-avf.tS-tW").send_keys(body)
    driver.find_element(By.CSS_SELECTOR, "div.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()  # Click on Send button


# Function to label an email as "Social"
def label_email(driver, label_name):
    time.sleep(2)  # Wait for the email to arrive
    driver.find_element(By.CSS_SELECTOR, "div.Cp").click()  # Click on the email
    time.sleep(2)  # Wait for email to open
    driver.find_element(By.CSS_SELECTOR, "div.T-I.J-J5-Ji.ar7.T-I-atl.L3").click()  # Click on More options
    driver.find_element(By.CSS_SELECTOR, "div.J-M-Jz:nth-child(2)").click()  # Click on Label as
    driver.find_element(By.XPATH, f"//div[text()='{label_name}']").click()  # Select the label


# Function to mark an email as starred
def mark_email_as_starred(driver):
    time.sleep(2)  # Wait for the email to load
    driver.find_element(By.CSS_SELECTOR, "div.Cp").click()  # Click on the email
    time.sleep(2)  # Wait for email to open
    driver.find_element(By.CSS_SELECTOR, "div.T-I.J-J5-Ji.ar7.T-I-atl.L3").click()  # Click on More options
    driver.find_element(By.CSS_SELECTOR, "div.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()  # Click on Star


# Function to verify email details
def verify_email(driver, expected_label, expected_subject, expected_body):
    time.sleep(2)  # Wait for the email to load
    label = driver.find_element(By.CSS_SELECTOR, "div.vR span")
    subject = driver.find_element(By.CSS_SELECTOR, "h2.hP")
    body = driver.find_element(By.CSS_SELECTOR, "div.a3s div")

    assert label.text == expected_label, f"Expected label: {expected_label}, Actual label: {label.text}"
    assert subject.text == expected_subject, f"Expected subject: {expected_subject}, Actual subject: {subject.text}"
    assert body.text == expected_body, f"Expected body: {expected_body}, Actual body: {body.text}"


# Main script
def test_mail():
    username = "******@gmail.com"
    password = "*********"
    to_email = "**********@gmail.com"
    subject = "Test Mail"
    body = "Test Email Body"
    label_name = "Social"

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Perform the tasks
        login_to_gmail(driver, username, password)
        compose_email(driver, to_email, subject, body)
        label_email(driver, label_name)
        mark_email_as_starred(driver)

        # Logout (optional, you can extend the script to logout if needed)

        # Verify email details
        verify_email(driver, label_name, subject, body)

    finally:
        # Close the browser
        driver.quit()
