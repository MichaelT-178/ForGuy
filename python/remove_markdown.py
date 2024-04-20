import json
import re

class RemoveMarkdown:

    def __init__(self, content):
        self.content = content

        self.hyperlink = r'\[([^\]]+)\]\((https?:\/\/[^\s]+)\)'
        self.routerlink = r'\(([^)]+)\)\[([^\s]+)\]'
        self.routerlink_props = r'@([^@]+)@\[\s*({.*?})\s*\]'
        self.download_link = r'\&([^\]]+)\&\((https?:\/\/[^\s]+)\)'
        self.scroll_link = r'(Different for multiple accounts|Scroll back up to original step|Scroll back to links|Scroll down)\((.*?)\)'


    def undo_all_links(self):
        for item in self.content:
            for idx, result in enumerate(item["Results"]):
                for key, value in result.items():

                    t, new_text = self.undo_link(value, self.hyperlink)
                    t, new_text = self.undo_link(new_text, self.routerlink)
                    t, new_text = self.undo_link(new_text, self.routerlink_props)
                    t, new_text = self.undo_link(new_text, self.download_link)
                    t, new_text = self.undo_link(new_text, self.scroll_link)

                    item["Results"][idx][key] = new_text

        return self.content

    def undo_link(self, text, markdown_pattern):
        if isinstance(text, int):
            return False, text
        
        match = re.search(markdown_pattern, text)

        cleaned_text = re.sub(markdown_pattern, r'\1', text)

        return match is not None, cleaned_text
    





