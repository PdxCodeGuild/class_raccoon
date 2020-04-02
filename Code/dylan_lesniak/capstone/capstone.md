Name:
Monku 

Project Overview:
    What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?

    Problem: 
        It's difficult to complain to companies. Their email or phone numbers are often inaccessible. Often due to companies hoping customers will give up. 

    Solution: 
        App will allow customers to select the company they'd like to complain to from a drop-down list. 
            (as the app grows, that should probably switch to a search function. However, while the app is not yet expansive, this could lead to too great expectations) 
        Once selected, use JS to render a text box with which to send an email directly to the company, as well as the best phone number with which to reach a human representative. 
        App should be designed mobile-first. 
        There are sites that supply the aforementioned phonenumbers, here's hoping they have an API. 

        

Functionality: 
    Walk through the application from the user's perspective. What will they see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

    View:
        - The basic layout of the app will be a basic page (probably blue background). It will have the app name and a drop-down list of the supported sites. There will also be a link to a how-to page, where I think I can just put screenshots or something similar showing how the site is used. 
        - Email functionlity should only be available to those who have signed in to their email account. 
        - Once the site is selected, a customer-support phone number and a text box will appear. 
        Mobile should take care of the actions for the phone number. 
        - Write out your email and hit submit. Make sure that there are "are you sure" and "email sent" modals. 


    Possible Add-ons:
        - Keep track of user submissions as well as meta-data of total user submissions. 

        - Post an average wait-time for the phone number and potentially an average wait time on email responses. 

        - Meta-ratings. Bring in ratings of said sites / services from sources such as yelp, foursquare, and google, and aggregate them. 


Data Model:
    What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'.

    Users:
        - Emails sent (total, by company, and the individual emails themselves). 

    Meta:
        - Scores of all emails sent to specific companies. 

    Companies:
        - Email addresses 
        - Phone numbers
        - Emails received


Schedule:
    
    Week1:
        Set up website. Get it working for a basic pretend user, and a basic pretend website

    Week2:
        Set up for a real website. I don't know how to test this without getting in trouble. I should create a fake email address for this purpose. 

    Week3:
        CSS and testing. Add additional features if time permits. 