def get_cats_info(path):
    try:
        with open(path, 'r',encoding='utf-8') as fh:
             cats = []
             for line in fh:
               if line.strip():
                id, name, age = line.strip().split(',')
                cats.append({"id": id, "name": name, "age": age})
             return cats
    except FileNotFoundError:
        print("File not found")
        return []
    
cats_info = get_cats_info("cats_file.txt")
print(cats_info)