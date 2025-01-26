def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return (file_contents)

def change_to_string(text):
     words = text.split()
     count = len(words)
     print (count)

def count_characters(text):
    lowered_text = text.lower()
    count_all={}  
    for character in lowered_text:
        if character in count_all:
            count_all[character] += 1
        else:
            count_all[character] = 1
    print (count_all)
        
    
  
text = main()
change_to_string(text)
count_characters(text)


