# Apna Search Engine khud banao 🔍 (build-your-own-x)

Google ka asli secret = **inverted index**. Ye 15 lines ka Python code ek chhota search engine banata hai.

- `index` → har **word** ke aage likha hai wo kin **document IDs** mein hai (bilkul kitaab ke peeche wale index jaisa)
- `search()` → query ke har word ke IDs nikaalo, jo **sabmein common** hai wahi result (set intersection)

## Run karo

```bash
python search.py
# python -> {1, 3}
# python website -> [3]
```

💻 Browser mein chalao (free editor): https://techbroz-code.sites.tab.bot/#l=python&c=ZG9jcyA9IHsxOiAicHl0aG9uIHNlZWtobyBmcmVlIG1laW4iLAogICAgICAgIDI6ICJqYXZhc2NyaXB0IHNlIHdlYnNpdGUgYmFuYW8iLAogICAgICAgIDM6ICJweXRob24gc2Ugd2Vic2l0ZSBhdXIgQUkifQoKaW5kZXggPSB7fQpmb3IgaSwgdGV4dCBpbiBkb2NzLml0ZW1zKCk6CiAgICBmb3Igd29yZCBpbiB0ZXh0LnNwbGl0KCk6CiAgICAgICAgaW5kZXguc2V0ZGVmYXVsdCh3b3JkLCBzZXQoKSkuYWRkKGkpCgpkZWYgc2VhcmNoKHEpOgogICAgaWRzID0gW2luZGV4LmdldCh3LCBzZXQoKSkKICAgICAgICAgICBmb3IgdyBpbiBxLnNwbGl0KCldCiAgICByZXR1cm4gc29ydGVkKHNldC5pbnRlcnNlY3Rpb24oKmlkcykpCgpwcmludCgicHl0aG9uIC0-IiwgaW5kZXhbInB5dGhvbiJdKQpwcmludCgicHl0aG9uIHdlYnNpdGUgLT4iLAogICAgICBzZWFyY2goInB5dGhvbiB3ZWJzaXRlIikpCg

📚 Full tutorials (Build your own Search Engine): https://github.com/codecrafters-io/build-your-own-x#build-your-own-search-engine

🎬 YouTube video: link soon

Made by Tech Bro Z — YouTube @techbrozdeveloper, Instagram @tech_bro_z_1
