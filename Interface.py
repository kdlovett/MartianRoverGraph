__author__ = 'keithlovett'
"""
Personal project. Displays some basic information about pictures taken by the Mars rovers.

Good test parameters:
Sol 580, Curiosity, FHAZ

Attribution:
Bucky Robert "thenewboston"'s Youtube tutorials were helpful for learning the basics behind tkinter.
Also found the eff-bot Python documentation on more minute aspects of tkinter quite helpful.
Thanks!
Utilizes Nasa's open source "Mars Rover Photos" data.
"""

import tkinter
import dataRetrieval
import copy

root = tkinter.Tk()
root.tk_setPalette(background = "black")
root.geometry('480x480')
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
            #Retrieves data for the appropriate sol
            solOneGet = dataRetrieval.retrieve(str(sol), self.rover.lower(), str(self.strCam.get()).lower())
            solTwoGet = dataRetrieval.retrieve(str(sol + 1), self.rover.lower(), str(self.strCam.get()).lower())
            solThreeGet = dataRetrieval.retrieve(str(sol + 2), self.rover.lower(), str(self.strCam.get()).lower())
            solFourGet = dataRetrieval.retrieve(str(sol + 3), self.rover.lower(), str(self.strCam.get()).lower())
            solFiveGet = dataRetrieval.retrieve(str(sol + 4), self.rover.lower(), str(self.strCam.get()).lower())
            solSixGet = dataRetrieval.retrieve(str(sol + 5), self.rover.lower(), str(self.strCam.get()).lower())

            #Creates deep copies of sol data in order to avoid making an unnecessary number of http requests.
            self.solOneData = copy.deepcopy(solOneGet)
            self.solTwoData = copy.deepcopy(solTwoGet)
            self.solThreeData = copy.deepcopy(solThreeGet)
            self.solFourData = copy.deepcopy(solFourGet)
            self.solFiveData = copy.deepcopy(solFiveGet)
            self.solSixData = copy.deepcopy(solSixGet)

            #Creates x label and fills with appropriate sol numbers
            self.xAxLabel["text"] = str(sol) + "\t" + str(sol + 1) + "\t" + str(sol + 2) + "\t " + str(sol + 3) + "\t" + str(sol + 4) + "\t" + str(sol + 5)

            #Creates five lines spanning the length of six selected sols.
            solOneLine = self.graph.create_line(11, 250 - self.solOneData.numb_pictures() * 6.8, 84.8,
                                                250 - self.solTwoData.numb_pictures() * 6.8, fill="green", width=2)
            solTwoLine = self.graph.create_line(84.8, 250 - self.solTwoData.numb_pictures() * 6.8, 158.6,
                                                250 - self.solThreeData.numb_pictures() * 6.8, fill="green", width=2)
            solThreeLine = self.graph.create_line(158.6, 250 - self.solThreeData.numb_pictures() * 6.8, 232.4,
                                                  250 - self.solFourData.numb_pictures() * 6.8, fill="green", width=2)
            solFourLine = self.graph.create_line(232.4,250 - self.solFourData.numb_pictures() * 6.8, 306.2,
                                                 250 - self.solFiveData.numb_pictures() * 6.8, fill="green", width=2)
            solFiveLine = self.graph.create_line(306.2,250 - self.solFiveData.numb_pictures() * 6.8, 380,
                                                 250 - self.solSixData.numb_pictures() * 6.8, fill="green", width=2)

            #Creates six dots at the corresponding selected sols' locations.
            solOneDot = self.graph.create_oval(8, 247 - self.solOneData.numb_pictures() * 6.8, 14,
                                               253 - self.solOneData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline = "green", activewidth = 2)
            solTwoDot = self.graph.create_oval(81.8, 247 - self.solTwoData.numb_pictures() * 6.8, 87.8,
                                               253 - self.solTwoData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline="green", activewidth = 2)
            solThreeDot = self.graph.create_oval(155.6, 247 - self.solThreeData.numb_pictures() * 6.8, 161.6,
                                               253 - self.solThreeData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline="green", activewidth = 2)
            solFourDot = self.graph.create_oval(229.4, 247 - self.solFourData.numb_pictures() * 6.8, 235.4,
                                               253 - self.solFourData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline="green", activewidth = 2)
            solFiveDot = self.graph.create_oval(303.2, 247 - self.solFiveData.numb_pictures() * 6.8, 309.2,
                                               253 - self.solFiveData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline="green", activewidth = 2)
            solSixDot = self.graph.create_oval(377, 247 - self.solSixData.numb_pictures() * 6.8, 383,
                                               253 - self.solSixData.numb_pictures() * 6.8, fill="green",
                                               activefill="blue", outline="green", activewidth = 2)

            #Binds each sol's dot on the graph to the mouse entering the line. Performs data assign function to assign
            #appropriate data to appropriate dot.
            self.graph.tag_bind(solOneDot, '<Enter>', self.data_assign)
            self.graph.tag_bind(solTwoDot, '<Enter>', self.data_assign)
            self.graph.tag_bind(solThreeDot, '<Enter>', self.data_assign)
            self.graph.tag_bind(solFourDot, '<Enter>', self.data_assign)
            self.graph.tag_bind(solFiveDot, '<Enter>', self.data_assign)
            self.graph.tag_bind(solSixDot, '<Enter>', self.data_assign)

    def data_assign(self, event):
        """
        Upon entering a dot on the graph, checks if the mouse coordinates x value is less than or equal to the maximum
        x value of the oval representing the dot. If so, display the info for the corresponding sol's data.
        """

        if (event.x <= 17 and event.x > 5):
            self.display_info(self.solOneData)
        elif (event.x <= 90.8 and event.x > 78.8):
            self.display_info(self.solTwoData)
        elif (event.x <= 164.6 and event.x > 152.6):
            self.display_info(self.solThreeData)
        elif (event.x <= 234.4 and event.x > 230.4):
            self.display_info(self.solFourData)
        elif (event.x <= 306.2 and event.x > 307.2):
            self.display_info(self.solFiveData)
        elif (event.x <= 380 and event.x > 374):
            self.display_info(self.solSixData)

    def display_info(self, solData):
        """
        Will continue working on here.
        """

        print(solData.numb_pictures())


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