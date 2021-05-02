
Python packages
1. Allauth


- Fonts
  - Montserrat
  - Material Icons


- PROFILE
  - Amend allauth template to get First and Last Name
    https://dev.to/gajesh/the-complete-django-allauth-guide-la3


Display Tuple in choices
https://stackoverflow.com/questions/54020156/display-value-of-choicefield-of-the-tuple-in-template-django

Thousands separator
https://docs.djangoproject.com/en/3.1/topics/i18n/formatting/


UPLOADING
https://b0uh.github.io/django-multiple-forms-in-one-class-based-view.html
http://www.joshuakehn.com/2013/7/18/multiple-django-forms-in-one-form.html
https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field
https://medium.com/@bhagyalakshmi18/uploading-multiple-files-in-django-b2f5ede55d09


![Responsive website images](/README/banner.jpeg "Responsive website images")

# **MILESTONE PROJECT FOUR**

For Milestone Project Four, which requires the development of a full stack site utilising Django dataset, users can subscribe a project to a cost report and management tool, Cost Report, to track the cost of changes occuring on a construction project.  Subscribing on a project-by-project basis, once a project is subscribed, the cost changes can be monitored.  Additional users can also be invited to be project users, and their privileges can be set to view only or edit permission.

The website can be viewed [here](https://ms4-cost-report.herokuapp.com/)

## **UX**

### **Who is the Website for?**

The website is for Developers, Cost Consultants and Project Managers of buidling projects.  They can subscribe to a service which will allow them to monitor and manage construction costs in a live, always up-to-date and transparent way.

Milestone Project 4 (MS4) shares similar purposes to Milstone Project 3 (MS3):-

***1. View the current cost position***<br>
*The website shall enable the developer, and other persons involved and with access, the ability to view the live, current cost position of the development.*

*Whilst the developer will probably be most interested in the Total Cost, other users may be more interested in the list of changes - and their individual cost impact.*

***2. Implement Consistent, Best Practice Cost Control***<br>
*The website shall enable the Cost Managers - those responsible for managing and reporting the current cost position of the development - to report costs immediately as they arise on a project.*

*The website will provide a consistent approach in the reporting of costs and changes, from project to project.  This will support familiarity and understanding for users.*

MS3 was designed to be implemented by users for their own use, it was not designed to be a service offering for the public.  The website would be hosted and managed for the developer's own use.

The purpose of MS4 is to offer these services and benefits to anyone through a subscription service.  Projects are private and only visible to Project Users that the Project Owner nominates.

<br>

### **User Stories**

On any property development, there will be methods for tracking and reporting costs.  A cost manager will normally implement a simple cost tracker utilising an Excel spreadsheet to list the changes and report this back to the Developer/Client.

I currently work for a developer and we require our cost managers to implement these procedures. The cost managers utilise the Excel cost tracker which can be viewed [here](/READMEinfo/CostTracker.xlsx)

My aspiration is to incorporate the principles of this template into a more robust data management system which can be used for different construction projects by different developers / clients.

As such, the fundamentals and principles are crystalised in the User Stories below, which will be translated into the final website.

*As a developer, I want to implement best practice cost control on my construction projects.*

 **Item** | **Experience** | **Objectives**
---------|----------------|---------------
&nbsp; | ***Viewing & Navigation*** | &nbsp;
1 | View list of projects that I can access | View and edit the project cost tracker
2 | View list of changes | Track the costs affecting a project
3 | View a cost summary | See the initil and forecast cost of a project
&nbsp; | ***Registration and User Accounts*** | &nbsp;
4 | Easily resiter for an account | Have a personal account and view my profile
5 | Receive an email confirmation when registering | Verify that my account resitration was successful
6 | Have a personalised user profile | View my projects/subscriptions, projects I can access, payment history and save my payment information
7 | Invite users | So that I can include users to participate on my project
&nbsp; | *Sorting and Searching* | &nbsp;
8 | Search for a specific change by name or descriptions | So that I can quickly filter changes
&nbsp; | ***Cost Tracker Items*** | &nbsp;
9 | Add a new change item | Track the latest cost position of the project
10 | Edit a change item | Update costs if they change on my project
11 | Upload associated change information (drawings, cost information, etc)
&nbsp; | ***Subscribing*** | &nbsp;
12 | Create a new project by subscribing for the monthly project | Start to monitor the costs of a construction project
13 | Enter payment details for recurring payments | Checvk out quickly with no hassles
14 | Switch off recurring payments | Stop subscribing
15 | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase
16 | View an order confirmation after checkout | Verify that I haven't made any mistakes
17 | Receive confirmation after each payment | Be notified of payments from my account
18 | View a history of payments | Verify all past payments
&nbsp; | ***Admin and Project Management*** | &nbsp;
19 | Delete a project | Permanently remove the data from the database
20 | Add/Remove users to my project | Control access to my project

<br>


### **Functions of the Website**

The functions of the website are to:-

1. Provide a visual summary of the current cost position of the development project.  This is represented in a Dashboard.
    ![Dashboard](/READMEinfo/function_dashboard.jpg "Dashboard")

2.  View a list of all the changes impacting on the cost of a construction project.  This is represented on the Register.
    ![Register](/READMEinfo/function_register.jpg "Register")

3. Ability to Add (create) / View (read) / Edit (update) / Delete changes which affect a construction project.
    ![Change](/READMEinfo/function_change.jpg "Change")

<br>

___
<br>

## **Design**

### **Responive UX Design**

![Responsive Pages](READMEinfo/responsive_screens.jpg "Responsive Pages")

The website has been designed for use across multiple screen sizes, adapting content display to optimise the information to be displayed.  The information shown on-screen is reduced to accommodate smaller display sizes.  The changes are noted below:-

- Large (desktop) screens - full information displayed on-screen, including filter options.
- Medium (tablet) screens - filter sidenav becomes a slideout field, operated by floating button.  The user can still access all information.
- Small (phone) screens - A final step is the reduction of information displayed on-screen.  Only key information is shown on small screens.  This is achieved by reducing the number of columns in the tables shown on the Dashboard and Register.

<br>


### **Key concepts**
The primary purpose of website is to show the current cost of a construction project and a list of the changes that have affected the cost since the establishment of the budget.

The intention of the site is to give this information in a clear, concise manner.  By giving users control of certain filters, it is envisaged that this will assist users understanding of the numbers being presented without the need for explanation.  The filters should give users a better insight on the information and numbers being presented, and in turn control of the project by being able to make more informed decisions.

Whilst the website has reached a point of deployment for presentation, feedback and testing with users, the page requires further development before being deployed in a live situation.

<br>

### **Wireframe**

Figma was used to develop a key concept into framework for developing the web page / app.  Only a desktop framework was formulated at this stage.

A copy of the original wireframe can be found here: [Figma](https://www.figma.com/file/NCiIRZCyfNSYk62uRwCqu3/MS3?node-id=0%3A1) or [PDF](READMEinfo/Figma.pdf)

<br>

### Typography

The [Montserrat](https://fonts.google.com/specimen/Montserrat) font (from Google Fonts) is the only font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly.

<br>

___

## Features

### Interactive Elements

The web page is interactive in the following ways:-

* Filter - on the Dashboard and Register, the Filter acts to filter and change the data presented on screen.
  1. Cost - option to switch between 'Nett' and 'Gross' total figures
  2. Status - selection of Status will update totals or filter the register for only those selected
  3. Change Type - selection of Change Type will update totals or filter the register for only those selected
  4. Period - selecting will update the totals to only include the changes within the period selected.

* Add / Edit Changes - users can add or edit changes, affecting the database accordingly.

* Auto-update input information on the Add / Edit pages:-
  1. Numbers auto-format with thousand separators when fields entered/updated;
  2. Gross total auto-calculates to ensure that it is the sum of the preceding numbers.


### Existing Features

An overview of the features on the website are listed below:

* **Dashboard**: The Dasboard provides a summary of the Cost Position of the project, providing users with a view of the Budget, accepted (Approved) and potential changes (Pending, WiP) and the Revised Estimate.  

  Users can use the Filter to switch between Nett or Gross costs, or include / exclude changes depending on the Status or Change Type.  By enabling users to carry out this function themselves, they will have a deeper understanding of the cost.

  ![Dashboard](/READMEinfo/existingF_dashboard.jpg "Add Change")

* **Register**: The Register is a complete list of all Changes stored in the DB.  Like the Dashboard, the Filter will hide from view changes which are not selected.

  By clicking on a row, the Change will open to View/Edit.

  ![Register](/READMEinfo/existingF_register.jpg "Register")

* **Add Change**: Users can add a change by clicking on the '+' button on the Register page, which will bring them to this input page.

  The Change Nr auto-populates based on incrementing the Nr of records in the DB collection.  The field is still editable in order that users can customise, as it is sometimes necessary to coordinate these values with other consultants working on projects.

  The Gross Cost also auto-calculates, and is the sum of the Nett Cost, Contingencies and Main Contractor On-Costs.  This ensures that there is no manual error in the calculation.

  ![Add Change](/READMEinfo/existingF_addChange.jpg "Add Change")

* **View / Edit Change**: Users can View/Edit a change by clicking on the row on the Register, which will bring them to this page.

  On load, the input fields are Read Only, but on clicking the 'Edit' button, the editable fields will become active.

  A delete button is also included on this page.  Deletion is permanent and therefore a warning pop-up is utilised to confirm the action before committing.

  ![Edit Change](/READMEinfo/existingF_editChange.jpg "Edit Change")

* **Budget**: This page allows users to amend the Approved Budget.

  ![Budget](/READMEinfo/existingF_budget.jpg "Budget")

* **Registration**: This page allows users to Register for access to the web page.

  ![Registration](/READMEinfo/existingF_registration.jpg "Registration")

* **Log In**

  ![Log In](/READMEinfo/existingF_login.jpg "Log In")

* **Log Out**: Removes all session cookies and ensures that pages / APIs cannot be accessed when not logged in.

  ![Log Out](/READMEinfo/existingF_logout.jpg "Log Out")


### Database

In order to implement CRUD (Create, Read, Update, Delete) functionality on the website, MongoDB - a NoSQL database - is used. A number of collections were created to support the operation of the website.  A record/extract from each collection has been inlcuded below for reference:-

* Register - this is the primary collection of the database, implementing full CRUD functionality which enables users to manage and track the cost of changes occurring on a project.  
![Register](/READMEinfo/DB_change.jpg "Users")  
Create [Y]  Read [Y]  Update [Y]  Delete [Y]  
Users are able create records on the 'Add' page.  
The read functionality is implemented in a variety of different ways across the website, whether it is through the Dashboard and the computation of values of the records to display a summary, the full list of records of the collection on the Register, or viewing the details of the record on the View page.
Records can be edited or deleted from the View page.

* Users - this collection is used to allow users to Login and new records are created when a user registers.
![users](/READMEinfo/DB_users.jpg "Users")  
Create [Y]  Read [Y]  Update [N]  Delete [N]
Update and Delete functionality could be implemented in future updates of the website.

* Status and Change Type - these collections are fixed and not intended to be changeable by Users.  They provide the options in Input Fields to Add / Edit a change.  
![Status](/READMEinfo/DB_status.jpg "Status")
![Change Type](/READMEinfo/DB_changetype.jpg "Change Type")  
Create [N]  Read [Y]  Update [N]  Delete [N]
It is not intended to permit users to add, change or delete these options in order that they are permanent and consistent.  They are associated with wider functionality of the website, including the Filters, and allowing further CRUD functionality would disrupt them (without further wider development of the website).

* Budget - this collection is currently only intended to host 1 record.  
![Budget](/READMEinfo/DB_budget.jpg "Budget")
Create [N]  Read [Y]  Update [Y]  Delete [N]
The record is required from the outset, even if the budget has not been established and the values are '0'/zero, so there is no requirement for Create functionality.  Likewise, the record cannot nor should be deleted.


### Features to Implement in the Future

The functions implemented on this website are for demonstration purposes only at this stage, there is further development required before the website can be deployed for a live development.  Those features required before live deployment include:-

* **Currency:** Ability to change the default currency displayed for the project.
* **Multiple Projects:** Currently the website assumes that there is only one project.  Extend the functionality of the application to enable the cost tracking of multiple projects.
* **Filter memory:** When a page reloads, the Filter currently returns to the default selection. Future development would consider maintaining selected filter options on page re-loads with a 'Reset' option to return to the default selection.
* **Authorisation of Registration:** After a user has registered, access will not be granted until an Administrator approves access and sets privileges.
*  **Update of User Profile:** Currently the User Profile is limited to Read Only.  This will be updated to enable the update of user details and also to delete if access is no longer required.
* **Access privileges:** Users will be granted different rights and viewer privileges dependent upon their role on the project. For example, a cost manager will be able to add and edit changes, whereas other users will only be able to view them.  An Adminstrator role will also be introduced for controlling these access privileges.
* **Graphical Representation:** To enhance and make the user experience more engaging, the Dashboard can benefit from graphs or other figurative representations of the data in a more visually absorbing way.
* **Upload Supporting Information:** Whilst the DB stores the high level costs associated with the change, being able to upload supporting information (breakdown of costs, design information) to provide full details of the change would be beneficial to users.

<br>

## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### Frameworks, Libraries and Programmes Used 

* [MongoDB](https://mongodb.com/)
MongoDB provides the backend database for storing the information submitted from, and viewed on, the website.

* [MaterializeCSS](https://materializecss.com/)  
Materialize is generally used to assist with the layout, utilising the in-built grid system, and design functionality.

* [Google fonts](https://fonts.google.com/)  
Google fonts is used to import the 'Montserrat' font into the style.css file which is used throughout the project.

* [jQuery, incl UI](https://jquery.com/)  
jQuery is used for Javascript DOM manipulation.

* [Git](https://git-scm.com/)  
Git was used for version control by utilizing the terminal in VSCode terminal to commit and push changes to GitHub.  
In addition, in order to track the purpose of commits, the following pre-fixes have been adopted, which are taken from the Commit Message Guidelines outlined by [Angular Framework](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines):-
  * feat: new feature has been added to the code
  * fix: bug fixed during on-going testing
  * refactor: 'tidy up' of code
  * docs: addition of comments to code or writing of README file

* [GitHub](https://github.com/)  
GitHub is used to store the projects code after being pushed from Git.

* [Heroku](https://www.heroku.com/)  
Heroku is used for deployment of the website / application.

* [Figma](https://www.figma.com/)  
Figma was used to create the wireframes during the design process.

* [Screen Recorder](https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden)  
Screen Recorder used for creating videos (edited in Kapwing) of website features in operation.


## Testing

### User Story Feedback and Testing

**1** | **Clearly see the current cost position of the project**
---------|----------------
**2** | **Determine the cost movement from start (budget) to current / forecast position**
(a) | Users can view the current cost position of the project on the Dashboard, including the Approved Budget and the Revised Estimate
(b) | Users can see the build-up to the Revised Estimate, so they know what changes are included in it
(c) | By switching the Nett and Gross Cost filter, users can be sure they know the basis of the cost.
(d) | ![Cost Position](/READMEinfo/US_1CurrentCostPosition.gif "Cost Position")
________________

<br>

**3** | **View a full list of the changes impacting the development**
---------|----------------
**4** | **Determine what changes in the latest period (30 days) have added to the revised total estimate**
(a) | The Register has a list of all changes being recorded on the project
(b) | As users will be particularly interested in 'new' or 'updated' changes, the Register can be filtered accordingly to show only those 'new' or 'updated' changes within the last 30 days.
(c) |![Full list](/READMEinfo/US_3+4Register+Period.gif "Full list")
_____________

<br>

**5** | **Depending on the purpose of my visit to the site, view only Accepted / Pending / WiP changes**
---------|----------------
**6** | **View changes / cost impacts by the type of change to understand their impact on the development**
(a) | On the Dashboard, the Filter can be used to show only those costs which are Selected.  This may be useful where, for example, a Client only wishes to know their *committed* costs, I the budget and those changes which are approved.  As such, Pending and WiP changes would not be included in the Revised Estimate and would be unchecked.
(b) | ![Dashboard Filter](/READMEinfo/US_5Filter.gif "Dashboard Filter")
(c) | Similarly on the Register, the Filter can be used in a similar way.  For example, a Client may wish to review only thos Pending changes for authorisation / acceptance.
(d) | ![Register Filter](/READMEinfo/US_5Filter_Register.gif  "Register Filter")
_____________

<br>

**6** | **Add new changes to the Cost Tracker with a breakdown of the cost**
---------|----------------
(a) | New changes may be added to the DB with a breakdown of the Cost.
(b) | ![Add change](READMEinfo/US_6AddChange.gif "Add change")
_____________

<br>

**7** | **Edit changes as details are updated or when the Status of a change is made**
---------|----------------
(a) | Changes listed on the Register can be made by clicking on the row to View / Edit the item
(b) | ![Edit Change](READMEinfo/US_7EditChange.gif "Edit Change") 
____________

<br>

### Validators

The W3C Markup Validator and W3C CSS Validator Services were used to validate the main pages of the project to ensure there were no syntax errors in the project.

**[W3C Markup Validator](https://validator.w3.org/)**

In order to check the HTML, the code was copied by 'Text Input' on the validator, as the code is not passed and checked by the 'Address' method.  There are no outstanding errors - screen captures of the results are shown on the links below.

**Results**
  - Dashboard
  ![Dashboard](READMEinfo/W3CValidator-Dashboard.jpg "Dashboard")
  - Register
  ![Regsiter](READMEinfo/W3CValidator-Register.jpg "Register")
  - Add Change
  ![Add Change](READMEinfo/W3CValidator-AddChange.jpg "Add Change")
  - Edit Change
  ![Edit Change](READMEinfo/W3CValidator-Dashboard.jpg "Edit Change")


<br>

**[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)** - [Results]("https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fms3dkeddie.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en")

There are no errors highlighted by the CSS validator.
<br>
<br>

### Javascript Code Quality - JSHint

[JSHint](https://jshint.com/) has been used to check and test the Code Quality of the Javascript used on this page.  The Javascript has been updated in line with warnings initially returned.  The following items remain and which are deemed not critical to the functioning of the site:-

![Warning 1](/READMEinfo/JSHint-1.jpg)
*Whilst not addressed, this warning could be refactored in future to address the concerns raised.*

<br>

![Warning 2](READMEinfo/JSHint-2-1.jpg)  
*These warnings are incorrect and the statements are not missing semi-colons*
![Extract from script.js](READMEinfo/JSHint-2-2.jpg)  



<br>

### Python compliance with PEP8

[PEP8 online](http://pep8online.com/) has been used to check compliance of the app.py file used in this application with PEP8 requirements.  The file was updated in line with non-compliance results that were initally returned.

There are no non-compliance remaining in the app.py file.

### Manual Testing of the Site

The following tests were carried out to ensure functionality before deployment:-

**Test**: Changes can be added and filtered for each Status and Change Type
* Steps followed:
  * Add a change which correlates to each Status/Change Type option (ie 4 x 6 = 24 changes)
  * Rotate through each status and change type to add a change
  * Check Dashboard and Register functions for each Status and Change Type on the Filter
* Results:  Dashboard and Register load as anticipated, with Status and Change Type filter operating to include / exclude applicable changes in the Totals on the Dashboard and list of changes on the Register.

**Test**: Test the Period Filter
* Steps followed:-
  1. Manually amend two Changes in the MongoDB collection, one for the 'date_added' field and the other for the 'date_changed' field.  The dates should be one year earlier than the current date, ie more than 30 days ago.
  2. Check the dates have been updated on the website / Register by selecting each item in turn and clicking the item to View.
  3. Return to the Register and select the Period filters to check that the Filter operates as intended
* Results:-
  * The period filter operated as expected, but removing the Changes with dates outwith the 30 day period.

**Test**: Test empty values in fields on the Add Change page
* Steps followed:-
  1. Entered no values into fields (ie did not enter the field) and submitted form
  2. Check Register loads
  3. Click on Change to View/Edit and confirm item loads
* Results:-
  * Register and View/Edit Change pages do not load.
  * On checking the DB, any fields not inputted with a value become 'null'.
  * Consequently, Jinja2 is not able to input valid text within the field.
* Fix:-
  * JS function included to populate any empty fields with '0' before the form is submitted.  This is implemented when the Submit button is clicked.
  * The Add change function now operates so that no values need to be inputted in order to function, the default value of these fields will now be '0'/zero.

**Test**: To test the thousand separator included in value fields, different values inputted to test the Add Change page
* Steps followed:-
  1. Entered values of 
      - '100000' (one hundred thousand), 
      - '1000000' (one million), and 
      - '100000000' (one hundred million)  

      to test how the form handles the values on (a) calculation of Gross Total and (b) submission of values to the DB
  2. Check that Gross Total is calculating properly
  2. Check Register loads
  3. Click on Change to View/Edit and confirm item loads
* Results:-
  * Value of 100,000 operates as expected.
  * Values of 1,000,000 and 100,000,000 do not calculate the Gross Total correctly.  The function to omit the only omits the first ',' from the values, preventing the calculation.
  * The Register and View/Edit pages do load, but are not the correct/anticipated values.
* Fix:-
  * JS function which removes the ',' from the number strings updated to omit all ','.
  * This now allows numbers of 999,999 to function on the website as anticipated.

During the on-going testing and development of the site, bugs were discovered and resolved.  These can be reviewed in the list of Git commits, specifically those with the 'fix' prefix.

For a list of the Git Commit history, this can be viewed [here](https://github.com/dkeddie/MS2/commits/master)


### Further Testing

During the development of the website, and again as a final, comprehensive and in-depth review, the following testing was carried out:-

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices: Desktop, Laptop, iPad.
* Buttons were checked to ensure when hovered or active that they are responsive and operate uniformly.


### Known Bugs

There are no known bugs.


## Deployment

### For Development Purposes

The website has been deployed on Heroku and is currently publicly accessible.

The development of the website has been undertaken on VSCode.

The steps from start to present were:-

**Connection to GitHub repository**

  1. Creation of repository on GitHub, utilising Code Institute template.

  2. Clone of GitHub repository to local machine but utilising GitBash to implement the command:-
  `git clone https://github.com/dkeddie/MS3.git`

**Deployment to Heroku**

  3. Creation of a new App on Heroku
  4. Go to 'Deployment Method' -> Select 'GitHub' and search for the repository that you want to deploy via Heroku from GitHub.
  ![Deployment](/READMEinfo/deploy_Heroku.jpg "Deployment")
  5. Go to 'Settings' and 'Reveal Config Vars' -> Input the settings required to deploy the website and connect to the Mongo Database as shown below ()
  ![Settings](/READMEinfo/deploy_Heroku2.jpg "Settings")
  ![Config Vars](/READMEinfo/deploy_Heroku3.jpg "Config Vars")
  6. Go to 'Deploy' and select to Enable Automatic Deploys
  ![Auto Deploy](/READMEinfo/deploy_Heroku4.jpg "Auto Deploy")

The website is now deployed and can be viewed at:
    [https://ms3dkeddie.herokuapp.com/](https://ms3dkeddie.herokuapp.com/)  
<br>

### Cloning of the Repository

Should you wish to deploy your own version of the website, the following steps may be followed to host your own version on GitHub:-

1. Visit my GitHub Repository: [MS3](https://github.com/dkeddie/MS3)

2. Click dropdown 'Code' and copy url to 'Clone with HTTPS'  
![Clone](READMEinfo/clone.png)

3. Select 'Import Repository' from the Menu dropdown, paste the url, give your new repository a name and click 'Begin Import'
![Clone instructions](READMEinfo/clone2.png)

4. Go to your new Repository.  You may chose to launch the repository in an IDE of your chosing in order to make changes to the website, and customise it to your requirements.

5. To deploy the website, follow step 3 of the **Deployment** section immediately above.


## Credits

### Content

All content and code was written by the developer, except where taken from libraries or documented within this file or the Code files.

### Code

* Snackbars - flash messages which hover over the page are adapted and inspired from [W3Schools](https://www.w3schools.com/howto/howto_js_snackbar.asp)
* Clickable table rows - code to make the row clickable to View/Edit the item was taken from [electrictoolbox](https://electrictoolbox.com/jquey-make-entire-table-row-clickable/)

### Acknowledgements

Thank you to my mentor for feedback and advice given throughout the project.