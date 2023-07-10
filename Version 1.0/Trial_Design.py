import random

def generate_range_overlap(increments):
        sequence = [0]
        for i in range(1, 9):
            sequence.append(sequence[len(sequence)-1] + increments)
        return sequence
    

def compile_trial_structure(increments, n_blocks):
    import random
    
    trial_dict = {}
    
    def generate_range_location():
        positions = []
        while len(positions) < 18:
            if len(positions) < 9:
                positions.append("left")
            else:
                positions.append("right")
        return positions
    
    
    for n in range(0, n_blocks):
        positions = generate_range_location()
        range_overlap_left = generate_range_overlap(increments)
        range_overlap_right = generate_range_overlap(increments)
        for i in range(1 + ((9*2)*n), 19 + ((9*2)*n)):
            location = random.choice(positions)
            positions.remove(location)
            if location == "left":
                overlap = random.choice(range_overlap_left)
                range_overlap_left.remove(overlap)
            if location == "right":
                overlap = random.choice(range_overlap_right)
                range_overlap_right.remove(overlap)
            trial_dict[i] = {"overlap": overlap, "location": location}
    
    return trial_dict


def compile_practice_trials(increments):
    
    dictionary_practice_trials = {}
    
    overlap_practice_trials_l = generate_range_overlap(increments)
    overlap_practice_trials_r = generate_range_overlap(increments)

    for x in range(0, 18):
        if len(dictionary_practice_trials) < 9:
            overlap = random.choice(overlap_practice_trials_l)
            dictionary_practice_trials[x] = {"overlap": overlap, "location": "left"}
            overlap_practice_trials_l.remove(overlap)
        else:
            overlap = random.choice(overlap_practice_trials_r)
            dictionary_practice_trials[x] = {"overlap": overlap, "location": "right"}
            overlap_practice_trials_r.remove(overlap)
            
    return dictionary_practice_trials


def generate_angles_test(n_angles):
    
    angles = []
    
    while len(angles) < n_angles:
        new_angle = random.randint(0, 360)
        if new_angle not in angles:
            angles.append(new_angle)
    
    return angles


def generate_angles_adaptation(n_angles):
    
    angles = []
    
    while len(angles) < n_angles:
        new_angle = random.randint(-360, 360)
        if new_angle not in angles:
            angles.append(new_angle)
            
    return angles


def generate_angles_top_up(n_angles_post, n_angles_top_up):
    
    angles = []

    while len(angles) < n_angles_post * n_angles_top_up:
        new_angle = random.randint(0, 360)
        angles.append(new_angle)
        
    return angles
