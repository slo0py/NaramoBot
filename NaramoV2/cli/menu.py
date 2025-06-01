import subprocess


# Note: this script seems to not like reading from other files like findHeat very well, as weird characters keep showing up. 
# Working on a fix.

ans=True
while ans: 
    print ("""
    1. Calculate Heat from Excess 
    2. Show Pressure-Heat graph (not implemented yet)
    3. Show Pressure-Excess graph (not implemented yet)
    4. Import values from CSV (depricated from V1 version)
    5. Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        exec(open("findHeatV2.py").read()) 

    elif ans=="2":
        print("Not functional")

    elif ans=="3":
        print("Not functional")

    elif ans=="4":
        print("Not functional")

    elif ans=="5":
        print ("\nQuitting.")
        ans = None

    elif ans !="":
      print("\n Not Valid Choice Try again") 



# subprocess.Popen(["python", "showGraph.py"])


# file_name = input("\nType the path of the new data file to import! (or just the name, if it's in the same folder as the file you're writing to.)\n-> ")

# subprocess.run(["python", "append_data.py", file_name], capture_output=True, text=True)
# print("\nOutput from script:")
# print("\n"+result.stdout)