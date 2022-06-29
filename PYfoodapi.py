import requests
import json


class foodapi:
    def __init__(self):
        self.__apikey = "C6e95NIQxZze2dwtANO0+A==C8xURwL7essFClbv"

    def makequery(self, foodQuery):
        # incase food not found
        try:
            # url to get requests from
            self.api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(
                foodQuery)  # add what food to find at end
            # Get the data from the api
            self.response = requests.get(
                self.api_url, headers={'X-Api-Key': self.__apikey})  # using the API key
            # If request was ok
            if self.response.status_code == requests.codes.ok:
                # Parse json data into dictionary
                self.data = json.loads(self.response.text[1:-1])
            else:
                # If request was not ok raise HTTP with status code
                raise requests.exceptions.HTTPError(self.response.status_code)
        except json.decoder.JSONDecodeError:
            # If json parse error means food not found so raise ValueError for foodname
            raise ValueError("Food not found")
        # make a copy of orginal data dictionary
        self.cleandata = self.data.copy()
        # remove unwanted data from dictionary
        for i in self.data.keys():
            # only keep name calories size and protein
            if not i in ['name', 'calories', 'serving_size_g', 'protein_g']:
                del self.cleandata[i]
        # return data with only keys we want
        return self.cleandata
