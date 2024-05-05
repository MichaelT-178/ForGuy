from termcolor import colored as c


cool = "nice"

print(f"Failed to fetch the website link. Status code:", end="")
print(c(f" {cool}", 'red'))





print(c(f\" {response.status_code}\", 'red'))