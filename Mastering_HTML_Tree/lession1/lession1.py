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

# Using `find_next_sibling` and `find_previous_sibling` to Navigate Sibling Nodes

# Finding the first paragraph.
first_p = soup.find('div', id="main").find('p')
print('First paragraph tag:', first_p)

# Finding the second paragraph.
second_p = first_p.find_next_sibling()
print('Second paragraph tag:', second_p)

# finding the first sibling from the second
first_p_from_second_p = second_p.find_previous_sibling()
print('First paragraph tag from second paragraph:', first_p_from_second_p)

