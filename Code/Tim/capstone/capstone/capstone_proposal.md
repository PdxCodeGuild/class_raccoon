# Name
### ChoraLib
(Trinity Episcopal Cathedral Choir Library App)
# Project Overview
The goal of this application is to provide a singular, phone-accessible source for Trinity Choir members to see what music should be in their folders and what music should be turned in. This is to mitigate an ongoing problem that takes up a significant amount of time and human resources for the music librarians.

# Functionality
At its base, this will be a SPA with collapsible dropdowns (accordions) to show "Music in My Folder", "Music to Turn in This Sunday", and "Music Turned in This Season" based on user type (Admin, Librarian, Adult Choir, and Choristers).

This will involve parsing the current music library excel sheet into a SQLite database to save on input time for librarians, creating a truly mobile-first web app for use by choir members, and allowing librarians to distribute music to virtual folders and set an expiration date so that music moves from Music in My Folder -> Music to Turn in This Sunday -> Music Turned in This Season based on the current date and the expiration date.

**Flow**

- Select User type (Admin and Librarian require login)
    - Admin - all functionality
    - Librarian - Ability to add new pieces and distribute music to all ensembles
    - Adult Choir and Choristers - Ability to view only
- View with 3-level accordion to display:
  - Music in My folders
  - Music to Turn in This Sunday
  - Music Turned in This Season


# Data Model
- User
  - Admin
  - Librarian
  - Choir


- Composition
  -  Catalog number (cat_num)
  -  Composer Last Name (comp_last)
  -  Composer First Name (comp_first)
  -  Title (title)
  -  Number of Copies (copies)
  -  Voicing (voicing)
    - SATB
    - SA
    - TB
    - SSA
    - TTBB
    - SSAATTBB
  -  Special Notes (spec_notes)
  -  Location (location)
  -  Final Performance Date this season (turn_in_date)
  -  Front Page image file (thumbnail) **future feature**
  -  Historical performance dates (hist_perf) **future feature**


# Schedule
**Week 1**
- Set up base Django app with Vue.js using dummy data
- Style html and css for mobile to match website

**Week 2**
- Work on functionality of compositions moving between accordion sections with turn-in date
- Work on User access levels and login system

**Week 3**
- debug app with dummy data and decide on a minimum viable project with remaining time
- deploy app
- migrate current excel library to SQLite database

**After Class**
- debug with live data
- deploy finished product to www.trinity-episcopal.org for soft release
- test with summer choir
- deploy live app for 20-21 season launch
