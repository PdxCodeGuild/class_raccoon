# SHIFTSWAP


## SCHEDULE

To do:

Week 1:
  [x]  Set up repository
  [x]  Start new Django project
  [x]  Start app, get basics
  []  Outline function/roadmap
  []  Create the JobPost model and some dummy user accounts
  []  Show a list of JobPosts and allow the user to search them

Week 2:
  []  Get basic HTML laid out
  []  Define user model (employer/contractor)
  []  register, login, logout
  []  Allow employers to create JobPosts
  []  Allow contractors to respond to JobPosts

Break:
  [] Have some fun

Week 3:
  []  Allow employers to create ContractorRatings
  []  Troubleshoot, clean code, style, etc...
  []  TEST



## PROJECT OVERVIEW

What is the primary function of the web application?
```
Bridging the gap between employers and contractors.
User can post resumes/qualification and apply for work.
Businesses can post for last minute fills jobs in the service industry, i.e sick call, no call/no show.
```
What problem is it attempting to solve?
```
Business owners/service industry searching for last minute work coverage.
Kitchen workers/Cooks, Host/Hostess, Bartenders, Food Handlers Card/OLCC.
```


## FUNCTIONALITY

Walk through the application from the user's perspective.
What will they see on each page? What can they input and click and see?

```
User function:
    Sign up/Create Account.
    Upload resume, select jobs.
    Search for jobs.
```

```
Employers function:
    Create Account.
    Post jobs: position, location, date & pay.
    Rate hired contractor.

```

## DATA MODEL

- Users
  - Employer/Contractor
- JobPost
  - EmployerID
  - Title
  - Description
  - StartDatetime
- ContractorRating
  - JobPostID
  - ContractorID (which contractor this was for)
