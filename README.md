# **Revforum**

## **Overview**

Revforum is an online forum made with Django framework. It allows people with their shared love for motorcycle to exchange options and experiences. On categories created by the admin, the users can create their own posts and comment on posts made by themselves or others. They can also like, favourite and report posts. When the post is reported, it is flagged for the admin to analyse.

![Main screen screenshot]()

## Table of contents

- [**Revforum**](#revforum)
  - [**Overview**](#overview)
  - [Table of contents](#table-of-contents)
  - [**Planning stage**](#planning-stage)
    - [**Target Audiences:**](#target-audiences)
    - [**User Stories:**](#user-stories)
    - [**Site Aims:**](#site-aims)
    - [**Forum Structure:**](#forum-structure)
  - [**Current Features**](#current-features)
      - [*Main Screen:*](#main-screen)
      - [*Post List screen:*](#post-list-screen)
      - [*Post screen:*](#post-screen)
      - [*Game:*](#game)
      - [*Congratulations and Game Over:*](#congratulations-and-game-over)
  - [**Future-Enhancements**](#future-enhancements)
  - [**Testing Phase**](#testing-phase)
  - [**Validators**](#validators)
  - [**Bugs**](#bugs)
  - [**Deployment**](#deployment)
  - [**Tech**](#tech)
  - [**Credits**](#credits)
    - [**Honorable mentions**](#honorable-mentions)
    - [**Content:**](#content)

## **Planning stage**

### **Target Audiences:**

* Users interested in motorcycles.
* Users interested in interact with other people with shared loved for motorcycles.
* Users interested in share their experiences.
​

### **User Stories:**

* As a user, I want to make a post.
* As a user, I want to comment a post.
* As a user, I want to update a post.
* As a user, I want to delete a post.
* As a user, I want to like a post.
* As a user, I want to report a post.
* As a user, I want to update a comment.
* As a user, I want to delete a comment.
* As an administrator, I want to create a category.
* As an administrator, I want to review a flagged post.
​

### **Site Aims:**

* To create a space for conversation regarding motorcycles.
* To present itself as another option for users to get and share information.
* To incentivate discussions.
* To facilitate the spread of information, specially regarding events or similar.
* To provide an excellent user experience without any errors or bugs.

### **Forum Structure:**

![Forum Structure]()

## **Current Features**

​

#### *Main Screen:*

* Main screen of the forum. User or visitors (they do not have to be logged) can see the categories.

![Main screen screenshot]()

#### *Post List screen:*

* Once the user/visitor clicks in one category, they are then redirected to all the posts inside that category. If the user is logged, the page shows the favourite posts first, from the newest to the last one.

![Post List screenshot]()

#### *Post screen:*

* When the user clicks the post, they are presented with: the title, the description, who made it, when it was made, when the last update was made (if there was), the possibility to like, comment and report.

![Post screenshot]()

#### *Post screen:*

- When the user clicks the post, they are presented with: the title, the description, who made it, when it was made, when the last update was made (if there was), the possibility to like, comment and report.

​

## **Future-Enhancements**

​

* Users could log through their social networks profiles (FB, X) or email.
* Create a profile page where users can add their personal photos and descriptions.
​

## **Testing Phase**

​

Implementation: 

Test: 

Result: 
***

## **Validators**

. Python Linter [Python Linter Validator](https://pep8ci.herokuapp.com/)

Only error related to the ASCII graphics (W605)
![Python Linter Validator screenshot - run.py](assets/images-docs/run_py_python_linter.png)

![Python Linter Validator screenshot - words.py](assets/images-docs/words_py_python_linter.png)

## **Bugs**

Problem 🐞: 

Cause🛠: 

Resolution✅: 
***

## **Deployment**


## **Tech**

- Python.
- Django.
- Django-allauth.
- Cloudinary.
- Crispy-forms.
​

## **Credits**

### **Honorable mentions**

* Larissa Moura (my wife) - She was my tester and also my design guru.
* Richard Wells (my Code Institute tutor) - Help me throughout the project in all aspects.
​

### **Content:**

- Navbar based on the one used on the code along project "I Think Therefore I Blog" from [CodeInstitute] (<https://github.com/Code-Institute-Solutions/Django3blog>)
- Ability to like and favourite post based on Tutorial made by [VeryAcademy](<https://www.youtube.com/watch?v=H4QPHLmsZMU&ab_channel=VeryAcademy>)
