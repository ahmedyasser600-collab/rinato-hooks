# rinato-hooks

Una skill gratuita per Claude che controlla il **primo secondo** dei tuoi reel prima che tu li pubblichi.
A free Claude skill that checks the **first second** of your reels before you post them. (English below.)

## Cosa fa

- Ti propone **3 hook diversi** per il tuo video: la frase detta, il testo a schermo, il primo fotogramma e il finale che li richiama.
- Dà un **voto da 0 a 100** a ciascuno e riscrive quelli sotto 80.
- Controlla il **ritmo** di tutto il video: se passano più di 15 secondi senza un momento forte, te lo segnala.

Le regole del controllo: il primo fotogramma si muove (mai un logo o una dissolvenza), la promessa arriva entro 1,5 secondi, testo e voce dicono la stessa cosa, e il video funziona anche muto.

## Installazione (circa 2 minuti)

**Su claude.ai**
1. Scarica `rinato-hooks.zip` da questa pagina (il file nella lista qui sopra, poi "Download raw file").
2. In Claude apri **Settings → Capabilities** e attiva **Code execution and file creation**.
3. Vai su **Customize → Skills**, premi **+**, poi **Create skill → Upload a skill**, e carica lo zip.
4. Scrivi a Claude: *"Scrivi 3 hook per un reel su …"*.

**Con Claude Code**
Copia la cartella `rinato-hooks/` in `~/.claude/skills/` (oppure in `.claude/skills/` del tuo progetto).

La skill è gratuita. Claude invece ha i suoi piani: le skill personalizzate su claude.ai richiedono l'esecuzione del codice attiva, e secondo la documentazione di Anthropic sono disponibili sui piani a pagamento (su quello gratuito le pagine di aiuto non sono concordi).

---

## English

**What it does:** 3 scored hook options for your video (spoken line, on-screen text, first frame, the ending it sets up), a 0–100 score that rejects weak hooks, and a pacing check that flags more than 15 seconds without a strong moment.

**Install (about 2 minutes).** claude.ai: download `rinato-hooks.zip`, turn on *Settings → Capabilities → Code execution and file creation*, then *Customize → Skills → + → Create skill → Upload a skill*. Claude Code: copy `rinato-hooks/` into `~/.claude/skills/`. The skill is free; custom skills on claude.ai need code execution and, per Anthropic's docs, a paid plan.

## Credits

- Story structure: Kane Kallaway's **Modern Story Arc** (summarised in our own words in `references/source-modern-story-arc.md`).
- Hook library: [rediumvex/viral-hooks-skill](https://github.com/rediumvex/viral-hooks-skill) `hooks-database.md`, MIT, copyright (c) 2026 Roman Knox. Its licence is kept in that file.
- Made by [Rinato Studio](https://rinato.studio), Padova.

## Licence

MIT (see `LICENSE`). The hook library keeps its own MIT notice.
