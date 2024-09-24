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

4. In src/data go to SearchPages and add your information.
```
{
    "id": 56,
    "Emoji": "ADD_EMOJI",
    "EmojiDescription": "DESCRIBE YOUR EMOJI AND OTHER HELPER SEARCH TERMS",
    "MenuName": "TITLE",
    "Link": "/CompSci/SetupProjects/REF"
},
```

5. In /python go to create_search_data.py and add the following function. Adjust the logic as necessary.

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

6. If it's multiset you'd use this template.

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

7. Call your function below with the other functions

```
<REF_NAME> = get_<REF_NAME>()
```

8. Put your variable name in the "all_data" list 

```
<REF_NAME>,
```

8. Done


# How to add a Section to Github.vue

1. Go to GitHub.json. In the "ScrollLinks" attribute list add your section name and ref.

```
{
    "id": 15,
    "name": "This is My New Section",
    "ref": "NewSectionRefName"
},
```

2. Scroll Down and paste the following code above the "Text" attribute. This is where you'll put your instructions.

"YourSectionName": [
    {
        "id": 1,
        "instruction": "",
        "Code": {
            "Name": "",
            "Description": "",
            "Language": "Command",
            "FormatCode": "",
            "CopyCode": ""
        }
    },
],

3. Now scroll down to the "Text" attribute. Under the last item in the list add the following JSON object. Your "Title" attribute should probably be the same as your "name" attribute in step 1 or at least similar.

```
{
    "title": "This is My New Section",
    "desc": "Describe what the instructions do."
}
```

4. Find the index of the new item in the list by running the following commands. Copy and record the index that's output.

```
cd top-bar
python3 python/find_index.py
```

5. Now go to GitHub.vue, above \"const text\" paste the following code. Replace YourSectionName with the value from step 2.

```
const yourSectionName = jsonData.value["YourSectionName"];
```

6. Now below "const AmotionsWorkflow" variable (or latest instruction variable) and paste the following code. Replace NewSectionRefName with the value of the "ref" attribute from step 1.

```
const NewSectionRefName = ref(null);
```

7. Now in the "const refs" array paste the name of the variable from step 6 below the "AmotionsWorkflow," variable or whatever the latest added section was.

```
NewSectionRefName,
```

8. Now scroll up to the "template" section. Right above the last &lt;p&gt; tag with the class "scroll-up-btn" paste the following code. Replace NEW_SECTION_REF with the value of the "ref" attribute from step 1. Replace the YOUR_INDEX variables with the value you copied in step 4. Replace YOUR_SECTION_NAME with the name of your variable from step 5.

```
<span class="scroll-up-link" v-html="processedTipContent(text[20].scrollToLinks)"></span>

<!-- Your Section Name  -->
<h2 class="gh-header-two" ref="NEW_SECTION_REF">{{ text[YOUR_INDEX].title }}</h2>
<p class="description-two">{{ text[YOUR_INDEX].desc }}</p>

<div v-for="point in YOUR_SECTION_NAME" :key="point.id">
    <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
        </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
    <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
</div>
```

9. Run your site, open it, then go to the Github page. Make sure your scroll link is working as expected.

```
cd top-bar
npm run dev

* Look up "Github" and test your scroll link *
```

10. Fill in your instructions in GitHub.json














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



**Other links**

```
http://localhost:5173/WhatIsThis
```

```
http://localhost:5173/FormatCode
```

## Topics Covered 
 - AWS 
 - Rest APIs 
 - Git
 - Flask, Spring Boot
 - Other CS Topics