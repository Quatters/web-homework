export default function sayHello(parent) {
  const node = document.createElement('p');
  node.innerText = 'Bye from second script';
  parent.append(node);
}
