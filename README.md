# Improved Design

![GitHub contributors](https://img.shields.io/github/contributors-anon/asdub/improved-telegram)
![GitHub top language](https://img.shields.io/github/languages/count/asdub/improved-telegram)
![GitHub language count](https://img.shields.io/website?url=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F)
![GitHub last commit](https://img.shields.io/github/last-commit/asdub/improved-telegram)

**A live version of this project can be found [here](https://improved-design-asdub.herokuapp.com/)**

The following accounts can be used for user and admin access: 


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
Specifically illustrations/ artwork in the form of Icons, Logos, Posters and general Custom Artwork.

Users can select from a variety of design services, select and enter their desired customisations. 
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
    * [Responsive](#responsive)
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
    * [AWS](#aws-setup)
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

My intention was to create a simple app that permits the user easy and considered access to the design services being presented.
Users can easily navigate and purchase design services and check on an orders status. While administrators can easily complete user orders, via an upload feature.

Having previously designed my own layouts and styles, I wanted to use a front-end framework with my own custom styling (and layouts in parts) for this project. The app has been built using the [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) front-end framework.


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
Deploying the app on Heroku is very straightforward. 


*Initial Heroku Setup*

Go to [Heroku](https://dashboard.heroku.com/) and login or create an account. 

1. Click on 'new' in the top right corner and then create app. 
2. Choose a name and select your region 
3. Your app overview will load. 
4. Select Resources > Add-ons, and choose Heroku Postgres - the 'Hobby Dev or Free' option.
5. Copy the the Postgres URI into a custom variable in settings called 'DATABASE_URL'


*Database Migration*

Back in the apps settings.py, the database settings need to be updated.
> Locate the default 'DATABASE' settings, and replace with:
 ```
 if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
*This piece of code checks the env for 'DATABASE_URL'. If false the default sqlite db is loaded. If true, the heroku postgres db is loaded via the dj_database_url dependency.*

Next you will need to run migrations. 
1. You can achieve this by running the following commands:
    ```
    python3 manage.py showmigrations 
    ```
    Check the output of the above contains migrations for each of the apps, once happy run:
    ```
    python3 manage.py migrate
    ```
2. Now that we have migrated the database, we need to load the data. The initial data for this app came from a JSON [fixture](https://docs.djangoproject.com/en/3.2/howto/initial-data/). Run the following commands to load the date:
    ```
    python3 manage.py loaddata categories
    ```
    Followed by:
    ```
    python3 manage.py loaddata products
    ```
    *Data must be loaded in order based on the models relationship.

3. Install gunicorn webserver with:
    ```
    Pip3 install gunicorn
    ```

4. Generate an up to date requirements.txt 
    > Make sure you are in the apps main folder and enter the following command:
    ```
    pip freeze --local > requirements.txt
    ```

5. Generate a Procfile, this tells Heroku to start your app.
    > You can create one by typing the following into your terminal:
    ```
    echo "web: gunicorn improved_design.wsgi:application" > Procfile
    ```

6. In the main apps settings.py, add the Heroku apps URL to 'Allowed Hosts', also include 'localhost'.

*Heroku Setup Continued*

6. Login into Heroku CLI with:
    ```
    heroku login -i
    ```
    Enter your login credentials when prompted. 
7. Temporarily disable collectstatic with:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app {app name}
    ```
8. Initialise Heroku git remote with: 
    ```
    heroku git:remote -a {app name}
    ```
9. Now we are ready for the initial commit to Heroku:
    ```
    git push heroku master
    ```
10. Back on the Heroku dashboard, we will setup automatic deploys. Navigate to Deploy > Deployment Method > Select GitHub. Search for your repo and then click connect. Then click enable automatic deploys. 


#### AWS Setup

*Initial Setup*
1. Go to https://aws.amazon.com/ > Create or Login to your AWS account. 
2. On the management console select or search and select 'S3'
3. Select 'Create Bucket' and populate the name field. 
4. Deselect 'block all public access' and select the related warning.
5. Click 'Create Bucket'

*Bucket Setup*
1. Under Properties 
    - Enable 'Static Website Hosting' in order to get an endpoint.
    - Set the defaults to index.html and error.html - these won't be used. 
2. Under Permissions:
    - Add the following CORS configuration:
    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]   
    ```
    - Under Bucket Policy:
        - Select Policy Generator:
            1. Select: 'S3 Bucket' Policy from the type dropdown.
            2. But ' * ' in the principal field.
            3. Select ‘get_object’ from the actions dropdown.
            4. Copy your ARN from Bucket Policy (on the previous page).
            5. Click add statement
            6. Copy the policy config into the Bucket Policy editor and save.
        - Under Access Control List
            1. Select ‘list’ under Everyone/ Public access.
            2. Accept the public warning and save. 

3. Creating a User:
    - From the service menu select 'IAM'.
    - First, create a group for the user by selecting ‘User groups’ > ‘Create User group’.
    - Enter group name (anything you like).
    - Click ‘Create Group’.
    - Next navigate to ‘Policies’.
        1. Click ‘Create policy’.
        2. Click the JSON tab then ‘Import managed policy’.
        3. Select AmazonS3FullAccess and import this policy.
        4. In the JSON tab, add your bucket ARN from above as a value for the ‘Resource’ key.
        5. Click Next - ignoring tags - And then ‘Review Policy’.
        6. Enter a name and description for your new policy.
        7. Then click ‘Create policy’.
    - Navigate back to ‘User groups’.
    - Click on the group created earlier > click permissions > Add permissions > Attach policy.
    - Select your policy from the list and then ‘Add Permissions’.
    - Now you can create a user. 
    - Navigate to ‘Users’ > ‘Add user’.
    - Enter your desired user name.
    - Select - ‘Access key - Programmatic access’
    - Select ‘Next Permissions’
    - Select the group made above.
    - Select ‘Next Tags’, again ignoring the tags page. Click ‘Next Review’
    - And finally! click ‘Create User’
    - Download the user keys via the CSV. 

You can find out more about connecting Django to AWS S3 [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)


## Testing

#### [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F) *(Results)*
The W3C validator found 3 initial issues:
1. Error: 'http-equiv' attribute whose value is 'X-UA-Compatible' must have a content attribute with the value 'IE=edge' [x]
2. Error: Element div not allowed as child of element button in this context. [x]
3. Error  Duplicate ID category-link. [x]
4. Error: Start tag a seen but an element of the same type was already open. [x]

#### [JS Hint](https://jshint.com/)
JS Hint found 1 initial issues:
1. *Warning* Missing semicolon. (line 111) [x]

#### [Flake8](https://flake8.pycqa.org/)
Found 50+ initial PEP8 issues, all related to 'line too long'. I corrected the errors highlighted. 
And omitted altering any files generated by Django, e.g. migrations. 

#### [WC3 CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) *(Results)*
WC3 CSS Validator found 1 error & 38 warnings:
1. *Error* & *Warnings* missing bracket (line 673) [x]


### Google Lighthouse

#### Initial Test
![Lighthouse Results](https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/lighthouse_results_a.png "Lighthouse Results")

**Performance**\
Issues reported, 
  - Image elements do not have explicit width and height

**Best Practices**\
Issues reported, 
  - Links to cross-origin destinations are unsafe

**Accessibility**\
Issues reported, 
  - Background and foreground colors do not have a sufficient contrast ratio.
  - Alt attrs missing from social media links


**SEO**\
Issues reported, 
  - Document does not have a meta description


#### Steps taken 
1. [Performance] The images in question are SVG's which do have heights and widths set!? [ ]
2. [Best Practices] Links to cross-origin destinations are unsafe - added  rel="noreferrer" to external links [x]
3. [Accessibility] Left colours as they are - I feel the contrast is perfectly sufficient [ ]
3. [Accessibility] Alt attrs missing from social media links - Adding alt attributes caused W3C errors  [ ]
4. [SEO] Added meta tags [x]\
*Several other errors are present relating to external scripts (Stripe & Jquery)*












