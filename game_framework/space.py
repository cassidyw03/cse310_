# # Basic arcade shooter

# # Imports
# import arcade
# import random

# # Constants
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Arcade Space Shooter"
# SCALING = 2.0

# class SpaceShooter(arcade.Window):
#     """Space Shooter side scroller game
#     Player starts on the left, enemies appear on the right
#     Player can move anywhere, but not off screen
#     Enemies fly to the left at variable speed
#     Collisions end the game
#     """

#     def __init__(self, width, height, title):
#         """Initialize the game
#         """
#         super().__init__(width, height, title)

#         # Set up the empty sprite lists
#         self.enemies_list = arcade.SpriteList()
#         self.clouds_list = arcade.SpriteList()
#         self.all_sprites = arcade.SpriteList()

#     def setup(self):
#         """Get the game ready to play
#         """

#         # Set the background color
#         arcade.set_background_color(arcade.color.SKY_BLUE)

#         # Set up the player
#         self.player = arcade.Sprite("basket4.png", SCALING)
#         # y position of the sprite
#         self.player.center_y = self.height / 2
#         # x position of the sprite
#         self.player.left = 10
#         self.all_sprites.append(self.player)



#         # Spawn a new enemy every 0.25 seconds
#         arcade.schedule(self.add_enemy, 0.25)

#         # Spawn a new cloud every second
#         arcade.schedule(self.add_cloud, 1.0)

#     def add_enemy(self, delta_time: float):
#     # """Adds a new enemy to the screen

#     # Arguments:
#     #     delta_time {float} -- How much time has passed since the last call
#     # """

#         # First, create the new enemy sprite
#         enemy = FlyingSprite("missile.png", SCALING)

#         # Set its position to a random height and off screen right
#         enemy.left = random.randint(self.width, self.width + 80)
#         enemy.top = random.randint(10, self.height - 10)

#         # Set its speed to a random speed heading left
#         enemy.velocity = (random.randint(-20, -5), 0)

#         # Add it to the enemies list
#         self.enemies_list.append(enemy)
#         self.all_sprites.append(enemy)

#         if enemy.right < 0:
#             enemy.remove_from_sprite_lists()

#         for enemy in enemies_list:
#             enemy.update()
    
#     def add_cloud(self, delta_time: float):
#         # """Adds a new cloud to the screen

#         # Arguments:
#         #     delta_time {float} -- How much time has passed since the last call
#         # """

#         # First, create the new cloud sprite
#         cloud = FlyingSprite("images/cloud.png", SCALING)

#         # Set its position to a random height and off screen right
#         cloud.left = random.randint(self.width, self.width + 80)
#         cloud.top = random.randint(10, self.height - 10)

#         # Set its speed to a random speed heading left
#         cloud.velocity = (random.randint(-5, -2), 0)

#         # Add it to the enemies list
#         self.clouds_list.append(cloud)
#         self.all_sprites.append(cloud)

# class FlyingSprite(arcade.Sprite):
# # """Base class for all flying sprites
# # Flying sprites include enemies and clouds
# # """
#     def update(self):
#         """Update the position of the sprite
#         When it moves off screen to the left, remove it
#         """

#         # Move the sprite
#         super().update()

#         # Remove if off the screen
#         if self.right < 0:
#             self.remove_from_sprite_lists()


#     def on_key_press(self, symbol, modifiers):
#     # """Handle user keyboard input
#     # Q: Quit the game
#     # P: Pause/Unpause the game
#     # I/J/K/L: Move Up, Left, Down, Right
#     # Arrows: Move Up, Left, Down, Right

#     # Arguments:
#     #     symbol {int} -- Which key was pressed
#     #     modifiers {int} -- Which modifiers were pressed
#     # """
#         if symbol == arcade.key.Q:
#             # Quit immediately
#             arcade.close_window()

#         if symbol == arcade.key.P:
#             self.paused = not self.paused

#         if symbol == arcade.key.I or symbol == arcade.key.UP:
#             self.player.change_y = 5

#         if symbol == arcade.key.K or symbol == arcade.key.DOWN:
#             self.player.change_y = -5

#         if symbol == arcade.key.J or symbol == arcade.key.LEFT:
#             self.player.change_x = -5

#         if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
#             self.player.change_x = 5


#     def on_key_release(self, symbol: int, modifiers: int):
#         """Undo movement vectors when movement keys are released

#         Arguments:
#             symbol {int} -- Which key was pressed
#             modifiers {int} -- Which modifiers were pressed
#         """
#         if (
#             symbol == arcade.key.I
#             or symbol == arcade.key.K
#             or symbol == arcade.key.UP
#             or symbol == arcade.key.DOWN
#         ):
#             self.player.change_y = 0

#         if (
#             symbol == arcade.key.J
#             or symbol == arcade.key.L
#             or symbol == arcade.key.LEFT
#             or symbol == arcade.key.RIGHT
#         ):
#             self.player.change_x = 0

#     def on_update(self, delta_time: float):
#         """Update the positions and statuses of all game objects
#         If paused, do nothing

#         Arguments:
#             delta_time {float} -- Time since the last update
#         """

#         # If paused, don't update anything
#         if self.paused:
#             return

#         # Update everything
#         self.all_sprites.update()

#         # Keep the player on screen
#         if self.player.top > self.height:
#             self.player.top = self.height
#         if self.player.right > self.width:
#             self.player.right = self.width
#         if self.player.bottom < 0:
#             self.player.bottom = 0
#         if self.player.left < 0:
#             self.player.left = 0

#     def on_draw(self):
#         """Draw all game objects
#         """
#         arcade.start_render()
#         self.all_sprites.draw()

#     if __name__ == "__main__":
#         # Create the game window
#         game = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#         game.setup()  # Set up the initial game state
#         arcade.run()  # Start the game loop

# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0

class FlyingSprite(arcade.Sprite):
    def update(self):
        super().update()
        if self.right < 0:
            self.remove_from_sprite_lists()

class SpaceShooter(arcade.Window):
    """Space Shooter game"""

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.paused = False

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = arcade.Sprite("fleur.png", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)
        arcade.schedule(self.add_enemy, 0.25)
        arcade.schedule(self.add_cloud, 1.0)

    def add_enemy(self, delta_time: float):
        enemy = FlyingSprite("missile.png", SCALING)
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)
        enemy.velocity = (random.randint(-20, -5), 0)
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

    def add_cloud(self, delta_time: float):
        cloud = FlyingSprite("fleur.png", SCALING)
        cloud.left = random.randint(self.width, self.width + 80)
        cloud.top = random.randint(10, self.height - 10)
        cloud.velocity = (random.randint(-5, -2), 0)
        self.clouds_list.append(cloud)
        self.all_sprites.append(cloud)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()
        elif symbol == arcade.key.P:
            self.paused = not self.paused
        elif symbol in {arcade.key.I, arcade.key.UP}:
            self.player.change_y = 5
        elif symbol in {arcade.key.K, arcade.key.DOWN}:
            self.player.change_y = -5
        elif symbol in {arcade.key.J, arcade.key.LEFT}:
            self.player.change_x = -5
        elif symbol in {arcade.key.L, arcade.key.RIGHT}:
            self.player.change_x = 5

    def on_key_release(self, symbol, modifiers):
        if symbol in {arcade.key.I, arcade.key.K, arcade.key.UP, arcade.key.DOWN}:
            self.player.change_y = 0
        if symbol in {arcade.key.J, arcade.key.L, arcade.key.LEFT, arcade.key.RIGHT}:
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        if self.paused:
            return
        self.all_sprites.update()
        if self.player.top > self.height:
            self.player.top = self.height
        elif self.player.right > self.width:
            self.player.right = self.width
        elif self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

def main():
    game = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()



        


