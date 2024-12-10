
class ListManager: 
    def __init__(self): 
        self.elements = [] 
    def append_element(self, element): 
        """Append an element to the list.""" 
        self.elements.append(element) 
        print(f"{element} has been added to the list.") 
    def delete_element(self, element): 
        """Delete an element from the list if it exists.""" 
        if element in self.elements: 
            self.elements.remove(element) 
            print(f"{element} has been removed from the list.") 
        else: 
            print(f"{element} is not in the list.") 
    def display_elements(self): 
        """Display all elements in the list.""" 
        if self.elements: 
            print("Current elements in the list:", self.elements) 
        else: 
            print("The list is currently empty.") 
# Menu-driven interface 
def menu(): 
    list_manager = ListManager() 
    while True: 
        print("\nMenu:") 
        print("1. Append an element") 
        print("2. Delete an element") 
        print("3. Display elements") 
        print("4. Exit") 
        choice = input("Enter your choice (1-4): ") 
        if choice == '1': 
            element = input("Enter an element to append: ") 
            list_manager.append_element(element) 
        elif choice == '2': 
            element = input("Enter an element to delete: ") 
            list_manager.delete_element(element) 
        elif choice == '3': 
            list_manager.display_elements() 
        elif choice == '4': 
            print("Exiting the program.") 
            break 
        else: 
            print("Invalid choice! Please enter a number between 1 and 4.") 
# Run the menu 
menu() 
