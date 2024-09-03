# Caldwell Cosmetics - My Milestone Project

![Responsive Display](documentation/responsive_screens.png)

## Introduction

Caldwell Cosmetics is a full-stack web application designed to showcase and manage a cosmetic brand's products and treatments offered. The website includes features like a landing page, designed to inform the user of everything the application has to offer; a treatments page, which provides detailed information on the treatments offered, products used and any aftercare required; an admin interface for content management and a booking system which will allow users to book timeslots on a calendar for their treatments. The project is built using Django and deployed on Heroku.

[Visit the Website Here](website_link)

<a href="https://github.com/HCaldwell95/caldwell-cosmetics-full-stack" target="_blank">
Visit the Project's GitHub Repository Here
</a>

\
&nbsp;

# Table of Contents

1. [Introduction](#introduction "Introduction")
2. [UX - User Experience Design](#ux---user-experience-design "UX - User Experience Design")
   * [Strategy](#strategy "Strategy")
     * [Purpose](#purpose "Purpose")
      * [User Stories](#user-stories "User Stories")
         * [For This Sprint](#for-this-sprint "For This Sprint")
         * [For Future Sprints](#for-future-sprints "For Future Sprints")
   * [Scope](#scope "Scope")
     * [Sprint 1](#sprint-1 "Sprint 1")
     * [Sprint 2](#sprint-2 "Sprint 2")
     * [Future Sprints](#future-sprints "Future Sprints")
   * [Structure](#structure "Structure")
      * [Project Applications](#project-applications "Project Applications")
     * [Project Databases](#project-databases "Project Databases")
		* [Website User](#websiteuser "Website User")
		* [Ticket](#ticket "Ticket")
   * [Surface](#surface "Surface")
    	* [Font](#font "Font")
    	* [Icons](#icons "Icons")
    	* [Colours](#colours "Colours")
    	* [Responsive Screens](#responsive-screens "Responsive Screens")


3. [Features](#features "Features")
   * [Existing Features](#existing-features "Existing Features")
		* [Landing Page](#landing-page "Landing Page")       
		* [Navigation Bar](#navigation-bar "Navigation Bar")       
		* [Scrolling Text Bar](#scrolling-text-bar "Scrolling Text Bar")       
		* [Find Us Map](#find-us-map "Find Us Map")       
		* [How to Book Treatments Section](#how-to-book-treatments-section "How to Book Treatments Section")       
		* [Footer](#footer "Footer")              
		* [Profile](#profile "Profile")   
        * [Treatments Page](#treatments-page "Treatments Page")
        * [Meet The Team Page](#meet-the-team "Meet The Team Page") 
		* [My Bookings Page](#my-bookings-page "My Bookings Page")       
		* [New Booking Page](#new-booking-page "New Booking Page")       
		* [Edit Booking Page](#edit-ticket-page "Edit Booking Page")       
		* [Delete Booking Page](#delete-ticket-page "Delete Booking Page")             
		* [Django Template Pages](#django-template-pages "Django Template Pages")       
		* [Messages](#messages "Messages")       
		* [Error Pages](#error-pages "Error Pages") 
4. [Technologies Used](#technologies-used)
   1. [Programming Language](#programming-language)
   2. [Tools Used To Develop The Application](#tools-used-to-develop-the-application)
   3. [Environment Variables](#environment-variables)
   4. [Database Configuration](#database-configuration)
5. [Testing](#testing)
   1. [Code Validation](#code-validation)
   2. [Manual Testing](#manual-testing)
   3. [Automated Testing](#automated-testing)
   4. [Resolved Bugs](#resolved-bugs)
6. [Deployment](#deployment)
   1. [Preparation](#preparation)
   2. [Deploying the Application to Heroku](#deploying-the-application-to-heroku)
   3. [Forking the Github Repository](#forking-the-github-repository)
   4. [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
7. [Credits](#credits)
   - [Code](#code)
   - [Media](#media)
8. [Disclaimer](#disclaimer)
\
&nbsp;

# UX - User Experience Design
User Experience of UX focuses on how accessible the website is to the user and it’s ease of use, which is crucial to the website’s success.

The UX aspect of the project can be broken down into 5 Planes:
* The Strategy Plane
* The Scope Plane
* The Structure Plane
* The Skeleton Plane
* The Surface Plane
\
&nbsp;

## Strategy
In order to ensure the project aligns with these planes, it is vital to keep the target audience at the forefront at all times. It is vital to ensure that the project has real world use and that its design is transferrable to other sports events which also require the user to book a ticket.

The target audience consists of:
* 18 – 65 year olds.
* People who are conscious of their well-being and enjoy self-care.
* People who like to look their best and treat themselves.
* People who may have minor skin conditions and are looking to alleviate them.

As a result, users will expect:
* A website with easy navigation and a logical progression to its flow.
* Lots of information relating to the treatment details and products used.
* The ability to register and log in to their account to review their treatment history and receive specific recommendations.
* The ability to book, edit and cancel treatments.
\
&nbsp;

### Purpose
The purpose of this website is to promote the Caldwell Cosmetics brand, providing users with the ability to book and amend treatments online. It also serves as a comprehensive resource, offering detailed information on each available treatment.

### User Stories
| id  |  Content | Label |
| ------ | ------ | ------ |
|  [1](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/1) | As a user, I can navigate through the website easily so that I can get more information about the treatments, products used and bookings. | Must Have |
|  [2](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/2) | As a user, I can get information regarding the treatment details so that I can spend less time having to search for the suitable information. | Must Have |
|  [3](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/3) | As a user, I can obtain treatment booking information so that I can easily book treatments. | Must Have |
|  [4](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/4) | As a user, I can find the business' social media accounts so that I can keep up-to-date with the latest treatments, products and deals offered. | Should Have |
|  [5](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/5) | As a user, I can see other people's bookings anonymously so that I can review remaining availability and book in my treatments accordingly.| Could Have |
| [6](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/6) | As a user, I can book an appointment so that I can attend and receive my treatment/products. | Must Have |
| [7](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/7) | As a user, I can register or log in so that I can manage my bookings. | Must Have |
| [8](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/8) | As a user, I can book treatments for others so that I can bring more people to the business. | Must Have |
| [9](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/9) | As a user, I can see if I am logged in so that I can easily log out or log in. | Must Have |
| [10](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/10) | As a user, I can obtain email confirmation of my ticket bookings so that I know I have successfully booked the treatments. | Could Have |
| [11](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/11) | As a user, I can select my preferred practitioner when booking treatments and review their remaining availability so I can book my treatments. | Must Have |
| [12](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/12) | As a user, I can easily use the navbar to navigate the website so that I can find all relevant content. | Must Have |
| [13](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/13) | As a user, I can edit and/or delete appointments I have booked when logged in so that I can make any necessary changes. | Must Have |
| [14](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/14) | As a user, I can edit my user details when logged in so that I can ensure that my details are up-to-date. | Must Have |
| [15](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/15) | As a user, I can easily reach the home page in case I get an error so that I am not stuck on an error page and have to select the back button. | Must Have |
| [16](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/16) | As an admin, I can log in so that I can access the website's backend. | Must Have |
| [17](https://github.com/HCaldwell95/caldwell-cosmetics-full-stack/issues/17) | As an admin, I can delete appointments booked by users so that I can alter bookings and amend errors when required. | Must Have |

\
&nbsp;

## Scope

To ensure the completion of the current sprint, which includes all elements required for the project submission, the focus was directed as follows:
\
&nbsp;

### Sprint 1
This sprint focuses on the “Must Haves” and the marking criteria:
* Development of a home page with basic information on booking treatments and accessing details about treatments and products.
* Implementation of a navigation bar that allows users to easily access different pages within the site..
* The ability of the user to login and create a profile.
* A booking system that enables users to schedule, edit, or cancel treatments as needed.
\
&nbsp;

### Sprint 2
This sprint builds on Sprint 1:
* Enhancement of the home page with additional details on booking procedures, improved treatment and product information, and added styling and animations for a more engaging user experience.
* Creation of a calendar feature that displays available time slots, allowing users to book treatments at their convenience.
\
&nbsp;

### Future Sprints
Elements to add to the site in the future:
* Integration of email confirmation for bookings.
* Option for users to input payment details to confirm bookings.
* Implementation of a third-party payment processing system to handle transaction payments.
\
&nbsp;

## Structure

Having a well-organized project structure facilitates a logical development process and ensures that sprint tasks can be efficiently tracked. The project is divided into applications to manage different functionalities and database tables to systematically store user data.

### Project Applications

The project consists of three applications:

* home_details: Provides an overview of Caldwell Cosmetics, including sections such as "About Us" and "Find Us." It provides brief descriptions of all treatments and guides users to various parts of the website and social media links.
* treatment_details: Delivers in-depth information about treatments and products, including aftercare instructions and details on who would likely benefit from each treatment.
* meet_the_team_details: Features profiles of the practitioners at Caldwell Cosmetics, highlighting their qualifications and experience to reassure users of their expertise.
* booking_details: Oversees the booking process, including creating, editing, and deleting of bookings. Users are required to create a profile, which is associated with their treatment reservations.

### Project Database

The project features two distinct databases to manage different functionalities:

Subscription Newsletter Database: Manages user subscriptions to the newsletter. This database stores information related to users who subscribe to receive updates and promotions via email.

Booking System Database: Facilitates the calendar-based booking system, allowing users to create, manage, and track their bookings. This database includes user profiles and booking details.

The schematic below illustrates the relationships between the relevant models:

#### Subscription Newsletter

The Subscriber model is used to manage information for users who subscribe to the newsletter. It includes the following field:

* email - The email address of the subscriber, which is used to send newsletters and updates.

#### Booking System

The BookingSystem model captures detailed information about users who book treatments. This model is used to gather comprehensive user data to enhance their booking experience. It includes:

username - A unique username selected by the user during registration.
first_name - The user's first name.
last_name - The user's last name.
email - The user's email address.
address - The user's home address.

The BookingSystem model is linked to the booking records as a foreign key in the booking system. This design allows users to update their personal information without duplicating data entry, thereby enhancing privacy and user experience.

## Skeleton

The initial skeleton provides a broad framework that is refined and expanded upon. It serves as a foundation for developing a plan that aligns with the requirements outlined in the [user stories](#user-stories "User Stories") and the [sprints](#scope "Sprints"). This framework facilitates the creation of wireframes, which act as design tools and outline the basic structure of the website.
\
&nbsp;

### Wirefames
[Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") was utilised to design the website's layout and navigation flow. I started by developing a mobile version following a mobile-first approach and then created versions for medium and large screens. Ensuring responsiveness across various devices was a key focus.

### Wireframes

Basic wireframes are provided below. Please note that these may differ slightly from the final website design:

* [Home Page](image.jpg "Home Page")
* [Treatments](image.jpg "Treatments") – The Treatments Page is very similar to the Home Page as I wanted to maintain consistency throughout the website, with each page acting as a different comprehensive source of information.
* [Meet The Team](image.jpg "Meet The Team") – The Meet The Team Page follows the same rulings and stylings as the Home Page and Treatments Page, showing only detailed information on the practitioners at Caldwell Cosmetics.
* [My Bookings](image.jpg "My Bookings") – The Bookings Page follows the trend, displaying only the information and fields required to create, edit and delete bookings.
\



## Surface

### Font
### Icons
### Colours
### Responsive Screens



# Features

## Existing Features

### Landing Page
### Navigation Bar
### Scrolling Text Bar
### Find Us Map
### How to Book Treatments Section
### Footer
### Profile
### My Bookings Page
### New Booking Page
### Edit Booking Page
### Delete Booking Page
### Django Template Pages
### Messages
### Error Pages



# Technologies Used

## Languages
## Tools
## Styling
## Validation
## Databases


# Testing

## Code Validation
### W3C HTML Validator
#### First Attempt of Home Page
#### Final Attempt of Home Page
#### Only Attempt of the Django Templates
#### First Attempt of Bookings Page
#### Final Attempt of Bookings Page

### W3C CSS Validator
#### First Attempt of CSS File

### JSHint
#### Final Attempt of JavaScript Files

### Python Syntax Checker PEP8 Validation
#### First Attempt of Python Files
#### Final Attempt of Python Files

## Lighthouse
### Final Attempt for Lighthouse

## Responsiveness
## Web Aim Contrast Checker
## Browser Compatability
## Manual Testing
## Automated Testing

# Bugs
## Resolved
## Unresolved

# Deployment
## Create Application
## ElephantSQL
## Cloudinary
## Final Repo Preparations
## Heroku Deployment

# Credits
## For Code Help and Advice
## Helpful Resources
## For Content and Code



## References

https://www.youtube.com/watch?v=LL6qXu8FmVo - Subscription Newsletter Feature

## Educational Disclaimer

This project has been created as a part of my personal learning journey in Full-Stack development. It is intended for educational purposes only and should not be considered a fully functional or production-ready application. The project may contain bugs, security vulnerabilities, or incomplete features, as it is designed to demonstrate concepts and practices learned during my studies.

By using this project, you acknowledge that it is a work in progress and should not be used in a live environment without further review and testing. I do not assume any responsibility for any issues, damages, or losses that may arise from its use.


## Personal Notes

Subscription Newsletter Functions:

    home_details Function:

    Purpose: Renders the home page template.
    Arguments: Takes an HTTP request object.
    Returns: An HTTP response that renders the home.html template.
    subscribe_to_newsletter Function:

    Purpose: Handles the subscription process for the newsletter.

    Arguments: Takes an HTTP request object.

    Returns: A JSON response indicating whether the subscription was successful or if there were errors.

    Steps:
    Check Request Method: Ensures the request method is POST.
    Form Handling: Creates a form instance with POST data and checks its validity.
    Save Subscriber: If valid, saves the subscriber to the database.
    Prepare Email: Constructs the email content using a template and context.
    Send Email: Sends an email to the subscriber using Django's send_mail function.
    Respond to AJAX: Sends a JSON response indicating success or failure.
    Invalid Request Handling: If the request is not POST, responds with an error message.