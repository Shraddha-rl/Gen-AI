import  requests
url=
try:
  response =requests.get(url,timeout=10)
  response.raise_for_status()

  data = response.json()

  if data["type"]=="single":
    print("Random Joke:")
    print(data["joke"])
  elif data["type"]=="twopart":
    print("Random Joke:")
    print(data["setup"])
    input("\nPress Enter to see the punchline...")
    print(data["delivery"])
except requests.RequestException as error:
  print("API request failed",error)