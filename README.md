
## Description
**NaramoBot** is a lightweight educational tool made in Python created for use in the Roblox Reactor Simulator [Naramo Nuclear Plant](https://www.roblox.com/games/98626216952426/UPDATE-Naramo-Nuclear-Plant). <br/>
While a Discord Bot integration and/or website is planned, it runs primarily through a shell or command line interface.

## Setup
*This assumes you are on Windows, although setup for Linux/MacOS should follow a similar premise.*

1. Download Python (https://www.python.org/) and complete the installer.
2. Press the Win/Search key and type in Command Prompt. Press ENTER.
3. Copy the following commands, and paste them into the prompt (one at a time) and press ENTER. Do not do all of them at once.
These commands should ensure you have everything you need to run the program.
   ```
   // Makes sure Pip, a package manager is installed
	py -m ensurepip --upgrade 

	// Downloads script dependencies using Pip
	pip install numpy pandas matplotlib scipy 
	```

Note: If your computer says `pip is not installed`, close and reopen command prompt, then run it again.

4. Download the latest version of the CLI scripts from the repo, then run them in your terminal using `python <script_name>`. (Or to make it simpler, just double click `menu.py).

## File Descriptions

### V1:
> **_NOTE:_**  *None of the Naramo/V1 scripts will be accurate to the latest game version due to their functionality being broken by the latest update. See [the latest version.](https://github.com/slo0py/NaramoBot/?tab=readme-ov-file#v2)* 

<br/>

`/NaramoV1/cli/`

**menu.py** - Command Line (CLI) tool to use the different functions.

**findHeat.py** - CLI tool that prompts the user for a target Excess level (such as a Power Order), and outputs estimated Reactor Heat required to reach that level within a certain Margin of Error.

**trainingdata.csv** - Comma Seperated Values list of reactor Heat and Excess values I collected from monitoring the Naramo reactor.

**showGraph.py** - Graphs the data from trainingdata.csv on a scatter plot. Draws a line that shows the linear trend of the data. Click to open.

**inputVals.py** - CLI tool to input new training data.

---

*Scripts that were either not used or are not integral to the overall program use.*

**validate.py** - CLI tool that checks the CSV file for errors. 

**appendCSV.py** - CLI tool that appends another CSV file with a comma delimiter to the end of trainingdata.csv. Takes in one argument, which is the name of the source CSV file. Skips duplicate data.

`/NaramoV1/core/`

**classes.py** - A start to a database entry feature that got scrapped with an update to Naramo.

**delete.py** - Ditto.

**trainingdata.sql** - Ditto.

### V2:
`/NaramoV2/cli/` <br/>

**menu.py** - Command Line (CLI) tool to use the different functions.

**findHeatV2.py** - CLI tool that prompts the user for a target Excess level (such as a Power Order), and outputs estimated Reactor Heat required to reach it.

- #### Planned:<br/>
**heatPres_relationship.py** - Shows a graph of the relationship between reactor Heat, and reactor Pressure.

**presGen_relationship.py** - Shows a graph of the relationship between reactor Pressure and reactor Generation.

**heatExcess_relationship.py** - Shows a graph of the calculated relationship between reactor Heat and reactor Excess levels (basically graphs linreg. might not do this one idk)

**inputVals.py** - CLI tool to input new data into the set, in case the developers decide to change the reactor again.

## Program Logic

### V1:
<details open>
<summary>Open</summary>
<br>
The old equation used to calculate heat from a given Excess amount:

	Heat = Heat level 
	Excess = Power lvl in MW
	Slope (Rate of change of Excess with respect to Heat, calculated off of training data)
	Intercept (Calculated excess value when heat is 0)
	
	Excess = Slope * Heat + Intercept
	Turns into:
	Heat = (Excess - Intercept) / Slope
</details>



### V2:

<details open>
<summary>Open</summary>
<br>
NaramoBot V2 uses a two-step linear regression approach to determine the required temperature for achieving target excess power levels.

### Data Processing

The program begins with three arrays of observational data from the Naramo Reactor (data provided by DuskyJay):
- **Temperature**: Reactor heat levels (17 data points) 
- **Pressure**: Reactor pressure readings (17 data points) 
- **Total Generation**: Raw power generation values (17 data points) <br/><br/>


The script converts total generation to **excess power** by subtracting the facility power requirement (25,000 units):
```
excess_power = total_generation - 25,000
```

### Linear Regression Models

Two separate linear regression models are calculated using scipy.stats:

#### Model 1: Temperature → Pressure
```
pressure = (temperature × slope₁) + intercept₁
```
This model captures the relationship between reactor heat settings and resulting pressure levels.

#### Model 2: Pressure → Excess Power
```
excess_power = (pressure × slope₂) + intercept₂
```
This model captures the relationship between pressure levels and the excess power output.

### Calculation

To find the required temperature for a target excess power level, the program works backwards through the relationships:

#### Step 1: Target Excess Power → Required Pressure
Using the inverse of Model 2:
```
required_pressure = (target_excess - intercept₂) ÷ slope₂
```

#### Step 2: Required Pressure → Required Temperature  
Using the inverse of Model 1:
```
required_temperature = (required_pressure - intercept₁) ÷ slope₁
```

### Validation and Output

The program includes several validation steps:
- **Range Checking**: Warns if the target excess power is outside the observed data range (with 20% tolerance)
- **Model Accuracy**: Displays R² values for both regression models to indicate fit quality
- **Results Display**: Shows the calculated temperature, pressure, and total generation requirements

### Mathmatical Assumptions

The approach assumes linear relationships between:
1. Temperature and pressure (thermal dynamics)
2. Pressure and power generation (mechanical energy conversion)

These assumptions are validated by the R² correlation coefficients calculated during model creation. High R² values (close to 1.0) indicate that linear regression is appropriate for the relationships in the training data.
</details>





## Credit
- **little_man9277**, for data collection & feedback for the V1 model.
- **DuskyJay**, for V2 data collection, in addition to providing very useful information regarding how the updated reactor actually calculates power output.
- **[3ND & Naramo Developers](https://www.roblox.com/communities/2704934/The-Noobic-Stratocracy#!/about)** 	for making such a cool game :)
- **ClaudeAI** and **ChatGPT** for helping resolve formatting issues, debugging and generation of parts of the README.