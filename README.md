# Milestone-4-Project
# An e-commerce website for an artist and their services. 

<img src="development/images/all-devices-black-milestone-4.webp">
(via https://websitemockupgenerator.com/) 

# Jane L.C Online Studio

## URL: https://milestone-4-9edac19c3460.herokuapp.com

# Table of contents
## 1. [Project Overview](#project-overview)
## 2. [User Stories](#user-stories)
### 1. [Must Haves](#must-haves)
### 2. [Should Haves](#should-haves)
### 3. [Could Haves](#could-haves)
## 3. [UX Design](#ux-design)
## 4. [UI Design](#ui-design)
## 5. [Deployment](#deployment)
### 1. [Live Site Link](#live-site-link)
### 2. [Technologies and Platforms Used](#technologies-and-platforms-used)
### 3. [Deployment Steps](#deployment-steps)
## 6. [Testing](#testing)
### 1. [Manual Testing](#manual-testing)
### 2. [Coding Validation](#coding-validation)
### 3. [Bugs Found and Resolved](#bugs-found-and-resolved)
### 4. [Responsiveness Screenshots](#responsiveness-screenshots)
## 7. [Security Considerations](#security-considerations)
## 8. [Next Step Features](#next-step-features)
## 9. [Coding Sources](#coding-sources)
## 10. [Media sources](#media-sources)
## 11. [Acknowledgements](#acknowledgements)
__________________
__________________

## 1. Project Overview

A responsive e-commerce website for an artist to showcase and sell their artwork and services online. The site allows users to browse available artworks, filter by categories, add items to a shopping cart, make custom artwork requests and complete purchases through a secure checkout process. The site also includes user registration and authentication, order management (viewing for users and superusers), and an admin portal for managing products and orders.

The superuser (the artist/website owner) is able to add, edit, and delete products, view all orders, and manage user accounts through the Django admin interface.

### Features

- User registration and authentication
- Artwork listing with filtering options
- Shopping cart and checkout process
- Email confirmation for orders
- View (user and superuser(owner)), edit(superuser), and cancel orders(superuser)
- Responsive design for all devices
- Biography page about the artist
- Admin portal for managing products, orders and requests.


## Criteria provided by Code Institute 
 
### External user’s goal: 
* The user would like to be able to view and purchase artworks from the artist online.

### Site owner's goal:
* The site owner would like the artist to be able to showcase and sell their artworks and services online, manage orders and products easily, and provide a seamless shopping experience for users.

## 2. User stories
* As a user, I want to be able to find out information about the artist, including their biography and available artworks.
* As a user, I want to be able to view available artworks, filter them by categories (e.g., price, subject, size), and see details for each artwork.
* As a user, I want to be able to add artworks to a shopping cart and proceed to checkout. Orders should be linked to my user account.
* As a user, I want the website to be simply presented and easily navigable.
* As a user, I want to be able to register and log-in to the website.
* As a user, I want to be able to make a custom artwork request online, providing extra information in a notes section if necessary.

### Must-haves
* User friendly navigation.
* User should be able to view available artworks and their details.
* User should be able to add artworks to a shopping cart and complete a secure checkout process.
* User should be able to register and log-in to the website.
* User should be able to make a custom artwork request online.
* Superuser (site owner) should be able to add, edit, and delete products (via Django admin).

### Should-haves
* User should be able to filter artworks by categories (e.g., price, subject, size).
* User should be able to view their order history.
* User should recieve an email confirmation following a successful order.


### Could-haves
* User could be able to edit or cancel their orders.
* Superuser could add and edit products via a custom admin panel on the site (not just via Django admin).
* User could view a separate gallery of artwork images.

## 3. UX Design

### Strategy
The aim of the project is to create a functional user registration and e-commerce store using Django and Python, with front-end design from HTML, CSS and JS. 

The user will be able to navigate the website using a navbar at the top of the page. The site will be responsive and easy to use on mobile, tablet and desktop devices.

### Scope
The project will consist of seven main pages (Home, Products, Biography, Custom Artwork Request, Profile, Checkout and Bag) as well as interim success/login pages.  

1. Homepage (/home) - Loading the page will bring the user to https://milestone-4-9edac19c3460.herokuapp.com/.  A navbar at the top of the page will allow the user to navigate to other templates and apps within the project.
2. Products (/products) - This page will show all available artworks for sale. Each artwork will have an image, title, price and short description. The user can click on an artwork to view more details.
3. Artist Biography (/biography) - This page will provide information about the artist, including their background, artistic style, and contact information.
4. Custom Artwork Request (/custom-artwork-request) - This page will include a form for users to submit custom artwork requests. The form will include fields for the user's name, email, artwork description, and any additional notes.
5. Profile (/profiles) - This page will allow users to view their order history and manage their account details.
6. Checkout (/checkout) - This page will allow users to review their shopping cart, enter shipping and payment information, and complete their purchase.
7. Bag (/bag) - This page will show the user's shopping cart, including the artworks they have added, quantities, and total price. Users can update quantities or remove items from their cart.

#### Additional/Interim pages for functionality

4. Sign Up (/accounts/signup) - This page includes input areas for username, password and password confirmation. This page includes the rules provided by django.allauth regarding username and password appropriateness. 
5. Sign-in (/accounts/login) - A simple page through which a user can sign in using their credentials. If they are not already registered, there is a link to register. 
6. Checkout Success (/checkout-success) - A simple interim page following a successful order which links the user back to the home page or to their profile to view their order history.


Once created, orders and custom artwork requests can be viewed and amended via /admin through the use of a superuser log-in. Registered user details can also be viewed within the /admin portal. The order model includes fields for user, order date, order total, and order items. The custom artwork request model includes fields for user, request date, artwork description, and additional notes.

All orders and custom artwork requests can be viewed by the superuser in the /profile page when they are logged in with their site-owner/superuser credentials.

The superuser can add, edit, and delete products via the Django admin interface as well as mark them as sold/unsold. A sold product will not appear on the products page for users to view or purchase.

### Admin Order View
Orders can be viewed and managed by the superuser in the admin panel.
<img src="development/images/admin_order.webp">

Products can be managed by the superuser in the admin panel.
<img src="development/images/admin_products.webp">

Custom Artwork Requests can be managed by the superuser in the admin panel.
<img src="development/images/admin_custom_artwork_requests.webp">

Categories can be managed by the superuser in the admin panel.
<img src="development/images/admin_categories.webp">


### Structure
(See wireframes section below)

### Skeleton
The user will navigate by clicking the links in the navbar menu (visible in tablet view and on desktop, collapsed on mobile devices). Main links are set to icons in mobile view.  Templates are linked sitewide by extending the base template. 

### Entity Relationship Diagram (ERD)

This project is hosted on Heroku and the database used is Heroku PostgreSQL.

Payments are handled by Stripe.

Four main models, apart from the Django User model, were created for this project: Orders, Products, CustomArtworkRequest, and UserProfile.

The following diagram represents the database structure for the e-commerce website:

<img src= "development/images/entity_relationship_diagram_m4.webp">

### Users (Django's built-in)
* id (PK)
* username
* email
* password
* ...

### Products
* id (PK)
* name
* description
* price
* image (URL)
* created_at
* updated_at    
* sold (Boolean)

### Orders
* id (PK)
* user (FK → Users)
* order_date
* total_amount
* status
* created_at
* updated_at

### OrderItems
* id (PK)
* order (FK → Orders)
* product (FK → Products)
* quantity
* price

### CustomArtworkRequest
* id (PK)
* user (FK → Users)
* request_date
* artwork_description
* additional_notes

### Relationships

### User > CustomArtworkRequest

* A User can make many CustomArtworkRequests
* Each CustomArtworkRequest belongs to one User

### Products > OrderItems

* Each Product can appear in at most one OrderItem (or OrderLineItem), since each product is unique and can only be sold once.
* Each OrderItem refers to one Product.

### Orders > OrderItems
* An Order can have many OrderItems.
* Each OrderItem belongs to one Order.

### Users > UserProfile

* Each User has one UserProfile (one-to-one relationship).
* Each UserProfile belongs to one User.




## 4. UI Design
### Surface
My aim was to keep the font decorative but readable. I wanted to ensure the website felt tasteful and refined. The lettering is clear against the light background. The colours across the pages were chosen to be soft and inviting, with a bisque and light olive green to create a warm and welcoming atmosphere.

The text of the site will be black #000000 against the contrasting background of light olive green and bisque to allow for readability.

<img src="development/images/color-picker-palette-milestone-4.webp">
(https://imagecolorpicker.com/ used to create palettes)

#### Accessibility considerations
* Buttons have hover functionality to assist their visual profile. 
* Aria labels for external links (social media links in footer)
* Contrasting font and background choices

#### Fonts
Primary font -  
<img src="development/images/primary-font-milestone-4.webp">

Logo font - 
<img src="development/images/logo-font-milestone-4.webp">

The two fonts had similarities in style and were both decorative and reflective of the site's theme. '"Tangerine", cursive' was used only for the logo in the navbar. '"Cormorant Upright", serif' was used for the remainder of the site to ensure maximum readbility while maintaining a consistent, elegant style.


## Initital design wireframes created using Balsamiq

Homepage (/home)
<img src="development/images/home-wireframe-milestone-4.webp">

Biography (/biography)
<img src="development/images/biography-wireframe-milestone-4.webp">

Products (/products)
<img src="development/images/products-wireframe-milestone-4.webp">

Product Detail (/products/<id>)
<img src="development/images/product-detail-wireframe-milestone-4.webp">

Custom Artwork Request (/custom-artwork-request)
<img src="development/images/custom-artwork-request-wireframe-milestone-4.webp">

Bag (/bag)
<img src="development/images/bag-wireframe-milestone-4.webp">

Checkout (/checkout)
<img src="development/images/checkout-wireframe-milestone-4.webp">

Checkout Success (/checkout-success)
<img src="development/images/checkout-success-wireframe-milestone-4.webp">

Profile (/profiles)
<img src="development/images/profile-wireframe-milestone-4.webp">

---
## 5. Deployment

## Deployment Steps 

1. Clone the repository:
   ```bash
   git clone https://github.com/TLC-1990/milestone-4/
   cd milestone-4
   ```
2. Set Up Environment Variables

   Create an env.py file or set environment variables for SECRET_KEY, database credentials, and any third-party API keys.
   On Heroku, add these variables via the dashboard under Settings > Config Vars.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
   * On Heroku, use:
   ```bash
   heroku run python manage.py migrate
   ```
5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
   * Whitenoise will serve static files in production.
6. Configure Allowed Hosts:
   In settings.py, set ALLOWED_HOSTS to include your Heroku app domain and any local domains.
7. Set Debug Mode: 
   Ensure DEBUG = False in production for security.
8. Prepare Procfile:
   Ensure your Procfile is present and contains:
   web: gunicorn jlc_art_ecommerce.wsgi
9. Deploy to Heroku:
   * Push your code to Heroku using Git.
   * Add necessary Heroku add-ons (e.g., Heroku Postgres for the database).
10. Check Logs: 
   For troubleshooting, use:
   heroku logs --tail
11. Update Requirements:
   Keep requirements.txt up to date with all dependencies.
12. Use .gitignore:
   Ensure .gitignore includes sensitive files (e.g., env.py, db.sqlite3) and unnecessary local files.
13. Access the Site:
   Visit your Heroku app URL to view the deployed site.
  https://milestone-4-9edac19c3460.herokuapp.com/home/

---

KEYS necessary for deployment and running the project:

- SECRET_KEY (from Django project)
- DATABASE_URL (from Heroku Postgres add-on)
- CLOUDINARY_URL (from Cloudinary account)
- STRIPE_PUBLIC_KEY (from Stripe account)
- STRIPE_SECRET_KEY (from Stripe account)
- EMAIL_HOST_USER (from email provider (gmail used here))
- EMAIL_HOST_PASSWORD (from email provider (gmail used here))

Saved in env.py, referenced in settings.py and set as Config Vars in Heroku.
## Deployment Process (further notes)

#### Project was deployed using GitHub, Visual Studio Code and Heroku.

1. Project was created in Visual Studio Code with a local folder. This was then linked to a Git repository and a first commit was pushed to link the two. The site was deloyed on Github. 

2. A new Heroku project was created and linked to the GitHub repository. This handled deployments throughout the project. 

3. PostgreSQL was used as a database (using the CLI database maker provided by Code Institute) for the final project and this was employed in Heroku dynos and in maintained in the VSCode settings through the env.py file. 

4. Throughout the project, a 'project board' was maintained on GitHub to track progress of project tasks and to help orgaise Must Haves, Should Haves and Could Haves. 

5. Regular commits with descriptions of progress were made throughout the project, as were migrations following amendments or additons to the models.

6. Heroku dynos and necessary KEYS were hidden securely within the project files to help prevent intrusion and external attack to the site. 

7. Static files for the project were handled by Whitenoise. 

8. Media files for the project were handled by Cloudinary.

9. Payments were handled by Stripe.

10. Debug was set to True during development and to False for submission.


**Live Site:**  
[milestone-4-9edac19c3460.herokuapp.com/home/](https://milestone-4-9edac19c3460.herokuapp.com/home/)

### Technologies Used
- Python 3.x
- Django 4.x
- Bootstrap 5
- Heroku
- Stripe (for payments)
- HTML, CSS
- JavaScript (external library scripts via CDN)
- Cloudinary (for media file handling)

## 6. Testing 

Website checked on Safari and on Chrome on desktop, ASUS laptop (Microsoft Edge and Chrome), Samsung Galaxy mobile browser (Android) and on IOS (Apple mobile). 
No bugs observed between browsers. 

### Manual Testing

#### Functionality Testing

I tested each feature of the site to ensure it works as intended and challenged possible bugs.

| Feature | Action | Expected Result | Pass/Fail | Notes |
| ------- | ------ | --------------- | --------- | ----- |
| Home page loads | Visit `/home` | Page loads with navbar (collapsed on mobile and smaller screens), splash page with enter store button. | ✅ Pass | No notes |
| Follow navbar links | Click `/biography` (sign up and login detailed below)  | Page changes to artist biography page |  ✅ Pass | Biography page loads successfully and is responsive. |
| Sign in | Visit `/accounts/login`. Entered correct and incorrect login details as well as missing details| Validation error was shown during incorrect login process, correct log in details take a user to /home | ✅ Pass | No Notes |
| Signup | Visit `accounts/signup`. Entered fully filled form and incorrect login details and then form with missing details (i.e. email) | Validation error was shown with missing details. A fully completed form sends a confirmation email to the given email address. A confirmed email, following an approved acceptance from the user, takes the user back to the sign in page. | ✅ Pass | A user's login details are saved to the database and can be viewed and edited by the superuser. The user's password is protected from view by AllAuth security. |
| View products | Visit `/products` | All available products are shown in a grid format with image, title, price and short description. | ✅ Pass | No notes |
| View product detail | Click on a product from `/products` | Product detail page is shown with larger image, full description, price and add to bag button. | ✅ Pass | No notes |
| Create a custom artwork request | Visit `/custom-artwork-request`. Fill out form with all fields and with missing fields. | Successful form submission leads to a success page. Unsuccessful validation shows the user errors for them to fix. A successful custom artwork request is logged in the database and viewable in the admin panel by the superuser. A user's requests are viewable in the Profiles view. | ✅ Pass | No notes |
| Add to bag | From product detail page and click 'Add to Bag' | Item is added to bag and toast message confirms that item has been added to `/bag` page. Bag icon in navbar updates to show number of items in bag and current total. | ✅ Pass | No notes |
| View bag | Click on bag icon in navbar or visit `/bag` | Bag page is shown with all items added, delivery options and total price. User can remove items from bag and update delivery options (courrier (paid) or collection (free)). | ✅ Pass | No notes |
| Complete checkout form |Follow `/checkout` (following items added to bag). Fill out fields successfully and missing information.| Successful validation and form submission lead to a success page. Unsuccessful validation and form submission bring up validation errors for the user. A successful order will be logged in the database and viewable in the admin panel by the superuser. A user's orders are viewable in the Profiles view. | ✅ Pass | Email sent to given email address with order details |
| Stripe payment handled successfully. | Follow `/checkout` (following items added to bag). Fill out fields successfully and missing information.| Successful payment confirmation is shown to the user following the payment process loading page, and the order is processed. Payment logged in Stripe dashboard and order added to admin panel | ✅ Pass | No notes |
| User profile page viewable with previous orders and custom requests | View last saved contact details, artwork orders and custom artwork requests at '/profiles' |If a user has orders, they will see a list of these with their details (price, shipping options, etc.). They will also see the details of any custom artwork requests as well as any uploaded images for reference. A user's details (name, address, email and phone number) are displayed at the bottom of the page for user reference. For superuser, a complete list of all orders and custom requests is shown, including user details and date of order. | ✅ Pass | Orders, custom requests and contact details are all viewable. Can be managed by superuser in Django admin panel. |
| Toast messages following successes or errors  | Toasts shown for login, signup, and other actions | Toast messages appear following successful or unsuccessful actions, providing feedback to the user. | ⚠️ Partial | Majority of toasts showing, however the change in delivery options seems not to appear despite the function being present and successful. |
| Order success page| Following a successful order a user will land on '/checkout-success' | Confirmation details are shown to a user including order summary and delivery details. If the user is logged in, a link to '/products' and '/profiles' is also shown. If the user is not logged in, a link to '/accounts/signup' is shown so they can sign up. | ✅ Pass | Confirmation page links back to the products for all users, different options are shown to users who are signed in and those who need to sign up. 
| Log out | Following the log out link in navbar whilst logged in | Confirmation request is shown and following confirmation user is logged out and is returned to `/home` | ✅ Pass | No notes |
| Sorting products by category | Visit `/products` and select a category | Products are filtered by the selected category and displayed accordingly. | ✅ Pass | If no products are found, a message is shown to the user. |

---

### Responsiveness Testing

Tested the site across multiple screen sizes using Chrome DevTools, Apple and Android devices and Windows laptops.

| Device             | Expected Behaviour                              | Pass/Fail |
| ------------------ | ----------------------------------------------- | --------- |
| Mobile (iPhone 14 Pro, Samsung Galaxy S23, iPhone 15 plus) | Navbar collapsed automatically, text readable and clear  | ✅ Pass    |
| Tablet (iPad)      | Navbar links clear, site clear, and checkout form clear and useable | ✅ Pass    |
| Desktop (1080p)    | Full layout visible, site responsive to browswer window size changes    | ✅ Pass    |

---

### Responsiveness Screenshots
#### Home Page (`/home`)
Mobile view (small screen)
<img src="development/images/phone_home.webp">
Tablet view (medium screen)
<img src="development/images/tablet_home.webp">
Laptop view (large screen)
<img src="development/images/laptop_home.webp">
Desktop view (xl screen)
<img src="development/images/desktop_home.webp">

#### Biography Page (`/biography`)
Mobile view (small screen)
<img src="development/images/phone_biography.webp">
Tablet view (medium screen)
<img src="development/images/tablet_biography.webp">
Laptop view (large screen)
<img src="development/images/laptop_biography.webp">
Desktop view (xl screen)
<img src="development/images/desktop_biography.webp">

#### Products Page (`/products`)
Mobile view (small screen)
<img src="development/images/phone_products.webp">
Tablet view (medium screen)
<img src="development/images/tablet_products.webp">
Laptop view (large screen)
<img src="development/images/laptop_products.webp">
Desktop view (xl screen)
<img src="development/images/desktop_products.webp">

#### Product Detail Page (`/products/<id>`)
Mobile view (small screen)
<img src="development/images/phone_product_detail.webp">
Tablet view (medium screen)
<img src="development/images/tablet_product_detail.webp">
Laptop view (large screen)
<img src="development/images/laptop_product_detail.webp">
Desktop view (xl screen)
<img src="development/images/desktop_product_detail.webp">

#### Custom Artwork Request Page (`/custom-artwork-request`)
Mobile view (small screen)
<img src="development/images/phone_custom_artwork_request.webp">
Tablet view (medium screen)
<img src="development/images/tablet_custom_artwork_request.webp">
Laptop view (large screen)
<img src="development/images/laptop_custom_artwork_request.webp">
Desktop view (xl screen)
<img src="development/images/desktop_custom_artwork_request.webp">

#### Profile Page (`/profiles`)
Mobile view (small screen)
<img src="development/images/phone_profile.webp">
Tablet view (medium screen)
<img src="development/images/tablet_profile.webp">
Laptop view (large screen)
<img src="development/images/laptop_profile.webp">
Desktop view (xl screen)
<img src="development/images/desktop_profile.webp">

#### Bag (`/bag`)
Mobile view (small screen)
<img src="development/images/phone_bag.webp">
Tablet view (medium screen)
<img src="development/images/tablet_bag.webp">
Laptop view (large screen)
<img src="development/images/laptop_bag.webp">
Desktop view (xl screen)
<img src="development/images/desktop_bag.webp">

#### Checkout Page (`/checkout`)
Mobile view (small screen)
<img src="development/images/phone_checkout.webp">
Tablet view (medium screen)
<img src="development/images/tablet_checkout.webp">
Laptop view (large screen)
<img src="development/images/laptop_checkout.webp">
Desktop view (xl screen)
<img src="development/images/desktop_checkout.webp">

#### Checkout Success Page (`/checkout-success`)
Mobile view (small screen)
<img src="development/images/phone_checkout_success.webp">
Tablet view (medium screen)
<img src="development/images/tablet_checkout_success.webp">
Laptop view (large screen)  
<img src="development/images/laptop_checkout_success.webp">
Desktop view (xl screen)
<img src="development/images/desktop_checkout_success.webp">

### Accessibility Testing

Used [WAVE](https://wave.webaim.org/) and Lighthouse accessibility checker.

#### Changes made following Wave assessement 

* <H...></H...> tags amended for consecutive consistency.
* Underlined text amended to italic to avoid confusion with links. 

| Check               | Expected Result                             | Pass/Partial/Fail |
| ------------------- | ------------------------------------------- | --------- |
| Alt text on images  | All images have alt attributes              | ✅ Pass    |
| Contrast ratio      | Text has sufficient contrast on most pages, but some elements have low contrast |   ⚠️ Partial  |
| Keyboard navigation | All interactive elements accessible via Tab | ✅ Pass    |
| ARIA labels on all external links and any links that are ambiguous | Checked and added where missing. Added appropriate labels to icons on mobile view  | ⚠️ Partial   |

### Lighthouse scores

Homepage (`/home`)

Mobile scores
<img src="development/images/home_mobile_m4_lighthouse.webp">
 
Desktop scores
<img src="development/images/home_desktop_m4_lighthouse.webp">


Biography scores (`/Biography`)

Mobile scores
<img src="development/images/biography_mobile_lighthouse.webp">

Desktop scores
<img src="development/images/biography_desktop_lighthouse.webp">

Products (`/products`)

Mobile scores
<img src="development/images/products_mobile_lighthouse.webp">

Desktop scores
<img src="development/images/products_desktop_lighthouse.webp">

Product Detail (`/products/<id>`)
Mobile scores
<img src="development/images/product_detail_mobile_lighthouse.webp">
Desktop scores
<img src="development/images/product_detail_desktop_lighthouse.webp">

Custom Artwork Request (`/custom-artwork-request`)
Mobile scores
<img src="development/images/custom_artwork_mobile_lighthouse.webp">
Desktop scores
<img src="development/images/custom_artwork_desktop_lighthouse.webp">

Profile (`/profiles`)
Mobile scores
<img src="development/images/profiles_mobile_lighthouse.webp">
Desktop scores
<img src="development/images/profiles_desktop_lighthouse.webp">

Checkout (`/checkout`)
Mobile scores
<img src="development/images/checkout_mobile_lighthouse.webp">  
Desktop scores
<img src="development/images/checkout_desktop_lighthouse.webp">

Checkout success (`/checkout-success`)
Mobile scores
<img src="development/images/checkout_success_mobile_lighthouse.webp">
Desktop scores
<img src="development/images/checkout_success_desktop_lighthouse.webp">

#### Issues

* Several third-party scripts affecting performance and causing HTTPS errors (Stripe, Cloudinary, FontAwesome and Bootstrap)
* Desktop scores generally higher than mobile scores due to third-party scripts and large images slowing load times on mobile devices.
* High-definition images, hosted on Cloudinary, causing slower load times on mobile devices.
* Some font clarity issues on mobile devices due to decorative font choice and tone.

### Bugs Found and Resolved
1) Artworks marked as sold were still appearing on the products page. Resolved by adding a sold = models.BooleanField(default=False) field to the Products model.

2) Allauth templates not loading correctly. Templates were not pulling from 'base.html' and were showing unstyled forms. Resolved by adding 'load static' to the top of all Allauth templates and ensuring that the templates extended 'base.html'. In settings.py, 'accounts' was included in TEMPLATE_DIRS erroneously, along with 'templates' and 'allauth'. 'accounts' was removed to resolve the issue.

3) Cloudinary installation caused an issue with Heroku deployment due to missing dependencies. Resolved by deleting old migrations and remaking them after adding Cloudinary to the local environment. 

4) Emails not sending correctly during development. EMAIL_BACKEND was not using smtp in settings.py during development. Resolved by adding the following code to settings.py: 'django.core.mail.backends.smtp.EmailBackend'

5) Toasts showing delivery information and grand total information during sign-in/logout processes. Resolved by adding 'extra_tags' to the messages in views.py to specify the type of message being sent (i.e. 'success' or 'info') and amending the toast code in base.html to only show toasts of a certain type in certain locations.

6) Images showing as all different sizes on the Products page. Resolved by adding CSS code to set a max-height and object-fit property to the product images on the products page.

7) Image in product detail page showing as very small on mobile devices. Resolved by adding CSS code to set a max-width of 100% for the product detail image on smaller screen sizes.

8) Overlay on homepage splash page showing a bar of the background image on laptop and desktop views. Resolved by checking unclosed tags in the HTML and amending the CSS for the overlay to ensure it covered the desired viewport height and width.

9) Bag view required side scrolling on mobile devices. Resolved by adding 'table-responsive' class and adjusting classes for images to make the bag table responsive on smaller screen sizes.

### CSS, HTML, Python and JS Validation

###  CSS validation
(W3C CSS validation service
(https://jigsaw.w3.org/css-validator/) used for CSS validation.)
<img src="development/images/css_validation_milestone_4.webp">

### HTML validation

W3C Markup Validation Service 
(https://validator.w3.org/) used for HTML validation

Issues found:
* Duplicate ID attributes between base.html and main-nav.html (resolved)
* aria-labelledby attribute missing correct ID (resolved)
* li and H4 elements not allowed as part of nav element (left as is for Bootstrap functionality - code taken from codeinstitute Boutique Ado project)
* The type attribute is unnecessary for JavaScript resources. (left as is for Bootstrap functionality - code taken from codeinstitute Boutique Ado project)
* 'strong' element and image url used in ol element (note to fix in future - left as is for now)




### Python validation
Pep8 validation (https://www.codewof.co.nz/style/python3/ and https://www.minifier.org/python-beautifier used to locate and resolve issues)

### Home app folder (home)
apps.py
<img src="development/images/apps_home.png">
urls.py
<img src="development/images/urls_home.png">
views.py
<img src="development/images/views_home.png">

### Custom_Artwork_Request app folder (custom_artwork_request)
admin.py
<img src="development/images/admin_custom_artwork.png"> 
apps.py
<img src="development/images/apps_custom_artwork.png">
forms.py
<img src="development/images/forms_custom_artwork.png">
models.py
<img src="development/images/models_custom_artwork.png">
urls.py
<img src="development/images/urls_custom_artwork.png">
views.py
<img src="development/images/views_custom_artwork.png">

### Products app folder (products)
admin.py
<img src="development/images/admin_products.png">
apps.py
<img src="development/images/apps_products.png">
models.py
<img src="development/images/models_products.png">
urls.py
<img src="development/images/urls_products.png">
views.py
<img src="development/images/views_products.png">

### Bag app folder (bag)
apps.py
<img src="development/images/apps_bag.png">
urls.py
<img src="development/images/urls_bag.png">
views.py
<img src="development/images/views_bag.png">
contexts.py
<img src="development/images/contexts_bag.png">

### Checkout app folder (checkout)
apps.py
<img src="development/images/apps_checkout.png">
urls.py
<img src="development/images/urls_checkout.png">
views.py
<img src="development/images/views_checkout.png">
models.py
<img src="development/images/models_checkout.png">
forms.py
<img src="development/images/forms_checkout.png">
signals.py
<img src="development/images/signals_checkout.png">
webhooks.py
<img src="development/images/webhooks_checkout.png">
webhook_handlers.py
<img src="development/images/webhook_handlers_checkout.png">

### Profiles app folder (profiles)
apps.py
<img src="development/images/apps_profiles.png">
urls.py
<img src="development/images/urls_profiles.png">
views.py
<img src="development/images/views_profiles.png">
models.py
<img src="development/images/models_profiles.png">



### Main Project Folder (jlc_art_ecommerce)

settings.py
<img src="development/images/settings_main_project.png">

urls.py
<img src="development/images/urls_main_project.png">

wsgi.py
<img src="development/images/wsgi_main_project.png">



### Steps taken to resolve errors:
* Lines shortened to under 79 characters, where possible without breaking code logic
* Fixed indentation issues
* Fixed missing blank lines at end of files
* Fixed missing two blank lines between classes and functions
* Fixed missing spaces after commas and around operators
* Fixed docstrings where missing

### JavaScript Validation

stripe_elements.js
<img src="development/images/stripe_elements_js_validation_milestone_4.webp">

* Missing semicolon added to end of line 116.

Inline JS in templates taken from Code Institute Boutique Ado project. 
Added missing semi-colon to remove-item JS script in bag.html. No other validation errors found.

## 7. Security Considerations
* SECRET_KEY and other sensitive information stored in env.py file, not in main settings.py file.
* Debug set to False for production deployment.
* Used Django's built-in authentication system for user registration and login. Users passwords are hashed and securely stored.
* Used HTTPS for secure communication (handled by Heroku).
* Validated and sanitized user inputs in forms to prevent SQL injection and XSS attacks.
* Used Django's CSRF protection for forms.
* Stripe handles payment information securely, ensuring PCI compliance.


## 8. Next Step Features	

Providing further payment options such as PayPal or Apple Pay would have been useful to give users more choice at the checkout stage.

Providing a wish list feature for users to save items for later consideration would improve the user experience.

Sorting and filtering options on the products page could be expanded to include price range and size.

Implementing a search function would also enhance the user experience by allowing users to quickly find specific products.

Creating a dedicated add/edit product page for the superuser to manage products directly on the site, rather than via the Django admin panel, would improve usability for the site owner.

Cancel/edit order functionality for users would enhance the user experience by allowing them to manage their orders more effectively.


## 9. Coding Sources

* Code taken from Bootstrap v5.0 and heavily adapted/edited to fit needs of site (NavBar, buttons)
* Code Institute lessons - "Love To Blog" and "Boutique Ado" python/django code along lessons as well as prior modules.
* Balsamiq was used to create wireframes
* Responsive Viewer Chrome add-on was used for responsiveness screenshots
* Django documentation used extensively throughout the project for model creation, views, forms and general functionality. https://docs.djangoproject.com/en/5.2/
* Django Allauth documentation used for user registration and authentication setup. https://django-allauth.readthedocs.io/en/latest/installation.html
* Cloudinary documentation and 'Love To Code' guidance used for media file handling. https://cloudinary.com/documentation/django_integration
* Whitenoise documentation used for static file handling. http://whitenoise.evans.io

Specific code snippets and advice taken from:

* Toast message code taken from Bootstrap documentation and Code Institute Boutique Ado project. https://getbootstrap.com/docs/5.0/components/toasts/

* extra_tags in messages was taken from Stack Overflow to help differentiate toast messages shown in different locations on the site. https://docs.djangoproject.com/en/5.2/ref/contrib/messages/

* Deployment steps taken from Code Institute Heroku deployment documentation and prior knowledge from Boutique Ado project.

* Decorator 'login_required' taken from Django documentation to protect views that require a user to be logged in. https://docs.djangoproject.com/en/5.2/topics/auth/default/#the-login-required-decorator

* if/else statements in templates taken from Django documentation to show different content based on user status. https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#if

* Stripe payment integration code taken from Stripe documentation and Code Institute Boutique Ado project. https://stripe.com/docs/payments/accept-a-payment

* Django template language documentation used extensively throughout the project for template creation and logic. https://docs.djangoproject.com/en/5.2/ref/templates/language/

* Django template conditional statements documentation used for logic in templates. https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#if

* table-responsive class from Bootstrap documentation to help make bag table responsive on smaller screen sizes. https://getbootstrap.com/docs/5.0/content/tables/#responsive-tables

* sold field added to Products model to help manage sold items so they do not appear on products page (Product.objects.filter(sold=False)). https://www.geeksforgeeks.org/python/booleanfield-django-models/

* Country set to default in checkout form using a default value in the model field, e.g. `country = models.CharField(max_length=40, default='UK')`. https://docs.djangoproject.com/en/5.2/ref/models/fields/#default

* /home redirect on homepage load via url patterns in urls.py file taken from Stack Overflow. 
path('', RedirectView.as_view(url='/home/', permanent=False)),
 https://stackoverflow.com/questions/15706489/redirect-to-named-url-pattern-directly-from-urls-py-in-django

VSCode Co-Pilot was consulted to assist in migration/deployment errors and issues faced with Stripe validation. Assistance sought early on to configure STATIC settings and later to assist with email errors and amending layout issues (i.e. the checkout page form alignment and spacing on the profiles page).
  

## 10. Media Sources
<table>
  <caption>
    Images used within site
  </caption>
  <thead>
    <tr>
      <th scope="col">Photo Title</th>
      <th scope="col"> Relative Path </th>
      <th scope="col">Source Link</th>
      <th scope="col">Page Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Art Easel Icon</th>
      <td>staticfiles/icon/art-easel-icon.ico</td>
      <td>https://www.flaticon.com/free-icon/art-easel_1000000</td>
      <td>All pages</td>
    </tr>
  </tbody>
</table>

All artwork images used within the site are the property of the site owner and artist. Photos used within the site are photographs of the artist's own work or of the artist herself.

Art material images on Request Custom Artwork page were created by me using my own photography and are the property of the site owner and artist.

## Reflection on project

This project has been a challenging but rewarding experience. It has allowed me to apply the skills I have learned throughout the course in a practical way, and to develop new skills in Django, Python, and web development in general.

I have found myself being able to problem-solve and think critically about how to implement features and functionality, and I have learned a lot about the importance of planning and organization in a project of this scale. Consistent testing and adjustment have been key to ensuring the site works as intended across different devices and browsers. 

I have thought carefully about the user experience and how to create a site that is both functional and visually appealing, while also considering accessibility and usability. I have gained the opinion of friends and family to help me assess the site from a user's perspective, which has been invaluable in identifying areas for improvement.

I look forward to being able to further develop this project in the future, adding new features and functionality as I continue to learn and grow as a developer so that it can become a fully-fledged e-commerce platform for the artist.

## 11. Acknowledgements 
* Dr Raghav Kovvuri (HE Lecturer- Computing at University Centre of Peterborough) for support and advice and understanding throughout the course. 
* Iuliia Konovalova, my wonderful, knowledgeable mentor. Thank you for trying to help stop my panic - sorry for the big Heroku headache!
* My family and friends for putting up with my stress, not seeing me for weeks on end and cancelling multiple plans, and for being my sounding board throughout the project. Also for testing the site and providing feedback from a user perspective.