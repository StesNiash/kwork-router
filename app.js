(() => {
  const grid = document.getElementById("service-grid");
  const empty = document.getElementById("empty");
  const loadError = document.getElementById("load-error");
  const buttons = Array.from(document.querySelectorAll("[data-filter]"));
  if (!grid) return;

  const escapeHtml = (value) =>
    String(value).replace(/[&<>"']/g, (character) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    }[character]));

  const statusLabel = (status) => {
    if (status === "active") return "опубликовано";
    if (status === "ready") return "демо готово";
    return "в работе";
  };

  const cardHtml = (item) => {
    const links = [];
    if (item.card) {
      links.push(`<a class="card-link" href="${escapeHtml(item.card)}">Текст карточки</a>`);
    }
    if (item.repo_url) {
      links.push(`<a class="card-link" href="${escapeHtml(item.repo_url)}" target="_blank" rel="noreferrer">Демо</a>`);
    }
    if (!links.length) {
      links.push('<span class="card-link is-muted">Скоро</span>');
    }
    const bullets = item.bullets.map((bullet) => `<li>${escapeHtml(bullet)}</li>`).join("");
    const chipClass = item.status === "planned" ? "chip" : "chip chip-active";
    return `
      <article class="card card-${escapeHtml(item.tone)}" data-status="${escapeHtml(item.status)}">
        <div class="card-top">
          <span class="number">${String(item.number).padStart(2, "0")}</span>
          <span class="${chipClass}">${statusLabel(item.status)}</span>
        </div>
        <h3>${escapeHtml(item.title)}</h3>
        <p>${escapeHtml(item.summary)}</p>
        <ul>${bullets}</ul>
        <div class="card-meta"><span>${escapeHtml(item.term)}</span><strong>от ${Number(item.price_from).toLocaleString("ru-RU")} ₽</strong></div>
        <div class="card-links">${links.join("")}</div>
      </article>`;
  };

  let families = [];
  const apply = (filter) => {
    let visible = 0;
    grid.querySelectorAll("[data-status]").forEach((card) => {
      const status = card.dataset.status;
      const show = filter === "all"
        || (filter === "ready" && (status === "active" || status === "ready"))
        || status === filter;
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (empty) empty.hidden = visible !== 0;
    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.filter === filter);
    });
  };

  fetch("data/services.json", { cache: "no-store" })
    .then((response) => {
      if (!response.ok) throw new Error(`catalog request failed: ${response.status}`);
      return response.json();
    })
    .then((data) => {
      families = data.families;
      grid.innerHTML = families.map(cardHtml).join("");
      document.getElementById("stat-total").textContent = String(families.length);
      document.getElementById("stat-ready").textContent = String(families.filter((item) => item.status === "active" || item.status === "ready").length);
      document.getElementById("stat-active").textContent = String(families.filter((item) => item.status === "active").length);
      buttons.forEach((button) => {
        button.addEventListener("click", () => apply(button.dataset.filter || "all"));
      });
      apply("all");
    })
    .catch((error) => {
      if (loadError) loadError.hidden = false;
      if (grid) grid.innerHTML = "";
      console.error(error);
    });
})();
