# Improved Design

![GitHub contributors](https://img.shields.io/github/contributors-anon/asdub/improved-telegram)
![GitHub top language](https://img.shields.io/github/languages/count/asdub/improved-telegram)
![GitHub language count](https://img.shields.io/website?url=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F)
![GitHub last commit](https://img.shields.io/github/last-commit/asdub/improved-telegram)

**A live version of this project can be found [here](https://improved-design-asdub.herokuapp.com/)**

You can use the following accounts can be used for user and admin access: 


*Admin User*\
User: asdub
Pass: hashb7790

*Standard User*\
User: laryta
Pass: hashb7795

<img src="https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/mobile_mockup.png" width="150" alt="Improved Design on Mobile" />


### Project Description
This is the final project for my software development diploma.

I have created an app to promote the services of a freelance designer. 
Allowing users to purchase custom design services. 
Specifically illustrations/ artwork. 

Users can select from a variety of services, select and enter their desired customisations. 
The user has the option of creating a profile to keep all their orders in one place and view or download their artwork. 
In addition, users receive email notifications regarding the status of their order. 

Site admins can add, edit or delete services. 
And also complete user orders by uploading completed artwork. 

<img src="https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/laptop_mockup.png" alt="Improved Design on Mobile" alt="Improved Design on Desktop"/>


## Contents 

* [User Experience (UX)](#user-experience-ux)
    * [Brief](#Brief)
    * [Project Aims](#the-aim-of-this-project-is-to)
    * [User Stories](#new-user-stories)
* [Design](#design)
    * [Frameworks (front-end)](#frameworks-front-end)
    * [Colours](#colours)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Iconography](#iconography)
    * [Illustrations](#illustrations)
    * [Responsive](#responsiv
    * [App Flow](#appflow)
    * [Database Design](#databasedesign)
    * [Features](#features)
    * [Future Features](#future-features)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [MongoDB & Dataset](#mongodb--dataset)
    * [Frameworks (back-end)](#frameworks-back-end)
    * [Dependencies](#dependencies)
    * [Version Control & Management](#version-control--management)
    * [Software/ Tools Used](#other-software-tools-used)
* [Deployment](#deployment)
    * [Fork](#fork)
    * [Clone (Locally)](#clone-locally)
    * [Heroku](#deploy-on-heroku)
* [Testing](#testing)
    * [W3C HTML](#wc3-html-validator-results)
    * [JS Hint](#js-hint)
    * [PEP8](#pep8)
    * [W3C CSS](#wc3-css-validator-results)
    * [Google Lighthouse](#google-lighthouse)
        * [Initial Test](#initial-test)
        * [Re-Test](#re-test)
    * [Manual Testing](#manual-testing)
        * [Testing Documentaition](https://github.com/asdub/improved-telegram/blob/main/readme/test/TESTME.md)
        * [User Stories Testing](#user-stories-testing)
    * [Known Bugs](#known-bugs)
    * [Credits](#credits)



## User Experience (UX)


### Brief

My intention was to create a simple app that permits the user easy  and considered access to the services being presented.
Users can easily purchase services and check on orders. While administrators can simply complete user orders.
Having previously designed my own layouts and styles, I wanted to use a front-end framework with my own custom styling (and layouts in parts) for this project. 
The app has been built using the [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) front-end framework.


Owing to the services, the user base is likely to be very broad. 
With this in mind the design and layout has been considered to appeal to all age groups and demographics. 


#### The aim of this project is to:
- Be simple and easy to use (as always!)
- Visually pleasing. 
- Provide users with a structured and easy to navigate freelance services. 
- Allow users to purchase a service (Stripe).
- Allow users to customise their service.
- Allow users to manage their address data (CRUD). 
- Provide users with email & on screen notifications regarding their ordered services.
- Provide defensive design in terms of data editing or deletion. 
- Provide seamless login/ registration functionality.
- Allow administrators to manage services. 
- Allow administrators to complete user orders. 

#### Business/ Monetisation
- The app provides an ecomm platform. An unlimited number of products or services can be added to the database. Managed by the administrator.


#### New User Stories
##### General
- I want the app purpose to be obvious or easy to figure out.
- I want to view recent artworks purchased by other users.
- I want to know about the service provider before purchase.
##### Services
- I want to view all available services.
- I want detailed information on each service. 
- I want the ability to search for services by keyword.
- I want to customise each service. 
##### Managing Services
- I want to update my order quantities. 
- I want to remove items from my order.
- I want to see the total cost of each order item. 
- I want to see a breakdown of customisation costs. 
##### Checkout/ Payments
- I want a simple payment process. 
- I want to know of any issues with payment. 
- I want to see payment confirmation and a summary of my order. 
##### Order Success
- I want to know when my order is available. 
- I want to easily access my order. 


#### Returning & Regular User Stories
- I want to view my order history. 
- I want to view the status of my order. 
- I want to view or download my order artwork. 
- I want to update my delivery address.
- I want to be easily able to login, log out and manage my account (password reset etc.)
- I would like the ability to also delete my own recipes. 


#### Site Owner/ Admin Stories
- I would like to add a service. 
- I would like to edit a service.
- I would like to delete a service. 
- I would like to see pending user orders. 
- I would like to complete a user order:
    - with the ability to upload user ordered artwork. 
    - and notify a customer when artwork is available. 



## Design 

### Frameworks (front-end)
The [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) front-end framework was used as the base app. 
With additional custom css. 

The app uses the following Bootstrap content, components & utilities:
- [Grid Layout](https://getbootstrap.com/docs/4.1/layout/grid/)
- [Typography](https://getbootstrap.com/docs/4.1/content/typography/)
- [Images](https://getbootstrap.com/docs/4.1/content/images/)
- [Tables](https://getbootstrap.com/docs/4.1/content/tables/)
- [Forms](https://getbootstrap.com/docs/4.1/components/forms/)
- [Card](https://getbootstrap.com/docs/4.1/components/card/)
- [Dropdowns](https://getbootstrap.com/docs/4.1/components/dropdowns/)
- [Toasts](https://getbootstrap.com/docs/4.3/components/toasts/)
- [Several Utilities Features](https://getbootstrap.com/docs/4.3/utilities/)


### Colours 
A limited palette of colours was used throughout the app. 

**There are four colours used in total throughout the app.**

Purple - *#6b63ff*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/colours/6b63ff.png" width="75" alt="Purple - #6b63ff" />

Grey - *#555555*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/colours/555555.png" width="75" alt="Grey - #555555" />

White - *#ffffff*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/colours/ffffff.png" width="75" alt="White - #ffffff" />

Black - *#000000*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/colours/000000.png" width="75" alt="Black - #000000" />


### Wireframes 

<img src="https://github.com/asdub/improved-telegram/blob/main/readme/wireframes/desktop_home_wire.png" width="400" alt="Wireframes" />
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/wireframes/tablet_products_wire.png" width="200" alt="Wireframes" />
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/wireframes/mobile_account_wire.png" width="150" alt="Wireframes" />

Wireframes were completed for desktop, tablet & mobile devices. 


### Typography

[Google Fonts](https://fonts.google.com/) is in use on this app.

To keep on the simplicity brief,
Only one font is in use:\
**Roboto** in weights of 400 & 600.

<img src="https://github.com/asdub/improved-telegram/blob/main/readme/type_icon/roboto_font.png" width="250" alt="Google Fonts - Roboto" />


### Iconography

All primary icons in this project are from [Noun Project](https://thenounproject.com/).\
With secondary icons from [Font Awesome](https://fontawesome.com/).

The following SVG icons have been used throughout the app:\
<img src="https://github.com/asdub/improved-telegram/blob/main/static/img/noun_checkout.svg" height="60" alt="Noun Project Icons"/>
<img src="https://github.com/asdub/improved-telegram/blob/main/static/img/noun_person.svg" height="60" alt="Noun Project Icons"/>
<img src="https://github.com/asdub/improved-telegram/blob/main/static/img/noun_search.svg" height="60" alt="Noun Project Icons"/>


### Illustrations

All illustrations/ artwork featured on this project are from [unDraw](https://undraw.co/).
An amazing open source project by Katerina Limpitsouni. 

*Example SVG*

<img src="https://github.com/asdub/improved-telegram/blob/main/static/img/portfolio.svg" width="400" alt="unDraw"/>


### Responsive 

The app uses the [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) front-end framework.
Which is fully responsive. Bootstrap uses a 12 column grid system for layout.

The app renders in three layouts for mobile, tablet and desktop. 
Additional css media queries have been included to ensure a consistent experience across device types. 


### App Flow
*App Flow Diagram*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/flow.drawio.png" width="400" alt="App Flow Diagram"/>


Users will initially land at */home*, a single page scroller containing a work/ portfolio section display the 8th most recent completed customer artworks.
And also an about and social contact section.
A large header (in all views) with dropdown navigation allows the user to quickly search, access account facilities and order bag. Dropdown menus allow the users to navigate to individual services, all services, or can sort the services by price, rating and type. 
Home contains a hero banner with a large CTA. Taking the user to an all services view.

Selecting a service takes the user to a detailed view. And features the customisation options available to the user. 
The user can add a service to their order from here. A toast notification will prompt the user to 'View their orders' where they can access their order bag. Or from the shopping card icon within the header. 

In the order bag view, the user can review their orders and customisations. See their item and total pricing. 
And also a breakdown of their customisation costs. A user can amend order quantities and remove items. 
A user can proceed to checkout/ payment from here. 

The checkout view displays an order summary, a customer form and payment facilities. 
Once the user completes their transaction, they are directed to an order success view, which details the order just made. 
A user will also receive an automated email confirming their order.  

A site administrator has access to a management view where they can add new products and check pending orders. 
An admin can access the complete customer order functionality from here. Where an admin can see an overview of pending customer orders. They can upload the customer artwork, once the admin selects complete - the customer will receive an email confirming their artwork is available to download and has been shipped. The email contains a link to view and download the artwork. 
If the user has an account setup they can view their historical orders and artwork (if complete). 

The apps functionality is explored in further detail in the [Features](#features) section below. 


### Database Design

As this app uses the Django web framework , the included default object-relational mapping layer (ORM) is used. 
Django uses SQLite by default Heroku Postgres in production. 

*Database Schema Overview*\
<img src="https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/db_schema.png" alt="Database Schema Diagram"/>

Data is organised around 5 core apps, the models associated with these apps are detailed below. 
The diagram above displays the relationships between these models. 

|  App    |  Model                                      | 
| :---    | :-----------------------------------------  |
| Home    |  Images                                     |
| Checkout|  UserProfile, Product, Order, OrderLineItem |
| Bag     |  Product                                    |
| Products|  Order, Image, Product, Category            |
| Profile |  Order, Image, UserProfile                  |


### Features

Improved Design is an ecommerce app providing users with the following functionality:

**Navigation**
- The app has a dynamic menu structure. Providing a standard horizontal text navbar on medium and large screens, and a hamburger menu with sidebar when used via a small/ mobile screen. Both menus have dropdown submenus. 
- Under /account an unregistered user has the navigation options of: *'Login'* and *'Register'*. 
- Under /account an authorised user has the following options: *'Profile'* and *'Log Out'*
- In addition to the above, an admin user also has access to *'Management'*

**Authentication** - AllAuth
- Users have the ability to register for a user profile.
- The registration process features email verification. 
- AllAuth also provides Login and logout views for the user. 
- A user can reset their password via the 'Forgot Password' hyperlink on the login form. 
- 

**Home** - *(/)*
- The home app contains a single view detailing a hero banner, work portfolio, about and contact sections. 
- The hero banner contains a CTA to the services view.
- Artwork for the work portfolio is generated from the 8 most recent admin completed artworks which have been uploaded. 
- A further CTA is located under the work/ portfolio section. 
- The contact section contains font awesome social media icon links with transition effects
- An app wide footer detailing copyright and links to terms & Conditions/ privacy policy. Improved design branding is also included. 

**Services** - *(services/)*
- The services view lists individual services in the form of service cards. 
- Service cards contain representational artwork, title, cost and rating. 
    - If authenticated as an admin, the options to edit and delete the service will also appear on the card.
 - A user can also filter & sort the services based on Price, Name & Category. In both ascending or descending order.

**Services Detail** - *(services/<product_id>)*
- Upon selecting a service on the Services View, the service detail view is rendered. 
- This view contains additional information in the form of a description and responsive image of the representational artwork.
- The user can also specify how they wish to customise their artwork, they can:
    - Choose the quantity
    - Detail their requirements
    - Choose a size
    - Provide text content
    - Choose a colour profile
- An 'Add to Order' button allows the user to add the order to their order bag. 
- Or return to the all services view.
- When an item is added to an order, a notification will appear inviting the user to 'View all Orders'

**Orders/ Bag** - *(orders/)*
- This view lists all the current orders the user has added. 
- Each order item is listed with the following data:
    - Service Image
    - Title
    - SKU
    - Size
    - Colour Profile
    - User customisations:
        - Requirements / Request
        - Text Content
    - Item Cost
    - Item Quantity 
    - Subtotal
- The user can amend quantities or remove an item in this view. 
- An order total, delivery cost and Grand Total is displayed under the list of order items. 
- A cost breakdown is also provided where the price has changed due to user customisations. 
- The user can proceed to checkout/ payment or return to the all services view via the buttons under the order view. 


**Checkout** - *(checkout/)*
- The checkout view provide the user with a form requiring their, 
    - Full Name, Email Address, Phone Number, Address and Credit Card Information. 
- If authenticated, an option to store the address information is made available. 
- A brief order summary of the users order items is display containing:
    - Service Image, Title, Size, Quantity and Item Subtotal.
    - The Order Total, Delivery Costs and Grand Total. 
- Payment processing is done with stripe - to test, use '4242 4242 4242 4242', an expiry date in the future, any 3-digit CCV code and a five digit postcode. 
- A user can complete their order and make payment by selecting the 'Complete Order' button.
- If there are any issues with payment a toast notification will appear.
- Stripe webhooks are used to complete the order and create the database entry should the user close the page or technical issues. 

**Checkout Success** - *(checkout_success/)*
If the payment is successful the user will be directed to the checkout success view. 
- This view confirms the successful order and order number. 
- Advises user of email confirmation sent. 
- Saves the user's delivery information, if selected. 
- Attaches the order to the UserProfile, if created/ exists. 
- A toast notification will also appear confirming the order, and presenting the user with the order number. 
- A CTA is located at the bottom of this view, directing the user back to the all services view. 
- If accessed from the 'View Order' button within profie views (detailed below), this CTA return the user to their profile.


**Account/ Profile** - *(account/)*
Once authenticated a user will have a 'Profile' option within the account dropdown menu. 
- The profile view displays the user's saved address. 
    - A user can also update this information from this view. 
- The profile view displays the dusers orders and status.
    - Completed orders are listed first, the user has the option to view their artwork. 
- The user can also view their original order confirmation.


**Artwork** - *(artwork/)*
- Accessed from the profile view above and also via URL sent to the user when an administrator completes their order. 
- Displays any artwork images associated with the order. 
- And two options to download and view the artwork. 


**Management** - *(add/)*
If a user is authenticated as an administrator a management option is available in the account dropdown. 
- In this view an admin can add additional services/ products. 
- View pending orders. 
- Access the customer order completion view. 


**Customer Order** - *(customer_order/<order_id>)*
An administrator can review a customer's order and upload artwork to the order. 
Upon selecting complete, the user will receive an email containing a link to view and download their artwork. 
And the administrator will be redirected back to the add service/ pending orders view. 


### Future Features 

#### Expand Customisation Fields
In a future version I would like to add more interactive customisation fields. Giving a user the ability to select colours. Draw shapes. 
And provide a mood board they could add images, colour swatches etc to. 

#### Security/ Authorisation
I would like to improve security on the app. 
And setup sign-in with social media/ gmail functionality to streamline the registration process. 

#### Admin Dashboard    
I would like to expand on the current offering to include:
    - Daily, Weekly, Monthly sales data. 
    - Apply the same breakdown to the number of services sold. 
    - Display metrics regarding registered users, active users. 

#### Order Abandonment 
In conjunction with the streamlined registration process, I would like to collect data and present metrics to the admin detailing order abandonment. 


## Technologies

### Languages
- **[HTML5](https://html.com/html5/)**
- **[CSS3](https://www.w3schools.com/css/)**
- **[Javascript](https://www.javascript.com/)**
- **[Python](https://www.python.org/)**
- **[Django template language](https://docs.djangoproject.com/en/3.2/ref/templates/language/)** (templating language)


### Django
Django is an open source framework for web development in Python. It is a flexible web development tool that can be used to create almost any type of website or app that is needed. Thanks to it's high usage, and extensive packages - there is often no need 'to reinvent the wheel' when deploying apps. And trusted and proven code can be used to deploy your project. 

Django's most powerful feature is its object-relational mapper (ORM), allowing the interaction with a database in a pythonic way - with no need need for SQL queries. 

Check out the [database schema](#databasedesign) above to see how this apps database is structured. 

The following Django dependencies apply to this app:
- **[asgiref](https://pypi.org/project/asgiref/)**
- **[boto3](https://pypi.org/project/boto3/)**
- **[botocor](https://pypi.org/project/botocore/)**
- **[dj-database-url](https://pypi.org/project/dj-database-url/)**
- **[Django](https://pypi.org/project/Django/)**
- **[django-allauth](https://pypi.org/project/django-allauth/)**
- **[django-countries](https://pypi.org/project/django-countries/)**
- **[django-crispy-forms](https://pypi.org/project/django-crispy-forms/)**
- **[django-storages](https://pypi.org/project/django-storages/)**
- **[gunicorn](https://pypi.org/project/django-gunicorn/)**
- **[jmespath](https://pypi.org/project/jmespath/)**
- **[oauthlib](https://pypi.org/project/oauthlib/)**
- **[Pillow](https://pypi.org/project/Pillow/)**
- **[psycopg2-binary](https://pypi.org/project/psycopg2-binary/)**
- **[PyJWT](https://pypi.org/project/PyJWT/)**
- **[python3-openid](https://pypi.org/project/python3-openid/)**
- **[requests-oauthlib](https://pypi.org/project/requests-oauthlib/)**
- **[s3transfer](https://pypi.org/project/s3transfer/)**
- **[sqlparse](https://pypi.org/project/sqlparse/)**
- **[stripe](https://pypi.org/project/stripe/)**


## Deployment

#### Fork
1. [Login](https://github.com/login) to your GitHub account([or join](https://github.com/join)).
2. Go to the repo by clicking [here](https://github.com/asdub/5km-parks-MP2).
3. Click fork in the top right corner of the screen. 

#### Clone (Locally)
1. [Login](https://github.com/login) to your GitHub account([or join](https://github.com/join)).
2. Go to the repo by clicking [here](https://github.com/asdub/5km-parks-MP2).
3. On the main page of the repository click on 'Code'. 
4. Click on the 'Clipboard'/ copy the clone URL (Clone with HTTPs). 
4. In your local environment open your terminal, navigate to or create a directory.
5. Paste the URL into your terminal and enter. The repo should be successfully cloned.  

#### Deploy on Heroku
Deploying the app on heroku is very straight forward. 