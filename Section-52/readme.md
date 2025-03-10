## RESOURCES:

[instagram](https://www.instagram.com/)

## Step 1 - Get Your Instagram Credentials
In order to complete this project, you will need an Instagram account. I recommend setting up a new account for this project rather than using your main account (Facebook may disable accounts that exhibit bot-like behaviour).

1. Set up a fresh Instagram account: https://www.instagram.com/.


Go through the sign up steps. Verify your email address. And then add one or two posts, follow some accounts manually, and add a profile picture to your new account.



2. Take note of any pop-ups or cookie warnings that you encounter. Copy the XPath of the buttons on these pop up windows. 




3. Figure out which account you would like to target. Pick a large account that has a lot of followers.



4. You should set up these constants:
![image info](./pictures/1.png)

## Step 2 - Create a Class
Because there are multiple steps to this Selenium bot, it's easier if we make our code organised using a class.

1. Create a class called InstaFollower

2. In the init() method, create the Selenium driver .

3. Create three methods - login() and find_followers() and follow().

4. Outside of the class, initialise the object and call the three methods in order.

## Step 3 - Login to Instagram
Visit Instagram.com using Selenium
1. If there is a pop up with a cookie warning, dismiss the cookie warning.

2. Use Selenium and Python to login to Instagram automatically using the email and password for your new account. Write your code in the login() method.

Here is the URL: https://www.instagram.com/accounts/login/

3. You will probably encounter some pop ups. These include prompts for saving your login information as well as turning on notifications. To dismiss any pop-ups or cookie warnings that you might encounter, you'll have to take a close look at them.

You'll probably notice that the XPATH and the selectors change every time you access the page! That's because they are dynamically generated on Instagram's side, so each time you visit the page, the elements will be different. How can we get around this problem? 

Hint: You'll need to use contains() and text() in your XPATH. For example, to find a button that has the words "Click me" on a page, you can use:



button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Click me')]")



Note: Run your program sparingly and also interact with the instagram account as a human. Remember to manually log out while testing your code and don't run your code too often or in quick succession (e.g., 5x in a row) as this may result in triggering Instagram's bot detection and get the account banned. 


## Step 4 - Find the followers of the target account
When you go to a target Instagram account, you can click on their follower count to see all their followers e.g.


The URL is the name of the Instagram account added to the end of instagram.com

e.g. https://www.instagram.com/chefsteps/

The list of followers in the popup is limited to around 15 when it first loads, in order to see more followers, we need to scroll down in the popup (not the main webpage).

1. See if you can do some research using Google/StackOverflow to figure out how to scroll down on the followers popup. Write your code in the find_followers() method. This is what you're aiming for:




As a developer, one of the most common things is to find out how to do something you've never done before. This is a key skill we have to develop.

HINT 1: https://www.google.com/search?q=how+to+scroll+popup+selnium+python&oq=how+to+scroll+popup+selnium+python&aqs=chrome..69i57j0.19371j0j9&sourceid=chrome&ie=UTF-8

HINT 2: https://stackoverflow.com/questions/38041974/selenium-scroll-inside-of-popup-div

https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollTop

https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollHeight

## Step 5 - Follow all the followers
1. Inside the follow() method find all the follow buttons in the modal (popup) and click on each of them in turn. Add a 1 second delay between each click, so you can seem more human. e.g.


2. Sometimes, you'll encounter an account that you have already followed, in this case, when you press on the button it will generate a popup asking if you want to unfollow that person e.g.


2. When this happens the follow button is hidden under the popup and you will get a ElementClickInterceptedException  if you try to continue clicking on the follow button. Handle this exception and when it occurs, simply click on the "Cancel" button to dismiss the popup and continue to follow other people. e.g.




SOLUTION to part 5



Here is the solution to the challenge all in one place:

Completed Code for the entire project

Note, Instagram will update it's website. So the CSS Selectors and XPATH may change.

