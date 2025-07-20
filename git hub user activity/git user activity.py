import requests
user = input("enter the username you want to fetch the data of : ")
response = requests.get(f"https://api.github.com/users/{user}/events")
if response.status_code==200:
    data = response.json()

    
    for event in data:
        event_type = event.get("type")
        repo = event.get("repo",{}).get("name","unknown repo")
        time = event.get("created_at","unknown time")

        if event_type== "PushEvent":
            commit_count = len(event.get("Payload",{}).get("commits",[]))

            print(f"Pushed {commit_count} commits to {repo} at {time}")
        elif event_type == "WatchEvent":
            print(f"starred to {repo} at {time}")
        elif event_type == "ForkEvent":
            print(f"Forked to {repo} at {time}")     
        else:
            print(f"did {event_type} on {repo} at {time}")
        print("----------------------------------------------------------------")
else:
    print("failed to fatch the data , try another username")