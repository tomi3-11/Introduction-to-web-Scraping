from bs4 import BeautifulSoup

html_content = """
<html>
<body>
    <div id="main">
        <h1>Welcome </h1>
        <p>Learn we scraping. </p>
        <p>It's a useful technique.</p>
    </div>
</body>
</html>

"""

soup = BeautifulSoup(html_content, 'html.parser')

main_div = soup.find('div', id='main')

# Printing the div
print("main div content")
print(main_div.prettify())
