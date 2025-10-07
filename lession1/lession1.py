from bs4 import BeautifulSoup

# Simpler html version
html_content = '<html><body><div id="main"><h1>Welcome</h1><p>Learn web scraping.</p></div></body></html>'

# Complex version( more organized )
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

# Printing the children and parents
children = main_div.children

# Printing the children
print("Children of the main div")

for child in children:
    print(child) # printing h1 tag and 2 p tag.
    
    
# Accessing the parents of the main div.
parents = main_div.parent

# printing the parents of the main div
print("\n Parents of the main div")

print(parents.name)

