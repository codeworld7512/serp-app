// obstacles.js

// const staticUrl = "{% static 'website/games/flappy-cat/' %}";

const obstaclesArray = [];

const redCrayon = new Image();
redCrayon.src = staticUrl + 'red_crayon.png';
const greenCrayon = new Image();
greenCrayon.src = staticUrl + 'green_crayon.png';

class Obstacle {
  constructor() {
    this.top = (Math.random() * canvas.height) / 3 + 20;
    this.bottom = (Math.random() * canvas.height) / 3 + 20;
    this.x = canvas.width;
    this.width = 20;
    this.color = "hsla(" + hue + ",100%,50%,1)";
    this.counted = false;
  }
  draw() {
    //top pipe drawing
    ctx.drawImage(redCrayon, this.x, 0, this.width, this.top);

    //bottom pipe drawing
    ctx.drawImage(greenCrayon, this.x, canvas.height - this.bottom, this.width, this.bottom);
  }
  update() {
    if (bird.dead === false) {
      this.x -= gamespeed;
      if (!this.counted && this.x < bird.x) {
        score++;
        this.counted = true;
      }
    }
    this.draw();
  }
}

function handleObstacle() {
  if (bird.dead === false) {
    if (frame % 150 === 0) {
      obstaclesArray.unshift(new Obstacle());
    }
    for (var i = 0; i < obstaclesArray.length; i++) {
      obstaclesArray[i].update();
    }
    if (obstaclesArray.length > 20) {
      obstaclesArray.pop(obstaclesArray[0]);
    }
  }
  else {
    for (var i = 0; i < obstaclesArray.length; i++) {
      obstaclesArray[i].update();
    }
  }
}
