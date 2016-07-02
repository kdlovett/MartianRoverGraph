__author__ = 'keithlovett'
"""
Personal project. Displays some basic information about pictures taken by the Mars rovers.

Attribution:
Bucky Robert "thenewboston"'s Youtube tutorials were helpful for learning the basics behind tkinter. Thanks!
"""

import tkinter

import dataRetrieval

root = tkinter.Tk()
root.tk_setPalette(background = "black")
root.geometry('480x480+0+0')
root.title("Martian Rover Graph")

class menu:

    def print_sol(self, event):
        """
        Prints the current sol. If entered number is valid (greater than or equal to 0),
        set label color to green. Else set to red.
        """
        sol = int(self.strSol.get())

        if (sol >= 0):
            self.solLabel["fg"] = "green"
            self.solLabel["text"] = "Current sol: " + str(self.strSol.get())
        else:
            self.solLabel["fg"] = "red"
            self.solLabel["text"] = "Current sol: Out of range"
            self.strSol.set("")

    def print_cam(self, event):
        """
        Prints the current camera. If the rover is curiosity, and if there is an applicable camera currently entered,
        turn green. Else turn red. Else if there is an applicable camera currently entered for another rover, turn red.
        """

        camera = str(self.strCam.get())

        if (self.rover == "Curiosity"):
            if (camera == "FHAZ" or camera == "RHAZ" or camera == "MAST" or camera == "CHEMCAM" or camera == "MAHLI" or camera == "MARDI" or camera == "NAVCAM"):
                self.camLabel["fg"] = "green"
                self.camLabel["text"] = "Current camera: " + camera
            else:
                self.camLabel["fg"] = "red"
                self.camLabel["text"] = "Current camera: Not valid"
                self.strCam.set("Choose a valid camera")
        else:
            if (camera == "FHAZ" or camera == "RHAZ" or camera == "NAVCAM" or camera == "PANCAM" or camera == "MINITES"):
                self.camLabel["fg"] = "green"
                self.camLabel["text"] = "Current camera: " + camera
            else:
                self.camLabel["fg"] = "red"
                self.camLabel["text"] = "Current camera: Not valid"
                self.strCam.set("Choose a valid camera")

    def curiosity_select(self, event):
        """
        Prints appropriate information for the Curiosity.
        """

        self.roverLabel["fg"] = "purple"
        self.rover = "Curiosity"
        self.roverLabel["text"] = self.rover
        self.validCams["text"] = "FHAZ RHAZ MAST CHEMCAM MAHLI MARDI NAVCAM"

    def opportunity_select(self, event):
        """
        Prints appropriate information for the Opportunity.
        """

        self.roverLabel["fg"] = "purple"
        self.rover = "Opportunity"
        self.roverLabel["text"] = self.rover
        self.validCams["text"] = "FHAZ RHAZ NAVCAM PANCAM MINITES"

    def spirit_select(self, event):
        """
        Prints appropriate information for the Spirit.
        """

        self.roverLabel["fg"] = "purple"
        self.rover = "Spirit"
        self.roverLabel["text"] = self.rover
        self.validCams["text"] = "FHAZ RHAZ NAVCAM PANCAM MINITES"

    def begin_search(self, event):
        """
        So long as valid sol, rover, and camera have been entered, retrieve data, and form graph.
        """

        self.graph.delete(tkinter.ALL)
        self.blueBox = self.graph.create_rectangle(10, 5, 380, 250, outline = "blue")

        sol = int(self.strSol.get())

        if (sol >= 0 and self.rover != "" and self.camLabel["fg"] == "green"):
            solOneData = dataRetrieval.retrieve(str(sol), self.rover.lower(), str(self.strCam.get()).lower())
            solTwoData = dataRetrieval.retrieve(str(sol + 1), self.rover.lower(), str(self.strCam.get()).lower())
            solThreeData = dataRetrieval.retrieve(str(sol + 2), self.rover.lower(), str(self.strCam.get()).lower())
            solFourData = dataRetrieval.retrieve(str(sol + 3), self.rover.lower(), str(self.strCam.get()).lower())
            solFiveData = dataRetrieval.retrieve(str(sol + 4), self.rover.lower(), str(self.strCam.get()).lower())
            solSixData = dataRetrieval.retrieve(str(sol + 5), self.rover.lower(), str(self.strCam.get()).lower())

            self.xAxLabel["text"] = str(sol) + "\t" + str(sol + 1) + "\t" + str(sol + 2) + "\t " + str(sol + 3) + "\t" + str(sol + 4) + "\t" + str(sol + 5)

            solOneLine = self.graph.create_line(11, 250 - solOneData.numb_pictures() * 6.8, 84.8, 250 - solTwoData.numb_pictures() * 6.8, fill = "green", width = 2, activewidth = 4)
            solTwoLine = self.graph.create_line(84.8, 250 - solTwoData.numb_pictures() * 6.8, 158.6, 250 - solThreeData.numb_pictures() * 6.8, fill = "red", width = 2, activewidth = 4)
            solThreeLine = self.graph.create_line(158.6, 250 - solThreeData.numb_pictures() * 6.8, 232.4, 250 - solFourData.numb_pictures() * 6.8, fill = "orange", width = 2, activewidth = 4)
            solFourLine = self.graph.create_line(232.4,250 - solFourData.numb_pictures() * 6.8, 306.2, 250 - solFiveData.numb_pictures() * 6.8, fill = "yellow", width = 2, activewidth = 4)
            solFiveLine = self.graph.create_line(306.2,250 - solFiveData.numb_pictures() * 6.8, 380, 250 - solSixData.numb_pictures() * 6.8, fill = "purple", width = 2, activewidth = 4)

    def __init__(self, master):
        """
        Constructor for the interface.
        """

        #Top frame contains sol entry and label
        topFrame = tkinter.Frame(master)
        topFrame.pack()

        #Middle frame contains rover buttons
        middleFrame = tkinter.Frame(master)
        middleFrame.pack()

        #Bottom frame contains camera selection
        bottomFrame = tkinter.Frame(master)
        bottomFrame.pack()

        #Go frame contains search
        goFrame = tkinter.Frame(master)
        goFrame.pack()

        #yAxis frame contains the y axis
        yAxisFrame = tkinter.Frame(master)
        yAxisFrame.pack(side = tkinter.LEFT, anchor = tkinter.N)

        #graph frame contains the graph, lines, and x axis
        graphFrame = tkinter.Frame(master)
        graphFrame.pack(side = tkinter.RIGHT)

        """
        Forms the graph and x label for this graph
        """
        self.graph = tkinter.Canvas(graphFrame, width = 400, height = 270)
        self.graph.pack()
        self.blueBox = self.graph.create_rectangle(10, 5, 380, 250, outline = "blue")

        self.xAxLabel = tkinter.Label(graphFrame, text = "Sol ")
        self.xAxLabel.pack(side = tkinter.BOTTOM, anchor = tkinter.W)

        """
        Forms the entry box and label for sol
        """

        solEntry = tkinter.Entry(topFrame)
        solEntry.pack(side = tkinter.RIGHT)

        self.strSol = tkinter.StringVar()
        self.strSol.set("1000")

        self.solLabel = tkinter.Label(topFrame, text = "Enter sol to examine:")
        self.solLabel.pack(side = tkinter.LEFT)

        solEntry["textvariable"] = self.strSol

        #Binds the return key to the function print_sol, with input from strSol
        solEntry.bind('<Key-Return>', self.print_sol, self.strSol)

        """
        Forms label and buttons for rover, and binds the buttons to left mouse click with the correct functions
        """

        self.roverLabel = tkinter.Label(middleFrame, text = "Click a rover to examine:")
        self.roverLabel.pack(side = tkinter.TOP)

        self.rover = ""

        selectCuriosity = tkinter.Button(middleFrame, text = "Curiosity", fg = "black")
        selectCuriosity.pack(side = tkinter.LEFT)
        selectCuriosity.bind('<Button-1>', self.curiosity_select)

        selectOpportunity = tkinter.Button(middleFrame, text = "Opportunity", fg = "black")
        selectOpportunity.pack(side = tkinter.RIGHT)
        selectOpportunity.bind('<Button-1>', self.opportunity_select)

        selectSpirit = tkinter.Button(middleFrame, text = "Spirit", fg = "black")
        selectSpirit.pack()
        selectSpirit.bind('<Button-1>', self.spirit_select)

        """
        Forms the entry box and label for camera
        """

        self.strCam = ""

        camEntry = tkinter.Entry(bottomFrame)
        camEntry.pack(side = tkinter.RIGHT)

        self.strCam = tkinter.StringVar()
        self.strCam.set("")

        self.camLabel = tkinter.Label(bottomFrame, text = "Enter camera to examine:")
        self.camLabel.pack(side = tkinter.LEFT)

        camEntry["textvariable"] = self.strCam

        #Binds the return key to the function print_cam, with input from strCam
        camEntry.bind('<Key-Return>', self.print_cam, self.strCam)

        """
        Forms label for cameras that are valid for each rover. These are then updated in the selection functions
        corresponding to the appropriate rover.
        """

        self.validCams = tkinter.Label(goFrame, text = "[Valid cameras for Rover]")
        self.validCams.pack(side = tkinter.TOP)

        """
        Forms the "go button" to start a search. Binds it to the left mouse button and the begin_search function.
        """

        goButton = tkinter.Button(goFrame, text = "Search", fg = "green")
        goButton.pack(side = tkinter.BOTTOM, anchor = tkinter.S)
        goButton.bind('<Button-1>', self.begin_search)

        """
        Creates the y axis label.
        """

        yAxLabel = tkinter.Label(yAxisFrame, text = "Images\n\n\n\n30\n\n25\n\n20\n\n15\n\n10\n\n5\n\n0")
        yAxLabel.pack(side = tkinter.LEFT, padx = 10)

gui = menu(root)
root.mainloop()