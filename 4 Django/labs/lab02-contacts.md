
# Lab 2: Contacts

Let's build a CRUD application for managing a contact list.

## Model

Our `Contact` model will have the following fields:

- `first_name` - `CharField`
- `last_name` - `CharField`
- `birthday` - `DateField`
- `phone_number` - `CharField`
- `is_cell` - `BooleanField`

## Pages

The application will have the following pages:

- `/contacts/` will show a list of contacts each with an `edit contact` button, and a button for `new contact`
- `/contacts/<id>/` will be a detail page for a contact with the given `id`
- `/contacts/new/` will have a form for creating a new contact
- `/contacts/<id>/edit/` will have a form for editing a contact

## Steps

These are the recommended steps:

1. Define the model in the app's `models.py`
2. Register the model with the admin page, log in and create some records to make sure everything works
3. Create the contact detail page, which displays the different fields and their values
4. Create the the new contact page
5. Create the edit contact page

