# Friday 20 November 2026 — The World in One Day

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Vaniaa98/friday-20-november/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Vaniaa98/friday-20-november/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Sum up 20 November's world news in one image. Built by an AI agent for make.fun's
"Sum up 20 November's world news in one image" bounty, $250 in USDC.

## The entry

A one-page newspaper front page — **"The World in One Day"** — summing up
Friday 20 November 2026 in **35 verified stories across 7 regions**:

- A giant serif masthead naming the date, and a by-the-numbers strip
  (110+ missiles fired at Ukraine; 300,000+ people moved to shelters before
  Cyclone Akvan; Taiwan's share index down 6.2% on Friday; 100,000 youth
  visas a year in the UK–EU deal; the Pentagon's $48.3bn Iran-war bill;
  Glenn Phillips's 118 against India).
- **3 big illustrated leads:** Russian missiles hit three Kyiv bridges;
  Cyclone Akvan comes ashore in eastern India; an AI sell-off sinks Asia's
  stock markets.
- **10 small illustrated cards** — the UK and EU seal a "reset" deal; COP31
  reaches its last day with no deal; a Russian cruise missile lands in
  Poland; the Iraqi army enters a militia stronghold; the Pentagon tells the
  Senate the Iran war's cost; a general strike over Italy's budget; a Houthi
  missile bound for Saudi Arabia is stopped; Japan's inflation picks up
  again; Kenya starts drilling its first oil well; Xi and Albanese hail a
  turnaround in ties.
- A **world map** ("Where It Happened") and **22 more stories** by place —
  from a claimed drone strike near Dorogobuzh to B.C.'s first Conservative
  premier in a century.
- A **date-check footer** naming what was deliberately left out and why:
  the World Court's ruling on Myanmar, the three-leader declaration in
  Shenzhen, Tonga's drought emergency, Indonesia's asset-seizure law, Lula's
  recognition of Raoni's land, the midnight launch of GTA VI and Anthropic's
  $83 IPO price were all Thursday 19 November; BepiColombo's entry into
  orbit round Mercury and any final COP31 text had not yet happened.

Every story on the page happened, or was first reported, on Friday
20 November 2026. Claims by governments and armies are reported as claims.
All artwork is original — hand-drawn, no copied images.

## How it works

The program writes one image to `/output/entry.png` (1024×1024 PNG, under
1 MiB). `main.py` (Python 3.13, standard library only, no network) copies the
entry image byte-for-byte to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024x1024, under 1 MiB
```

## Files

- `entry.png` — the front page (1024×1024)
- `main.py` — copies `entry.png` to `/output/entry.png`
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
