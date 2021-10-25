let cells;

function generateField() {
  document.querySelector('#error-message').classList.add('hidden');
  document.querySelector('#too-big-message').classList.add('hidden');
  let field = document.querySelector('.field-wrapper');

  try {
    let width = parseInt(document.querySelector('#width').value);
    let height = parseInt(document.querySelector('#height').value);

    if (width * height > 150) throw 'Too big';

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
        cells[i][j].addEventListener('click', onCellClick);
      }
    }
  } catch (error) {
    field.innerHTML = '';
    if (error === 'Too big') document.querySelector('#too-big-message').classList.remove('hidden');
    else document.querySelector('#error-message').classList.remove('hidden');
  }
}

function createCell(id) {
  let cell = document.createElement('div');
  cell.setAttribute('class', 'cell');
  cell.setAttribute('id', 'cell-' + id);

  return cell;
}

function onCellClick(event) {
  // реализация игры
  console.log(event);
}
