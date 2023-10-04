'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver and open the login page
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://github.com/login")
    yield driver
    # After the test, close the browser
    driver.quit()

def test_login(driver):
    # Find the username and password input fields and the login button
    username_field = driver.find_element(By.ID, "login_field")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.NAME, "commit")

    # Enter login credentials
    username_field.send_keys("nikhil.grandhi@kanerika.com")  # Replace with your username
    password_field.send_keys("Nikhil@5775")  # Replace with your password

    # Click the login button
    login_button.click()

    # Check if the login was successful by verifying the title
    assert "GitHub" in driver.title
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import PyPDF2

@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome WebDriver using your provided code
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    # After the test module, close the WebDriver
    driver.quit()

def extract_text_from_pdf(pdf_url):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_url)

    # Read the text from each page
    pdf_text = ''
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_text += page.extractText()

    return pdf_text

@pytest.mark.parametrize("pdf_url", ["https://www.africau.edu/images/default/sample.pdf"])  # Replace with your PDF URL
def test_extract_pdf_text(driver, pdf_url):
    # Open the PDF URL in the web browser
    driver.get(pdf_url)

    # Use JavaScript to extract the PDF content from the browser
    pdf_content = driver.execute_script("return document.body.innerText")

    # Extract text from the PDF content
    extracted_text = extract_text_from_pdf(pdf_content)

    # Perform assertions or data processing as needed
    assert "Your Expected Text" in extracted_text  # Replace with your expected text

