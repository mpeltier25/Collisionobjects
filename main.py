import pygame, collisionObjects

def main():
    #intializes pygame put the code in the main method instead of having it outside of it.
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Mathew Peltier project 1")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    lblOutput = collisionObjects.Label()
    lblOutput.center = (100, 50)
    lblOutput.text = "Hi"
    """The following code uses the classes that I made in collision objects and puts them into
a group of allSprites"""
    Orc = collisionObjects.Orc()
    Bluemonster = collisionObjects.Bluemonster()
    Bluemonster2 = collisionObjects.Bluemonster2()
    Bluemonster3 = collisionObjects.Bluemonster3()
    allSprites = pygame.sprite.Group(Bluemonster, Bluemonster2, Bluemonster3, Orc, lblOutput)

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        """These if statements will make it so that if the orc that the user controls with the
mouse goes over one of the Bluemonster images, it will make that image disappear. Please note 
that I left the ping images with the brown outline of the square so you could see exactly what point 
that the image will disappear. """
        if Orc.rect.colliderect(Bluemonster.rect):
            Bluemonster.kill()
        if Orc.rect.colliderect(Bluemonster2.rect):
            Bluemonster2.kill()
        if Orc.rect.colliderect(Bluemonster3.rect):
            Bluemonster3.kill()
        lblOutput.text="get the monsters!"
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    pygame.mouse.set_visible(True)

if __name__ == "__main__":
    main()

