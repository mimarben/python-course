import tkinter as tk
import random

# Game constants
WIDTH = 500
HEIGHT = 600
PLAYER_SPEED = 20
BULLET_SPEED = 10
ALIEN_SPEED = 2
ALIEN_DROP = 40

class SpaceInvaders:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders (Tkinter Edition)")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Player
        self.player = self.canvas.create_rectangle(WIDTH//2-20, HEIGHT-40, WIDTH//2+20, HEIGHT-20, fill="cyan")
        self.bullets = []
        self.aliens = []
        self.alien_direction = 1
        self.game_over = False

        self.create_aliens()
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
        self.update()

    def create_aliens(self):
        for i in range(5):
            for j in range(7):
                alien = self.canvas.create_rectangle(60*j+30, 40*i+30, 60*j+60, 40*i+60, fill="lime")
                self.aliens.append(alien)

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.player, -PLAYER_SPEED, 0)
            if self.canvas.coords(self.player)[0] < 0:
                self.canvas.move(self.player, -self.canvas.coords(self.player)[0], 0)

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.player, PLAYER_SPEED, 0)
            if self.canvas.coords(self.player)[2] > WIDTH:
                self.canvas.move(self.player, WIDTH - self.canvas.coords(self.player)[2], 0)

    def shoot(self, event):
        if not self.game_over:
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            bullet = self.canvas.create_rectangle((x1+x2)//2-3, y1-10, (x1+x2)//2+3, y1, fill="yellow")
            self.bullets.append(bullet)

    def update(self):
        if not self.game_over:
            self.move_bullets()
            self.move_aliens()
            self.check_collisions()
            self.check_game_over()
            self.root.after(30, self.update)

    def move_bullets(self):
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, -BULLET_SPEED)
            if self.canvas.coords(bullet)[1] < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)

    def move_aliens(self):
        move_down = False
        for alien in self.aliens:
            self.canvas.move(alien, ALIEN_SPEED * self.alien_direction, 0)
            x1, y1, x2, y2 = self.canvas.coords(alien)
            if x2 > WIDTH or x1 < 0:
                move_down = True
        if move_down:
            self.alien_direction *= -1
            for alien in self.aliens:
                self.canvas.move(alien, 0, ALIEN_DROP)

    def check_collisions(self):
        for bullet in self.bullets[:]:
            bx1, by1, bx2, by2 = self.canvas.coords(bullet)
            for alien in self.aliens[:]:
                ax1, ay1, ax2, ay2 = self.canvas.coords(alien)
                if bx1 < ax2 and bx2 > ax1 and by1 < ay2 and by2 > ay1:
                    self.canvas.delete(alien)
                    self.aliens.remove(alien)
                    self.canvas.delete(bullet)
                    self.bullets.remove(bullet)
                    break

    def check_game_over(self):
        for alien in self.aliens:
            x1, y1, x2, y2 = self.canvas.coords(alien)
            if y2 >= HEIGHT-40:
                self.game_over = True
                self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 40, "bold"))
                break
        if not self.aliens:
            self.game_over = True
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="YOU WIN!", fill="lime", font=("Arial", 40, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvaders(root)
    root.mainloop()
