import requests  # Make online requests
import json  # Parse json response to py dict


class nutritionInfo:  # Api class
    def __init__(self):  # initialize
        pass

    def makequery(self, foodQuery):  # func to make food query
        # incase food not found
        try:
            # url to get requests from
            self.api_url = "https://api.api-ninjas.com/v1/nutrition?query="
            # Get the data from the api using
            self.response = requests.get(
                self.api_url + str(foodQuery), headers={
                    'X-Api-Key': 'C6e95NIQxZze2dwtANO0+A==C8xURwL7essFClbv'})
            # If request was ok
            if self.response.status_code == requests.codes.ok:
                # Parse json data into dictionary
                self.data = json.loads(self.response.text[1:-1])
            else:
                # If request was not ok raise HTTP with status code
                raise requests.exceptions.HTTPError(self.response.status_code)
        except json.decoder.JSONDecodeError:
            # If json parse error, food not found, raise ValueError for food
            raise ValueError("Food not found")
        # make a copy of orginal data dictionary
        self.cleandata = self.data.copy()
        # remove unwanted data from dictionary
        for i in self.data.keys():
            # only keep name calories size and protein
            if i not in ['name', 'calories', 'serving_size_g', 'protein_g']:
                del self.cleandata[i]
        # return data with only keys we want
        return self.cleandata
