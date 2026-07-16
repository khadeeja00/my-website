# Hunza Handicrafts & Souvenir Store

A static e-commerce style website (no real payments) built with HTML, CSS and vanilla JavaScript.

## Structure

```
HunzaHandicrafts/
│── index.html      Homepage — hero image, categories, featured products
│── products.html   Full shelf with category filters
│── product.html    Single product detail (reads ?id= from the URL)
│── about.html      Artisans, valley map, craft methods
│── contact.html    Contact form with validation
│── README.md
│── css/
│   └── style.css
│── js/
│   └── main.js     Product data, cart, filters, detail page, validation
│── images/
    ├── hero-valley.jpg
    ├── shawl.jpg  cap.jpg  rug.jpg
    ├── bowl.jpg   panel.jpg
    ├── pendant.jpg  cuff.jpg
    └── apricots.jpg  bottle.jpg
```

## Features

- Nine products across four categories, rendered from a JS data array
- Individual product pages with materials, dimensions, time-to-make and a "how it's made" story
- Category filtering on the shop page (also works via `products.html?cat=textiles`)
- Slide-out shopping cart UI with add, increase, decrease and running total
- Contact form with client-side validation and a success state
- Artisan profiles cross-linked to the pieces each person makes
- SVG map of the valley showing which village each craft comes from
- Responsive down to mobile, keyboard focus states, reduced-motion support

## Publish on GitHub Pages

1. Create a new repository on GitHub (public).
2. Upload every file and folder from this project into the repo root — `index.html` must sit at the top level, not inside a subfolder.
3. Go to **Settings → Pages**.
4. Under **Source**, choose **Deploy from a branch**.
5. Pick branch `main` and folder `/ (root)`, then **Save**.
6. Wait a minute or two. Your site appears at `https://<your-username>.github.io/<repo-name>/`.

Via command line instead:

```bash
git init
git add .
git commit -m "Hunza Handicrafts static site"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Then follow steps 3–6 above.

## Notes

- Product images were generated procedurally with Python/Pillow (`gen_images.py` is included if you want to regenerate or tweak them). To use real photographs instead, drop them into `images/` and update the `img:` field for that product in `js/main.js` — no other changes needed.
- Product detail pages are driven by a query string (`product.html?id=p3`), which works on GitHub Pages because it's all client-side.
- The checkout button is intentionally non-functional — it shows an alert explaining this is a demo.
- Cart contents are held in memory and reset on page refresh, which is expected for a static coursework site.
