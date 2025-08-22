import os #importing to check file existence

def similar_head(read_file,number_of_lines,write_to_file):
    """
    Reads a specified number of non-empty lines from a file and either prints them
    or writes them to another file.
    """
  if not os.path.exists(read_file):
    print("The file {read_file} doesn't exist")
    return False
  
  reader = open(read_file,'r')
  
  if not write_to_file:
    lines_read = 0
    while lines_read < number_of_lines:
      line=reader.readline()
      if not line:
        break #signifies end of file
      if line.strip():
        print(line.strip())
        lines_read+=1

    reader.close()
    return True
  
  else:
    writer=open(write_to_file,'w')
    lines_read=0
    while lines_read < number_of_lines:
      line=reader.readline()
      if not line:
        break
      if line.strip():
        writer.write(line)
        lines_read+=1

    writer.close()
    reader.close()
    return True

def main():
  print("Name of the fie to be read: en_paragraph_7.txt\n")
  read_file="en_paragraph_7.txt"

  number_of_lines_str=input("Enter the desired number of lines to be read:\n")
  
  if not number_of_lines_str.isdigit():
    print("Invalid input. Please enter a valid integer number.")
    return
  
  number_of_lines=int(number_of_lines_str)
  
  write_to_file = input("Name of the file where the lines will be written to. Leave this blank to print to the console:\n")
  
  similar_head(read_file,number_of_lines,write_to_file)

main()
