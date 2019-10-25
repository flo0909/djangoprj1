# Django Project 
## Issue Tracker.  

1. Django Project - uses a relational database and users can store and manipulate data records  
2. The project has 5 apps that are reusable  
3. The project contains 8 models  
4. The project contains an accounts app that does the user authentication  
5. The user can interact with models, can update the post or ticket , can update her or his profile informations  
6. The cart app is using Stripe for e-commerce functionality. After purchasing the user gains functionality in form of discounts and a  VIP status.The payment system uses Stripe's test functionality.  
7. The project has a main navigation menu , is using Bootstrap4 for structuring content.Also on Index page has additional options to navigate to the desired section of project.  
8. The project is using JavaScript to add functionality and enhance user experience  
9. The project has a Readme File included in Git Hub repository  
10. The project can be found in a Git Hub repository for version control  
11. The codes that I have taken from external sources are credited in the files comments  
12. The project is deployed on Heroku - please find link below.  
13. The passwords are not included in the deployed code of the project or in the repository.The Debug mode is False.  



***The Project***

I have taken inspiration from the 'Issue Tracker' idea provided.  
The project is using Django 2.2.5. , Python 3.7.3, PostgreSQL provided by Heroku , Html5 , CSS3 , JavaScript, DC , D3 , Stripe, Bootstrap4, Crispy Forms, the rest please find in requirements.txt.  
The user images are uploaded into an AWS bucket.  

***The UX***

The user can see first the landing page that explains the purpose of the project and offers the options  
to navigate further.The user has two main options - the free features where he/she can post for a request to fix a 'bug'  
or the paid request for a feature development. For accessing both, the user needs to create an account and to use an email  
address and a password.The creating account form uses validation to make sure the informations are correct.    
After creating an account, the user can use a form to post a request to fix a problem discovered in the main application  
, or can use a form to post a feature request in the feature requests section. While posting is free and the site admin is promising to dedicate a part of time to develop the feature, to be able to speed up the feature development, the users can buy it and have it done as soon as possible. Also the users can vote for both sections, for posts and feature requests, voting is free for both sections. The user is able to update the informations from their own posts/feature requests. The users can get an answer at their post/request from the site admin. 
At the feature requests section the user is able to access a ticket stats page that compares the chosen feature with another two sample tickets that are currently in use. The ticket without any progress will not be able to display any stats and the user will be redirected to the feature list page.   
After deciding if they want to support a specific feature they can contribute to the development by adding to cart.The user is able to modify the amount of support that they want to contribute with , by increasing the cart quantity of the same product or choosing different features if they decide to do so.  
The user can use the stripe form to complete the payment and are redirected to an order complete page where they can continue contribute to the desired feature especially because after completing the first purchase the user gets a VIP status that grants a fixed discount to all future feature requests.  
The app is responsive , tested on main mobile device sizes and desktops and is using a "mobile-first" design.




**Project Deployed** - https://djangoprj1.herokuapp.com.  
**Wireframes credits** - I have used Gimp to create the wireframes for the project  
**Default Icon credits** - I have used Gimp to create the default User Icon  
**Font credits** - I have used few font awesome fonts  
**Background credits** - Photo by Brandi Redd on Unsplash.   
**Cards Background credits** - Photo by Ferdinand Stöhr on Unsplash.  
**User Face-1 credits** - Photo by x ) on Unsplash.  
**User Face-2 credits** - Photo by Sergio de Paula on Unsplash.  
**User Face-3 credits** - Photo by Foto Sushi on Unsplash.  
**User Face-4 credits** - Photo by Reza Biazar on Unsplash.  
**User Face-5 credits** - Photo by Radu Florin on Unsplash.  
**User Face-6 credits** - Photo by Aleksandr Minakov on Unsplash.  



