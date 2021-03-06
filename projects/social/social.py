
import random 
import collections
import time 
# from random import randit 
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False 
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True 

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users

        # hint 1: to create n random friendships, 
        # you could create a list with all possible friendship combos 

        # num_users = 5 
        friendship_combinations = []

        # On^2
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendship_combinations.append((user, friend))

        self.fisher_yates_shuffle(friendship_combinations)

        # take as many
        # then grab the first N elements from the list 
        total_friendships = num_users * avg_friendships

        friends_to_make = friendship_combinations[:(total_friendships // 2) ]
         # Create friendships
        for friendship in friends_to_make:
            self.add_friendship(friendship[0], friendship[1])

    # hash the user name or something 
    # if you are in the same bucket of the hash table, you are friends

    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0 
        self.users = {}
        self.friendships = {} 

        for user in range(num_users):
            self.add_user(user)

        total_friendships = num_users * avg_friendships
        friendships_made = 0 


        while friendships_made < total_friendships:
            user = random.randint(1, self.last_id)
            friend = random.randint(1, self.last_id)

            was_friendships_made = self.add_friendship(user, friend)

            if was_friendships_made:
                friendships_made += 1
       

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # # !!!! IMPLEMENT ME

        # path_queue = collections.deque()

        # path_queue.append([user_id])

        # while len(path_queue) > 0:
        #     path = path_queue.popleft()

        #     friend_id = path[-1]
        #     if friend_id in visited: 
        #         continue 

        #     visited[friend_id] = path 


        #     for id in self.friendships[friend_id]:
        #         new_path = path.copy()
        #         new_path.append(id)
        #         path_queue.append(new_path)

        # friend_coverage = (len(visited) - 1) / (len(self.users) -1 )

        # total_length = 0

        # for path in visited.values():
        #     total_length += len(path) - 1

        # if len(visited) > 1: 
        #     avg_separation = total_length / (len(visited) -1)
        # else: 
        #     print("no friends")
        # return visited
        # Tims
        visited = {}

        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0: 
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node not in visited:
                visited[current_node] = current_path 
                friends = self.friendships[current_node]

                for friend in friends: 
                    friend_path = current_path.copy()
                    friend_path.append(friend)

                    q.enqueue(friend_path)

            
        return visited 


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(10, 2)
    start_time = time.time()
    sg.populate_graph(1000, 50)
    end_time = time.time()

    print(end_time - start_time)



    start_time = time.time()
    sg.populate_graph_linear(1000, 50)
    end_time = time.time()
    print(end_time - start_time)
    connections = sg.get_all_social_paths(1)

    # percentage of users in this user's extended social network 
    print("percebtage of users in this user's social network:" , len(connections)/ 1000 * 100) 

    # average  degree of separation 
    # aka how many people do i need to introduce ? 
    total = 0
    for path in connections.values():
        total += len(path)
    average = total / len(connections)

    print("average degree of separation: ", average)