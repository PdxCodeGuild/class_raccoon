
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

### What problem is it attempting to solve?

- last minute plan-making for poor people
- opportunities for organizations and communities to have a place to display their cheap happenings in a nice format
- one stop shop for cheap entertainment

### What are the major features of your web application?

- show the user a list of events under $10
- nav bar with search, search history, directions, saved venues, saved pins, login, logout, save/create/delete event
- search by venue, event type, name, location
- map (zoomable) *(defaults to displaying "day of" events)*
- default icons based on type of venue or event
- events will disappear as the mandatory end time of the event expires
- A legend in corner of screen that the user can hide and will display event icons and meanings
- compass that can also be hidden
- single page application using vue seems like the right way to go about this, right?
- Notifications from users events or venues
- customizable themes for your event page or venue page that display a small/quick overview of your event/venue

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
- displayed with icons
- on click description page

**displayed search results**
- based on day/time & location
- when searching, will populate concurrently with search typing?
- once searched, will populate with search results based on venue, event type, name or location

**legend in corner**
- icons and meanings *(most common in area shown)*
- text/icon coloring based on day of, week of, month of or far out

**nav bar on the side**
- login/logout
- save/create/delete event
- search
    - by venue, event type, name, location
- notifications
- your data shows up concurrently in map
- your saved places
- search history
- directions
- recommendations

**transparent compass**
- located in bottom corner
- can remove from page

**on click descriptions**
- description page *(pick a theme when creating an event)*

#### User Create/Edit/Delete Page

**A Form with these inputs and options**
- Pic
- Name
- Email
- Default Location *(not mandatory)*
- Notification/Privacy Settings
- Event list
- notifications
- save VENUES
- save event types for notifications
- simple drop pin and save Functionality without making an event or venue page

#### Event Create/Edit/Delete Page

**A Form with these inputs and options**
- pic upload
- event type selector w/ auto icon that displays as pin on main page
- input name
- input timeframe *(mandatory expire time)*
- input place
- input requirements
- create/edit/delete buttons
- display settings

#### Venue Create/Edit/Delete Page *(if inactive for a year, delete..)*

**A Form with these inputs and options**
- pic upload *(probably a stretch goal.. probably gonna have to go to another page)*
- name
- venue type selector w/ auto icon that only displays on description page
- short bio
- regular hours
- website link
- create/edit/delete buttons
- todays event!
- display settings *(probably a stretch goal...not sure how this will work... i want this to be where they choose an icon and border color for their hover box..)*

#### User Description Page
- Display's Users details
- Settings buttons
- create an event or venue buttons
- edit/delete buttons for events or venues this user has created

#### Event Description Page
- Display's Event details *(Should I use a Table?)*

#### Venue Description Page *(Is it a good idea to have this as a stretch goal for deployment?)*
- Display's Venue details *(Should I use a Table?)*

### How will their actions correspond to events on the back-end?
- saving and recording info about venues and events

## Data Model

### What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'.

**USER(ABSTRACT USER)**
- Pic
- Name
- Email
- Default Location *(not mandatory)*
- Notification/Privacy Settings
- Event list
- notifications
- save VENUES
- save event types for notifications
- simple drop pin and save Functionality without making an event or venue page

**EVENTS**
- Pic
- Name
- Event type
- Venue
- Description
- Price
- Link
- Start time and end time
- settings

**VENUES**
- Pic
- Name
- Venue type
- Event List
- description
- Link
- prices *(mandatory under $10)*
- regular hours
- todays event
- settings

**LEGEND**
- default populate icons
- icons by type

**SETTINGS**
- privacy
- display theme

## Schedule

### Here you'll want to come up with some (very rough) estimates of the timeframe for each section. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

**Week 1**
- Research API's for getting event data or set up [example](https://gitlab.com/flux2341/aapdx/-/blob/master/app/management/commands/create_dummy_events.py)
- Implement Event model, add dummy data, show events on page using vue or template rendering
- Picking Name & creating a logo
- Research google maps api to embed a map, show events as pins on map

**Week 2**
- Setting up the User Functionality (login, logout, database model)
- Allow the user to create/edit/delete events
- Allow the user to 'favorite' events, view a list of 'favorited' events

**Week 3**
- Styling & Tweaking

**Stretch**
- Any additional things i didn't achieve in the time span i had
- Deployment
- More tweaking
- Linking with popular apps
- More user options & settings
- recommendations in nav bar
