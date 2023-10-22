// bird.js

// const staticUrl = "{% static 'website/games/flappy-cat/' %}";

const birdSprite = new Image();
birdSprite.src = staticUrl + 'flying_spritesheet.png';
const birdDeadSprite = new Image();
birdDeadSprite.src = staticUrl + 'dead_spritesheet.png';
const gameOverSprite = new Image();
gameOverSprite.src = staticUrl + 'game_over_spritesheet.png';
class Bird {
  constructor() {
    this.x = 150;
    this.y = 200;
    this.vy = 0;
    this.originalWidth = 413;
    this.originalHeight = 423;
    this.width = this.originalWidth / 20;
    this.height = this.originalHeight / 20;
    this.weight = 1;
    this.frameX = 0;
    this.dead = false;
    this.frameDead = 0;
  }
  update() {
    if (this.dead === false) {
      let curve = Math.sin(angle) * 20;
      if (this.y > canvas.height - this.height * 3 + curve) {
        this.y = canvas.height - this.height * 3 + curve;
        this.vy = 0;
      } else {
        this.vy += this.weight;
        this.vy *= 0.9;
        this.y += this.vy;
      }
      if (this.y < 0 + this.height) {
        this.y = 0 + this.height;
        this.vy = 0;
      }

      if (spacePressed) this.flap();
    } else {
      this.vy = 0;
    }
  }
  draw() {
    ctx.fillStyle = "#30f";
    if (this.dead === false) {
      ctx.drawImage(birdSprite, this.frameX * this.originalWidth, 0, this.originalWidth, this.originalHeight, this.x - 10, this.y - 6, this.width * 1.7, this.height * 1.7);
    } else {
      ctx.drawImage(birdDeadSprite, this.frameX * 422, 0, 422, 466, this.x - 10, this.y - 6, this.width * 1.7, this.height * 1.7);
      if (this.frameX >= 7) this.frameX = 0;
      else if (frame % 4 === 0) this.frameX++;
      if (this.frameDead < 5) {
        ctx.drawImage(gameOverSprite, this.frameDead * 536, 0, 536, 539, this.x, this.y, 50, 50);
      }
      if (frame % 2 === 0) this.frameDead++;
    }
  }
  flap() {
    this.vy -= 2;
    if (this.frameX >= 7) this.frameX = 0;
    else if (frame % 2 === 0) this.frameX++;
  }
}

const bird = new Bird();
