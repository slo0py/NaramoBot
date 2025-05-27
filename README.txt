**FILE INFO**
menu.py - Command Line (CLI) tool to use the different functions.

findHeat.py - CLI tool that prompts the user for a target Excess level (such as a Power Order), and outputs estimated Reactor Heat required to reach that level within a certain Margin of Error.

trainingdata.csv - Comma Seperated Values list of reactor Heat and Excess values I collected from monitoring the Naramo reactor.

showGraph.py - Graphs the data from trainingdata.csv on a scatter plot. Draws a line that shows the linear trend of the data. Click to open.

InputVals.py - CLI tool to input new training data. 

*not strictly necessary programs.*

validate.py - CLI tool that checks the CSV file for errors. 

appendCSV.py - CLI tool that appends another CSV file with a comma delimiter to the end of trainingdata.csv. Takes in one argument, which is the name of the source CSV file. Skips duplicate data.



**SETUP**
This assumes you are on Windows.

1) Download Python (https://www.python.org/) and complete the installer.
2) Press the Win/Search key and type in Command Prompt. Press ENTER.
3) Copy the following commands, and paste them into the prompt (one at a time) and press ENTER. Do not do all of them at once.
These commands should ensure you have everything you need to run the program.

	py -m ensurepip --upgrade

	pip install numpy pandas matplotlib

Note: If your computer says "pip is not installed", close and reopen command prompt, then run it again.

4) Find the Directory you put the Scripts and .CSV file in, then go back to Command Prompt.
	4a) Type in cd <folder name/path> then press ENTER

	(For example, if you put it in Downloads, type cd Downloads. Same for Documents.)
	If you put it within a folder that is harder to get to, you may have to do the full file path to the location where you saved it, or use multiple cd commands.
	For example, if I put it within a subfolder within Documents, you would do 
	cd Documents <ENTER>
	cd <folder> <ENTER>
	*OR*
	cd C:\Users\<username>\Documents\<folder> <ENTER>

5) Type in the full name of the program you want to use!



**THE MATHS**
*How heat is calculated from excess levels*

	Heat = Heat level 
	Excess = Power lvl in W
	a = slope (Rate of change of Excess with respect to Heat, calculated off of training data)
		Don't ask me to explain how slope is calculated. I don't want to think about any of this again until college.
	b = intercept (Calculated excess value when heat is 0)
	
	Excess= a*Heat+b
	Turns into:
	Heat=(Excess - b)/a


*Heat MOE calculation*
	delta excess: Excess fluctuations at stable reactor temperature. Found to be close to 1000.
	delta heat: idk if delta is the right word for this but. Basically the amount the heat estimate could be off by given the Excess amount.

	delta heat = delta excess / |slope|


**DISCLAIMER**
Although this was designed and built by me, ChatGPT was utilized on select occasions during this project.
1) I initially used the CSV module for this project, until I learned about Pandas. ChatGPT was used to convert my existing code to work with Pandas.
2) Additionally, I hate working with Pandas. I asked it many questions regarding syntax for the project as a whole, as well as debugging for the graphical script, showGraph.py.
3) validate.py and appendCSV.py are some small scripts that validate and merge CSV files. They are not a core part of this project, and out of convenience, I had ChatGPT create them for me.