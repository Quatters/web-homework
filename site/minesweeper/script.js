import * as field from '../field-handler.js';

const generateButton = document.querySelector('.generate-button');
const bombPercentInput = document.querySelector('#bombs-percent');
const flagsSpan = document.querySelector('#flags');
const victorySpan = document.querySelector('#victory');
const loseSpan = document.querySelector('#lose');
const defaultBombChance = 0.25;

let bombChance;
let flagImg, bombImg;
let areBombsGenerated = false;
let bombsAmount;
let openedCells = 0;
let gameEnded = false;
let marks = 0;

window.onload = function () {
  field.setMax(529);
  field.setMin(36);
  generateButton.addEventListener('click', field.generateField.bind(this, onCellClick), false);
  generateButton.addEventListener('click', onGenerateCells);

  flagImg = document.createElement('img');
  flagImg.setAttribute('width', 28);
  flagImg.setAttribute('src', '/site/img/flag_red.png');

  bombImg = document.createElement('img');
  bombImg.setAttribute('width', 28);
  bombImg.setAttribute('src', '/site/img/bomb.png');
};

function onGenerateCells() {
  initializeField();
  flagsSpan.innerText = 'Флагов: 0/0';
  marks = 0;
  areBombsGenerated = false;
}

function generateBombs(openedCell) {
  try {
    let percent = parseInt(bombPercentInput.value);
    if (isNaN(percent)) throw 'NaN';
    if (percent > 90) throw 'Too big';
    if (percent < 10) throw 'Too small';
    bombChance = percent / 100;
  } catch (error) {
    bombChance = defaultBombChance;
    bombPercentInput.value = '';
  }
  bombsAmount = Math.round(field.height * field.width * bombChance);

  for (let i = 0; i < bombsAmount; i++) {
    let index;
    do {
      index = getRandomIndex();
    } while (field.cells[index.i][index.j].isBomb || field.cells[index.i][index.j] == openedCell);

    field.cells[index.i][index.j].isBomb = true;
    // field.cells[index.i][index.j].classList.add('bomb');
  }

  flagsSpan.innerText = `Флагов: 0/${bombsAmount}`;

  areBombsGenerated = true;
}

function initializeField() {
  for (let i = 0; i < field.width; i++) {
    for (let j = 0; j < field.height; j++) {
      field.cells[i][j].innerHTML = '';
      field.cells[i][j].innerText = '';
      field.cells[i][j].classList.remove('opened');
      field.cells[i][j].opened = false;
      field.cells[i][j].isBomb = false;
      field.cells[i][j].marked = false;
      field.cells[i][j].addEventListener('contextmenu', onRightClick);
    }
  }

  openedCells = 0;
  victorySpan.classList.add('hidden');
  loseSpan.classList.add('hidden');
  gameEnded = false;
}

function getRandomIndex() {
  const i = Math.floor(Math.random() * field.width);
  const j = Math.floor(Math.random() * field.height);

  return { i, j };
}

function onCellClick(event) {
  if (gameEnded || event.currentTarget.marked) return;

  if (!areBombsGenerated) {
    generateBombs(event.currentTarget);
  }

  if (event.currentTarget.isBomb) {
    gameOver();
  } else {
    openCell(event.currentTarget);
  }
}

function onRightClick(event) {
  event.preventDefault();
  if (gameEnded || !areBombsGenerated) return;

  let cell = event.currentTarget;
  if (!cell.opened) {
    switchMark(cell);
  }
}

function switchMark(cell) {
  if (!cell.marked) {
    cell.append(flagImg.cloneNode());
    marks++;
    flagsSpan.innerText = `Флагов: ${marks}/${bombsAmount}`;
    cell.marked = true;
  } else {
    marks--;
    flagsSpan.innerText = `Флагов: ${marks}/${bombsAmount}`;
    cell.innerHTML = '';
    cell.marked = false;
  }
}

function openCell(cell) {
  if (cell.isBomb || cell.opened) return;

  cell.opened = true;
  openedCells++;
  cell.classList.add('opened');

  let neighbors = getNeighbors(cell);
  let bombsAround = 0;

  neighbors.forEach(neighbor => {
    if (neighbor.isBomb) bombsAround++;
  });

  if (bombsAround > 0) cell.innerText = bombsAround;
  else
    neighbors.forEach(neighbor => {
      openCell(neighbor);
    });

  if (openedCells === field.width * field.height - bombsAmount) victory();
}

function getNeighbors(cell) {
  let neighbors = [];
  let index = field.indexOf(cell);

  for (let i = index.i - 1; i <= index.i + 1; i++) {
    if (i < 0 || i >= field.width) continue;
    for (let j = index.j - 1; j <= index.j + 1; j++) {
      if (j < 0 || j >= field.height || (i === index.i && j === index.j)) continue;

      neighbors.push(field.cells[i][j]);
    }
  }

  return neighbors;
}

function gameOver() {
  gameEnded = true;
  loseSpan.classList.remove('hidden');
  showBombs();
}

function showBombs() {
  for (let i = 0; i < field.width; i++) {
    for (let j = 0; j < field.height; j++) {
      if (field.cells[i][j].isBomb) {
        if (field.cells[i][j].marked) switchMark(field.cells[i][j]);
        field.cells[i][j].append(bombImg.cloneNode());
      }
    }
  }
}

function victory() {
  gameEnded = true;
  victorySpan.classList.remove('hidden');
}
