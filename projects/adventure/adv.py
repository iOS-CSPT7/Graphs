from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import collections 

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
player.current_room = world.starting_room
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
room_map = {} 

default_direction = 's'

change_direction = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
direct_inverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

def add_room_to_map(room):
    if room not in room_map:
        room_map[room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}
        exits = room.get_exits()
        for direction in room_map[room]:
            if direction not in exits: 
                room_map[room][direction] = 'NONE'
        return True
    else: 
        return False 

def add_relation_to_map(starting_room, direction, ending_room):
    room_map[starting_room][direction] = ending_room
    room_map[ending_room][direct_inverse_direction[direction]] = starting_room
    # building relationships to the inverse 

def path_to_unexplored_exits(starting_room):
    visited = set()
    path_queue = collections.deque()

    path_queue.append((starting_room, []))

    while len(path_queue) > 0:
        room, path = path_queue.popleft()

        if room in visited:
            continue 
        else: 
            visited.add(room)

        for exit_direction in room_map[room]:
            if room_map[room][exit_direction] == '?':
                return path 

            elif room_map[room][exit_direction] != 'NONE':
                new_path = path.copy()
                new_path.append(exit_direction)
                new_room = room_map[room][exit_direction]
                path_queue.append((new_room, new_path))
    return [] 

add_room_to_map(player.current_room) 

while len(room_map) < len(room_graph):
    room = player.current_room
    exits = room.get_exits()

    unexplored_exit = False 

    direction = default_direction

    for _ in range(len(change_direction)): 
        if room_map[room][direction] == '?' and direction in exits: 
            unexplored_exit = True 

            player.travel(direction)
            next_room = player.current_room
            traversal_path.append(direction)

            if not add_room_to_map(next_room): 
                player.travel(direct_inverse_direction[direction])
                traversal_path.pop()
            # if visited, go back , take off path to move elsewhere 
        
            add_relation_to_map(room, direction, next_room)
            break
        else: 
            direction = change_direction[direction]
    if not unexplored_exit: 
        path = path_to_unexplored_exits(room)

        traversal_path.extend(path) 
        for direction in path: 
            player.travel(direction)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
