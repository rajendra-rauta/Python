import urllib.request
import urllib.parse
import json

# Function to retrieve and parse JSON data, then get the first plus_code
def get_plus_code(location):
    # Construct the URL with the location as a parameter
    base_url = "http://py4e-data.dr-chuck.net/opengeo?"
    params = {'q': location}
    url = base_url + urllib.parse.urlencode(params)
    
    # Retrieve the data from the URL
    print('Retrieving', url)
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print(f"Retrieved {len(data)} characters")
    
    # Parse the JSON data
    json_data = json.loads(data)
    
    # Extract and return the first plus_code
    if 'plus_codes' in json_data:
        plus_code = json_data['plus_codes'][0]
        return plus_code
    else:
        return "No plus code found"

# Main program
if __name__ == "__main__":
    # Get the location from the user input
    location = "UNIVERSIDAD DE Buenos Aires" 
    
    # Get the plus code for the given location 
    plus_code = get_plus_code(location) 
      
    # Print the results 
    print(f"Plus code {plus_code}") 
   