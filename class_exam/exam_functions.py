
def list_from_file(self, file_name):
    user_list = []
    try:
        for line in open(file_name, 'r'):
            person = line.strip('\n')
            self.user_list.append(person)
    except IOError:
        return "You're in the wrong directory."
    return user_list


class ClassList:

    def __init__(self, my_list):
        self.user_list = my_list

    def read_list(self):
        user_name = raw_input("Enter your name: ")
        if user_name in self.user_list:
            print "You're on the list."
            return user_name, True
        else:
            print "You're not on the list, %s" % user_name
            return user_name, False

    def rearrange_list(self, u_name):
        """

        @param u_name: Name of person to bring to front of list
        @param u_list: List of people
        @return: Rearranged list of people with u_name in front
        """
        i = self.user_list.index(u_name)
        self.user_list.insert(0, self.user_list.pop(i))
        return self.user_list

    def modify_list(self):
        u_input = raw_input("Would you like to add or remove a user? ").lower()
        if u_input == "add":
            n_input = raw_input("Enter a name to add: ")
            self.user_list.append(n_input)
        elif u_input == "remove":
            try:
                n_input = raw_input("Enter a name to remove: ")
                self.user_list.remove(n_input)
            except ValueError:
                return "Specified user did not exist!"
        else:
            return "Invalid command, please type 'add' or 'remove'"
        return self.user_list