/* Hunza Handicrafts — site behaviour
   Static demo only. No payment processing. */

/* ---------- Product data ---------- */

const PRODUCTS = [
  {
    id: "p1",
    name: "Handwoven Mountain Shawls",
    maker: "Zainab Bibi",
    valley: "Ganish",
    cat: "textiles",
    price: 8500,
    tag: "Handwoven",
    img: "images/handmade-shawls.jpg",
    desc: "Bright geometric shawls and runners — red, gold, yellow and teal — hung the way they are sold in the open-air market.",
    story: "These pieces come off narrow pit looms in Ganish and neighbouring villages. Each stripe and diamond is counted by hand; the long fringe is tied after the cloth leaves the loom. Zainab keeps a few colours on the rail at a time so buyers can see how the weave catches mountain light.",
    specs: { Material: "Handwoven wool & cotton blend", Pattern: "Traditional geometric bands", Finish: "Hand-tied fringe", "Time to make": "2–3 weeks per piece", Care: "Cold hand wash, dry flat" }
  },
  {
    id: "p2",
    name: "Embroidered Ladies Cap",
    maker: "Nasreen Karim",
    valley: "Gulmit",
    cat: "textiles",
    price: 3200,
    tag: "Hand-stitched",
    img: "images/handmade-ladies-hat.jpg",
    desc: "A structured flat-top cap in magenta, orange and black, dense with floral embroidery and tiny mirror work.",
    story: "Nasreen stitches these caps for weddings and festivals. The star on the crown and the hexagonal flower band are worked in cotton thread; small mirrors are set into the embroidery so the piece flashes in sunlight. One size, firm enough to keep its shape.",
    specs: { Material: "Embroidered cloth, mirror accents", Style: "Flat-top traditional topi", Colours: "Magenta, orange, black, white", "Time to make": "4–5 days", Care: "Spot clean only" }
  },
  {
    id: "p3",
    name: "Wool Pakol with Feather",
    maker: "Ghulam Abbas",
    valley: "Gulmit",
    cat: "textiles",
    price: 2800,
    tag: "Felted wool",
    img: "images/handmade-mens-cap.jpg",
    desc: "Cream felted pakol with a rolled brim and a white feather plume — the classic high-country cap.",
    story: "The pakol is felted from mountain wool, then rolled at the base so it can be pulled down over the ears when the wind rises. Ghulam adds the plume for ceremonial wear; without it, the same hat is everyday gear from Gilgit to Sost.",
    specs: { Material: "Felted mountain wool", Colour: "Natural cream", Accent: "Feather plume", Sizes: "One size, adjustable roll", Care: "Brush clean, keep dry" }
  },
  {
    id: "p4",
    name: "Tribal Embroidered Skullcap",
    maker: "Nasreen Karim",
    valley: "Passu",
    cat: "textiles",
    price: 2100,
    tag: "Hand-embroidered",
    img: "images/traditional-cap.jpg",
    desc: "A bright cylindrical topi covered in pink, yellow, purple and green floral-geometric stitch work.",
    story: "Every panel of this skullcap is filled with embroidery — no plain cloth showing through. Nasreen works the crown motif first, then the side band, finishing with a small knot at the edge. Made for everyday wear and for guests who want something clearly from the north.",
    specs: { Material: "Cotton embroidery on fabric base", Style: "Cylindrical tribal topi", Palette: "Magenta, yellow, purple, green", "Time to make": "3 days", Care: "Spot clean only" }
  },
  {
    id: "p5",
    name: "Hand-knotted Valley Carpet",
    maker: "Zainab Bibi",
    valley: "Karimabad",
    cat: "textiles",
    price: 45000,
    tag: "Hand-knotted",
    img: "images/handmade-carpets.jpg",
    desc: "Rich oriental carpets in rust, cream and indigo — medallions, tree-of-life motifs and tribal geometry.",
    story: "Carpets like these are knotted over months on upright looms. The rust medallion pieces and the cream pictorial rugs you see hanging in the shop are finished one knot at a time; smaller kilims on the floor are flat-woven for everyday use.",
    specs: { Material: "Hand-knotted wool pile", Motifs: "Medallion, tree of life, geometric", Origin: "Northern Pakistan weaving shops", "Time to make": "Several months", Care: "Professional clean, rotate yearly" }
  },
  {
    id: "p6",
    name: "Embroidered Cream Chogah",
    maker: "Karim Shah",
    valley: "Altit",
    cat: "textiles",
    price: 18500,
    tag: "Embroidered",
    img: "images/handmade-mens-chogah.jpg",
    desc: "Full-length cream coat with deep maroon embroidery along the front, cuffs and hem, worn with a matching belt.",
    story: "The chogah is the long open coat of the north — cream cloth for summer gatherings, heavy wool for winter. Karim’s version carries maroon floral and geometric borders down the front opening and around the cuffs, with a simple belt to shape the waist.",
    specs: { Material: "Woven cream cloth, maroon thread", Style: "Open-front belted coat", Length: "Full length", "Time to make": "About 3 weeks", Care: "Dry clean or gentle hand wash" }
  },
  {
    id: "p7",
    name: "Jute Shoulder Bag",
    maker: "Hunza Women's Co-op",
    valley: "Aliabad",
    cat: "accessories",
    price: 2200,
    tag: "Handmade",
    img: "images/handmade-wool-bag.jpg",
    desc: "Natural jute messenger bag with a multicolour woven band, lime-green trim and tassel fringe.",
    story: "The co-op weaves the colourful centre strip on a small loom, then stitches it onto a sturdy jute body. Lime binding finishes every edge; short jute tassels hang from the flap. Light enough for market days, tough enough for the jeep ride home.",
    specs: { Material: "Jute with woven accent band", Trim: "Lime-green cloth", Style: "Flap shoulder / cross-body", "Time to make": "2 days", Care: "Shake out, spot clean" }
  },
  {
    id: "p8",
    name: "Needlepoint Wallet Panel",
    maker: "Rukhsana Bano",
    valley: "Karimabad",
    cat: "accessories",
    price: 1800,
    tag: "Needlepoint",
    img: "images/handmade-wallet.jpg",
    desc: "Burgundy and charcoal star motifs on cream canvas, framed in a durable black border — a hand-stitched wallet face.",
    story: "Rukhsana works these panels on needlepoint canvas, alternating burgundy and charcoal star flowers down the centre with diamond borders on each side. The black edge protects the stitching when the piece is folded into a wallet or clutch.",
    specs: { Material: "Needlepoint on canvas, black border", Motif: "Geometric star flowers", Colours: "Cream, burgundy, charcoal", "Time to make": "About 1 week", Care: "Wipe clean, keep dry" }
  },
  {
    id: "p9",
    name: "Embroidered Men's Wallet",
    maker: "Rukhsana Bano",
    valley: "Karimabad",
    cat: "accessories",
    price: 2400,
    tag: "Hand-stitched",
    img: "images/handmade-mens-wallet.jpg",
    desc: "A compact traditional wallet finished with hand embroidery on the face — made for everyday pockets.",
    story: "Small enough for a shalwar pocket, sturdy enough for bazaar change. Rukhsana embroiders the outer panel, then lines and stitches the pockets by hand so the piece opens flat without the stitching pulling.",
    specs: { Material: "Embroidered cloth / fabric body", Style: "Folding men's wallet", Use: "Cards and notes", "Time to make": "3–4 days", Care: "Spot clean only" }
  },
  {
    id: "p10",
    name: "Lapis Lazuli Spearhead Necklace",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 6500,
    tag: "Natural stone",
    img: "images/lapis-lazuli-real-stone-necklace.jpg",
    desc: "Deep blue lapis disk beads with a carved spearhead pendant on an adjustable blue cord.",
    story: "Sher Ali cuts the pendant from a single piece of lapis so the gold flecks of pyrite stay visible. Matching disk beads are strung on cord with a simple tie closure — no clasp to lose on the trail.",
    specs: { Material: "Natural lapis lazuli, cord", Pendant: "Carved spearhead", Closure: "Adjustable tie", "Time to make": "2 days", Care: "Avoid chemicals and hard knocks" }
  },
  {
    id: "p11",
    name: "Ethnic Floral Stud Earrings",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 2900,
    tag: "Oxidized",
    img: "images/ethnic-earrings.png",
    desc: "Oxidized silver flower studs with dark faceted stones, a small jhumka drop and three pearl tips.",
    story: "The flower head is set with dark teardrop stones around a textured silver centre. Below it hangs a tiny engraved bell and a short pearl fringe — light enough for all-day wear, detailed enough for festive dress.",
    specs: { Material: "Oxidized silver-tone metal", Stones: "Dark faceted accents", Accents: "Pearl drops", Closure: "Post stud", Care: "Wipe dry after wear" }
  },
  {
    id: "p12",
    name: "Amethyst Silver Jewellery Set",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 12500,
    tag: "925 set",
    img: "images/amethyst-925-silver-set-680x911.jpg",
    desc: "Matching necklace, studs and ring — oval purple amethyst centres in a floral pavé silver setting.",
    story: "A full set for one occasion: pendant on a fine chain, matching studs, and a ring with the same scalloped halo of clear stones around a deep purple oval. Polished silver so the purple reads clean against white cloth.",
    specs: { Material: "925 silver-tone, amethyst stones", Includes: "Pendant, studs, ring", Style: "Floral halo", Occasion: "Formal / gift", Care: "Polish with a soft cloth" }
  },
  {
    id: "p13",
    name: "Blue Sapphire Silver Set",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 13500,
    tag: "925 set",
    img: "images/blue-sapphire-925-silver-set-680x911.jpg",
    desc: "Royal-blue oval stones in a petal halo — pendant, drop earrings and matching ring.",
    story: "The same floral-halo design as the amethyst set, cut in sapphire blue. Drop earrings hang from a small lever back; the pendant and ring share the oval centre and clear pavé border.",
    specs: { Material: "925 silver-tone, blue sapphire stones", Includes: "Pendant, drop earrings, ring", Style: "Floral halo", Occasion: "Formal / gift", Care: "Polish with a soft cloth" }
  },
  {
    id: "p14",
    name: "Black Tourmaline Silver Set",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 11800,
    tag: "925 set",
    img: "images/black-tourmaline-925-silver-set-572x1024.jpg",
    desc: "Dark tourmaline centres in polished silver — a quieter, evening version of the floral set.",
    story: "Black tourmaline reads almost ink-dark under the clear halo stones. Chosen when someone wants the same silhouette as the coloured sets without bright gem colour.",
    specs: { Material: "925 silver-tone, black tourmaline", Includes: "Matching set pieces", Style: "Floral halo", Finish: "Polished silver", Care: "Polish with a soft cloth" }
  },
  {
    id: "p15",
    name: "Oxidized Silver Stone Bangles",
    maker: "Rukhsana Bano",
    valley: "Karimabad",
    cat: "jewellery",
    price: 4800,
    tag: "Pair",
    img: "images/buy-silver-bangles-in-pakistan.jpg",
    desc: "Chunky oxidized bangles with green, red, black and blue cabochons and a traditional screw-pin clasp.",
    story: "These kada-style bangles are textured with granulation and mesh panels, then set with smooth cabochon stones. The screw-pin clasp is the old way of locking a thick bangle shut — secure, and part of the look.",
    specs: { Material: "Oxidized silver-tone metal", Stones: "Multi-colour cabochons", Sold: "As a pair", Closure: "Screw-pin clasp", Care: "Wipe dry; avoid perfume" }
  },
  {
    id: "p16",
    name: "Meenakari Turquoise Jhumkas",
    maker: "Rukhsana Bano",
    valley: "Karimabad",
    cat: "jewellery",
    price: 3400,
    tag: "Hand-painted",
    img: "images/meenakari-jhuka-earrings-handpainted.png",
    desc: "Gold-tone bell jhumkas with turquoise enamel, red floral meenakari and dangling blue beads.",
    story: "Meenakari is enamel painted into metal cells. Rukhsana fills the dome in turquoise, paints small red flowers with green leaves, then hangs a ring of turquoise beads from the rim so the earrings move when you walk.",
    specs: { Material: "Gold-tone metal, enamel, glass beads", Style: "Bell jhumka", Closure: "Fishhook", Colours: "Turquoise, red, gold", Care: "Keep dry; store separately" }
  },
  {
    id: "p17",
    name: "Pearl Moti Jhumka Earrings",
    maker: "Rukhsana Bano",
    valley: "Karimabad",
    cat: "jewellery",
    price: 3900,
    tag: "Pearl drops",
    img: "images/moti-jhumka-with-fresh-water-pearls.png",
    desc: "Classic jhumkas finished with freshwater pearl drops for weddings and festive wear.",
    story: "Moti means pearl — here, small freshwater pearls fringe the bell so the earrings catch light with every turn of the head. Made for bridal and Eid dressing, but light enough for an evening out.",
    specs: { Material: "Metal base, freshwater pearls", Style: "Traditional jhumka", Accent: "Pearl fringe", Occasion: "Festive / bridal", Care: "Wipe gently; avoid water" }
  },
  {
    id: "p18",
    name: "Oxidized Pearl Jhumka Earrings",
    maker: "Sher Ali",
    valley: "Karimabad",
    cat: "jewellery",
    price: 4200,
    tag: "Antique finish",
    img: "images/oxidized-silver-jhumka-earrings.jpg",
    desc: "Antique-finish jhumkas with red and green teardrop stones, engraved bell domes and a dense pearl fringe.",
    story: "Sher Ali darkens the silver so the floral engraving on each dome stands out. The studs carry red or green teardrop stones in filigree; the bells end in a full ring of white pearls.",
    specs: { Material: "Oxidized silver-tone metal, pearls", Stones: "Red & green teardrops", Style: "Statement jhumka", Finish: "Antique / oxidized", Care: "Wipe dry after wear" }
  },
  {
    id: "p19",
    name: "Woven Wool Market Bag",
    maker: "Hunza Women's Co-op",
    valley: "Aliabad",
    cat: "accessories",
    price: 2600,
    tag: "Handwoven",
    img: "images/wool-bag.jpg",
    desc: "A sturdy handwoven wool bag for market days — thick cloth, practical strap, made to be used hard.",
    story: "Thicker than the jute messenger, this wool bag is woven for carrying shopping through the bazaar. The co-op finishes each one with a strong strap and a simple closure so it survives jeep rides and crowded aisles.",
    specs: { Material: "Handwoven wool", Style: "Everyday market bag", Use: "Shoulder carry", "Time to make": "3–4 days", Care: "Spot clean, air dry" }
  }
];

const CATS = {
  textiles: "Textiles",
  jewellery: "Jewellery",
  accessories: "Bags & wallets"
};

const BG = {
  textiles: "#F1EBDD",
  jewellery: "#ECEDEA",
  accessories: "#EFE6DC"
};

/* ---------- Helpers ---------- */

const rs = (n) => "Rs " + n.toLocaleString("en-PK");
const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

/* ---------- Cart (in-memory only) ---------- */

let cart = [];

function addToCart(id) {
  const found = cart.find((l) => l.id === id);
  if (found) found.qty += 1;
  else cart.push({ id, qty: 1 });
  renderCart();
  openCart();
}

function setQty(id, delta) {
  const line = cart.find((l) => l.id === id);
  if (!line) return;
  line.qty += delta;
  if (line.qty <= 0) cart = cart.filter((l) => l.id !== id);
  renderCart();
}

function cartCount() {
  return cart.reduce((n, l) => n + l.qty, 0);
}

function cartTotal() {
  return cart.reduce((n, l) => {
    const p = PRODUCTS.find((x) => x.id === l.id);
    return n + p.price * l.qty;
  }, 0);
}

function renderCart() {
  const box = $("#cartItems");
  const countEl = $("#cartCount");
  const totalEl = $("#cartTotal");
  if (!box) return;

  if (!cart.length) {
    box.innerHTML = '<p class="cart-empty">Your cart is empty. Browse the shelf and add something made by hand.</p>';
  } else {
    box.innerHTML = cart
      .map((l) => {
        const p = PRODUCTS.find((x) => x.id === l.id);
        return `<div class="line">
          <div>
            <span class="line-name">${p.name}</span>
            <small>${p.maker} &middot; ${p.valley}</small>
            <div class="qty">
              <button type="button" data-minus="${p.id}" aria-label="Remove one ${p.name}">&minus;</button>
              <span>${l.qty}</span>
              <button type="button" data-plus="${p.id}" aria-label="Add one ${p.name}">+</button>
            </div>
          </div>
          <span>${rs(p.price * l.qty)}</span>
        </div>`;
      })
      .join("");
  }

  if (countEl) {
    const n = cartCount();
    countEl.textContent = n;
    countEl.style.display = n ? "inline-block" : "none";
  }
  if (totalEl) totalEl.textContent = rs(cartTotal());
}

function openCart() {
  $("#cart")?.classList.add("open");
  $("#overlay")?.classList.add("open");
}

function closeCart() {
  $("#cart")?.classList.remove("open");
  $("#overlay")?.classList.remove("open");
}

/* ---------- Product rendering ---------- */

function cardHTML(p) {
  return `<article class="card" data-cat="${p.cat}">
    <a class="card-art" href="product.html?id=${p.id}" aria-label="View ${p.name}">
      <span class="tag">${p.tag}</span>
      <img src="${p.img}" alt="${p.name}, made by ${p.maker} in ${p.valley}" loading="lazy" width="900" height="675">
    </a>
    <div class="card-body">
      <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
      <p class="maker">By <b>${p.maker}</b> &middot; ${p.valley}</p>
      <p class="desc">${p.desc}</p>
      <div class="card-foot">
        <span class="price">${rs(p.price)}</span>
        <button class="add" type="button" data-add="${p.id}">Add to cart</button>
      </div>
    </div>
  </article>`;
}

/* ---------- Product detail page ---------- */

function renderDetail() {
  const host = $("#detail");
  if (!host) return;
  const id = new URLSearchParams(location.search).get("id");
  const p = PRODUCTS.find((x) => x.id === id);

  if (!p) {
    host.innerHTML = `<div class="notfound">
      <h2>We can't find that piece</h2>
      <p>The link may be out of date. Everything we have is on the shelf.</p>
      <a class="btn" href="products.html">Back to the shelf</a>
    </div>`;
    return;
  }

  document.title = p.name + " — Hunza Handicrafts";

  const specs = Object.entries(p.specs)
    .map(([k, v]) => `<div class="spec"><dt>${k}</dt><dd>${v}</dd></div>`)
    .join("");

  const related = PRODUCTS.filter((x) => x.cat === p.cat && x.id !== p.id).slice(0, 3);

  host.innerHTML = `
    <nav class="crumbs">
      <a href="products.html">Shelf</a> <span>/</span>
      <a href="products.html?cat=${p.cat}">${CATS[p.cat]}</a> <span>/</span>
      <span>${p.name}</span>
    </nav>

    <div class="detail-grid">
      <figure class="detail-shot">
        <img src="${p.img}" alt="${p.name}" width="900" height="675">
        <figcaption>${p.tag} &middot; ${p.valley}</figcaption>
      </figure>

      <div class="detail-info">
        <p class="eyebrow">${CATS[p.cat]}</p>
        <h1>${p.name}</h1>
        <p class="maker big">By <b>${p.maker}</b> in ${p.valley}</p>
        <p class="price big">${rs(p.price)}</p>
        <p class="lede">${p.desc}</p>
        <button class="btn" type="button" data-add="${p.id}">Add to cart</button>
        <p class="note left">Demo store — no payment is taken.</p>

        <dl class="specs">${specs}</dl>
      </div>
    </div>

    <div class="detail-story prose">
      <h2>How it's made</h2>
      <p>${p.story}</p>
    </div>

    ${
      related.length
        ? `<div class="section-head" style="margin-top:3rem">
             <h2>More ${CATS[p.cat].toLowerCase()}</h2>
             <p>From the same craft.</p>
           </div>
           <div class="products">${related.map(cardHTML).join("")}</div>`
        : ""
    }
  `;
}

function renderProducts(filter = "all", target = "#productGrid", limit = null) {
  const grid = $(target);
  if (!grid) return;
  let list = filter === "all" ? PRODUCTS : PRODUCTS.filter((p) => p.cat === filter);
  if (limit) list = list.slice(0, limit);
  grid.innerHTML = list.map(cardHTML).join("");
}

/* ---------- Wire up ---------- */

document.addEventListener("DOMContentLoaded", () => {
  // Nav toggle
  $("#navToggle")?.addEventListener("click", () => {
    $("#nav").classList.toggle("open");
  });

  // Initial products
  const grid = $("#productGrid");
  if (grid) {
    const limit = grid.dataset.limit ? Number(grid.dataset.limit) : null;
    const start = new URLSearchParams(location.search).get("cat") || "all";
    renderProducts(start, "#productGrid", limit);
    $$(".chip").forEach((c) =>
      c.setAttribute("aria-pressed", String(c.dataset.filter === start))
    );
  }

  // Filters
  $$(".chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      $$(".chip").forEach((c) => c.setAttribute("aria-pressed", "false"));
      chip.setAttribute("aria-pressed", "true");
      renderProducts(chip.dataset.filter);
    });
  });

  // Delegated clicks
  document.addEventListener("click", (e) => {
    const add = e.target.closest("[data-add]");
    if (add) addToCart(add.dataset.add);

    const plus = e.target.closest("[data-plus]");
    if (plus) setQty(plus.dataset.plus, 1);

    const minus = e.target.closest("[data-minus]");
    if (minus) setQty(minus.dataset.minus, -1);
  });

  $("#cartOpen")?.addEventListener("click", openCart);
  $("#cartClose")?.addEventListener("click", closeCart);
  $("#overlay")?.addEventListener("click", closeCart);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeCart();
  });

  $("#checkout")?.addEventListener("click", () => {
    if (!cart.length) return;
    alert("This is a coursework demo, so there's no checkout. Your cart total is " + rs(cartTotal()) + ".");
  });

  renderDetail();
  renderCart();

  // Contact form
  const form = $("#contactForm");
  form?.addEventListener("submit", (e) => {
    e.preventDefault();
    let ok = true;
    ["name", "email", "message"].forEach((f) => {
      const input = $("#" + f);
      const err = $("#err-" + f);
      let bad = !input.value.trim();
      if (f === "email" && input.value.trim() && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(input.value)) bad = true;
      err.classList.toggle("show", bad);
      if (bad) ok = false;
    });
    if (ok) {
      $("#sent").classList.add("show");
      form.reset();
    }
  });
});
