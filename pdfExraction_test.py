from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PyPDF2 import PdfReader
import io
import requests

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the PDF URL in the web browser
driver.get("https://www.africau.edu/images/default/sample.pdf")
driver.maximize_window()

# Get the current URL
urlString = driver.current_url

# Create a URL object
url = requests.get(urlString)

# Load the PDF document from the URL
pdfdocument = PdfReader(io.BytesIO(url.content))

# Print the number of pages in the PDF
print(len(pdfdocument.pages))

# Extract text from the first page of the PDF
for i in range(2):
    docText = pdfdocument.pages[i].extract_text()
    print(docText)

# Print the extracted text

# Close the PDF document and quit the WebDriver
# driver.quit()

