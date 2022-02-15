# The Amber Tree Booking System & Site WebApp

![AT logo](/static/images/readme/logo.png)

This WebApp is a booking system and general website for the mock restaurant The Amber Tree.

The backend runs on the Django 3.2 python web-framework with a PostgreSQL database using the Django MVT model (similar to the standard MVC), the front-end web pages are rendered from templates served by the Django backend, these templates were written in a combination of HTML5 & Django templating language which allows for pythonic functions such as loops and variables to be utilised. 

CSS3, Bootstrap 5, JavaScript & jQuery were also utilised to gain the desired front-end functionality and UX based on initial wireframes. AJAX requests will be performed using the JavaScript Fetch API.

This WebApp is hosted on Heroku with all static & media files hosted on Cloudinary and dealt with by Django.

[Click here for the live version](https://theambertree.herokuapp.com/)

## Features
### Current Features

**Guest Features**
* Navigation
    * About 
    * Menu
    * Drinks
    * Contact
    * Make a Booking 
    
    ![Navigation](/static/images/readme/nav_large.png)

<!-- ![Navigation Mobile](assets/images/readme/multiplayer.png) -->

* Single Index Page for majority of the content
    * About
    ![About Page](/static/images/readme/about_page.png)

    * Menu
    ![Menu Page](/static/images/readme/menu_page.png)

    * Drinks
    ![Drinks Page](/static/images/readme/drinks_page.png)

    * Contact
    ![Contact Page](/static/images/readme/contact_page.png)


* Make a Booking - Booking Form
    * Accepts User Input
    * User selects a date and time then all available tables are show.
    * User then must complete the required details form and select their slot.
    * User then submits form and is redirected to a booking complete page with the booking details
    * If the form is incorrect or booking unavailable the user is redirected to a booking failed page with the reason for failure 
    ![Booking Form](/static/images/readme/booking_form.png)

**Staff Features**
* Django Admin - currently only accessible with superuser
    * Accessed via adding /admin to the root directory of the app in a browser.
    * Create, update and delete objects in all the models.

    ![Django Admin](/static/images/readme/django_admin_page1.png)
    ![Django Admin](/static/images/readme/django_admin_page3.png)


<!-- * Menu
    * Create, Update & Delete menu items

    ![Menu]() -->

<!-- * Drinks
    * Create, Update & Delete drink items
    * Images for drinks can be uploaded and rendered with the drink item to the drinks Page

    ![Drinks]() -->

* User Management - currently only accessible with superuser 
    * Accessed via Django Admin panel
    * Create, update and delete a user in the Users model.
    * Set user access and privilege

        ![User management models](/static/images/readme/django_admin_page4.png)
        ![User management page](/static/images/readme/django_admin_page5.png)

### Current Features & Functionality Left to Implement

**Guest Features**

* __Booking Complete Page__
    - This feature will allow users to know that there booking has been successful
    
    - This feature will allow users to view a summary of there booking

* __Booking Failure Page__
    - This feature will allow users to know that there booking has been unsuccessful

    - This feature will allow users to know why there booking was unsuccessful

* __Contact us Form__
    - This feature will allow users to complete a form and send enquires such as party booking to the restaurant. 

**Admin/Staff Features**

* __Menu & Drinks menu management system__
    - This feature will all users who are authenticated as staff or higher to create, update and delete database entries for items to be displayed on both the menu page and drinks page. It will also allow for an image to be uploaded for each item which will can be rendered as part of the item in the menu/drinks page.

* __Contact us Messages__
    - This feature will all users who have access to the Django admin to view all enquires from the contact us form

* __Custom Admin Panel__
    - This feature would allow users who are authenticated as staff or higher to create, update, and delete bookings without the need to access Django admin

    - This feature will also allow the users who are authenticated as staff or higher to quickly create and manage open time slots for future bookings in batch requests rather than having to create and manage each slot individually in the Django admin

    - This feature will also allow the users who are authenticated as staff or higher to quickly manage any received contact us forms

**Functionality**

* __Ajax requests__ (Fetch API)
    - This feature will allow the booking form to dynamically update the available timeslots based on the user input for the date

    - This feature will then allow the booking form to dynamically update the available tables based on the user input for the time

* __Django Messages__ 
    - This feature will allow the user to recieve messages from Django such as error or success.

* __Mobile Version of Site / Site Dynamics__ (CSS media queries/set bootstrap classes)
    - This feature would allow users to access the webapp via medium and small devices and have a pleasant experience with the UI

* __Multiple Table Booking__
    - This feature will allow the user to add more than one table to the booking form before submission

* __Unique Booking reference numbers__
    - This Feature will allow for each booking to be assigned a unique booking reference number.

### Future Features
* Customer accounts.
    * Attach bookings to accounts when logged in
    * Allow customer accounts to amend or cancel bookings
    * Set up email verification
    * Autonomous booking confirmation email
* Allow guest bookings to amend and cancel bookings
    * Autonomous guest booking confirmation email
    * Unique URLs based on booking reference number attached to booking confirmation email for easy amend or cancel
* Customer reviews
* Sign in with Social Account

## How To Use

### Booking System

This booking system uses multiple models available in the Django Admin Panel

Upon initialisation, It is recommended you create objects in this order:

1. **Tables**

    Each Table represents a table available to have bookings made for it. 

    ![Creat a Table](/static/images/readme/add_table.png)

    Repeat for each table at the establishment:
    - Create a new Table
    - Give new Table a number
    - Give new Table a capacity

2. **Time Slots**

    Each Time Slot represents a defined segment of time for a booking e.g., 6:00 PM - 7:30 PM is a 90 min slot.
    Restaurant can customise start & end times for these slots.

    ![Create a Time Slot](/static/images/readme/add_timeslot.png)

    Repeat for each time slot:
    - Create a new Time Slot
    - Give new Time Slot a start time
    - Give new Time Slot an end time
    - Set new Time Slot status:
        - 'Closed': Unavailable for selection when making a Booking Slot (Default)
        - 'Open': Available for selection when making a Booking Slot

    **Please Note:** *If you wish to close a Time slot for any particular reason then change the Status to 'Closed'*

3. **Booking Slots**

    Each booking slot represents an empty booking for a single table with a defined time slot with a start time and end time and defined date

    ![Create a Booking Slot](/static/images/readme/add_bookingslot.png)

    Repeat for each Booking Slot:
    - Create a new Booking Slot
    - Select a Table for new Booking Slot
    - Select a Date for new Booking Slot
    - Select a Time Slot for new Booking Slot
    - Set new Booking Slot Status:
        - 'Draft': Unavailable for selection when making a Booking (Default)
        - 'Published': Available for selection when making a Booking
    - Set new Booking Slot Booking Status:
        - 'Available': Available for selection when making a Booking (Default)
        - 'Booked': Unavailable for selection when making a Booking

    **Please Note:** *If you wish to close a booking slot for any particular reason then either change the Status to 'Draft' or Booking Status to 'Booked'*

4. **Bookings**

    A booking is the attachment of the guests details to either one or multiple Booking Slots.

    Bookings can be updated and deleted here.

    ![Manage Bookings](/static/images/readme/django_admin_page2.png)
    
    ***Booking Attended:***

    - Find the guests booking in Bookings and set status to 'Attended' 
    <br />
    <br />

    ***Booking Amended:***

    - Find the guests booking in Bookings and update the booking slots by de-selecting the current ones and selecting the desired slot for amendment (multiple can be selected) 
    <br />
    <br />

    ***Booking Cancelled:***
    - Find the guests booking in Bookings and set status to 'Cancelled' 
    - Find Booking Slot from for booking in Booking Slots and change Booking Status back to 'Available'
    <br />
    <br />

    *It doesn't matter which order these two are completed as long as both are completed after each cancellation so the Booking Slot is visible to other guests* 
    
    <br />

    If creating a booking manually this can be done via Bookings on the Django admin. 
    
    **Please Note:** *Creating a manual booking is **not** advised. If you have to then you must make sure the timeslot selected in the booking has its status manually changed to booked before making the booking as to not allow a site guest to double book.*

## Data Model
<!-- I decided to use class and Player classes as my models.  -->

<!-- The game creates an instance for the game board to hold the board size, VS title, layout, counter positions and also has a board `print` function.

While also creating two separate instances, one for each player to hold the name, counter color data and player type (Human or Computer). -->

## Testing 

### General Testing
- N/A
<!-- - I tested this webapp works in different browsers: Chrome, Firefox, Edge.
- I confirmed that the ... results are always correct.
- I confirmed that the project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.
- I confirmed the name entry input works; requires an entry into the field, accepts only characters (Desktop). Start button works and user name is added to the DOM.
- I confirmed the colours and fonts chosen are easy to read and accessible by running it through lighthouse in devtools. -->

### Javascript Testing
**Jest**
- N/A

### Django Testing
**Coverage**
- N/A

### User Testing

**Guest**
- N/A

**Staff**
- N/A

### Browser Testing
**Lighthouse**
- N/A
<!-- ![Lighthouse Results]()
- I confirmed that ... are all readable and easy to understand. -->

### Validator Testing 

**HTML**
- N/A
    <!-- - No errors were returned when passing through the official [W3C validator]
    () -->
**CSS**
- N/A
    <!-- - No errors were found when passing through the official [(Jigsaw) validator]() -->
**JavaScript**
- N/A
    <!-- - No errors were found when passing through the official [Jshint validator]
    ()
      - The following metrics were returned: 
      - There are 30 functions in this file.
      - Function with the largest signature takes 3 arguments, while the median is 0.
      - Largest function has 13 statements in it, while the median is 6.
      - The most complex function has a cyclomatic complexity value of 7 while the median is 2. -->

## Deployment

This project was deployed using Heroku.

### Steps for deployment

* Fork or clone this repository
* Create a new Heroku app
* Create new PostgreSQL database for your Heroku app
* Set the build packs to `Python`
* Link the Heroku app to the repository
* Set Config Vars in settings as follows:
    * CLOUDINARY_URL : Your Cloudinary API Environment variable
    * DATABASE_URL : PostgreSQL database URL
    * SECRET_KEY : A_SECRET_KEY_OF_YOUR_CHOICE
* Click on **Deploy**
* Run Heroku console:
    ```
        $ python3 manage.py migrate
    ```
* Finally to create a super user, in the Heroku console:
    ```
        $ python3 manage.py createsuperuser
    ```

The live link can be found here - [TheAmberTree](https://theambertree.herokuapp.com/)

## Design

### Model Designs

**Initial Models:**

![Initial Slot Model](/static/images/readme/InitialSlotModel.png)
![Initial Booking Model](/static/images/readme/InitialBookingModel.png)

**Current Models:**

### Initial Wireframes & Design Features

![Wireframe](/static/images/readme/wireframe.png)

In my initial design I went with the functionality of a single page for the whole site other than the booking form.

**Index**

This single page is scrollable and designed with a responsive side navigation panel which indicates to the user which part of the page they are scrolling on, as seen by the larger link for in the sidebar in the wireframes.

**Bookings**

A form allowing the user to make a future booking at the restaurant. This form should dynamically load available tables based on the date and time inputted using AJAX fetch requests.

## Credits 

**Python Packages:**
- Django (3.2) - Web-Framework
- gunicorn (20.1.0) - Python WSGI HTTP Server for UNIX
- django-allauth (0.48) - Authentication
- django-crispy-forms (1.14.0) - Bootstrap Form Tags
- Cloudinary (1.29.0) - Static & Media file hosting
- dj3-cloudinary-storage (0.0.6) - Cloudinary for Django
- dj-database-url (0.5.0) - Allows connection to db
- psycopg2 (2.9.3) - Interact with PostgreSQL

**Front end:**

- [Bootstrap 5](https://getbootstrap.com/) - CSS Framework
- [jQuery](https://jquery.com/) - JavaScript Library
- [Font Awesome](https://fontawesome.com/) - Icons

**Media:**
- The images used in this webapp were sourced from [Pexels](https://www.https://www.pexels.com/)
- The Tree SVG used in the logo was sourced from [freesvg.org](https://freesvg.org/maple-tree-vector-drawing)

**Fonts**
- Some of the fonts used in this webapp were sourced from [Google Fonts](https://fonts.google.com/)




