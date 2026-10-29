(() => {
  const buttons = Array.from(document.querySelectorAll("[data-filter]"));
  const cards = Array.from(document.querySelectorAll("[data-status]"));
  const empty = document.getElementById("empty");

  if (!buttons.length || !cards.length) return;

  const apply = (filter) => {
    let visible = 0;
    cards.forEach((card) => {
      const show = filter === "all" || card.dataset.status === filter;
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (empty) empty.hidden = visible !== 0;
    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.filter === filter);
    });
  };

  buttons.forEach((button) => {
    button.addEventListener("click", () => apply(button.dataset.filter || "all"));
  });
})();
