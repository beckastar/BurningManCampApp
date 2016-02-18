This is a Django app which was built to facilitate the management of a Burning Man camp.  It tracks campers, budget, inventory, and work shifts on and off playa. 

Bioluminati is a 20 year old Burning Man camp with 35 campers attending each year, and 150 total members.  We have a complicated infrastructure, including a fully functional kitchen, with walls and an ice box and a grill, as well as a chill dome, and uber tents and yurts, and a bike pool.  We store everything in an 18 foot trailer in Gerlach.  All of this infrastructure requires a lot of orchestration and tracking. 
 

This CRUD webapp allows administrators to add items and edit data for:

- Camp inventory:  the camp owns an 18 foot trailer that holds all the supplies needed to house its  members, as well as a full kitchen and kitchen supplies. 

- Bicycles: the camp keeps 25 bicycles in the truck, and these are carefully inventoried, maintained and designated to campers each year.

- Art supplies (shown as PYB materials): the camp runs a service at Burning Man where people can decorate their bikes, and throughout the year, our members collect materials for this purpose.  This allows for data input of material and quantity, and displays everything which has been acquired.

Campers can create and edit their profiles, and sign up for meal shifts or drop their meal shifts.  Users input their arrival dates as well as their meal restrictions, transit information, emergency contact information, and other relevant information.  All the profiles are displayed in a table view, and a user can view all members, or only those who are coming this year. 

While we're at Burning Man, members are asked to take four kitchen shifts - each meal is one shift, and there are three three possible roles.  There is a master view where you can see all shifts, or you can filter for only available shifts.  You can sign up by clicking a button, and remove yourself by clicking a button.  There are two meals each day, and the number of shifts per  meal is determined by the chef, but each meal has at least the following three roles:

-Chef
-Sous Chef
-KP

We run Bike Mutation Station, where people at Burning Man can decorate their bikes with paint, fabric, and other assorted odds and ends.  In the app is a form where people can sign up for shifts at Bike Mutation. We haven't decided whether or not we'll be using this. 

All data is displayed in tables, with embedded forms at the top row for people to input new data, and the design of the website is deliberately simple and accessible, with a minimalist approach to design and user interface. 

A master view displays the deatils for the week. In a calendar view for the week, each day is displayed individually, and people can easily see who is in camp on which days, and which meal restrictions need to be considered for any given meal. 

There's an admin script that deletes the data that is known to change every year, which can be run at the terminal with python manage.py happy_new_year.  It resets the arrival and departure days in people's profiles, sets the value for whether or not people are attending that year to False, and clears all of the meal shift assignments. 

It can be viewed on Heroku at https://sheltered-island-22241.herokuapp.com/

The following features are still under development:

1. Design changes -   Create wireframes. Adjust color scheme, borders, centering.
2. UI changes - accessibility and user flow
3. Export / download data  
4. Chef's control page, where the chef signs up for a meal, inputs the menu, and dictates the amount of support s/he will need in the kitchen
5. Get access to bioluminati.org 

Nice to have features I'm planning to add:

1. Tell each camper how many more shifts they need still need to sign up for
2. Chef control, where each chef can create the number of shifts required for their particular meal
3. Auto CSV exports included in the happy_new_year script before data is deleted
4. Easy view into old data

 


 
