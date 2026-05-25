import json
import pandas as pd
import os


class FewShorts:
    def __init__(self, file_path=None):

        self.df = None
        self.unique_tags = None

        if file_path is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            file_path = os.path.join(
                current_dir,
                "Data",
                "processed_posts.json"
            )

        self.load_post(file_path)

    def load_post(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            posts = json.load(file)
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.length)
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = set(all_tags)
            

    def length(self, line_count):
        if line_count <= 8:
            return "Short"
        elif 9 <= line_count <= 16:
            return "Medium"
        else:
            return "Long"
        
    def get_unique_tags(self):
        return self.unique_tags  

    def get_filtered_posts(self, length, language, tag):
        filtered_list = self.df [
        (self.df["length"] == length) &
        (self.df["language"] == language) &
        (self.df["tags"].apply(lambda x: tag in x))
    ]
        return filtered_list.to_dict(orient="records")
        
         

if __name__ == "__main__":    
    fs = FewShorts()
    posts = fs.get_filtered_posts("Medium","English","Fiction")  
    print(posts)         