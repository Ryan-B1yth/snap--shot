# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [JS validation](#jshint-javascript-validator)
      * [PEP8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
      * [Unit testing](#unit-testing)
    - [Manual testing](#manual-testing)
   - [Testing User Stories](#testing-user-stories)
   - [Bugs](#bugs)


## Automated Testing

- Every file in this project was subjected to its file type's respective validator and passed 100% as seen below. Not all results are displayed as many of them look exactly the same however I have picked the files with the largest / more complex code base to demonstrate their results. 

### [W3C Markup Validator](https://validator.w3.org/) 

- Below are the results for the main pages of the site. The home page, products page, product detail page, product edit page, and profile page were chosen to display the main functional pages of the site. The final image is a screenshot of all the errors the validator threw for the checkout page. This is there to show the only errors that were being thrown when pages had to be tested through direct text input.

  - Validation before

    ![HTML Validation Before](static/assets/documentation/images/html_validation_before.png)

  - Validation after

    ![HTML Validation After](static/assets/documentation/images/html_validation_after.png)

  - Products before

    ![HTML VProducts before](static/assets/documentation/images/html_validation_products_before.png)
  
  - Products after 

    ![HTML PProducts after ](static/assets/documentation/images/html_validation_products_after.png)

  - Product detail 

    ![HTML Product detail](static/assets/documentation/images/html_validation_product_detail.png)

  - Product edit

    ![HTML Product edit](static/assets/documentation/images/html_validation_product_edit.png)

  - Profile

    ![HTML Profile](static/assets/documentation/images/html_validation_profile.png)
  
  - Checkout 

    ![HTML Checkout](static/assets/documentation/images/html_validation_text_input.png)


### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 

- Again, below are the results for some of the larger, more complex CSS file.

  - styles.css

  ![Styles CSS](static/assets/documentation/images/styles_css_validation.png)

  - products.css

  ![Products CSS](static/assets/documentation/images/products_css_validation.png)
  
  - product_detail.css

  ![Product Detail CSS](static/assets/documentation/images/product_detail_css_validation.png)

  - product_review.css

  ![Product Review CSS](static/assets/documentation/images/product_review_css_validation.png)

  - testimonies.css

  ![Testimonies CSS](static/assets/documentation/images/testimonies_css_validation.png)
     
### [JSHint JavaScript Validator](https://jshint.com/) 

- The JavaScript in this project was separted into very small files for their respective pages containing perhaps a single function. The largest three files with complex functionality are shown below.

  - Products

  ![Products JS](static/assets/documentation/images/products_js_validation.png)

  - Product detail

  ![Product detail JS](static/assets/documentation/images/product_detail_js_validation.png)

  - Stripe

  ![Stripe elements JS](static/assets/documentation/images/stripe_elements_js_validation.png)

    
### [PEP8 Validator](http://pep8online.com/)

- Lighthouse Scores
  
  - Home page

  - Product page

  - Product detail page

  - Form pages

    
## Unit Testing 
  - Automated testing was done for some of the project. Forms, models, and views were tested in each app that used a significant amount of code in these files. 

  ![Coverage Report](static/assets/documentation/images/coverage_report.PNG)

  - A coverage report of the project gave a 68% coverage.

## Testing User Stories 

<!-- Using excel spreadsheet numbers, input screenshots of each repective page -->
      
## Manual Testing

- Manual testing of the site was undertaken at every step of development. 

- All URLs were followed to ensure they resolved correctly. An error message page is displayed to a user who tries to navigate to a page they shouldn't have access to and allows them to navigate back to the home page.

- All CRUD functionality on the user end was tested manually. As only the superuser will have access to CRUD functionality, only the superuser can access site management, and add, edit, and delete products from the site.

- Forms have validation and will not post data if any errors are raised.

- The site was tested on Google Chrome using their developer tools and viewed on Firefox, Microsoft Edge, and Safari to ensure it worked across multiple platforms. The site was also viewed on multiple devices of varying screen sizes to ensure its responsive design works as expected. 


## Bugs

  