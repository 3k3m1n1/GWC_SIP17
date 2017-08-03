class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def getUserName(self):
        return self.user_name

    def getUserId(self):
        return self.user_id

    def getConnections(self):
        return self.connections

    def addConnection(self, other_user_name):
        self.connections.append(other_user_name)
        # not mutual (run it twice)

class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        return len(self.users)

    def getUserId(self, user_name):
        for index in range(len(self.users)):
            possible_user = self.users[index]
            if (possible_user.getUserName() == user_name):
                return possible_user.getUserId()
        return -1

    def addUser(self):
        new_user_name = input("Create a new username: ")
        new_user_id = len(self.users)
        new_user = User(new_user_name, new_user_id)
        self.users.append(new_user)
        print("User created!")

    def addConnection(self, user_name1, user_name2):
        user_id_1 = self.getUserId(user_name1)
        user_id_2 = self.getUserId(user_name2)
        if (user_id_1 == -1 or user_id_2 == -1):
            print("ERROR: One of these users do not exist in the network.")
        else:
            user1 = self.users[user_id_1]
            user2 = self.users[user_id_2]
            user1.addConnection(user_name2)
            user2.addConnection(user_name1)
            print("Connection added!")
            # mutual friends (appends one user to the other's list of connections, and vice versa)

    def getUserNames(self):
        print("All network users:")
        for index in range(len(self.users)):
            each_user = self.users[index] # only gets their position in the list
            print(each_user.getUserName())

    def getAllConnections(self):
        for index in range(len(self.users)):
            current_user = self.users[index]
            print("\n" + current_user.getUserName() + "'s connections:")

            if (len(current_user.connections) == 0):
                print("Sorry, this friends list is empty!")
            else:
                for i in range(len(current_user.connections)):
                    friends = current_user.connections[i]
                    print(friends)

def main():
    # appnexus_employee = User("AppNexus", 12)
    # print("Welcome, " + appnexus_employee.getUserName() + "!")

    net = Network()

    print("\n** This is a test run of all functions included in the code! **\n")
    print("TEST: Add 3 users.\n")
    net.addUser()
    net.addUser()
    net.addUser()

    print("\nTEST: Printing users below...\n")
    net.numUsers() # returns don't show up in main(), but this line IS working
    net.getUserNames()

    any_user = input("\nTEST: Get a user's ID by typing their username here: ")
    net.getUserId(any_user) # it works!
    print("(This function uses a 'return', so the output isn't going to print. Don't panic!)")

    print("\nTEST: Pair two users.")
    person1 = input("Type user 1's name here: ")
    person2 = input("Type user 2's name here: ")
    net.addConnection(person1, person2)

    print("\nTEST: Pair another two users.")
    person1 = input("Type user 1's name here: ")
    person2 = input("Type user 2's name here: ")
    net.addConnection(person1, person2)

    print("\nTEST: Listing all network connections below...")
    net.getAllConnections()

    print("\n** Test run complete! **")

if __name__ == "__main__":
    main()
# If we call the file from Terminal, run main method
