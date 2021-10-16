# Improved Design

![GitHub contributors](https://img.shields.io/github/contributors-anon/asdub/improved-telegram)
![GitHub top language](https://img.shields.io/github/languages/top/asdub/improved-telegram)
![GitHub language count](https://img.shields.io/website?url=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F)
![GitHub last commit](https://img.shields.io/github/last-commit/asdub/improved-telegram)

**A live version of this project can be found [here](https://img.shields.io/website?url=https%3A%2F%2Fimproved-design-asdub.herokuapp.com%2F)**

You can use the following admin account for backend access: 


*Admin User*\
User: asdub
Pass: hashb7790

*Standard User*\
User: laryta
Pass: hashb7795

<img src="https://github.com/asdub/improved-telegram/blob/main/readme/screenshots/mobile_mockup.png" width="150" alt="Improved Design on Mobile" />


### Project Description
This project was made as part of the Code Institute Full Stack Development Course. 

I have created an app to promote the services of a freelance designer. 
Allowing users to purchase custom design services. 
Specifically illustrations/ artwork. 

Users can select from a variety of services, select and enter their desired customistations. 
The user has the option of creating a profile to keep all their orders in one places and view or download their artwork. 
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
    * [Version Control & Managment](#version-control--managment)
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
        * [Testing Documentaition](https://github.com/asdub/laughing-cookbook/blob/master/readme/test/TESTME.md)
        * [User Stories Testing](#user-stories-testing)
    * [Known Bugs](#known-bugs)
    * [Credits](#credits)



## User Experience (UX)


### Brief

My intention was to create a simple app that permits the user easy  and considered access to the services being presented.
Users can easily purchase services and check on orders. While administrators can simply complete user orders.
Having previously designed my own layouts and styles, I wanted to use a front-end framework with my own custom styling (and layouts in parts) for this project. 
The app has been built using the [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) front-end framework.


Owing to the services, the user base is likey to be very broad. 
With this in mind the design and layout has been considered to appeal to all age groups and demographics. 


#### The aim of this project is to:
- Be simple and easy to use (as always!)
- Visually pleasing. 
- Provide users with a structured and easy to navigate freelance services. 
- Allow users to purchase a service (Stripe).
- Allow users to customise their service.
- Allow users to manage their address data (CRUD). 
- Provide users with email & on screen nofications regarding their ordered services.
- Provide defensive design in terms of data editing or deletion. 
- Provide seamless login/ registration functionality.
- Allow administrators to manage services. 
- Allow administrators to complete user orders. 

#### Business/ Monetisation
- The app provides an eccomm platform. An unlimtied number of products or services can be added to the database. Managed by the administrator.


#### New User Stories
##### General
- I want the app purpose to be obvious or easy to figure out.
- I want to view recent artworks purchased by other users.
- I want to know about the service provider before purchase.
##### Services
- I want to view all available services.
- I want detailed information on each service. 
- I want the ability to search for serivces by keyword.
- I want to customise each service. 
##### Managing Services
- I want to update my order quantities. 
- I want to remove items from my order.
- I want to see the total cost of each order item. 
- I want to see a breakdown of customistion costs. 
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




