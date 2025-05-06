Download the Starting Project
1. Download the starting .zip files from this lessons resources.



2. Unzip and open the project in PyCharm. PyCharm may prompt you to create a new virtual environment and install the dependencies listed in the requirements.txt. Agree and click OK.


This should do the trick. However, if you still see any red underlines in your main.py then tell PyCharm to check the virtual environment and dependencies again by going to File -> Reload All from Disk.


3. (Troubleshooting) If you don't get prompted set up a virtual environment, set one up manually by adding a new Python interpreter.


You can also find this under File  -> Settings -> Project -> Python Interpreter. Click Add Interpreter -> Add Local Interpreter.

Leave the default settings and click OK


Do not tick "inherit global site-packages". When you click OK, you will create a new venv folder in your project. All of the project requirements and packages will be installed into this venv folder. This keeps the packages isolated from global settings and your operating system as well as all other projects. This is the ideal setup for all Python projects.



4. (Troubleshooting) If you still see red underlines in the main.py, you are missing the required packages (imports). To install all the required packages you can open the Terminal in PyCharm (bottom left).

On Windows type:

python -m pip install -r requirements.txt
On MacOS type:

pip3 install -r requirements.txt


5. Look around the project. You should see a .csv file with data on some of London's cafes.





Resources for this lecture