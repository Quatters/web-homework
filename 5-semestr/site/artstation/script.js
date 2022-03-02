fetch('/site/img/mems.json').then(response => {
  response.json().then(result => {
    addImage(result.diffMem);
    addImageBase64(result.wolfMem);
    addImage(result.breadMem);
  });
});

function addImage(url) {
  const img = document.createElement('img');
  img.setAttribute('src', url);
  document.querySelector('.content').append(img);
}

function addImageBase64(base64) {
  const img = new Image();
  img.src = base64;
  document.querySelector('.content').append(img);
}
