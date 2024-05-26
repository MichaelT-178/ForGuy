# For Guy

This is the website repository for guy.

WHEN YOU'RE DONE HOST THE RESUMETEMPLATE.DOCX FILE ON THIS WEBSITE

WHEN YOU'RE DONE CHANGE THE EMAIL IN APPSTODOWNLOAD TO HIS ACTUAL EMAIL

WHEN YOU'RE DONE CHANGE THE EMAIL IN VSCodeExtensions TO HIS ACTUAL EMAIL

WHEN YOU'RE DONE CHANGE THE DOWNLOAD LINK ON THE HOME PAGE.

CISCO SECURE CLIENT DOWNLOADS SETUP PROJECT

TEMPLATES ZIP FOLDER

## How to Add a Section 

1. Go to src/Views/folder where you want to put your new view 
2. Go to router/index.js and add your path to your view 
3. Go to src/components/MenuItems.vue add your item.
4. Go to src/data/SearchPages.json

### How to Update Settings.json in VSCode Settings page

1. Go to python/real_settings.txt and paste your updated json data.
2. Run create_settings_file.py


# How to add an Instruction set

1. In src/data/CompSci/Instructions add your Instruction set file.

2. In src/data/CompSci/Instructions go to the DisplayLinks file and add your information.

3. In src/data/CompSci/Instructions go the InstructionSets file and add your information.

3. In src/data go to SearchPages and add your information.
```
{
    "id": 56,
    "Emoji": "ADD_EMOJI",
    "MenuName": "TITLE",
    "Link": "/CompSci/SetupProjects/REF"
},
```



4. In /python go to create_search_data.py and add the following function. Adjust the logic as necessary.

```
def get_<REF_NAME>():
	with open("../src/data/CompSci/Instructions/<NAME_OF_FILE>.json", "r") as file:
		content = json.load(file)

		info = content["Info"]
		instructions = content["Instructions"]
		instructions = modify_list_with_code_separation(instructions, "Code")

		Title = "<TITLE EMOJI>"
		Link = "/CompSci/SetupProjects/<REF>"
		Results = info + instructions

		return { "Title": Title, "Link": Link, "Results": Results }
```

5. If it's multi-line you'd use this template.

```
def get_<REF_NAME>():
    with open("../src/data/CompSci/Instructions/<NAME_OF_FILE>.json", "r") as file:
        content = json.load(file)
		
        multi_set = content["MultiSet"]

        Results = []

        for obj in multi_set:
            info = obj["Info"]
            instructions = obj["Instructions"]
            instructions = modify_list_with_code_separation(instructions, "Code")

            Results += info + instructions

        Title = "<TITLE EMOJI>"
        Link = "/CompSci/SetupProjects/<NAME_OF_FILE_NO_EXT>"
        
        return { "Title": Title, "Link": Link, "Results": Results }
```

6. Call your function below with the other functions

```
<REF_NAME> = get_<REF_NAME>()
```

7. Put your variable name in the "all_data" list 

```
get<REF_NAME>,
```

8. Done











## Commands to run when you clone

```
git clone https://github.com/MichaelT-178/ForGuy.git
```

```
cd ForGuy
```
<br>

**This might take a while, just be patient. Give it like 5 minutes.**
```
npm install vite --save-dev
```

<br>

```
npm run dev
```