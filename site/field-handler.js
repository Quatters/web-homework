let cells, width, height;
let isReady = false;

function generateField(cellListener) {
  hideErrorMessages();
  let field = document.querySelector('.field-wrapper');

  try {
    let w = parseInt(document.querySelector('#width').value);
    let h = parseInt(document.querySelector('#height').value);

    if (w * h > 150) throw 'Too big';

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

export { cells, isReady, width, height, generateField, hideErrorMessages, showError };
