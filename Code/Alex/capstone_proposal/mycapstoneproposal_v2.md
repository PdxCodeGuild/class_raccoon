
# Capstone Proposal
*(please feel free to comment as you go)*

## My Main Concerns
    - deployment now or stretch goal
    - what api's
    - mobile friendly from the start
    - am i missing anything? pages?
    - i think this will be a many to many kind of thing

## Name

**Live Cheap or Party Free** *(still thinking)*

## Project Overview

### What are the major features of your web application?

    - home page map display (with zoom) of $10 or under events *(default displays "day of" events)*
    - customizable hover boxes for your event or venue that display a small/quick overview of your event/venue
    - create event/venue with customizable display icons or default icons based on type of venue or event
    - events will disappear as the mandatory end time of the event expires
    - single page application using vue seems like the right way to go about this, right?

### What problem is it attempting to solve?

    - last minute plan making for poor people
    - opportunities for organizations and communities to have a place to display their cheap happenings in a nice format
    - one stop shop for cheap entertainment

### What libraries or frameworks will you use?

    **VUEJS       DJANGO      HTML5      CSS3** *(possibly: bootstrap, foundation or materialize)*

## Functionality


### Walk through the application from the user's perspective.

    - I'm a local small organization looking for more people to attend my shows/gatherings/whatever and now i have an easy to use application to upload my events on to, where people can easily see info about what we're all about.

    - I'm a college student looking for volunteer opportunities to put on my resume

    - Wow, I just realized I'm a young or old person and have nothing better to do than make friends cheaply near me. I wonder if there's an app that just displays all the possible cheap options all in one place... BAM! Live Cheap or Party Free (still have to come up with an actual name).. I can see all these different things i could do with the community and with easy to see descriptions and locations. My life is totally different now :)

### What will they see on each page?

    - I think I will only need 4 pages *(shooting for as few as possible)*

#### Main Display Page

    **todays events**
        - displayed in icons/dropped pins
        - on click descriptions

    **displayed search results**
        - based on day/time
        - based on location

    **key in corner**
        - icons and meanings *(most common in area shown)*
        - text/icon coloring based on day of, week of, month of or far out

    **nav bar on the side**
        - login/logout
        - save/create/delete event
        - search
            - by venue, event type, name, location
        - notifications
        - your data in map
        - your places
        - directions
        - recommendations

    **transparent compass**
        - located in bottom corner
        - can remove from page

    **hover descriptions**
        - transparent text box with only a border *(editable when user creates event)*
        - border color is the colored based on date/time colors

#### Event Create/Edit/Delete Page
    **A Form with these inputs and options**

    - pic upload
    - input name
    - input timeframe *(mandatory expire time)*
    - input place
    - input requirements
    - create/edit/delete buttons
    - display settings

#### Venue Create/Edit/Delete Page
    **A Form with these inputs and options**

    - pic upload *(probably a stretch goal.. probably gonna have to go to another page)*
    - name
    - short bio
    - regular hours
    - website link
    - create/edit/delete buttons
    - todays event!
    - display settings *(probably a stretch goal...not sure how this will work... i want this to be where they choose an icon and border color for their hover box..)*

#### Event Description Page
    - Display's Event details *(Should I use a Table?)*
    - Create/edit/delete buttons

#### Venue Description Page *(Is it a good idea to have this as a stretch goal for deployment?)*
    - Display's Venue details *(Should I use a Table?)*
    - Create/edit/delete buttons

### How will their actions correspond to events on the back-end?

    - I'm hoping that my back end will be able to successfully populate the page with results similar to whatever they search for. I think that's going to take a lot but I'm not sure. They should be able to save and be notified and also add events
**KEY DEFAULT POPULATE**
    <!-- Models, Views, Data -->

## Data Model

### What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'.

**EVENTS        VENUES        KEY DEFAULT POPULATE         IMAGES         ICONS         DISPLAY SETTINGS         USER         RECOMMENDATIONS         NOTIFICATIONS**

## Schedule

### Here you'll want to come up with some (very rough) estimates of the timeframe for each section. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

    **Week 1**
        - Monday:
        - Tuesday:
        - Wednesday:
        - Thursday:
        - Friday:

        - PROTOTYPES
        - Choosing API's
        - Picking Name & creating a logo
        - Hope to have my basic skeleton in ready in Django and Html
        - I'm also hoping to start on week 2's stuff towards the end of my first week

    **Week 2**
        - Monday:
        - Tuesday:
        - Wednesday:
        - Thursday:
        - Friday:

        - Setting up the User Functionality
        - Getting all my pages working
        - API's and Database formats and everything finalized

    **Week 3**
        - Monday:
        - Tuesday:
        - Wednesday:
        - Thursday:
        - Friday:

        - Styling & Tweaking

    **Stretch**
        - Any additional things i didn't achieve in the time span i had
        - Deployment
        - More tweaking
        - Linking with popular apps
        - More user options & settings


## Your Concerns
    -
