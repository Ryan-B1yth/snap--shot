## Credits
[Memory Box](https://memory-box.co.uk/blog/picture-frame-size-guide/)
[Smasking Logo](https://smashinglogo.com/en/)

<!-- Add a warning to superuser that states an image cannot be changed after publication. -->

# SnapShot

**Disclaimer: Do not use your own credit/debit card to purchase anything from this website - no orders will be fulfilled. This site was created as a course project and will not ship any orders although you may still be charged. If you wish to test the purchasing feature please use the following card details:**

```
Card number: 4242 4242 4242 4242 
Expiry date: 4/24
CVC: 242
ZIP: 42424
```
***

SnapShot is an E-commerce store where users can browse and search for art, both digital and physical, which they can purchase using Stripe Payments. The conception of this project was for a Milestone 5 project for Code Institute. 

You can view the live project [here](https://snap-shot-store.herokuapp.com/).


![4 screen sizes image of the site]()

## Contents 

- [User Experience (UX)](#user-experience-ux)
   * [User Stories](#user-stories) 
      + [Current Features](#current-features)
      + [Features to implement in the future](#features-to-implement-in-the-future)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
     + [Colour Scheme](#colour-scheme)
     + [Typography](#typography)
     + [Imagery](#imagery)
     + [Design Choices](#design-choices)
- [Technologies](#technologies)
   * [Languages used](#languages-used)
   * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

- [Challenges](#challenges)

- [Testing](#testing)
   
- [Deployment](#deployment)
   * [Creation](#creation)
   * [Forking](#forking)
   * [Clone](#clone)
   * [Setting up AWS](#setting-up-aws)
   * [Setting Up Stripe](#setting-up-stripe)
   * [Setting Up Project](#setting-up-project)
   * [Heroku Deployment](#heroku-deployment)

- [Credits](#credits)
   * [Code](#code)
   * [Content](#content)
   * [Media](#media)
   * [Acknowledgements](#acknowledgements)


## User Experience (UX)

   ### User Stories

   - #### Unregistered Visitor
     - As an unregistered user, I want to be able to: 
        - View all products so that I can select items to purchase.
        - View a selection of products by category so that I can narrow my search by type.
        - See all a product's detail so that I can find the price, select a size, and read the description of a product.
        - Search for specific products so that I can find exactly what I am looking for.
        - Filter by rating and price so that I can shop for the best items.


   - #### First Time Visitor (in addition to above)
     - As a first time user, I want to be able to:
       - Navigate the site easily and intuitively.
       - Find what I am looking for easily. 
       - Keep track of my basket total so I do not overspend.
       - Add and remove item's from my basket so I can make sure I have the correct items, sizes, and quantities.
       - Checkout easily and be sent confirmation of my purchase to my email.


   - #### Registered Returning Visitor Goals
     - As a registered user, I want to be able to:
       - Save my checkout information so I can purchase items easier the next time I visit the site.
       - Sign up to a news letter so that I can be told about special offers and savings.
       - Update my information when it changes so that my items are aways delivered to the correct address.
       - Recieve an email to verify my registration so that I can be sure I have an account.
       - Change and recover my password so I do not have to create a new account if I forget it.
       - Access a profile so that I can view my order history, confirmations, and payment information.

   - #### Superuser goals
     - As a superuser / admin, I want to be able to:
       - Add, edit, and remove items from the site so that I can sell more products and remove the products that are not being sold to improve revenue.

       <!-- Add screenshot of excel user stories here -->


   ### Current features 

-   Responsive design to work on all screens
-   Accessibility
-   Easy to navigate (Single use learning)
-   Interactive elements
-   Social Links
-   Logged in / out status changes for a user depending on their current status.
-   Able to search products by keywords.
-   Able to view products using predefined filtes including price, rating, and category.
-   'Back to top' button.
-   Logged in user can save an address for future purchases.
-   A user profile so a logged in user can update their information as and when it changes.
-   Admin / superuser has full CRUD control of the site.
-   Confirmation emails for registration and purchase.

   ### Future features


### Structure

#### Category

| name | friendly_name |
|------|---------------|
| physical | Physical |
| digital | Digital |

#### Product

| category | name | description | price | rating | image_url | image | sizes | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| ForeignKey(Category) | CharField | TextArea | DecimalField | DecimalField | URLField | ImageField | BooleanField |

#### Order 

| order_no | user_profile | name | email | phone_number | country | county | city | address_1 | address_2 | postcode | delivery_amount | order_amount | grand_total | date | original_basket | stripe_pid | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| CharField | ForeignKey(Profile) | CharField | CharField | CharField | CharField | CharField | CharField | CharField | CharField | CharField | DecimalField |  DecimalField |  DecimalField | DateTimeField | TextField | CharField | 

#### OrderLineItem 

| order | product | product_size | quantity | lineitem_total | 
| --- | --- | --- | --- | --- |
| ForeignKey(Order) | ForeignKey(Product) | CharField | IntegerField | DecimalField | 

### WireFrames 


### Color Scheme
    
- The color scheme follows a similar color scheme to an earlier project of mine: Be Mindful. A simplistic off-white and grey color scheme with just the pops of color from the images used for the products accent the interactable portions of the site. The product detail pages have the product image as a blurred backdrop to darken the page slightly which emphasizes the white boxes that contain the product information. 

        
### Typography

- The main font used throughout the site is Barlow fron Google Fonts which was chosen for its simplistic typeface. The site has a clear purpose and the typeface should not get in the way of that. As such Barlow is easy to read and is typed in a color the easily contrasts the background to that all the informaiton is easily accessable.

### Imagery

- As discussed later, all the imagery was generated by DALLE which takes a prompt and generates images based off its AI.

### Design Choices
 
## Technologies 

### Languages Used

-   HTML5
-   CSS3
-   JavaScript
-   Python and Django

### Frameworks, Libraries and Programs Used

- [Bootstrap v4.6.0](https://getbootstrap.com/docs/4.6.0/getting-started/introduction/)
- [Google Fonts](https://fonts.google.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Am I responsive](http://ami.responsivedesign.is/)
- [Chrome devtools](https://developer.chrome.com/docs/devtools/)
- [jQuery](https://jquery.com/)
- [Heroku](https://dashboard.heroku.com/apps)
- [Postgres](https://www.postgresql.org/)
- [Django](https://www.djangoproject.com/)
- [Stripe](https://stripe.com/gb)
- [Django Secret Key Generator](https://djecrety.ir/)
- [AWS](https://aws.amazon.com/)

## Challenges 

## Testing

Testing and results can be found [here](TESTING.md)

## Deployment

 - ### Creation 

  - ### Forking

  - ### Clone

- ### Setting Up Project
 
- ### Setting up AWS
   
- ### Setting up Stripe

- ### Heroku deployment

## Credits

### Code

- All code was written by the developer with help from Code Institute and specifically their [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) project.

### Content

-  All content was written by the developer.
    
-   README and TESTING layout developed through an amalgamation of my previous projects, [Code Institutes](https://github.com/Code-Institute-Solutions/SampleREADME) guidence, as well as [Natalie Kate Alexander's](https://github.com/natalie-kate/music_to_my_ears) 'Music to my Ears' project.

### Media

- All images used in this project were generated by [DALLE](https://huggingface.co/spaces/dalle-mini/dalle-mini).
 
### Acknowledgements
