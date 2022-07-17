# The Amber Tree Booking System & Site WebApp

![AT logo](/static/images/readme/logo.png)

This WebApp is a booking system and general website for the mock restaurant The Amber Tree.

The backend runs on the Django 3.2 python web-framework with a PostgreSQL database using the Django MVT model (similar to the standard MVC), the front-end web pages are rendered from templates served by the Django backend, these templates were written in a combination of HTML5 & Django templating language which allows for pythonic functions such as loops and variables to be utilised. 

CSS3, Bootstrap 5, JavaScript & jQuery were also utilised to gain the desired front-end functionality and UX based on initial wireframes. AJAX requests will be performed using the JavaScript Fetch API.

This WebApp is hosted on Heroku with all static & media files hosted on Cloudinary and dealt with by Django.

[Click here for the live version](https://theambertree.herokuapp.com/)

# Features
## Current Features

### **User Features**
* Main Navigation
    * Home 
    * Menu
    * Drinks
    * Contact
    * Make a Booking 
    
    #### Desktop Nav:
    ![Navigation](/static/images/readme/nav_large.png)

    #### Tablet / Medium Devices Nav:
    ![Navigation](/static/images/readme/nav_medium.png)

    #### Mobile / Small Devices Nav:
    ![Navigation](/static/images/readme/nav_small.png)

* Single Index Page for majority of the content
    * Welcome
    ![About Page](/static/images/readme/welcome_page.png)

    * Menu
    ![Menu Page](/static/images/readme/menu_page.png)

    * Drinks
    ![Drinks Page](/static/images/readme/drinks_page.png)

    * Contact
    ![Contact Page](/static/images/readme/contact_page.png)


* Make a Booking - Booking Form
    * Accepts User Input
    * User can only intitially select a date.
    * Once a valid date has been selected, available times are then shown for that date.
    * After a date & time has been selected all available tables are then shown.
    * Once a table has been selected a User must then complete the required details form and select their slot.
    * Users can switch between dates & available times and the form will update to the relevant available tables.
    * User then submits the form and is redirected to a booking success page with a link to there bookings
    * The user is unable to select dates or times that are not available and therefore should not result in any booking being unsuccessful<sup>**</sup>

    <sub>** - Currently no check to see if a user has already booked that slot, this can only occur if multiple users are using the form at the same time and selecting the same date & time within the same short timescale as the form updates on date or time change.</sub>
    
    ![Booking Form](/static/images/readme/booking_form.png)

* Login / Register - Accounts Authorisation

### **Staff Features**

**Dashboard**

* Home - Will include metrics and todays bookings and recently canceled bookings etc.
    ![Dashboard Home](/static/images/readme/dashboard_home.png)
* Tables - Staff users create, update and delete tables with capacities for each of the tables in the restaurant.
    ![Dashboard Tables](/static/images/readme/dashboard_tables.png)
* Times - Staff users create, update and delete time slots, all is needed is a start time and the end time is auto generated as start time + 90 mins.
    ![Dashboard Times](/static/images/readme/dashboard_times.png)
* Schedule - Staff users create, update and delete empty booking slots, these booking slots become available and can be booked through the booking form on the main site or through the booking tab in the dashboard.
    ![Dashboard Schedule](/static/images/readme/dashboard_schedule.png)
* Bookings - Staff users create, update and cancel Bookings for the restaurant. All booking that have been booked or canceled will show here.
    ![Dashboard Bookings](/static/images/readme/dashboard_bookings.png)
* Food - Staff users create, update and delete items which are visible on front page food menu.
    ![Dashboard Food](/static/images/readme/dashboard_food.png)
* Drink - Staff users create, update and delete items which are visible on front page drinks menu.
    ![Dashboard Drinks](/static/images/readme/dashboard_drinks.png)
* Messages - Currently not available - Will contain all messages sent using the contact form on the main site contact section. (See Current Features & Functionality Left to Implement below)
* Help - Currently not available - General FAQ's and how to's with regards to using the system.

### **Dev Admin**

* Django Admin - currently only accessible with superuser
    * Accessed via adding /admin to the root directory of the app in a browser.
    * Create, update and delete objects in all the models.

    ![Django Admin](/static/images/readme/django_admin_page1.png)
    ![Django Admin](/static/images/readme/django_admin_page3.png)


* User Management - currently only accessible with superuser 
    * Accessed via Django Admin panel
    * Create, update and delete a user in the Users model.
    * Set user access and privilege

        ![User management models](/static/images/readme/django_admin_page4.png)
        ![User management page](/static/images/readme/django_admin_page5.png)

### Current Features & Functionality Left to Implement

**Guest Features**

* __Guest Booking__
    - This feature will allow guest users to make bookings without the need to register for an account.

* __Contact us Form__
    - Front end is complete, a back end needs to be sorted and piped up to the contact form on the contact us section of the homepage. 

**Admin/Staff Features**

* __Contact us Messages__
    - This feature will allow staff users with access to the Dashboard to view all messages sent from the contact us form on the main site.

* __Custom Admin Panel__

    - This feature is still in need of further development

    - Booking Slots tab New Booking Slots button which will allow for the batch creation and processing of booking slots. This feature will also allow the users who are authenticated as staff or higher to quickly create and manage open time slots for future bookings in batch requests rather than having to create and manage each slot individually

    - UI & UX improvement needed

    - Few Bugs left to iron out (See Manual Testing Below)

    - This feature will also allow the users who are authenticated as staff or higher to quickly manage any received contact us forms

**Functionality**

* __Django Messages__ 
    - This feature will allow users to receive  confirmation messages from Django such as errors or success'.


* __Multiple Table Booking__
    - This feature will allow the user to add more than one table to the booking form before submission

* __Unique Booking reference numbers__
    - This Feature will allow for each booking to be assigned a unique booking reference number.

### Future Features
* Customer accounts.
    * Allow customer accounts to amend bookings
    * Set up email verification
    * Autonomous booking confirmation email
* Guest Bookings
    * Allow guest bookings to amend and cancel bookings
    * Autonomous guest booking confirmation email
    * Unique URLs based on booking reference number attached to booking confirmation email for easy amend or cancel
* Food menu Items Pictures & Customer reviews
* Customer user reviews of Establishment
* Customer user reviews of Food & Drink Menu items.
* Sign in with Social Account

## How To Use

### Booking System -- outdated: New Staff Dashboard instead of django admin but similar method (Tables > Time Slots > Booking slots > Bookings)

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

- I confirmed the name entry input works; requires an entry into the field, accepts only characters (Desktop). Start button works and user name is added to the DOM.


## Testing 

### General Testing
- I tested this webapp works in different browsers: Chrome, Firefox, Edge.
- I confirmed that the project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.
- I confirmed the colours and fonts chosen are easy to read and accessible by running it through lighthouse in devtools.

### Javascript Testing
**Manual Testing**
- Manual tests spreadsheet can be found in /manual_testing/TheAmberTree - Manual Testing.ods

**Jest**
- N/A - Not Used

### Django Testing
**Coverage** - Ran on local sqlite3 database.
- Bookingsys coverage report found in /bookingsys_coverage/
![Bookingsys coverage report](/static/images/readme/bookingsys_coverage.png)
- TheAmberTree coverage report found in /theambertree_coverage/
![TheAmberTree coverage report](/static/images/readme/theambertree_coverage.png)
-Dashboard coverage report found in /dashboard_coverage/
![Dashboard coverage report](/static/images/readme/dashboard_coverage.png)

### User Testing

**Guest**
- Manual tests spreadsheet can be found in /manual_testing/TheAmberTree - Manual Testing.ods

**Staff**
- - Manual tests spreadsheet can be found in /manual_testing/TheAmberTree - Manual Testing.ods

### Browser Testing
**Lighthouse**
- Mobile Results
![Mobile Lighthouse Report](/static/images/readme/mobile_lighthouse_report.png)

- Desktop Results
![Desktop Lighthouse Report](/static/images/readme/desktop_lighthouse_report.png)
<!-- ![Lighthouse Results]()
- I confirmed that ... are all readable and easy to understand. -->

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
- Cloudinary (1.29.0) - Static & Media file hosting
- dj3-cloudinary-storage (0.0.6) - Cloudinary for Django
- dj-database-url (0.5.0) - Allows connection to db
- psycopg2 (2.9.3) - Interact with PostgreSQL
- Pillow (9.2.0) - Not yet implemented, ready for menu images.

**Front end:**

- [Bootstrap 5](https://getbootstrap.com/) - CSS Framework
- [jQuery](https://jquery.com/) - JavaScript Library
- [Font Awesome](https://fontawesome.com/) - Icons

**Media:**
- The images used in this webapp were sourced from [Pexels](https://www.https://www.pexels.com/)
- The Tree SVG used in the logo was sourced from [freesvg.org](https://freesvg.org/maple-tree-vector-drawing)

**Fonts**
- Some of the fonts used in this webapp were sourced from [Google Fonts](https://fonts.google.com/)




