def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return (file_contents)

def change_to_string(text):
     words = text.split()
     count = len(words)
     return count 

def count_characters(text, count):
    lowered_text = text.lower()
    count_all={}  
    for character in lowered_text:
        if character in count_all:
            count_all[character] += 1
        else:
            count_all[character] = 1
    
    # Create the report list    
    report_list = []
    for key in count_all:
        report_dic = {"name": key, "num": count_all[key]}
        report_list.append(report_dic)

    # Filter only alphabetic characters
    alp_report_list = []
    for char_entry in report_list:
        if char_entry["name"].isalpha():
            alp_report_list.append(char_entry)
   
    # Sort the list by character count in descending order
    alp_report_list.sort(key=lambda x: x["num"], reverse = True)
    
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()

    for entry in alp_report_list:
        print(f"The '{entry['name']}' character was found {entry['num']} times")
    
    print("--- End report ---")
    
 
text = main()
count = change_to_string(text)
count_characters(text, count)


