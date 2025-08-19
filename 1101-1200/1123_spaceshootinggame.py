import math
import random
import sys
from dataclasses import dataclass
import pygame

WIDTH, HEIGHT = 960, 600
FPS = 60
STAR_LAYERS = [(90, 1), (60, 2), (30, 3)]  
PLAYER_SPEED = 6
BULLET_SPEED = 12
BULLET_COOLDOWN = 220  
ENEMY_SPAWN_BASE = 1100  
ENEMY_SPAWN_MIN = 400
LEVEL_UP_EVERY = 20  
BLACK = (10, 10, 14)
WHITE = (240, 240, 240)
GREY = (120, 120, 140)
RED = (220, 60, 70)
GREEN = (70, 200, 120)
YELLOW = (240, 210, 80)
CYAN = (90, 200, 230)
ORANGE = (255, 150, 60)
PURPLE = (180, 100, 220)

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: float
    color: tuple
    size: float

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt

    def draw(self, surf):
        if self.life <= 0:
            return
        alpha = int(255 * clamp(self.life, 0, 1))
        s = max(1, int(self.size))
        particle = pygame.Surface((s, s), pygame.SRCALPHA)
        pygame.draw.circle(particle, (*self.color, alpha), (s // 2, s // 2), s // 2)
        surf.blit(particle, (self.x - s // 2, self.y - s // 2))
        
class Starfield:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.layers = []
        for count, speed in STAR_LAYERS:
            stars = [
                [random.randint(0, w), random.randint(0, h), random.randint(1, 3)]
                for _ in range(count)
            ]
            self.layers.append({"stars": stars, "speed": speed})

    def update(self, dt):
        for layer in self.layers:
            for star in layer["stars"]:
                star[0] -= layer["speed"] * dt * 60
                if star[0] < 0:
                    star[0] = self.w
                    star[1] = random.randint(0, self.h)

    def draw(self, surf):
        for i, layer in enumerate(self.layers):
            for x, y, r in layer["stars"]:
                c = 200 - i * 40
                pygame.draw.circle(surf, (c, c, c), (int(x), int(y)), r)
class Player:
    def __init__(self):
        self.w, self.h = 46, 32
        self.x = 80
        self.y = HEIGHT // 2
        self.speed = PLAYER_SPEED
        self.color = CYAN
        self.health = 100
        self.max_health = 100
        self.last_shot = 0
        self.fire_cooldown = BULLET_COOLDOWN
        self.rapid_fire_timer = 0
        self.invincible_timer = 0

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.w // 2), int(self.y - self.h // 2), self.w, self.h)

    def update(self, dt, keys):
        dx = dy = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1
        mag = math.hypot(dx, dy)
        if mag:
            dx, dy = dx / mag, dy / mag
        self.x = clamp(self.x + dx * self.speed, 0 + self.w // 2 + 6, WIDTH * 0.6)
        self.y = clamp(self.y + dy * self.speed, 0 + self.h // 2 + 6, HEIGHT - self.h // 2 - 6)
        if self.rapid_fire_timer > 0:
            self.rapid_fire_timer -= dt
            self.fire_cooldown = 90
        else:
            self.fire_cooldown = BULLET_COOLDOWN
        if self.invincible_timer > 0:
            self.invincible_timer -= dt

    def can_fire(self, now_ms):
        return now_ms - self.last_shot >= self.fire_cooldown

    def mark_shot(self, now_ms):
        self.last_shot = now_ms

    def draw(self, surf, t):
        r = self.rect
        if self.invincible_timer > 0:
            glow = pygame.Surface((r.w + 12, r.h + 12), pygame.SRCALPHA)
            pygame.draw.ellipse(glow, (*YELLOW, 80), glow.get_rect())
            surf.blit(glow, (r.x - 6, r.y - 6))

        pygame.draw.rect(surf, self.color, r, border_radius=6)
        nose = [(r.right, r.centery), (r.right - 12, r.top), (r.right - 12, r.bottom)]
        pygame.draw.polygon(surf, WHITE, nose)
        flicker = 6 + 3 * math.sin(t * 12)
        pygame.draw.polygon(
            surf,
            ORANGE,
            [
                (r.left - 10, r.centery),
                (r.left - 10 - flicker, r.centery - 6),
                (r.left - 10 - flicker, r.centery + 6),
            ],
        )
        pct = self.health / self.max_health
        hb_bg = pygame.Rect(20, 20, 200, 12)
        pygame.draw.rect(surf, GREY, hb_bg, border_radius=6)
        hb_fg = hb_bg.copy()
        hb_fg.w = int(hb_bg.w * pct)
        pygame.draw.rect(surf, GREEN if pct > 0.35 else RED, hb_fg, border_radius=6)
        pygame.draw.rect(surf, WHITE, hb_bg, 2, border_radius=6)

class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.r = 4
        self.speed = BULLET_SPEED
        self.alive = True
        
    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r * 2, self.r * 2)

    def update(self, dt):
        self.x += self.speed
        if self.x > WIDTH + 20:
            self.alive = False

    def draw(self, surf):
        pygame.draw.circle(surf, YELLOW, (int(self.x), int(self.y)), self.r)

class Enemy:
    TYPES = [
        {"color": RED, "w": 32, "h": 24, "hp": 1, "speed": 3.5},
        {"color": PURPLE, "w": 44, "h": 30, "hp": 2, "speed": 2.8},
        {"color": ORANGE, "w": 28, "h": 20, "hp": 1, "speed": 4.2},
    ]

    def __init__(self, level):
        spec = random.choice(Enemy.TYPES)
        self.w, self.h = spec["w"], spec["h"]
        self.color = spec["color"]
        self.x = WIDTH + random.randint(0, 60)
        self.y = random.randint(30, HEIGHT - 30)
        base = spec["speed"] + (level * 0.15)
        self.vx = -base
        self.hp = spec["hp"] + level // 3
        self.alive = True
        self.time = 0
        self.sin_amp = random.uniform(8, 40)
        self.sin_freq = random.uniform(1.2, 2.2)

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.w // 2), int(self.y - self.h // 2), self.w, self.h)

    def update(self, dt):
        self.time += dt
        self.x += self.vx
        self.y += math.sin(self.time * self.sin_freq * 4) * (self.sin_amp * dt)
        if self.x < -80:
            self.alive = False

    def draw(self, surf):
        r = self.rect
        pygame.draw.rect(surf, self.color, r, border_radius=4)
        tip = [(r.left, r.centery), (r.left + 12, r.top), (r.left + 12, r.bottom)]
        pygame.draw.polygon(surf, WHITE, tip)
        if self.hp > 1:
            for i in range(self.hp):
                pygame.draw.rect(surf, GREEN, (r.centerx - 10 + i * 8, r.top - 6, 6, 4))


class PowerUp:
    KINDS = ["rapid", "heal", "shield"]

    def __init__(self, x, y):
        self.kind = random.choice(PowerUp.KINDS)
        self.x, self.y = x, y
        self.vx = -2.2
        self.alive = True
        self.r = 10

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r * 2, self.r * 2)

    def update(self, dt):
        self.x += self.vx
        if self.x < -20:
            self.alive = False

    def apply(self, player: Player):
        if self.kind == "rapid":
            player.rapid_fire_timer = 6.0
        elif self.kind == "heal":
            player.health = clamp(player.health + 30, 0, player.max_health)
        elif self.kind == "shield":
            player.invincible_timer = 4.0

    def draw(self, surf):
        c = {"rapid": YELLOW, "heal": GREEN, "shield": CYAN}[self.kind]
        pygame.draw.circle(surf, c, (int(self.x), int(self.y)), self.r)
        pygame.draw.circle(surf, WHITE, (int(self.x), int(self.y)), self.r, 2)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Shooter — Pygame")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 20)
        self.big_font = pygame.font.SysFont("consolas", 48, bold=True)

        self.starfield = Starfield(WIDTH, HEIGHT)
        self.reset()

    def reset(self):
        self.player = Player()
        self.bullets = []
        self.enemies = []
        self.particles = []
        self.powerups = []
        self.score = 0
        self.destroyed = 0
        self.level = 1
        self.state = "menu"
        self.next_spawn_ms = ENEMY_SPAWN_BASE
        self.last_spawn_time = 0
        self.time = 0

    def spawn_enemy(self):
        self.enemies.append(Enemy(self.level))

    def spawn_explosion(self, x, y, base_color):
        for _ in range(20):
            ang = random.uniform(0, math.tau)
            spd = random.uniform(60, 220)
            vx = math.cos(ang) * spd / 60
            vy = math.sin(ang) * spd / 60
            life = random.uniform(0.3, 0.9)
            color = tuple(clamp(c + random.randint(-30, 30), 30, 255) for c in base_color)
            self.particles.append(Particle(x, y, vx, vy, life, color, size=random.uniform(2, 5)))

    def update(self, dt):
        self.time += dt
        keys = pygame.key.get_pressed()
        if self.state == "running":
            self.starfield.update(dt)
            self.player.update(dt, keys)
            now = pygame.time.get_ticks()
            if (keys[pygame.K_SPACE] or keys[pygame.K_RETURN]) and self.player.can_fire(now):
                self.player.mark_shot(now)
                spread = 0.18 if self.player.rapid_fire_timer > 0 else 0.06
                for off in (-spread, 0, spread) if self.player.rapid_fire_timer > 0 else (0,):
                    bx = self.player.rect.right + 8
                    by = self.player.y + math.sin(self.time * 12 + off) * 2
                    b = Bullet(bx, by)
                    if off:
                        b.speed = BULLET_SPEED
                    self.bullets.append(b)
            for b in self.bullets:
                b.update(dt)
            self.bullets = [b for b in self.bullets if b.alive]
            if pygame.time.get_ticks() - self.last_spawn_time >= self.next_spawn_ms:
                self.spawn_enemy()
                self.last_spawn_time = pygame.time.get_ticks()
                self.next_spawn_ms = max(
                    ENEMY_SPAWN_MIN, int(ENEMY_SPAWN_BASE - (self.level - 1) * 80 + random.randint(-120, 120))
                )
            for e in self.enemies:
                e.update(dt)
                if e.rect.colliderect(self.player.rect):
                    if self.player.invincible_timer <= 0:
                        self.player.health -= 25
                        self.player.invincible_timer = 1.0
                    e.alive = False
                    self.spawn_explosion(e.x, e.y, e.color)
            for e in self.enemies:
                if not e.alive:
                    continue
                for b in self.bullets:
                    if e.rect.colliderect(b.rect):
                        e.hp -= 1
                        b.alive = False
                        self.particles.append(Particle(b.x, b.y, 0, 0, 0.2, YELLOW, 4))
                        if e.hp <= 0:
                            e.alive = False
                            self.destroyed += 1
                            self.score += 10 + 2 * self.level
                            self.spawn_explosion(e.x, e.y, e.color)
                            if random.random() < 0.15:
                                self.powerups.append(PowerUp(e.x, e.y))
            for e in self.enemies:
                if e.alive and e.x < self.player.x - 60:
                    e.alive = False
                    self.player.health -= 10
            for p in self.powerups:
                p.update(dt)
                if p.rect.colliderect(self.player.rect):
                    p.apply(self.player)
                    p.alive = False
            self.powerups = [p for p in self.powerups if p.alive]
            for pr in self.particles:
                pr.update(dt)
            self.particles = [pr for pr in self.particles if pr.life > 0]
            self.enemies = [e for e in self.enemies if e.alive]
            if self.destroyed and self.destroyed % LEVEL_UP_EVERY == 0:
                self.level = 1 + self.destroyed // LEVEL_UP_EVERY
            if self.player.health <= 0:
                self.state = "gameover"

        elif self.state == "menu":
            self.starfield.update(dt)
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                self.state = "running"
        elif self.state == "gameover":
            self.starfield.update(dt)

    def draw_grid(self, surf):
        step = 40
        for x in range(0, WIDTH, step):
            pygame.draw.line(surf, (20, 20, 26), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, step):
            pygame.draw.line(surf, (20, 20, 26), (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid(self.screen)
        self.starfield.draw(self.screen)
        for pr in self.particles:
            pr.draw(self.screen)

        if self.state in ("running", "gameover"):
            for e in self.enemies:
                e.draw(self.screen)
            for b in self.bullets:
                b.draw(self.screen)
            for p in self.powerups:
                p.draw(self.screen)
            self.player.draw(self.screen, self.time)

        if self.state == "running":
            info = f"Score: {self.score}   Level: {self.level}   Destroyed: {self.destroyed}"
            txt = self.font.render(info, True, WHITE)
            self.screen.blit(txt, (20, 40))
            tip = self.font.render("Move: WASD/Arrows   Fire: Space/Enter   Pause: P   Quit: ESC", True, GREY)
            self.screen.blit(tip, (20, HEIGHT - 30))
        elif self.state == "menu":
            title = self.big_font.render("SPACE SHOOTER", True, WHITE)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 140))
            sub = self.font.render("Your rocket launches from the left. Enemies approach from the right.", True, GREY)
            self.screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 210))
            ctl = self.font.render("Move with WASD/Arrows, Fire with Space/Enter", True, GREY)
            self.screen.blit(ctl, (WIDTH // 2 - ctl.get_width() // 2, 240))
            start = self.font.render("Press Space to Start", True, YELLOW)
            self.screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 300))
        elif self.state == "gameover":
            over = self.big_font.render("GAME OVER", True, RED)
            self.screen.blit(over, (WIDTH // 2 - over.get_width() // 2, 160))
            score = self.font.render(f"Score: {self.score}   Level Reached: {self.level}", True, WHITE)
            self.screen.blit(score, (WIDTH // 2 - score.get_width() // 2, 230))
            restart = self.font.render("Press R to Restart or ESC to Quit", True, GREY)
            self.screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, 270))

        pygame.display.flip()

    def run(self):
        paused = False
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_p and self.state == "running":
                        paused = not paused
                    if event.key == pygame.K_r and self.state == "gameover":
                        self.reset()
                        self.state = "running"

            if not paused:
                self.update(dt)
            self.draw()
            
if __name__ == "__main__":
    Game().run()
