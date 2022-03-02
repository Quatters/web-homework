const startButton = document.querySelector('.start-button');
const countdown = document.querySelector('.countdown');
const delay = 66;

let seconds, milliseconds;

startButton.addEventListener('click', function () {
  startButton.innerText = 'Запустить';
  countdown.classList.remove('color-red');

  seconds = 3;
  milliseconds = 0;

  const promise = new Promise((resolve, reject) => {
    const interval = setInterval(() => {
      updateCountdown();
      milliseconds -= delay;
      if (milliseconds <= 0) {
        milliseconds = 1000;
        seconds--;
      }
      if (seconds < 0) {
        seconds = 0;
        milliseconds = 0;
        updateCountdown();
        clearInterval(interval);
        resolve('Ok');
      }
    }, delay);
  });

  promise.then(function () {
    countdown.classList.add('color-red');
    startButton.innerText = 'Перезапустить';
  });
});

function updateCountdown() {
  countdown.innerText = `00:${('00' + seconds).slice(-2)}:${('000' + milliseconds).slice(-3)}`;
}
