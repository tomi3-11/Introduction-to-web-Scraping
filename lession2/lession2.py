# Lession 2
"""
1. Mastering CSS Selectors with BeautifulSoup in Python Web Scraping

    Welcome! In this lesson, we're going to focus on Using CSS Selectors
    in BeautifulSoup. CSS Selectors are a powerful tool that allow you to
    pinpoint and extract precise information from a web page. Not only will
    you learn about the role of CSS selectors in web scraping, but also how
    to use these selectors with BeautifulSoup to scrape data effectively from
    a webpage using the power of Python.
    
    ```<div class="product">Product A</div>
       <div id="special">Product B</div>```
       
    .product {
    color: blue;
    font-size: 16px;
    }

    #special {
        color: red;
    }
""" 

# Using CSS Selectors with BeautifulSoup
"""
    Now that you understand the concept of CSS selectors, let's dive into how you
    can use them with BeautifulSoup.

    BeautifulSoup's .select() method allows us to use CSS selectors to grab elements
    from an HTML document. The select() method returns a ResultSet object containing
    all the elements that match the CSS selector.

    Take a look at our solution code to see how select() is used in practice:
"""

from Bs4 import BeautifulSoup

html_content = """
<div class="products">
    <div class="product">
        <p>Product 1</div>
    </div>
    <div class="product" id="special">
        <p>Product 2</p>
    </div>
    <div>
        <p>Another Item </p>
    </div>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class 'product'
products = soup.select('.product')
for product in products:
    print(product.p.text)
    
"""
Similarly we can select elements based on their ID. 
For example, #special will select the element with ID "special".
"""

special_product = soup.select('#special')
print(special_product[0].p.text) # Output: Product 2

# CSS Selectors – Parent-Child Relationships and Nested Selectors

# Select direct child paragraphs of div with id Parent
child_para = soup.select('#Parent > .child')
print(child_para)

super_nested_by_id = soup.select('#Parent > #super-nested')
print(super_nested_by_id)
