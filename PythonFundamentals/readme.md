Terminologies - 

Virtual Environments - these are seperated private copies of each projects and we can make any changes we want in those copies so that real application will not break. 

Create VE - using VS Code Command Palette
1. Open your project in VS Code
2. Press Ctrl/Cmd + Shift + P
3. Type "Python: Create Environment"
4. Select "View"
5. Select your Python Installation
6. VS Code creates and activates everything for you!

or using CMD terminal - "python3 -m venv .venv"



Packages - pre-written code that others have created for us to use. Instead of writing everything from scratch. We can import these packages, for eg - 
1. requests - for downloading web pages
2. pandas - for working with data
3. openai - for using AI models

To install these packages, we can use pip(pip installs packages) is Python's package manager, it:
- Downloads packages from the internet
- Installs them in your environment
- Manages versions and dependencies

each package has different versions, and different projects might need different versions. 

What this command does - 
 'pip install requests' - 
    - pip connected to PyPI (Python Package Index) - a huge website where developers share their code
    - Downloaded the requests package - just a bunch of Python files that someone else wrote
    - Saved it in your .venv folder specifically in .venv/lib/python3.x/site-packages