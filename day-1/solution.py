
try:
    FILE = open('./data/day-1/data.txt', 'r')
except:
    raise FileNotFoundError("Advent of Code Day 1 Data Not Found")

# helper for getting tuple of direction and turn amt
def extract_turn(line):
    return (line[0], int(line[1:]))

# helper for computing new position given start, distance, and direction
def compute_position(start, distance, direction):
    if direction == 'R':
        return (start + distance) % 100
    elif direction == 'L':
        return (start - distance) % 100
    else:
        raise ValueError("Invalid direction")

def compute_password():
    dial = 50
    total = 0
    clean_data = [line.strip() for line in FILE.readlines()]
    for turn in clean_data:
        turn_tuple = extract_turn(turn)
        new_pos = compute_position(dial, turn_tuple[1], turn_tuple[0])
        if new_pos == 0:
            total += 1
        dial = new_pos
    return total
        
            

def main():
    password = compute_password()
    print(f'The password is {password}!')

if __name__ == "__main__":
    main()