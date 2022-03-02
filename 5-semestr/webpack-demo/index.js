import firstHello from './scripts/first.js';
import secondHello from './scripts/second.js';

window.onload = function () {
  const body = document.querySelector('body');
  firstHello(body);
  secondHello(body);
};
