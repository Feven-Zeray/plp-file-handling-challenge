def main():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Open the file for reading
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified file saved as {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read or written.")

if __name__ == "__main__":
    main()
