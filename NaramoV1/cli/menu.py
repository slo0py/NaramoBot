import subprocess

ans=True
while ans:
    print ("""
    1. Calculate Heat from Excess 
    2. Show Graph
    3. Input new Heat/Excess
    4. Import values from CSV
    5. Exit/Quit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
        exec(open("findHeat.py").read()) 

    elif ans=="2":
        subprocess.Popen(["python", "showGraph.py"])

    elif ans=="3":
        exec(open("inputVals.py").read())

    elif ans=="4":
        file_name = input("\nType the path of the new data file to import! (or just the name, if it's in the same folder as the file you're writing to.)\n-> ")

        subprocess.run(["python", "append_data.py", file_name], capture_output=True, text=True)
        print("\nOutput from script:")
        print("\n"+result.stdout)

    elif ans=="5":
        print ("\nQuitting.")
        ans = None

    elif ans !="":
      print("\n Not Valid Choice Try again") 