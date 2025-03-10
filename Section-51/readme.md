## RESOURCES
[vice](https://www.vice.com/en/article/this-bot-will-tweet-at-comcast-whenever-your-internet-is-slower-than-advertised/)
[speedtest](https://www.speedtest.net/)
[news](https://www.huffingtonpost.co.uk/2014/07/15/comcast-call-from-hell_n_5586679.html)
[twiter complains](https://time.com/4894182/twitter-company-complaints/)


## Step 1 - Setup Your Twitter Account
In order to tweet at an internet provider, we of course need a twitter account. If you want, you can set up a new Twitter account instead of using your personal account.

1. Sign up for a Twitter account here:

https://twitter.com/i/flow/signup

2. Additionally, you'll need to get your Internet Service Provider (ISP)'s guaranteed internet speeds. This should be in your contract somewhere. Alternatively, you could just use an example speed, e.g. 150Mbps download, 10Mbps upload.

3. Create a new Python project and add these details as constants in the file. e.g.

## Step 2 - Create a Class
Because there are multiple steps to this Selenium bot, it's easier if we make our code organised using a class.

1. Create a class called InternetSpeedTwitterBot

2. In the init() method, create the Selenium driver and 2 other properties down and up .

3. Create two methods - get_internet_speed() and tweet_at_provider() .

4. Outside of the class, initialise the object and call the two methods in order. Where you first get the internet speed and then tweet at the provider.

HINT: We talked about classes and object in Python extensively in day 16-20, this might be a good time to revise those lessons if you can't remember how to do the steps above.

## Step 3 - Get Internet Speeds
1. Use this speedtest website to get your current live download and upload speeds manually. e.g.


2. Use Selenium and Python to get the same result printed out in your console. e.g.


HINT 1: First use Selenium to get the speedtest address, then see which steps you have to make your bot go through to get those results.

HINT 2: Depending on your internet speeds, you might need to add a 60-180s delay to wait for the results.

HINT 3: Consider using XPATH, if you can't figure out how to target the element.


## Step 4 - Building a Twitter Bot to Tweet at your Internet Provider
1. Go through the process of logging-in and tweeting on Twitter as a human to study which selectors/id/classes/XPATHs you could target.

2. Use Python and Selenium to complete the same process, login to Twitter, compose the tweet to include your up/down speeds and your promised speeds then send the tweet.
NOTE: If you don't want to mention (@) the internet provider, just compose a simple tweet like this:


NOTE: If you are logging into Twitter repeatedly, they will make you complete a Re-CAPTCHA/send a confirmation code to your email to prove you are human. Go through this process to continue testing.



