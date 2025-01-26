def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return (file_contents)

def change_to_string(text):
     words = text.split()
     count = len(words)
     print (count)


    
text = main()
change_to_string(text)


