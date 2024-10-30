import arcade
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Flower Falling Fun"
PLAYER_SPEED = 5
SPRITE_SCALING = 0.75

class FlyingSprite(arcade.Sprite):
    """Class to represent the good objects falling down."""
    def update(self):
        self.center_y -= 3  # Move down
        if self.top < 0:    # If it goes off the screen, remove it
            self.kill()

class EnemySprite(arcade.Sprite):
    """Class to represent the enemy objects falling down."""
    def update(self):
        self.center_y -= 3  # Move down faster than flying sprites
        if self.top < 0:    # If it goes off the screen, remove it
            self.kill()

class Player(arcade.Sprite):
    """Class to represent the player."""
    def __init__(self):
        super().__init__("basket5.png", SPRITE_SCALING)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 40
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        # Keep the player within screen bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

class CatchGame(arcade.Window):
    """Main game class."""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.flying_sprites = None
        self.enemy_sprites = None
        self.score = 0
        # background variable
        self.background = None

    def setup(self):
        """Set up the game and initialize variables."""
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = Player()
        self.flying_sprites = arcade.SpriteList()
        self.enemy_sprites = arcade.SpriteList()
        self.score = 0
        self.background = arcade.load_texture("back.png")

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        # background
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player.draw()
        self.flying_sprites.draw()
        self.enemy_sprites.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        """All the game logic goes here."""
        self.player.update()
        self.flying_sprites.update()
        self.enemy_sprites.update()

        # Check for collisions with good sprites
        good_hits = arcade.check_for_collision_with_list(self.player, self.flying_sprites)
        for sprite in good_hits:
            sprite.kill()
            self.score += 1

        # Check for collisions with enemy sprites
        bad_hits = arcade.check_for_collision_with_list(self.player, self.enemy_sprites)
        if bad_hits:
            # print("You caught a bee! Try again")
            arcade.close_window()  # End the game if player hits an enemy

        # Occasionally add new flying or enemy sprites
        if random.randint(1, 50) == 1:
            flying_sprite = FlyingSprite("fleur.png", SPRITE_SCALING)  
            flying_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            flying_sprite.center_y = SCREEN_HEIGHT
            self.flying_sprites.append(flying_sprite)

        if random.randint(1, 175) == 1:
            flying_sprite = FlyingSprite("flo.png", SPRITE_SCALING)  
            flying_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            flying_sprite.center_y = SCREEN_HEIGHT
            self.flying_sprites.append(flying_sprite)

        if random.randint(1, 80) == 1:
            enemy_sprite = EnemySprite("bee.png", SPRITE_SCALING)  
            enemy_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            enemy_sprite.center_y = SCREEN_HEIGHT
            self.enemy_sprites.append(enemy_sprite)

    def on_key_press(self, key, modifiers):
        """Handle key presses."""
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """Handle key releases."""
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

def main():
    """Main method"""
    game = CatchGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
