# Social Yoga - Full Stack - Milestone 4
 
This app allows users to sign up for simple yoga classes that instructors can make available.  
If the user likes the free lessons an instructor created, they can purchase other paid lessons
from them.

* [Live link to site](#/ 'Heroku live link to app')
* [This Repository](https://github.com/KelvinHere/milestone-4 'Github repository link')

## ToDo
contact email and social media links
subsort rating so lessons with most reviews appear higher
add a confirm layer to deleting lessons
setup development database before submitting

## Bugs
messages not showing color on topbar
Error on stripe checkout when checking out on deployed version

## Contents
 
1. [**UX**](#ux)
   * [Project Purpose](#project-purpose)
   * [Wireframe Designs](#wireframe-designs)
   * [User Stories](#user-stories)
   * [Business Goals](#business-goals)
   * [Developer Goals](#developer-goals)
   * [Design Choices](#design-choices)   
       * [*General Design*](#general-design)
       * [*Colours and Fonts*](#colours-and-fonts)
2. [**Features**](#features)
   * [Existing Features](#existing-features)
       * [*Sorting*](#sorting)
       * [*Database*](#database)
       * [*Backend*](#backend)
       * [*Frontend*](#frontend)
   * [Future Features](#future-features)
       * [*Near Future*](#near-future)
       * [*Far Future*](#far-future)
3. * [**Changes during Development**](#changes-during-development)
4. * [**Testing**](#testing)
5. * [**Technologies Used**](#technologies-used)
6. * [**Deployment**](#deployment)
        * [Version Control](#version-control)
        * [Local Deployment](#local-deployment)
        * [Heroku Deployment](#heroku-deployment)
        * [Deployment with Gunicorn](#deployment-with-gunicorn)
7. * [**Credits**](#credits)
       * [Content](#content)
       * [Media](#media)
       * [Acknowledgements](#acknowledgements)
 
## UX
 
#### Project Purpose

The purpose of this app is to create a platform where students can learn yoga remotely and
instructors can sell their lessons.  Users will be able to find an instructor and lessons 
through the search and filtering options then view ratings on instructors and reviews/ratings on
lessons.

#### Wireframe Designs
 
- The home page
![HomePage](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/wireframe/1-Index.jpg "Home page")
- Signup / Register / Logout page
![AccountsPage](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/wireframe/2-Login_Out.jpg "Login / out / signup page")
- Sortable list of instructors on the site
![InstructorsPage](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/wireframe/3-Instructors.jpg "Instructors page")
- An instructors page, includes profile and all lessons with ability to subscribe or buy
![InstructorPage](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/wireframe/4-Instructor.jpg "Instructor page")
- A typical lesson page, paid or free
![LessonPage](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/wireframe/5-Lesson.jpg "Lesson page")

#### User Stories
As a site user I want to
1. Be able to register to the site to save my info for future use *
2. Quickly log in or out of the site *
3. Be able to recover my password *

As a student user I want to
1. Have a free lessons to see if I like an instructor *
2. Find an instructor through reviews as I need to have some confidence before buying lessons *
3. Learn yoga by watching videos *
4. Be able to buy a lesson I like the look of *
5. Be able to get extra information about a lesson before I use / buy it *
6. Leave a review of a lesson because I may like or dislike it enough to comment on it *

As an Instructor I want to
1. Create free lessons to get students interested in me as an instructor *
2. Create paid lessons to make some money *

As site admin I want to:
1. See requests from instructors *
2. Change privilages for users and instructors *
3. View reviews that users flag as innapropriate because I want to keep my website family friendly *
 
#### Business Goals

The business goal of this site is to sell yoga lessons to students.  The lessons will be created by instructors who
would like to join the site, who can create free lessons and paid lessons.  The website will take a 
cut of the lessons sold.  It will create a safe marketplace where users can get feedback by ratings and reviews of
instructors before buying lessons through a secure service.
 
#### Developer Goals
 
Each feature must be well programmed, function properly and tested to be bug free.
 
This project will display I have an understanding of full stack development from inception
to deployment.
 
Show an understanding of Django, Python, Postgres, Javascript, jQuery,
HTML, CSS, Gunicorn, Stripe payments and more, and how they all interact to form a final product.
 
#### Design Choices

##### General Design

Bootstrap is my chosen framework to create the app as it is quick to style pages in a familliar way.  It will follow common 
design principles so it will be familliar and intuative to use.  The site will keep a minimal clean look to keep information 
clear on smaller screens as this will be a responsive mobile first app.

As the database of stuents and lessons grow, filtering, searching, sorting and subscribing to lessons & instructors
will be available.

Navigation and selection will be consitent throughout the app, with no need to use the browser back button.

##### Colours and Fonts
 
**Font 1**  - Lato is used for branding, titles, a strong font that is not completely serious lines up with the sytle and feel of this apps.
 
**Font 2** - Quicksand is used for content.  A more delicate font that takes second seat to the more important information displayed in Lato.
 
**Colours** - Main colours of white (modern and clean) with blocks of medium brown (earth/nature) set the tone of mellow, natural and modern without resoring to garish colours.  Text will be brown on white or off-white on brown for consistancy.  The only strong colours are call to action and function buttons to help the user with the interface.  Any other colours will be light pastal.  All this will set the canvas for the instructor generated content and should not take away from their lesson and profile images.
 
## Features

### Quick feature breakdown

A quickreview of features on the site, more detailed descriptions futher down.

- User can:
    - Register / Sign In / Signout / Confirm Email / Reset Password
    - View their profile
        - Edit their profile
        - Request to become an instructor
        - View a list of purchased lessons
    - Search available instructors
        - Sort these results by Name / Rating / Number of lessons available
    - View lessons
        - By Instructor
        - Search lessons
        - Filter these results by All / Purchased / Subscribed
        - Sort these results by Name / Instructor / Rating / Price
            - All searching, sorting and filtering can be applied in any order and the results will stack
        - Subscribe / Unsubscribe to a lesson
        - Start a lesson that is free or they own
    - Buy lessons
        - Add a lesson they do not own to their basket
        - Remove a lesson from their basket
        - See if they qualify for a discount
        - See the cost of each lesson and mini-description in thier basket
        - See a grand total
        - Checkout with Stripe
        - Start their lessons right from the checkout page
    - Review lessons
        - Create / Edit / Delete thier reviews
        - Flag a review for administrator review

- Instructor can:
    - Do anything a User can
    - View a list of lessons they created
        - Create / Edit / Delete their lessons

- Administrator can:
    - Do anythng a User can
    - View all requests to be an instructor
        - Accept / Reject that request
    - View a list of instructors
        - Remove the instructor priveliage
    - View a list of flagged reviews
        - Ignore the flag or delete the review

### Nav bar

The nav bar appears on every page, it is locked to the top on larger screens and can be scrolled away on smaller screens.  The basket will display how many
items it has inside.  Each time the navbar is loaded it uses a variable in a context processor in the checkout app called `product_count`, which allows the navbar
to always have the information needed, this context processor is documented in the 
[Solved Interesting Bugs](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/testing.md#solved-interesting-bugs) section of testing.md as an interesting 
case "Instructor deletes lesson that is already a users basket"

- Logo Brand is always a link home
- Navbar expands from burger button on larger screens
- If logged in basket is always on the navbar and never collapses
- basket has "+n" where n is equal to the number of items in it
- 'Instructors' link takes user to a list of instructors to chose from
- If logged in 'Lessons' dropdown gives choice of All / Subscribed / Purchased lessons
- 'Account' link is personalised if user is logged in and has the following options
    - Logged out: Register / Signin
    - Logged in User: My Profile / Logout
    - Logged in Instructor: Instructor Admin / My Profile / Logout
    - Logged in Administrator: Superuser Admin / My Profile / Logout

### Home page

- Website main text is personalised to the user if logged in
- "Your subscribed lessons" call to action button if logged in to promote engagement
- "Instructor admin" call to action button if user is an Instructor to promote engagement
- Personalised Toast to show login success in unobtrusive position


### Superuser_admin page

Allows an administrator to easily deal with user requests and privalages without using the django /admin page.
It consists of three tabs, Request, All Instructors, Flagged.

The page is responsive, the tabs are collapsed to a vertical arrangement on mobile and horizontal on larger screens.

- Requests - User requests to become instructors
    - **Functionality**
    - This tab displays current amount of user requests to be dealt with using a styled red icon, ie 'Requests **+2**'
    - Each card under this shows the profile picture, Username, Profile and Email link so an administrator can contact them and decide to 'Accept' of 'Reject' the request from the buttons below the request.
    - If accepted the user is granted instructor status which gives access to the Instructor Admin page to create / edit / delete lessons.  The request is removed from the superuser_admin page
    - If rejected the users request is set back to standard user and the request is removed from the superuser_admin page
    - **Responsiveness**
    - The user request changes layout between small and large screens for easier viewing

- All Instructors - A list of all instructors
    - **Functionality**
    - This tab displays a list of all instructors
    - A button to remove instructor status is on each instructor if needed
    - **Responisivness**
    - Items change layout from small to larger screens for easier viewing

- Flagged - Flagged reviews
    - **Functionality**
    - This tab displays a list of flagged reviews
    - The flagged review cards show
        - Who created the review
        - The lesson it was created for
        - The review content
        - A list of people who flagged the review
        - An 'Ignore' button if the review is fine
        - A 'Remove Review' button to remove the review from the database
    - `LessonReviewFlagged` is the model used to handle flags
        - It contains two foreign key fields `Profile` of the user who flagged the review and `LessonReview` the actual review
        - If a flag is ignored all entries of `LessonReviewFlagged` that contain the `LessonReview` in question are deleted to save the administrator having to delete them individually or them staying redundantly in the database forever.
        - If a `LessonReview` is deleted all entries of `lessonReviewFlagged` that contain the foreign key `LessonReview` are removed as the field is set to on_delete=models.CASCADE.
    - **Responsiveness**
    - None needed

### Instructors page

This page gives the user a list of instructors, by default they are sorted by rating high to low.

- **Functionality**
- Instructors can be searched by name or partial name
- Instructors can be sorted by Rating / Name / Number of lessons available
- Sorting can be stacked with searching
- The user can press the "Enter Studio" button to get more information about an instructor and a list of ther lessons to start / subscribe / buy
    - With this "studio page" the user can filter, sort **and** query the passed instructors lessons
- **Responsiveness**
- On small screens the instructor card is vertically stacked with a small profile image
- Larger screens the card is layed out horizontally with a larger profile image

### Instructor Admin page

Through tabs the instructor can view lessons they have created and also create new lessons.  Each lesson will be displayed as a card with extra information such as how many students have bought or are subscribed
to it.  Sales will show in date order, newest first all sales the instructor has made, and the amount they will receive after the 
sites cut.  Support will have the current sites email link

- **Functionality**
- lessons are sorted by date added, newest first
    - 'Edit' button allows user to edit a lesson
    - 'Delete' button allows an instructor to delete a lesson as long as no one has bought it
    - 'Create lesson' allows an instructor to make a new lesson
- Sales displays all sales this instructor has made
- Support displays the current sites email
- **Responsiveness**
- On small screens the lesson card is vertically stacked with a small profile image
- Larger screens the card is layed out horizontally with a larger profile image
- The sales div re-orders for easier viewing over screen sizes

### Lessons page

This page shows a lists of lessons using pagination, they can be searched filtered and sorted.

To save on repeat code (DRY principle) the 'instructor studio' uses this lessons page with an 'instructor_profile_header' snippet activated by context to display instructor information over their filtered lessons.

- **Searching / Sorting / Filtering**
- Lesons can be filtered and sorted
    - Filter by All / Subscribed / Purchased
        - A tick shows which filter is currently applied
    - Sort by Rating / Name / Price / Instructor Name
        - All sorting can be reversed
- Lessons can be searched by name
    - All filtering and sorting is retained

- Example of a complex search = Search by instructor 'Sophia' & search lesson name 'dog' & filter by subscribed & sort by rating descending
    - This would return Lessons you are subscribed to, made by 'Sophia' that contain 'dog' in the lesson name and will be sorted by highest rating first.
 
**Lesson cards**
A lesson card contains a lesson image, name, instructor, price, small description, more details button and context sensitve buttons.
- **Main functions**
    - Pagination saves long loading times an scrollbars by distributing large lists of lessons into pages
    - Logged out users: A call to action button "Signup to view" encourages the user to join the site and directs them to the Signup page
    - Logged in users :-
        - Paid Lessons that are unpurchased will show an add to basket button ie "€5.99" with an add to basket icon.
        - Lessons that are free or purchased that are not subscribed to show a red "Subscribe to lesson" button.
        - Lessons that are subscribed to show an Unsubscribe and Start Lesson button.
- **Buttons**
    - Next and Previous buttons take user to next and previous page of lessons while keeping filter/search/sort parameters
    - Clicking 'Subscribe to lesson' repalces that button using JS to the 'Unsubscribe' and 'Start Lesson' buttons
    - Clicking 'Unsubscribe' replaces itself and the 'Start Lesson' button using JS with the 'Subscribe' button.
    - Clicking 'Start Lesson' starts the lesson
    - Clicking a buy lesson button adds the lesson to the basket, uses JS to change the button to "Added" created a popover on the basket saying "Your lesson has been added to the basket" and adds +1 to the basket icon on the navbar.
    - Clicking the button "Added" uses JS to create a popover saying "You have already added this to your basket"
- **Dynamic**
    - The rating is an average of all the reviews the lesson has, if there are no reviews the lesson says Rating: None so the user knows it isn't an aweful 0 rated lesson.
    - Paid lessons that have been purchased have their price changed to a green "Purchased" to inform the user is one of their purchased lessons.
    - On mobile the lesson cards are vertically stacked with a small image
    - On larger screens the cards are layed out horizontally with a larger image
- **Modal**
    - The More Details link uses Ajax to POST a csrf token and lesson_id to a get_modal_data view, if valid the view will return json data
    - The json data contains a status key and a modal that is inserted into the page and activated with jQuery
    - This modal contains the lesson information with a longer description and all of its reviews
    - The modal is created by using render_to_string on a snippet called lesson_modal.html that is given the context 'lesson instance' and 'MEDIA_URL_for_json' as it will not be parsed the same as a rendered template.

### Studio page

This is the page where the actual lesson happens, it has the lesson name, the embedded video, a dropdown for description and reviews underneath.

- **Functionality**
    - Embeded video can be viewed on this page
    - Users who have no bought a paid lesson will be refused access to this page with an error message "You do not own this lesson"
    - A description button hides a collapsed description
    - If no current user review exists a 'Write review' buton exists which takes the user to a form to Write a lesson and give it a score out of technologies
    - If a current user review exists that review will be displayed at the top of the reviews with an edit and delete icon to perform those actions
    - If no reviews exist (discounting the current user) a prompt of "No more reviews exist" is displayed
    - If other reviews exist they will be displayed in date order (newest first)
    - Flag icon
        - Reviews that do not belong to the logged in user have a flag icon to report the review to an administrator
        - Administrators can see all flagged reviews on the superuser_admin.html (/home/superuser_admin view)page
        - If a user flags a review they will receive a success message "{{ User }}'s review has been flagged and will be reviewed by an administrator soon."
        - If a user tries to flag a review more than once they will receive the error message "You have already flagged {{ User }}'s review it will be reviewed by an administrator soon."

### Profile page

The profile page shows the user their profile, lets them edit it and request to become an instructor.  A list of purchased lessons and buttons to start them are also on this page.

- **Functionality**
- An 'Edit Profile' button takes the user to a form where they can edit their profile information and change their picture
- When pressed the 'Request Instructor Status' button :-
    - Will put a flag on the Userprofile that they want to be an instructor, this request can be seen by administrators on superuser_admin.html and change the button via JS to "Under Review: Press to cancel" and thier profile status to "Under review".
    - Pressing "Under Review: Press to cancel" removes the flag and cancels the request
    - If the user has not finished their user profile will be prompted by toat "Error, you must complete your profile first."
    - If the users request is granted the button is disabled changed color and displays "Instructor Status Granted" the profile status is changed to "Instructor"
- **Responsiveness**
- On small screens the instructor profile is vertically stacked with a small profile image and purchased lessons underneath
- Larger screens the instructor profile is layed out horizontally with a larger profile image and purchased lessons underneath

### Instructor created lesons page

This page gives a list of lessons the logged in instructor has created , they are prompted "You have not created any lessons yet" if they have made none.  'Create new lesson' button available under the list of lessons.
Each created lesson has its own card with the lesson image, title, rating, price, short description, edit and delete button.

- **Functionality**
- 'Edit' button takes instructor to a pre-filled form with the completed lesson data in it, this can be edited and submitted to update the lesson.
- 'Delete' button deletes the lesson from the database
    - After lesson is deleted, the a method is called in the instructors `UserProfile` to update the amount of lessons they have created
- 'Create new lesson' button takes the instructor to a form that will create a new lesson if submitted
    - After lesson is created the lesson finds out how many lessons were made by this instructor can passes it to the instructor profile method `_update_lesson_count()`
- Instructor cant make two lessons with the same name
- Instructor can make a lesson with the same name as another instructor to prevent 'name reserving'
- **Responsiveness**
- On small screens the instructor profile is vertically stacked with a small profile image and purchased lessons underneath
- Larger screens the instructor profile is layed out horizontally with a larger profile image and purchased lessons underneath

### Basket page

The basket page shows cards of items added to the basket with image, title, instructor, price and a delete button.
The Total, any discount and grand total are shown with a prompt of how much more they need to spend to avail of a discount if they have
not reached that amount yet.
Finally a checkout button at the bottom.

- **Functionality**
    - A button stlyed as a red trash can icon will remove the item from the basket
    - The checkout button will take the user to the checkout page ready for card payment
- **Responsiveness**
    - The table resizes its self to fit nicely on any size screen over 300px wide.

### Checkout page

The checkout page displays a the total that will be charged to the user and how many items they are buying, for example "Total: €8.99 \ For 2 items"
A form asks for a full name and email-address where a confirmation email will be sent and a card number.

- **Functionality**
    - Email address has to be valid format
    - Card details are checked on the fly and any error message from invalid input is displayed below
    - 'Complete order' button starts the process of placing the order through Stripe and unlocking the lesson for the user
    - See checkout testing in testing.md for information on webhooks used to validate order
    - 'Back to basket' button takes the user back to their basket
    - If an order fails to process the user is given the error message that the order failed and they were not charged
- **Responsiveness**
    - On larger screens the checkout window sits on top of a blured yoga studio image as there is little information on this screen and having it all white was too jarring.
    - On smaller screens the checkout window takes the full screen

### Checkout success page

The checkout success page tells the user their order was successful and gives them their order information of, name, email, order number, total, discount if applicable.
Also a list of all items ordered with buttons to start these lessons

- **Functionality**
    - Using django signals each lesson item that is purchased will automatically create a subscription for that lesson so the user can find it easily and begin right away
    - "Begin" button on each bought lesson item will start that purchased lesson
- **Responsiveness**
    - On larger screens the checkout window sits on top of a blured yoga studio image as there is little information on this screen and having it all white was too jarring.
    - On smaller screens the checkout window takes the full screen

Regarging signals, if for any reason an `OrderLineItem` (the database entry that shows a lesson has been purchased by a user) is or has to be deleted, a signal (pre_delete) is used to delete the subscriptions that user may have for the lesson.

#### Database
 
 - The database is postgres, below is the initial map when creating the app

![Database](https://github.com/KelvinHere/Yoga_Milestone_4/blob/master/design/database/db_design.jpg "Database design")

- The final database with new features at the end of development



 
#### Performance

- Rating system
    - Situation: I wanted a rating system for Instructors and Lessons that would show the average score of each instructor by lessons and each lesson by their reviews, but at scale for example 1000 lessons each had 100 reviews, everytime a user would request a list of all lessons there would be 1000 x 100 = 100,000 objects in the queryset returned to get all the review ratings.
    - Task: To reduce the number of objects in the queryset needed to return the information requested by the user.
    - Action: After a review is created and saved it will call its lesson to run a method to update its average score.  This is only done when a review is created, once the lesson rating is updated it will call the Instructor that created it to run a method that updates their score from all their (precalculated) lesson ratings.
    - Result: Now when a lesson list is called the average scores have been pre-calculated and in this example only 100 objects in the queryset are returned as opposed to 100,000

### Changes during development
As this was a learning project some changes were made in development for me to get the most out of it.  Most notibly I changed 
the "book video time" feature with a "paid lesson" feature.  This allowed me to make a more comprehensive "store", 
with adding / removing from a basket, and creating a system where once a lesson is paid for they are unlocked for users.
This allowed me to create a better showcase for my portfolio using many more features of Django.

### Future Features

##### Near Future
- Use a private video hosting service to give the site more control and better security for paid lessons.

##### Far Future
- Create live-streaming paid lessons, where an instructor can sell positions to join realtime lessons with direct tutor feedback.

## Testing
 
[Testing Documentation](#) - Documentation for testing

## Dependancies
- `pip3 install pillow` image field
- `pip install django_resized` resize image field

## Technologies Used
 
- **HTML5/CSS3**
- [Django](https://www.djangoproject.com/) - Framework
- [Postgresql](https://www.postgresql.org/) - Database
- [SQLite](https://www.sqlite.org/index.html) - Django default database
- [Python](https://www.python.org/) Programming language
- [Javascript](https://www.javascript.com/) Programming language
- [jQuery](https://jquery.com/) - JavaScript Library
- [Heroku](https://www.heroku.com/) - Cloud Application Platform
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server
- [Gitpod](https://www.gitpod.com) - Development environment
- [Git](https://git-scm.com/) - Version control
- [Github](https://www.github.com) - Code hosting platform
- [Draw.io](https://www.draw.io/) -Prototyping wireframing tool
- [Photoshop CS](https://www.adobe.com/) - Image editing software
 
## Deployment
 
This project was created in [GitPod](https://gitpod.io/) with the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) and version controlled through 'Git', the project was committed and pushed to [GitHub](https://github.com/).
The project was then deployed to [Heroku](https://www.heroku.com/) with media and static files hosted on [Amazon s3](https://aws.amazon.com/).
 
### Version Control
* After files are created or modified they are committed to a GitHub repository using git by :-
    - adding the modified files locally using `git add .` or `git add filename.extension`
    - commiting the modified files with a message of changes using `git commit -m "changes here"`
    - pushing the new commit to the master branch on GitHub repository with `git push`
    - updating an out of date local branch with `git fetch origin` and pulling changes with `git pull origin`
 
* Branches & an example
    - When adding the pagination feature I created a new `branch` on github, this allowed me to experiment with pagination without breaking my master branch and having to do a hard reset back to a working commit
    - Once the feature was working in the `Add pagination branch` I created a `pull request` to `merge` this new branch back into the `master`, since the master branch was a couple of `commits` ahead at this point I had to confirm there were no `conflicts` and I was happy to go ahead with this operation
    - With the merge complete the master branch now contains the pagination feature and the commits in the master branch that were ahead of my `Add pagination branch` at the time 

### Local Deployment
  
### Heroku Deployment
 
The deployed version of 'Social Yoga' is hosted on Heroku and was deployed with the following steps.
 
* Requirements
    - A locally deployed version of the Book Review App from the instructions above
    - A Heroku account
    - A postgresql addon from Heroku > Resources
    - [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed locally, instructions in [this link](https://devcenter.heroku.com/articles/heroku-cli)
 
1. Login to your Heroku account
2. Click New > App
3. Give the app a name, select a region and create the app

4. Setup the database
    4. The local app need 'dj_database_url' and 'psycopg2-binary' installing
    4. free requirements


4. Setup enviromental variables in Heroku :-
    - Select your app in Heroku and click settings
    - Under Config Vars set up the key value pairs as below
    - IP = 0.0.0.0
    - PORT = 5000
    - 
5. Login to Heroku from your terminal with `heroku login -i` then follow prompts
6. `pip freeze --local > requirements.txt` to update your requirements.txt in case of new requirements
7. `git init` if you have not initialised your git repo
8. `heroku git:remote -a YOUR_APP_NAME` to add remote
9. `git add .` and `git commit` your changes
10. `git push heroku master` to deploy to Heroku
11. From the Heroku website
    - You many need to click 'More' in the Heroku app and select 'Restart all dynos'
    - Click 'Open App' 
    - The App should now be running through Heroku
 
### Deployment with Gunicorn
 
As specified in the [Flask deployment](https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment) documentation, Flasks built in server is not suitable for production as it does not scale well.
I decided to deploy to Heroku with Gunicorn as the server, deployment instructions on the Heroku website in [this link](https://devcenter.heroku.com/articles/python-gunicorn).
 
A quick summary of instructions with basic configuration below.
 
1. Locally install gunicorn with `pip install gunicorn`
2. `pip freeze --local > requirements.txt` to update your requirements.txt to include gunicorn
3. Create a point of entry for gunicorn, I created a file called [wsgi.py](https://github.com/KelvinHere/book-review-app/blob/master/wsgi.py) click to see its contents
4. Update the procfile to `web: gunicorn wsgi:app` so Heroku will launch the app through gunicorn
5. Log into heroku CLI and run `heroku config:set WEB_CONCURRENCY=3` to add an environmental variable into the app on heroku to take advantage of concurrency and make the app more responsive at scale
6. Commit your changes as before
7. Push to heroku with `git push heroku master`
8. The app should now be on heroku running on gunicorn
 
## Credits

- [Colour scheme inspired by icolorpalette](https://icolorpalette.com/palette-by-themes/yoga)

### Content
 
- This project was created by KelvinHere
 
### Media

* [Background image](https://www.istockphoto.com/photo/young-woman-practicing-yoga-in-the-nature-female-happiness-pose-balance-body-vital-gm1221748282-358248235?clarity=false)
* [simple_stretching.jpg and stretching descriptions](https://www.realsimple.com/health/fitness-exercise/stretching-yoga/stretching-exercises)
* [Instructor profile pictures from free images, contributor below](https://www.freeimages.com/)
    - [Instructor 1 - By Matteo Canessa](https://www.freeimages.com/photo/yoga-relax-1556603)
    - [Instructor 2 - By Aaron Neifer](https://www.freeimages.com/photo/yoga-1240391)
    - [Instructor 3 - By Lorant Fulop ](https://www.freeimages.com/photo/yoga-1433499)
    - [Instructor 4 - By Bimbo Cabochan](https://www.freeimages.com/photo/beach-yoga-1186865)
    - [Instructor 5 - By Martin Louis](https://www.freeimages.com/photo/yoga-1482810)
* [Drawn lesson poses](https://www.tummee.com/)
* [Lesson image poses 'self'](https://www.self.com/gallery/must-know-yoga-poses-for-beginners)
* [Yoga studio image on account and checkout pages](https://classpass.com/classes/space-yoga-studio-brighton?page=37)


### Acknowledgements
 
* [Geeks for Geeks - Ajax information](https://www.geeksforgeeks.org/handling-ajax-request-in-django/)
* [Django Documentation](https://docs.djangoproject.com/en/3.1/).
* [Code Institute](https://codeinstitute.net/).
* My mentor Spencer.
