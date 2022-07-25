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

- [W3C Markup Validator](https://validator.w3.org/) 

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
     
- [JSHint JavaScript Validator](https://jshint.com/) 
    
- [PEP8 Validator](http://pep8online.com/)

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

  