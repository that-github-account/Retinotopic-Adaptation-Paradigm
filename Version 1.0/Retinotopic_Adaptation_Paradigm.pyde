
#Packages
import random
import Trial_Design

#Settings ---------------------------------------------------------------------------------------------------------------------------
WindowX = 1920
WindowY = 1080

speed = 20
example_speed = 2.5 #speed for the examples animations playable in the instructions
fixation_cross_speed_adjust = 0.1 #must be multiple of 10 as based on visual degree calculations

visual_degree_disc_size = 1.5 #in visual degree
fixation_cross_size = 10 #

visual_degree_fixation_location = 5 #in visual degree
distance_from_screen = 500 #in mm

n_angles_pre = 2 #traditionally 180, current possible max is 360
n_angles_post = 1 #traditionally 180, current possible max is 360
n_angles_adaptation = 1 #traditionally 640, current max is 720
n_angles_practice = 1 #total 18
n_angles_top_up = 16 #traditionally 16, number of top up angles per angle post test

increments_overlap = 0.125 #the difference in overlap between discs
n_blocks = 1 #number of blocks to run, one block traditionally contains 9 levels of overlap for both location (18 trials total), traditionally 10 blocks

position_left = "left"
position_right = "right"

adaptation_sequence_intertrial_delay = 100

autostart = False
sequence = ""
repositioned = False
next = False
require_response_switch = True


#Setting up functions ---------------------------------------------------------------------------------------------------------------
from Collision_Animations import Collision
from Fixation_Cross import Fixation_Dot
from Response_Log import Responses
from Text_Files import Text

#Visual Degree Conversion -----------------------------------------------------------------------------------------------------------
screen_horizontal_ratio = 1920/509.76 #pixels per mm
screen_vertical_ratio = 1080/286.74 #pixels per mm

visual_degree_fixation_location_in_radian = radians(visual_degree_fixation_location)
visual_degree_disc_size_in_radian = radians(visual_degree_disc_size)

screen_size_of_fixation_location = tan(visual_degree_fixation_location_in_radian)*distance_from_screen
screen_size_of_disc_size = tan(visual_degree_disc_size_in_radian)*distance_from_screen

fixation_location_in_pixels = round(screen_size_of_fixation_location*screen_horizontal_ratio, 2)
disc_size_in_pixels = round(screen_size_of_disc_size*screen_horizontal_ratio, 2) #note that the disc needs to be defined along the X and Y axis but as we are displaying a circle both ratios would return the same size

#Speeds  ----------------------------------------------------------------------------------------------------------------------------
fixation_cross_speed = fixation_location_in_pixels*fixation_cross_speed_adjust
#print("fixation cross speed in pixels", fixation_cross_speed)

#Compiling Data Structure and Trial Lists  ------------------------------------------------------------------------------------------
trial_dict_pre = Trial_Design.compile_trial_structure(increments_overlap, n_blocks)

trial_dict_post = Trial_Design.compile_trial_structure(increments_overlap, n_blocks)

dictionary_practice_trials = Trial_Design.compile_practice_trials(increments_overlap)


angles_pre_adaptation = Trial_Design.generate_angles_test(n_angles_pre)
angles_post_adaptation = Trial_Design.generate_angles_test(n_angles_post)

angles_adaptation = Trial_Design.generate_angles_adaptation(n_angles_adaptation)

angles_top_up = Trial_Design.generate_angles_top_up(n_angles_post, n_angles_top_up)
                        

initial_fixation = random.randint(0, 1)

if initial_fixation == 0:
    trial_fixation = "left"
    adaptation_fixation = "right"
else:
    trial_fixation = "right"
    adaptation_fixation = "left"

#Defining Functions  ----------------------------------------------------------------------------------------------------------------
Collision = Collision(0, 100, disc_size_in_pixels, WindowX, WindowY, fixation_location_in_pixels)
fixation_dot = Fixation_Dot(WindowX, WindowY, fixation_location_in_pixels, fixation_cross_size, fixation_cross_speed)
response_request = Responses(WindowX, WindowY)
txt = Text(WindowX, WindowY)


#Defining additional variables  -----------------------------------------------------------------------------------------------------
delaysequence = 0
value = 0
timeinms = 0

practice_counter = []
practice_time = 0

count_for_top_up = n_angles_top_up

example_intro = "none"

example_counter = {"LAUNCH": 0, "PASS": 0}


#Checks ----------------------------------------------------------------------------------------------------------------------------
print("Practice Trials " + str(len(dictionary_practice_trials)))
print("Pre-Adaptation Trials " + str(len(trial_dict_pre)))
print("Post-Adaptation Trials " + str(len(trial_dict_post)))
print("Angles pre " + str(len(angles_pre_adaptation)))
print("Angles post " + str(len(angles_post_adaptation)))
print("Angles adaptation " + str(len(angles_adaptation)))
print("Angles top_up " + str(len(angles_top_up)/16))

if  len(trial_dict_pre) < len(angles_pre_adaptation) or len(trial_dict_post) < len(angles_post_adaptation):
    print("There are not enough angles specified to run all trials.")
    exit()


def setup():
    fullScreen()
    frameRate(60)
    
def draw():
    background(0)

    #Settings
    show_FPS = False
    display_grid = False
    check_display_circularity = False
    display_visualdegree = False
    check_animation_time = False
    
    test = False    
    
    WindowX = displayWidth
    WindowY = displayHeight
        
    #Global variables 
    global repositioned
    global next
    global autostart
    global sequence
    global require_response_switch
    global visualdegree
    global delaysequence
    global value
    global timeinms
    global begin_practice_trials
    global count_for_top_up
    global example_intro
    global adaptation_sequence_intertrial_delay
    global example_speed
    global n_angles_practice
    global n_angles_top_up
    global example_counter


    if autostart == False:
        
        if keyPressed: 
            if key == ' ':
                autostart = True
                sequence = "Introduction"
                delay(1000)
                
            if key == TAB:
                delay(1000)
        else:
            txt.start_message_display()
            
    else:
        
        
##------Introduction 

        if sequence == "Introduction":
            
            if keyPressed:
                if key == "d":
                    example_intro = "launch"
                    delaysequence = "wait"
                    timeinms = millis()
                    
                if key == "k":
                    example_intro = "pass"
                    delaysequence = "wait"
                    timeinms = millis()
                
                if key == ' ':
                    sequence = "starting practice"
                    timeinms = millis()

                    
            if example_intro == "launch":
                
                txt.example_instructions_header()
                txt.example_launch()
                
                if delaysequence == "wait":
                    
                    if millis() - timeinms < 500:
                        background(0)
                        txt.example_instructions_header()
                        txt.example_launch()
                    else:
                        delaysequence = 0
                else:
                    
                    if repositioned == False:
                        
                        fixation_dot.refixate(adaptation_fixation)
                        
                        Collision.reposition(fixation_dot.xpos, "override; adaptation", fixation_dot.ypos, 45, 0, 1)
                        
                        example_counter["PASS"] = example_counter["PASS"] + 1
                        
                        repositioned = True
                            
                    else:
                            
                        if repositioned == True:
    
                            Collision.single_iteration(example_speed)
                            
                            if Collision.iterations == 0:
                                
                                repositioned = False
                                example_intro = "wait"
                                timeinms = millis()
                            
            if example_intro == "pass":
                
                txt.example_instructions_header()
                txt.example_pass()
                
                if delaysequence == "wait":
                    
                    if millis() - timeinms < 500:
                        background(0)
                        txt.example_instructions_header()
                        txt.example_pass()
                    else:
                        delaysequence = 0
                else:
                    
                    if repositioned == False:
                        
                        fixation_dot.refixate(adaptation_fixation)
                        
                        Collision.reposition(fixation_dot.xpos, "override; adaptation", fixation_dot.ypos, 45, 1, 1)
                        
                        example_counter["LAUNCH"] = example_counter["LAUNCH"] + 1
                        
                        repositioned = True
                            
                    else:
                            
                        if repositioned == True:
    
                            Collision.single_iteration(example_speed)
                            
                            if Collision.iterations == 0:
                                
                                repositioned = False
                                example_intro = "wait"
                                timeinms = millis()
                            
            if example_intro == "wait":
                    
                if millis() - timeinms < 500:
                    background(0)
                    txt.example_instructions_header()
                else:
                    example_intro = "none"
                            
            if example_intro == "none":
                txt.main_instructions_display()        
        
        
        
        
        
##------Practice
        
        if sequence == "starting practice":
            if keyPressed and millis() - timeinms > 500:
                if key == ' ':
                    sequence = "Practice"
                    delaysequence = "wait"
                    timeinms = millis()
            else:
                txt.practice_instructions_display()
        
        if sequence == "Practice":
            
            fixation_dot.refixate(trial_fixation)
            fixation_dot.display()
            
            if delaysequence == "wait":
            
                if millis() - timeinms < 1500:
                    fixation_dot.refixate(trial_fixation)
                    fixation_dot.display()
                else:
                    delaysequence = 0
                    
                    repositioned = False
            
            else:
                
                
                if repositioned == False:
                    
                    number_of_trial = random.choice(list(dictionary_practice_trials.keys()))
                    dict_of_trial = dictionary_practice_trials.get(number_of_trial)
                    dictionary_practice_trials.pop(number_of_trial)
        
                    overlap = dict_of_trial["overlap"]
                    location = dict_of_trial["location"]
                        
                    Collision.reposition(fixation_dot.xpos, location, fixation_dot.ypos, 45, overlap, 1)
                    
                    repositioned = True
                        
                else:
                        
                    if repositioned == True and response_request.awaiting_response == False:

                        Collision.single_iteration(speed)
                        
                        if Collision.iterations == 0:
                            
                            response_request.awaiting_response = True
                            
                    else:
                        if response_request.awaiting_response == True:
                            
                            response_request.get_response_practice(fixation_dot.xpos, fixation_dot.ypos)
                            
                            
                            if response_request.awaiting_response == False:
                                
                                delaysequence = "wait"
                                timeinms = millis()
                                
                                if len(dictionary_practice_trials) == 18 - n_angles_practice:
                                    sequence = "starting main exp"
                                    print("The time of the practice trials was " + str(millis()))
                                    
                
                
                
                
                
                
##------PRE-ADAPTATION                   
                
        if sequence == "starting main exp":
            
            if keyPressed:
                if key == ' ':
                    sequence = "Pre-Adaptation"
                    delaysequence = "wait"
                    timeinms = millis()
            else:
                txt.pre_adaptation_trials_instructions_display()
            
        if sequence == "Pre-Adaptation":
            
            fixation_dot.refixate(trial_fixation)
            fixation_dot.display()
        
            if delaysequence == "wait":
            
                if millis() - timeinms < 1500:
                    fixation_dot.refixate(trial_fixation)
                    fixation_dot.display()
                else:
                    delaysequence = 0
                    repositioned = False
            
            else:
        
                if repositioned == False:
                    
                    number_of_trial = list(trial_dict_pre.keys())[0]
                    trial_dict_entry = trial_dict_pre.get(number_of_trial)
                    trial_dict_pre.pop(number_of_trial)

                    overlap = trial_dict_entry["overlap"]
                    location = trial_dict_entry["location"]
                        
                    Collision.reposition(fixation_dot.xpos, location, fixation_dot.ypos, random.choice(angles_pre_adaptation), overlap, 1)
                    angles_pre_adaptation.remove(Collision.angle)
                    
                    repositioned = True
                    
                else:
                        
                    if repositioned == True and response_request.awaiting_response == False:

                        Collision.single_iteration(speed)
                        
                        if Collision.iterations == 0:
                            
                            response_request.awaiting_response = True 
                    
                    else:
                                                    
                        if response_request.awaiting_response == True:
                            
                            if Collision.sfrl == trial_fixation:
                                response_request.get_response_test(Collision.overlap, "retinotopic", fixation_dot.xpos, fixation_dot.ypos)
                            else:
                                response_request.get_response_test(Collision.overlap, "spatiotopic", fixation_dot.xpos, fixation_dot.ypos)
                                
                            if response_request.awaiting_response == False:
                            
                                delaysequence = "wait"
                                timeinms = millis()
                                
                                if len(angles_pre_adaptation) == 0 and response_request.awaiting_response == False:
                                    sequence = "starting adaptation"
                                    fixation_dot.require_refixation = True
                                    repositioned = False
                                    
                                    print("The time of the pre-adaptation trials was " + str(millis()))
                            
                          
                                                
##------ADAPTATION                                
                                
        if sequence == "starting adaptation":
            
            if keyPressed:
                if key == ' ':
                    sequence = "Adaptation"
                    
                    delaysequence = "intermediate-fixation"
                    timeinms = millis()
                    
            else:
                txt.adaptation_instructions_display()
                        
        if sequence == "Adaptation":
            
            if delaysequence == "intermediate-fixation":
                
                if fixation_dot.require_refixation == True:
                    fixation_dot.move_fixation(adaptation_fixation)
                    fixation_dot.display()
                else:
                    fixation_dot.display()
                    
                    delaysequence = "wait"
                    timeinms = millis()
                    
            else:
                 
                fixation_dot.refixate(adaptation_fixation)
                fixation_dot.display() 
                 
                if delaysequence == "wait":
                
                    if millis() - timeinms < 1500:
                        fixation_dot.refixate(adaptation_fixation)
                        fixation_dot.display()
                    else:
                        delaysequence = 0
                else:
                    
                    if repositioned == False and delaysequence != "adaptation":
                        Collision.reposition(fixation_dot.xpos, "override; adaptation", fixation_dot.ypos, random.choice(angles_adaptation), 0, 1)
                        angles_adaptation.remove(Collision.angle)
                        
                        delaysequence = "adaptation"
                        timeinms = millis()
                        
                    if repositioned == False and delaysequence == "adaptation":
                        if millis() - timeinms < adaptation_sequence_intertrial_delay:
                            background(0)
                            fixation_dot.display()
                        else:
                            repositioned = True
                            delaysequence = 0
                        
                    if repositioned == True:
                        
                        Collision.single_iteration(speed)
                        
                        if Collision.iterations == 0:
                            
                            if len(angles_adaptation) == 0:

                                sequence = "starting post-adaptation"
                                fixation_dot.require_refixation = True
                                repositioned = False
                                
                                print("The time of the adaptation trials was " + str(millis()))
                            else:
                                repositioned = False
                                #print("Stimuli remaining in the sequence: " + str(len(angles_adaptation)))
                                
                                #KURZER DELAY HERE
                                                            
                                                            


##------POST-ADAPTATION                               
                            
        if sequence == "starting post-adaptation":
            
            if keyPressed:
                if key == ' ':
                    sequence = "Post-Adaptation"

                    delaysequence = "intermediate-fixation"
                    timeinms = millis()
            else:
                txt.post_adaptation_instructions_display()
        
        if sequence == "Post-Adaptation":

            if delaysequence == "intermediate-fixation":
                if fixation_dot.require_refixation == True:                
                    fixation_dot.move_fixation(trial_fixation)
                    fixation_dot.display()
                else:
                    fixation_dot.display()
                    
                    delaysequence = "wait"
                    timeinms = millis()
            
            else:
                fixation_dot.refixate(trial_fixation)
                fixation_dot.display()

                if delaysequence == "wait":
                    
                    if millis() - timeinms < 1500:
                        fixation_dot.refixate(trial_fixation)
                        fixation_dot.display()
                    else:
                        delaysequence = 0
                        repositioned = False
                
                else:

                    if repositioned == False:
                                            
                        number_of_trial = list(trial_dict_post.keys())[0]
                        trial_dict_entry = trial_dict_post.get(number_of_trial)
                        trial_dict_post.pop(number_of_trial)
            
                        overlap = trial_dict_entry["overlap"]
                        location = trial_dict_entry["location"]
                         
                        Collision.reposition(fixation_dot.xpos, location, fixation_dot.ypos, random.choice(angles_post_adaptation), overlap, 1)
                        angles_post_adaptation.remove(Collision.angle)
                        
                        repositioned = True
                    
                    else:
                        
                        if repositioned == True and response_request.awaiting_response == False:

                            Collision.single_iteration(speed)
                            
                            if Collision.iterations == 0:
                                
                                response_request.awaiting_response = True
                                    
                        else:
                            
                            if response_request.awaiting_response == True:
                                
                                if Collision.sfrl == trial_fixation:
                                    response_request.get_response_test(Collision.overlap, "retinotopic", fixation_dot.xpos, fixation_dot.ypos)
                                else:
                                    response_request.get_response_test(Collision.overlap, "spatiotopic", fixation_dot.xpos, fixation_dot.ypos)
                                    
                                if response_request.awaiting_response == False:
                                    
                                    #print("Trials remaining in the sequence " + str(len(angles_post_adaptation)))
                                    
                                    if len(angles_post_adaptation) == 0:
                                        sequence = "save responses"
                                        print("The time of the post-adaptation trials was " + str(millis()))
                                    else:
                                        repositioned = False
                                        
                                        fixation_dot.require_refixation = True
                                    
                                        delaysequence = "intermediate-fixation top-up"
                                        timeinms = millis()
                                        
                                        sequence = "top-up"
                                        

            
        if sequence == "top-up":
            
            if delaysequence == "intermediate-fixation top-up":
                
                if fixation_dot.require_refixation == True:
                    fixation_dot.move_fixation(adaptation_fixation)
                    fixation_dot.display()
                else:
                    fixation_dot.display()
                
                    delaysequence = "wait top-up"
                    timeinms = millis()
            else:
                
                fixation_dot.display()
                
                if delaysequence == "wait top-up":
                    
                    if millis() - timeinms < 1500:
                        fixation_dot.refixate(adaptation_fixation)
                        fixation_dot.display()
                    else:
                        delaysequence = 0
                        
                else:
                    if repositioned == False and delaysequence != "adaptation":
            
                        Collision.reposition(fixation_dot.xpos, "override; adaptation", fixation_dot.ypos, random.choice(angles_top_up), 0, 1)
                        angles_top_up.remove(Collision.angle)
                        
                        delaysequence = "adaptation"
                        timeinms = millis()
                        
                    if repositioned == False and delaysequence == "adaptation":
                        if millis() - timeinms < adaptation_sequence_intertrial_delay:
                            background(0)
                            fixation_dot.display()
                        else:
                            repositioned = True
                            delaysequence = 0
                        
                    if repositioned == True:
                        if repositioned == True:
                            
                            Collision.single_iteration(speed)
                            
                            if Collision.iterations == 0:
                                
                                if count_for_top_up == 1:
                                    
                                    delaysequence = "intermediate-fixation"
                                    timeinms = millis()
                
                                    fixation_dot.require_refixation = True
                                    repositioned = False
                                    
                                    count_for_top_up = n_angles_top_up
                                    
                                    sequence = "Post-Adaptation"
                                    
                                else:
                                    count_for_top_up = count_for_top_up - 1
                                    
                                    repositioned = False
                    
                        

##------DEBRIEF   
        
        if sequence == "save responses":
            
            file = open("results_main.csv", "a")
            
            for trial in range(len(response_request.response_dictionary)):
                file.write("".join(response_request.response_dictionary[trial]) + ",")
            
            file.write("\n")            
            
            file.close()
            
            
            file = open("results_practice.csv", "a")
            
            file.write("launch " + str(response_request.response_dictionary_practice["LAUNCH"]) + "," + "pass " + str(response_request.response_dictionary_practice["PASS"]))
            
            file.write("\n")
            
            file.close()
            
            
            file = open("results_instructions.csv", "a")
            
            file.write("launch " + str(example_counter["LAUNCH"]) + "," + "pass " + str(example_counter["PASS"]))
            
            file.write("\n")
            
            file.close()
            

            file = open("reaction_times.csv", "a")
            
            for rt in response_request.reaction_times_trials:
                file.write(str(rt)+",")
            
            file.write("\n")
            
            file.close()
            
            #This is just here to print results in the console after testing.
            for trial in range(len(response_request.response_dictionary)):
                print("".join(response_request.response_dictionary[trial]) + ",")

            print("launch " + str(response_request.response_dictionary_practice["LAUNCH"]) + "," + "pass " + str(response_request.response_dictionary_practice["PASS"]))

            print("launch " + str(example_counter["LAUNCH"]) + "," + "pass " + str(example_counter["PASS"]))
            
            
            sequence = "Debrief"
            
            delaysequence = "pause"
            timeinms = millis()
            print("The total time was " + str(millis()))
        
        if sequence == "Debrief":
            
            if delaysequence == "pause":
                
                if millis() - timeinms < 1000:
                    background(0)
                else:
                    txt.debrief_message_display()

            

        
##------DEVELOPMENT FEATURES       

    if show_FPS == True:
        fill(255)
        textSize(25)
        text(frameRate, 0, 20)

    if check_display_circularity == True:
        for numbers in xrange(360):
            Collision.reposition(WindowX, WindowY, numbers, 5)
            Collision.display()
    
    if display_grid == True:
        rectMode(CENTER)
        rect(Collision.StartX, Collision.StartY, 4, 4)
        rect(Collision.EndX, Collision.EndY, 4, 4)
        rect(Collision.CenterX, Collision.CenterY, 4, 4)
        line(Collision.StartX, Collision.StartY, Collision.EndX, Collision.EndY)
        
    if display_visualdegree == True:
        rectMode(CENTER)
        rect(WindowX/2, WindowY/2, 4, 4)
        rect(WindowX/2 + visualdegree, WindowY/2, 4, 4)
        rect(WindowX/2 - visualdegree, WindowY/2, 4, 4)
        
    if check_animation_time == True:
        
        if keyPressed:
            if key == "c":
                delaysequence = "run"
      
        if delaysequence == "run":
              
            if repositioned == False:
                    
                    fixation_dot.refixate(adaptation_fixation)
                    
                    Collision.reposition(fixation_dot.xpos, "override; adaptation", fixation_dot.ypos, 45, 0, 1)
                    
                    timeinms = millis()
                    
                    repositioned = True
                    
            else:
                if repositioned == True:

                    Collision.single_iteration(speed)
                    
                    if Collision.condition == 3:
                        print(millis() - timeinms)
                    
                        repositioned = False
                        
                        delaysequence = 0
