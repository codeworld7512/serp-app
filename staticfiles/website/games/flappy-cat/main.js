function preventSpaceScroll(e) {
  if (e.code === 'Space') {
    e.preventDefault();
  }
}

const startGame = document.getElementById('startGame');

startGame.addEventListener('click', function () {
  this.style.display = 'none'; // hide the button
  gameState = 'playing';
  animate();
  // Add the event listener to prevent default space bar action
  window.addEventListener('keydown', preventSpaceScroll);
});

const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");
canvas.width = 600;
canvas.height = 400;

let spacePressed = false;
let angle = 0;
let hue = 0;
let frame = 0;
let score = 0;
let gamespeed = 2;
var gameState = 'paused';
const gradient = ctx.createLinearGradient(0, 0, 0, 70);
gradient.addColorStop("0.4", "#fff");
gradient.addColorStop("0.5", "#000");
gradient.addColorStop("0.55", "#4040ff");
gradient.addColorStop("0.6", "#000");
gradient.addColorStop("0.65", "#fff");

const background = new Image();
background.src = staticUrl + 'background.png';
const BG = {
  x1: 0,
  x2: canvas.width,
  y: 0,
  width: canvas.width,
  height: canvas.height
};

function handleBackground() {
  if (BG.x1 <= -BG.width + gamespeed) BG.x1 = BG.width;
  else BG.x1 -= gamespeed;
  if (BG.x2 <= -BG.width + gamespeed) BG.x2 = BG.width;
  else BG.x2 -= gamespeed;
  ctx.drawImage(background, BG.x1, BG.y, BG.width, BG.height);
  ctx.drawImage(background, BG.x2, BG.y, BG.width, BG.height);
}

function animate() {
  if (gameState === 'playing') {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    handleBackground();
    handleObstacle();
    handleParticles();
    bird.update();
    bird.draw();
    ctx.fillStyle = gradient;
    ctx.font = "90px Georgia";
    ctx.strokeText(score, canvas.width / 2, 70);
    ctx.fillText(score, canvas.width / 2, 70);
    handleCollision();
    if (handleCollision()) {
      gamespeed = 0;
    }
    requestAnimationFrame(animate);
    angle += 0.12;
    hue++;
    frame++;
  }
}

// function init() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);
//   ctx.font = "30px Arial";
//   ctx.fillText("Click to Play", canvas.width / 2 - 100, canvas.height / 2);
// }

// init();

document.getElementById('canvas1').addEventListener('click', function () {
  if (gameState === 'paused') {
    gameState = 'playing';
    animate();
  }
});

window.addEventListener("keydown", function (e) {
  if (bird.dead === false) {
    if (e.key === "Escape") {
      window.location.reload();
    }
    else if (e.code === "Space") spacePressed = true;
  }
  else {
    window.location.reload();
  }
});

window.addEventListener("mousedown", function (e) {
  if (bird.dead === false) {
    spacePressed = true;
  }
  else {
    window.location.reload();
  }
});

window.addEventListener("touchstart", function (e) {
  if (bird.dead === false) {
    spacePressed = true;
  }
  else {
    window.location.reload();
  }
});

window.addEventListener("keyup", function (e) {
  if (e.code === "Space") spacePressed = false;
  bird.frameX = 0;
});

window.addEventListener("mouseup", function (e) {
  spacePressed = false;
  bird.frameX = 0;
});

window.addEventListener("touchend", function (e) {
  spacePressed = false;
  bird.frameX = 0;
});


function handleCollision() {
  for (var i = 0; i < obstaclesArray.length; i++) {
    if (
      bird.x < obstaclesArray[i].x + obstaclesArray[i].width &&
      bird.x + bird.width > obstaclesArray[i].x &&
      ((bird.y < 0 + obstaclesArray[i].top && bird.y + bird.height > 0) ||
        (bird.y > canvas.height - obstaclesArray[i].bottom &&
          bird.y + bird.height < canvas.height))
    ) {
      bird.dead = true;
      gameState = 'paused'; // add this line to pause the game when there's a collision
      ctx.font = "24px sans-serif";
      ctx.fillStyle = "Red";
      ctx.fillText(
        "Game Over (tap to restart), Score: " + score,
        50,
        canvas.height / 2 - 10
      );
      return true;
    }
  }
}