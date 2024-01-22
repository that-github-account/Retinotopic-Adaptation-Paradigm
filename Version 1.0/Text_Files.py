class Text(object):
    
    def __init__(self, WindowX, WindowY):
        
        self.WX = WindowX
        self.WY = WindowY
        
        
    def generic_instructions_layout(self):
                
        fill(255)
        
        textAlign(CENTER, TOP)
        textSize(75)
        text("Instructions", self.WX/2, self.WY*0.1)
        
        textAlign(CENTER, BOTTOM)
        textSize(25)
        msg = "Please press SPACE to continue."
        text(msg, self.WX/2, self.WY*0.9)
        
        
    def start_message_display(self):
        
        fill(255)
        
        textAlign(CENTER)
        textSize(25)
        msg = "Please press SPACE to start the experiment when you are ready."
        text(msg, self.WX/2, self.WY/2)  
        
    def main_instructions_display(self):
        
        self.generic_instructions_layout()
        
        fill(255)
        
        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "During this experiment you will see a red fixation cross (    ). Please focus on the fixation cross throughout the experiment. Do NOT look away. Two moving circles will appear to the side of the fixation cross. One circle will either hit and launch the other (a LAUNCH event), or one circle will pass over the other (a PASS event). Your task is to judge whether each event is a LAUNCH or a PASS, WITHOUT directly looking at the event itself. It may be difficult to tell, but you MUST keep looking at the fixation cross the whole time. \n\nPress (D) to view an example of a LAUNCH and press (K) to view an example of a PASS."
        text(msg, self.WX/2, self.WY/2, self.WX*0.9, self.WY*0.9)
        
        stroke("#D21404")
        fill("#D21404")
        rectMode(CENTER)
        rect(self.WX*0.36325, self.WY*0.41, 2*(6) + 5, (6)/2)
        rect(self.WX*0.36325, self.WY*0.41, (6)/2, 2*(6) + 5)
        
    
    def example_instructions_header(self):
        
        fill (255)
    
        textAlign(CENTER, TOP)
        textSize(75)
        text("Instructions", self.WX/2, self.WY*0.1)
        
    def example_launch(self):
        
        fill (255)
    
        textAlign(CENTER, TOP)
        textSize(35)
        text("This is a launch.", self.WX/2, self.WY*0.3)
        
    def example_pass(self):
        
        fill (255)
    
        textAlign(CENTER, TOP)
        textSize(35)
        text("This is a pass.", self.WX/2, self.WY*0.3)

    def training_instructions_display(self):
       
        self.generic_instructions_layout()
        
        fill(255)

        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "You will now complete a training phase consisting of 10 trials. \n\nPlease fixate on the red cross and respond when it turns green by pressing (D) for a LAUNCH event or (K) for a PASS event. \n\nWhen you get 80% correct, you will be able to proceed to the main experiment. You have 5 attempts at this after which the experiment will be terminated if you do not succeed."
        text(msg, self.WX/2, self.WY/2, self.WX*0.9, self.WY*0.9)
                
                                
    def practice_instructions_display(self):
       
        self.generic_instructions_layout()
        
        fill(255)

        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "You will now complete 18 practice trials. \n\nPlease fixate on the red cross and respond when it turns green by pressing (D) for a LAUNCH event or (K) for a PASS event. \n\nThis section will take approximately 1 minute to complete."
        text(msg, self.WX/2, self.WY/2, self.WX*0.9, self.WY*0.9)

        
    def pre_adaptation_trials_instructions_display(self):
        
        self.generic_instructions_layout()
        
        fill(255)
        
        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "You have now completed the practice trials. \n\nNext you will complete some test trials. There will be 180 trials that will take approximately 10 minutes to complete. \n\nRemember to focus on the red cross and try not to look away."
        text(msg, self.WX/2, self.WY/2)
        
        
    def adaptation_instructions_display(self):
        
        self.generic_instructions_layout()
        
        fill(255)
        
        textAlign(CENTER)
        textSize(25)
        msg = "You have now completed the first set of trials. \n\nIn the next phase you will not be asked to give any response. You will simply view a series of animations lasting for approximately 12 minutes. \n\nDuring this phase the red cross may also move. Remember to not directly look at the events but concentrate on the red cross throughout."
        text(msg, self.WX/2, self.WY/2)
    
    
    def post_adaptation_instructions_display(self):

        self.generic_instructions_layout()
        
        fill(255)
        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "You will now complete the final set of trials. \n\nIn this final set of trials you will only respond after some animations. There will be 180 trials lasting for approximately 25 minutes. \n\nPlease keep following the cross and respond when it turns green."
        text(msg, self.WX/2, self.WY/2)
        
        
    def debrief_message_display(self):

        fill(255)

        textAlign(CENTER, CENTER)
        textSize(25)
        msg = "This is the debrief."
        text(msg, self.WX/2, self.WY/2)
        
        
        
        
