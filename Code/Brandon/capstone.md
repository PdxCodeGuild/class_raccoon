# Capstone Proposal for Brandon Gonzalez

## Names:
    - Site Name: Illumine 
        - App Names:
            - Virtual Barkeep
                - Plan a drink menu using the liqour you have or liqour you want
            - Virtual Sous Chef
                - Plan a menu using variations of diet
            
### **The SDLC**
 requirements/what is the problem?
 design/planning/solution
 implementation/coding
 deployment
 maintenance

1. Project overview:
    - Problem
        - What is the hardest thing to do when planning a party or a get together? Picking out drinks and food that people will talk about then and after. Illumine will provide the user with the tools to "branch" out with their ideas, pair food and drink that they otherwise wouldn't have and to explore variations using ingredients that they know, but haven't fully capitalized on. 
    - Possible libraries and frameworks:
        - HTML5, CSS3, JS, VueJS, Bootstrap, Foundation

2. Requirements
    - This virtual meal/drink planner will provide the end user with a custom list of meal and drink recipes. This benefits of a program like that will directly coincide with the requirements needed to consistently provide customers, friends and families with a diversified menu.
3. Functionality
    - Virtual Barkeep and Virtual Sous Chef will be similar in style but will provide some different functionality. The bartender app will have fewer parameters than the sous chef app. 
        - Virtual Barkeep
            1. user interface for searching drink by name, and by ingredient.
            2. add feature for saving to a list
            3. random drink suggestions button
        - Virtual Sous Chef
            1. user interface for searching by food type, ingredients, dietary restrictions
            2. add feature for saving to list
            3. random recipe generator based on food genre.
        - Virtual Planner
            1. User register and login
            2. adding and saving selections
            3. possible pairing suggestions
            4. compile a "menu" for the user based on pinned recipes
            5. shopping list functionality
4. Data Model:
    - User Database
        - First Name, Last Name, Username, Email
    - Saved recipes
        - Collection of drink and food recipes for use later.
        - Event associated recipes
    - Shopping cart?
        - For use of selected recipes, saved to database, and possibly use an api to tie into something like amazon fresh.
5. Timeline:
    - Week one:
        1. Basic layout and design of pages to be used.
            - Home Page
            - Register/login
            - User Page
        2. Django and vue initialization.
        3. Framework/Library Testing and component choice.
    - Week two:
        - Database creation and linking
        - Display Data on multiple pages
        - JS interactivity
    - Week three:
        - Styling
        - Page Condensing
        - Testing
        
       