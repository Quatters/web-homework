import * as field from '../field-handler.js';

const playButton = document.querySelector('.play-button');
const generateButton = document.querySelector('.generate-button');
const timeSpan = document.querySelector('.time');
const scoreSpan = document.querySelector('.score');
const initialTimeleft = 30;

let prevActiveCell = null;
let activeCell = null;
let score = 0;
let delay = 700;
let timeLeft = initialTimeleft;
let gameloop, timer;
let isPlaying = false;

window.onload = function () {
  playButton.addEventListener('click', play);
  generateButton.addEventListener('click', field.generateField.bind(this, onCellClick), false);
};

function play() {
  if (isPlaying) {
    stopGame();
    return;
  }

  if (!field.isReady) {
    field.hideErrorMessages();
    field.showError('field-not-ready');
    return;
  }

  timeSpan.innerText = `Осталось времени: ${timeLeft} сек`;
  score = 0;
  scoreSpan.innerText = `Очки: ${score}`;

  startGameloop();
  startTimer();
  isPlaying = true;
  generateButton.setAttribute('disabled', 'disabled');
  playButton.innerText = 'Стоп';
}

function startTimer() {
  timer = setInterval(() => {
    timeLeft--;
    timeSpan.innerHTML = `Осталось времени: ${timeLeft} сек`;
    if (timeLeft <= 0) {
      stopGame();
    }
  }, 1000);
}

function startGameloop() {
  gameloop = setInterval(() => {
    let x = Math.floor(Math.random() * field.width);
    let y = Math.floor(Math.random() * field.height);

    activeCell = field.cells[x][y];

    let img = document.createElement('img');
    img.setAttribute('src', '/site/img/mole.png');
    img.setAttribute('alt', 'Mole');
    img.setAttribute('width', 30);

    if (prevActiveCell !== null) {
      prevActiveCell.innerHTML = '';
    }
    activeCell.append(img);
    prevActiveCell = activeCell;
  }, delay);
}

function stopGame() {
  isPlaying = false;
  playButton.innerText = 'Играть';
  timeSpan.innerText = 'Осталось времени: 0 сек';
  generateButton.removeAttribute('disabled');

  clearInterval(gameloop);

  timeLeft = initialTimeleft;
  clearInterval(timer);

  for (let i = 0; i < field.width; i++) {
    for (let j = 0; j < field.height; j++) {
      field.cells[i][j].innerHTML = '';
    }
  }
}

function onCellClick(event) {
  if (!isPlaying) return;

  if (event.currentTarget == activeCell) {
    score++;
    scoreSpan.innerText = `Очки: ${score}`;
    activeCell.innerHTML = '';
  }
}
