function highlightWinner(combo) {
  if (!combo) return;
  for (let index of combo) {
    board.children[index].classList.add("winner");
  }
}
