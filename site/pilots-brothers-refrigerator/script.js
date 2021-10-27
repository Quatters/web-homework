import * as field from '../field-handler.js';

const generateButton = document.querySelector('.generate-button');

let moves = 0;
let movesSpan = document.querySelector('.moves');
let inversedCount = 0;
let victory = false;

window.onload = function () {
  generateButton.addEventListener('click', field.generateField.bind(this, onCellClick), false);
  generateButton.addEventListener('click', onGenerateButtonClick);
};

function onGenerateButtonClick(event) {
  document.querySelector('.victory').classList.add('hidden');
  moves = 0;
  movesSpan.innerText = `Ходов: ${moves}`;
  victory = false;
  inversedCount = 0;
}

function onCellClick(event) {
  if (victory) return;

  moves++;
  movesSpan.innerText = `Ходов: ${moves}`;

  const cell = event.currentTarget;
  const cellX = parseInt(cell.id[5]);
  const cellY = parseInt(cell.id[6]);

  switchCell(cell);

  for (let i = 0; i < field.width; i++) {
    switchCell(field.cells[i][cellY]);
  }
  for (let i = 0; i < field.height; i++) {
    switchCell(field.cells[cellX][i]);
  }

  if (inversedCount === field.width * field.height) {
    victory = true;
    document.querySelector('.victory').classList.remove('hidden');
  }
}

function switchCell(cell) {
  if (cell.classList.contains('inversed')) {
    cell.classList.remove('inversed');
    inversedCount--;
  } else {
    cell.classList.add('inversed');
    inversedCount++;
  }
}
