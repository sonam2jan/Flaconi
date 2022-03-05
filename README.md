# Flaconi
Test data:
URL: https://www.flaconi.de/
1) Main navigation menu - check if all links from the main navigation menu are valid links and return 
200 HTTP response status codes
a) Hover over MAKE-UP main nav menu
b) Check status code for all sub-links
************************************
Automation is done using Python Selenium.
Below libraries are used:
    selenium
    selenium.webdriver.common.action_chains (to mouse over)
    requests (to fetch the status code)
    advertools (to get all the links)
    pandas (store the links in csv)
 
 *************************************
 2) Select a random product under PARFUM main nav 
menu and add the product to the cart
a) Navigate to PARFUM category
b) Select a random product from the category 
page
c) Add product to the cart
d) Navigate to the Cart page
e) Enter the following code “abc123” to 
Gutscheincode field
f) Assert that the following error is displayed “Es tut 
uns Leid! Der Gutscheincode ist nicht verfügbar.”


 *************************************
Automation is done using Python Selenium.
Below libraries are used:
  time
  unittest(for assert)
