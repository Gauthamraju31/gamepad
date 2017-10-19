import pygame
import socket

#HOST='172.16.25.187'

HOST='172.16.25.187'

PORT=5500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

pygame.init()
 
#Loop until the user clicks the close button.
done = False

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    
    # For each joystick:
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    #lists
    axis=[0,0,0,0]
    button=[0,0,0,0,0,0,0,0,0,0,0,0]
    
        # Get the name from the OS for the controller/joystick
    name = joystick.get_name()
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
    axes = joystick.get_numaxes()
     
    for i in range( axes ):
        axis[i] = joystick.get_axis( i )
            
    buttons = joystick.get_numbuttons()
    
    for i in range( buttons ):
        button[i] = joystick.get_button( i )
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
    hats = joystick.get_numhats()
    
    
    hat = joystick.get_hat( 0 )
        
    straxis=str(axis)
    strbutton=str(button)
    strhat=str(hat)
    
    datastr="" +strbutton, " " +strhat
    #print (axis)
    #print("The values axis buttons"  +str(button), "hat" +str(hat))
    
    #data send over TCP
    #axestmp, hat ,button
    s.sendall(str(datastr))
    data=s.recv(1024)

s.close()
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
