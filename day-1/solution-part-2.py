
try:
    FILE = open('./data/day-1/data.txt', 'r')
except:
    raise FileNotFoundError("Advent of Code Day 1 Data Not Found")

# helper for getting tuple of direction and turn amt
def extract_turn(line):
    return (line[0], int(line[1:]))

# helper for computing new position given start, distance, and direction
def compute_position_with_cycles(start, distance, direction):
    pos = start
    cycles = 0

    step = 1 if direction == 'R' else -1

    for _ in range(distance):
        pos = (pos + step) % 100
        if pos == 0:
            cycles += 1

    return pos, cycles

def crosses_boundary(start, distance, direction):
    if direction == 'L':
        return True if distance > start else False
    elif direction == 'R':
        return True if (distance + start) > 100 else False
    else:
        raise ValueError("Invalid direction")
    
def compute_password():
    dial = 50
    total = 0
    clean_data = [line.strip() for line in FILE.readlines()]
    for turn in clean_data:
        turn_tuple = extract_turn(turn)
        new_pos, cycles = compute_position_with_cycles(dial, turn_tuple[1], turn_tuple[0])
        dial = new_pos
        total += cycles
    return total
        
            

def main():
    password = compute_password()
    print(f'The password is {password}!')

if __name__ == "__main__":
    main()