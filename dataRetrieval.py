__author__ = 'keithlovett'
"""
Personal project. Shows short trends of Mars rovers in the form of a graph.

Attribution:
Bucky Robert "thenewboston"'s Youtube tutorials were helpful for learning the basics behind tkinter.
Also found the eff-bot Python documentation on more minute aspects of tkinter quite helpful.
Retrieval requires a nasa api key to be present in the secrets file. (My brother showed me the best way
of going about making the api call, with the key in a separate file.)
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

        self.url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/' + rover + '/photos?sol=' + sol + '&camera='\
                   + camera + '&api_key=' + nasaApi

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

        if (self.data == {"photos": {}}):
            return 0
        else:
            return len(self.data["photos"])

    def earth_date(self):
        """
        Returns the Earth date of a given sol.
        """

        if (self.data == {"photos": {}}):
            return "No data"
        else:
            return self.data["photos"][1]["earth_date"]

    def camera_name(self):
        """
        Returns the full name of a camera used to take a picture.
        """

        if (self.data == {"photos": {}}):
            return "No data"
        else:
            return self.data["photos"][1]["camera"]["full_name"]