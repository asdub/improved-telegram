# Testing - The Cookbook app

Return to main README file - [Click Here.](https://github.com/asdub/improved-telegram/blob/main/README.md)

## Manual Testing 

#### Responsive Testing
Responsivity tested on physical iPhone & Anrdroid phones (iPhone 11 Pro Max / iPhone 12 / Samsung Galaxy s21)

Also tested within mobile device views in Chrome Dev Tools & Safari Web Tools.
The following screen sizes were tested using both above tools: 

**iOS Mobile & Tablet devices**
| Device         | Pixel Size   | Viewport  |
| :--------------|:-------------| :---------|
|iPhone XR       | 828 x 1792.  | 414 x 896 |
|iPhone XS       | 1125 x 2436  | 375 x 812 |
|iPhone XS Max   | 1242 x 2688  | 414 x 896 |
|iPhone X	     | 1125 x 2436	| 375 x 812 |
|iPhone 8 Plus   | 1080 x 1920	| 414 x 736 |
|iPhone 8	     | 750 x 1334	| 375 x 667 |
|iPhone 7 Plus   | 1080 x 1920	| 414 x 736 |
|iPhone 7	     | 750 x 1334	| 375 x 667 |
|iPhone 6/6S Plus|1080 x 1920   | 414 x 736 |
|iPhone 6/6S     |750 x 1334	|375 x 667  |
|iPhone 5	     |640 x 1136	|320 x 568  |		
|iPod Touch	     |640 x 1136	|320 x 568  |	
|iPad Pro	     |2048 x 2732	|1024 x 1366|
|iPad 3 & 4 Gen  |1536 x 2048	|768 x 1024 |
|iPad Air 1 & 2  |1536 x 2048	|768 x 1024 |
|iPad Mini 2 & 3 |1536 x 204 	|768 x 1024 |
|iPad Mini  	 |768 x 1024	|768 x 1024 |


**Anroid Mobile & Tablet devices**
| Device         | Pixel Size   | Viewport  |
| :------------- |:-------------| :---------|
|Nexus 6P	     |1440 x 2560	|412 x 732  |
|Nexus 5X	     |1080 x 1920	|412 x 732  |
|Google Pixel 4XL|1440 x 869	|412 x 869  |
|Google Pixel 4	 |1080 x 2280	|412 x 869  |
|Google Pixel 3a |1080 x 2220	|412 x 846  |
|Google Pixel 3XL|1440 x 2960	|412 x 847  |
|Google Pixel 3	 |1080 x 2160	|412 x 824  |
|Google Pixel 2	 |1440 x 2560	|412 x 732  |
|Google Pixel XL |1440 x 2560	|412 x 732  |
|Google Pixel	 |1080 x 1920	|412 x 732  |

**Desktops & Browsers** *(Physical devices)*
| Device        | Browser    | Browser 2 | Browser 3|
| :------------ |:---------- | :-------- | :--------|
|MacBook Pro    | Chrome     | Safari    | Firefox  |
|Chromebook     | Chrome     | N/a       | N/a      |
|Dell (Win10)   | Chrome     | Edge      | Firefox  | 
|Dell (Win7)	| IE11       | Firefox   | -        |

All elements are  visible and all features are usable. 
Background images vary in terms of visibility. But overall still great the desired effect.
I did not test on anything under IE11. 


### Manual testing process

    Header/ Navbar
    --------------
    - Logo & navigation clearly visible and unobstructed on all views. 
    - Noun project icon clearly visible and unobstructed on all views. 
    - Confirm the following navigation menu items function:
        - Design Services 
            - Custom Design
            - Leaflet Design
            - Icon Design
            - Poster Design
            - Logo Design
        - All Services
            - By Price
            - By Rating
            - By Type
            - View All Services
        - About
            - Our Work
            - About/ Contact
    - Confirm the search bar is present, screens over 992px.
    - Confirm search icon and dropdown search bar is present/ functioning on screen under 992 px.
    - Confirm Account icon and dropdown menu is present/ function:
        - Login 
            -  Confirm 'Forgotten Password function is working
        - Register
            - Confirm registration process and email verification is working. 
    - Confirm authorised users see the following account menu options:
        - My Profile
        - Sign Out
            - Confirm sign out functionality is working. 
    - Confirman admin user, in addition to the above should also see:
        - Management dropdown menu item under account.
    - Confirm on medium/ small screens that the nav text links change to hamburger menu icon.
    - Confirmthe dropdown menu appears and is functioning when mobile menu icon is selected. 
    - Make sure the welcome text contains the correct recipe count. 
    - Confirm the bag/ card icon is viable and link is functioning
        - Value should be 0.00
        - Add service and confirm value is aligned with products in card. 
    
    Home
    ----
    - Confirm transition effects are functioning on page load. 
    - Confirm background image is visible on all views (mobile, tablet, Desktop)
    - Confirm Hero Banner text present
    - Confirm Hero Banner CTA is functioning
    - Confirm Work Section title and text is visible and rendered correctly on all types 
        - Confirm the 8 most recent user artworks are displayed in a grid. 
        - Check grid and images are responsive. 
    - Confirm About section title and text is visable and rendered correctly on all view types
    - Confirm Social Media contact links (4x) function and open in new tab. 

    Footer
    ------
    - Confirm footer is positioned correctly at the end of each page. 
    - All links are functioning. 

    Services/ All Products
    ----------------------
    - Confirm all services view (Accessed from both home CTA's and menu) are functioning. 
    - Confirm Title and text render correctly on all view types. 
    - Conform All product cards are present, and contain the following data:
        - Service Images
        - Title 
        - Price 
        - Rating
        - Edit/ Delete functionality (If admin user)
    - Confirm, cards render correctly on all views.
    - Confirm sort dropdown is functioning, and contains the following options:
        - Pricing - ascending
        - Pricing - descending
        - Rating - ascending
        - Rating - descending
        - Name - ascending
        - Name - descending
        - Category - ascending
        - Category - descending
    - Confirm service/ product card transition effects function on hover/ focus.
    - Confirm service/ product card links to product detail view.

    Service/ Product Detailed
    -------------------------
    - Confirm this view renders correctly on all screen sizes.  
    - Confirm service image is present. 
    - Confirm following data is displayed:
        - Service Title
        - Service Price
        - Category 
        - Rating
        - Edit/ Delete functionality (If admin user)
        - Service description
    - Confirm the following user customisation fields are present:
        - Quantity
        - Detail your requirements
        - Size
        - Provide text content for artwork
        - Colour radio buttons.
    - Confirm 'Back' and 'Add to Order' buttons function. 
    - Confirm toast notification appears when item added to bag.
        - On notification, confirm product name is displayed
        - Confirm 'View Orders' button is functioning.  

    Orders/ Bag
    -----------
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Order title is present. 
    - Confirm Order items are present, and display the following data:
        - Service Image
        - Service Title
        - Service SKU
        - Service selected size 
        - Service selected colour
        - Price 
        - Quantity
        - Subtotal 
        - Detailed requirements
        - Provided text content
    - Confirm quanity can be updated
    - Confirm item can be removed from bag 
    - Confirm order totals:
        - Order Total
        - Delivery Total
        - Cost breakdown list
        - Grand Total
    - Confirm 'Checkout' button functions. 
    - Confirm 'Add more Services' button functions.

    Checkout
    --------
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Checkout title is present. 
    - Confirm Order Summary is present, containing following data:
        - Service Image
        - Service Title
        - Service selected size 
        - Quantity
        - Subtotal 
        - Detailed requirements
        - Provided text content
    - Confirm Order Summary totals:
        - Order Total
        - Delivery Total
        - Grand Total
    - Confirm checkout form has rendered correctly. 
    - Confirm the following fields are present:
        - Full Name
        - Email 
        - Address (Made up of multiple fields)
    - Confirm 'Save Address' checkbox is present for auth users
    - OR Create an Account or Login to save this information if no auth. 
    - Check Credit Card field is functioning. 
    - Confirm Credit Card field errors are displaying. 
    - Confirm text informing user of amount to be charged is present. 
    - Confirm 'Adjust Order' & 'Complete Order' buttons function. 
    - If payment fails, confirm toast notification displaying error. 


    Checkout Success
    ----------------
    - Confirm success toast notification appears and displays order number
    - Confirm 'Thank you' Title and confirmation text is displaying. 
    - On order confirmation, confirm the following data is present:
        - Order Info
            - Order Number
            - Order Date
        - Order Details
            - Service (Name, Quantity, Size, Colour)
        - Delivery (Address, Contact Number)
        - Billing (Total, Delivery, Grand Total)
    - Confirm background image is rendering correctly on all screens. 
    - Confirm 'Forgot Something' button functioning 
    - Confirm order confirmation email sent/ received and data within is correct. 

    Profile
    -------
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Profile title and text is present. 
    - Confirm user delivery information is displayed if stored. 
    - Change data and 'Update', confirm new data is stored. 
    - Confirm 'Your Orders' displays:
        - All pending orders
        - All complete orders
        - Complete orders should be sorted to top. 
        - Pending orders by date. 
        - Complete orders displays 'View Artwork' button, which functions. 
        - Pending & Complete orders displays 'View order button, which functions. 
    - Confirm 'Your Orders' card displays following data:
        - Date & Time
        - Order Status
        - Order Number
        - Service items included in order
        - Order total price

    Order History
    -------------
    This is the same view as 'Checkout Success'
    Confirm button at bottom of page displays:
        - Back to profile when accessed from profile view. 

    View Artwork
    ------------
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Artwork title and text with order number data is present. 
    - Confirm Artwork cards are present for any images attached to order
    - Confirm image is displayed is responsive on all screen sizes. 
    - Confirm ' Back to Profile' button functions. 

    Management/ Add
    ----------------
    - When logged in as admin - 
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Profile title and text is present. 
    - Confirm form to add new product/ service is present and functioning. 
    - Confirm pending user orders are displays in order. 
    - Confirm 'Your Orders' card displays following data:
        - Date & Time
        - Order Status
        - Order Number
        - Service items included in order
        - Order total price
    - Confirm 'Complete Order' button is functioning. 

    Complete Order/ Order Management
    --------------
    - When logged in as admin - 
    - Confirm this view renders correctly on all screen sizes. 
    - Confirm Order Management title and text is present. 
    - Confirm the complete order card contains the following data:
        - Order Number
        - Order Toal
        - Name / Email / Phone
        - Order Date
        - Order Items
        - Artwork Requirements
        - Artwork Content/ Copy
        - File Upload. 
    - Confirm file upload functions correctly (multi)
    - Confirm warning text appears once files selected
    - Confirm 'Complete Order' button functions. 
    - Confirm toast notification appears on order completion, confirming email sent. 
    - Confirm user received order email, with 'View Artwork' link. 
    - Confirm 'View Artwork' link from user email functions. 
