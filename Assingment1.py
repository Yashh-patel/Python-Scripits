#assingment 1 
# yash patel(200583043)  
# in the first step here taking input as a file inorder to read file ,so here i just take a file input 
def reading_afile(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    return data
#in the second step here using methods of strings inorder to remove everything to convert into list so i can directly count words using if ,else logic
def numbering_of_lines(text):
    counting_words = {}
    for word in text.split():
        word = word.lower()
        if word in counting_words:
            counting_words[word] += 1
        else:
            counting_words[word] = 1
    return counting_words
#saving files using function with arguments , as a arguments i take above funtion name like reading_afile and numbring of line as parameters
def save_file(counting_words, report_file):
    with open(report_file, 'w') as fileOpen:
        fileOpen.write("Word     Frequency\n")
        for word, count in counting_words.items():
            fileOpen.write(f"{word.ljust(10)}|    {count}\n")
    print("samplereport.txt is created.")

# using main function to call every thing order to complete this and step by step every function will doing his work like in the first take input ,
#then convert in to list and remove commas and then counting words and at the end saving report to get proper output as per requirements 

def main():
    file_name = "sample.txt"  
    report_file = "samplereport.txt"  

    text = reading_afile(file_name)
    counting_words = numbering_of_lines(text) 
    save_file(counting_words, report_file)

if __name__ == "__main__":
    main()
