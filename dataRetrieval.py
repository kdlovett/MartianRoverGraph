__author__ = 'keithlovett'
"""
Personal project. Displays some basic information about pictures taken by the Mars rovers.

Attribution:
Bucky Robert "thenewboston"'s Youtube tutorials were helpful for learning the basics behind tkinter.
Also found the eff-bot Python documentation on more minute aspects of tkinter quite helpful.
Thanks!
Utilizes Nasa's open source "Mars Rover Photos" data.
"""

import urllib.request
import json

secret_file = open('.secrets.json','r')
secrets = json.loads(secret_file.read())

nasaApi = secrets['nasa_api_key']

class retrieve():

    def __init__(self, sol, rover, camera):
        """
        Constructor method. Parameters include queries for sol, rover, and camera to be used in a url request.
        Returns the json data of this url request.
        """

        self.url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/' + rover + '/photos?sol=' + sol + '&camera=' + camera + '&api_key=' + nasaApi

        """
        In the case that no photos are available, a bad http request error is made. Instead, just make the data
        a dictionary with the appropriate key, that is empty
        """
        try:
            request = urllib.request.Request(self.url)
        except:
            self.data = {"photos": {}}
            print("Bad request made.")

        """
        Same as in previous try/catch.
        """
        try:
            response = urllib.request.urlopen(request)
            strResponse = response.readall().decode('utf-8')
            self.data = json.loads(strResponse)
        except:
            self.data = {"photos": {}}
            print("Bad request made.")

    def numb_pictures(self):
        """
        Returns the number of pictures taken on the given sol by the given rover by the given camera.
        """
        return len(self.data["photos"])

    def print_all(self):
        """
        Prints the data corresponding to each photo.
        """
        for lines in self.data["photos"]:
            print(lines)