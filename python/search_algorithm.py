import json

def load_data():
    with open("delete.json", "r") as file:
        content = json.load(file)
        return content

def highlight_string(text, search_string):
    idx = 0
    highlighted_text = ''
    search_length = len(search_string)
    lower_text = text.lower()
    lower_search_string = search_string.lower()
    count = 0 
    
    while idx < len(text):
        next_find = lower_text.find(lower_search_string, idx)
        if next_find == -1:
            highlighted_text += text[idx:]
            break
        highlighted_text += text[idx:next_find] + '**' + text[next_find:next_find + search_length] + '**'
        idx = next_find + search_length
        count += 1 
    
    return highlighted_text, count

def search_in_results(results, search_string):
    matched_results = []
    total_highlight_count = 0 
    if results is None:
        return matched_results, total_highlight_count 
    for result in results:
        for key, value in result.items():
            if isinstance(value, str) and search_string.lower() in value.lower():
                highlighted_text, count = highlight_string(value, search_string)
                matched_results.append(highlighted_text)
                total_highlight_count += count
            elif isinstance(value, (int, float)) and search_string.isdigit():
                if search_string == str(value):
                    matched_results.append('**' + str(value) + '**')
                    total_highlight_count += 1
    return matched_results, total_highlight_count

def search_json(data, search_string):
    total_count = 0
    for item in data:
        results = item.get('Results', []) 
        matched_results, highlight_count = search_in_results(results, search_string)
        if matched_results:
            print(f"\n\nTitle: {item['Title']}")
            print(f"Link: {item['Link']}")
            for result in matched_results:
                print(f"• {result}")
            total_count += highlight_count
    print(f"\nTotal number of highlighted occurrences: {total_count}")

data = load_data()

search_string = input("Enter search term: ")
search_json(data, search_string)
