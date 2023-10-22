// particles.js

const particleArray = [];

class Particle {
  constructor() {
    this.x = bird.x;
    this.y = bird.y;
    this.size = Math.random() * 10 + 0;
    this.spaceY = Math.random() * 1 - 0.5;
    this.color = 'hsla(' + hue + ', 100%, 50%, 0.8)';
  }
  update() {
    this.x -= gamespeed;
    this.y += this.spaceY;
  }
  draw() {
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.lineWidth = 2;
    ctx.strokeStyle = 'purple';
    ctx.stroke();
  }
}

function handleParticles() {
  if (bird.dead === false) {
    particleArray.unshift(new Particle());
    for (var i = 0; i < particleArray.length; i++) {
      particleArray[i].update();
      particleArray[i].draw();
    }

    // if more than 200 particles, remove 20 particles
    if (particleArray.length > 200) {
      for (var i = 0; i < 20; i++) {
        particleArray.pop(particleArray[i]);
      }
    }
  }
  else if (bird.frameDead < 50) {
    for (var i = 0; i < particleArray.length; i++) {
      particleArray[i].update();
      particleArray[i].draw();
    }
  }
}
