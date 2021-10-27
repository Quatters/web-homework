let cells, width, height;
let isReady = false;

let min = 16;
let max = 150;

function generateField(cellListener) {
  hideErrorMessages();
  let field = document.querySelector('.field-wrapper');

  try {
    let w = parseInt(document.querySelector('#width').value);
    let h = parseInt(document.querySelector('#height').value);

    if (w * h > max) throw 'Too big';
    if (w * h < min) throw 'Too small';

    width = w;
    height = h;
    cells = new Array(width);
    field.innerHTML = '';

    let row = document.querySelector('#row-template').content;

    for (let i = 0; i < width; i++) {
      let currentRow = row.cloneNode(true);
      field.append(currentRow);
      currentRow = field.querySelectorAll('.row').item(i);

      cells[i] = new Array(height);

      for (let j = 0; j < height; j++) {
        cells[i][j] = createCell(i + '' + j);
        currentRow.append(cells[i][j]);
        cells[i][j] = currentRow.querySelector('#cell-' + i + '' + j);
        cells[i][j].addEventListener('click', cellListener);
      }
    }

    isReady = true;
  } catch (error) {
    isReady = false;
    field.innerHTML = '';
    if (error === 'Too big') showError('too-big-message');
    else if (error === 'Too small') showError('too-small-message');
    else showError('error-message');
  }
}

function createCell(id) {
  let cell = document.createElement('div');
  cell.setAttribute('class', 'cell');
  cell.setAttribute('id', 'cell-' + id);

  return cell;
}

function hideErrorMessages() {
  const errorWrapper = document.querySelector('.error-wrapper');
  const errors = errorWrapper.querySelectorAll('.error');

  for (let i = 0; i < errors.length; i++) {
    errors[i].classList.add('hidden');
  }
}

function showError(id) {
  const error = document.querySelector(`#${id}`);
  if (error !== null) {
    error.classList.remove('hidden');
  }
}

function indexOf(cell) {
  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      if (cells[i][j] === cell) return { i, j };
    }
  }
  return null;
}

function setMax(value) {
  max = value;
}

function setMin(value) {
  min = value;
}

export { cells, isReady, width, height, generateField, hideErrorMessages, showError, setMin, setMax, indexOf };
