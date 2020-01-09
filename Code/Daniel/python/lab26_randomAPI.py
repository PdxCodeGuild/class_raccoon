# Look at the documentation, find out the endpoints and general capabilities
# Find a url and if possible, enter it into your browser and see if you can get JSON
# Look into authentication, might have to register an account to get an API key
# Send the request through Python, look at the format of the response
# Copy the data into a JSON viewer
# Write code to extract the relevant data and display it




import requests
import json

def launch_five():
    url = 'https://launchlibrary.net/1.3/launch/next/5'
    response = requests.get(url) 
    print(response.text)
    data = json.loads(response.text)["launches"] 
    launch_1 = data[0]
    launch_2 = data[1]
    launch_3 = data[2]
    launch_4 = data[3]
    launch_5 = data[4]
    # List next 5 launches
    # print(f"The next five scheduled launches are: \n1. {launch_1['name']} \n2. {launch_2['name']} \n3. {launch_3['name']} \n4. {launch_4['name']} \n5. {launch_5['name']}")
    # # Loop to let user get more information on specific launches
    # while True:
    #     user_choice = input("Which launch would you like to know more about 1, 2, 3, 4, 5, or quit? ").lower()
    #     if user_choice == "1":
    #         print()
    #         print(f"{launch_1['name']} is launching from {launch_1['location']['name']} on the {launch_1['rocket']['name']}. The launch window starts at {launch_1['windowstart']}")
    #         print()
    #     elif user_choice == "2":
    #         print()
    #         print(f"{launch_2['name']} is launching from {launch_2['location']['name']} on the {launch_2['rocket']['name']}. The launch window starts at {launch_2['windowstart']}")
    #         print()
    #     elif user_choice == "3":
    #         print()
    #         print(f"{launch_3['name']} is launching from {launch_3['location']['name']} on the {launch_3['rocket']['name']}. The launch window starts at {launch_3['windowstart']}")
    #         print()
    #     elif user_choice == "4":
    #         print()
    #         print(f"{launch_4['name']} is launching from {launch_4['location']['name']} on the {launch_4['rocket']['name']}. The launch window starts at {launch_4['windowstart']}")
    #         print()
    #     elif user_choice == "5":
    #         print()
    #         print(f"{launch_5['name']} is launching from {launch_5['location']['name']} on the {launch_5['rocket']['name']}. The launch window starts at {launch_5['windowstart']}")
    #         print()
    #     elif user_choice == "quit":
    #         print()
    #         print("Goodbye")
    #         print()
    #         break
    #     else:
    #         print("Invalid entry")


launch_five()



