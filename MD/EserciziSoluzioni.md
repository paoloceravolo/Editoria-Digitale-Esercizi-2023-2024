# Esercizi di Pandoc con Soluzioni

Benvenuto a questi esercizi di Pandoc. Scopriremo come utilizzare Pandoc per svolgere diverse trasformazioni sui documenti. Prima di svolgere gli esercizi, assicurati di avere Pandoc installato sul tuo sistema.

## Esercizio 1: Conversione da Markdown a HTML

**Richiesta:** Converti il file "input.md" in un documento HTML chiamato "output.html".

**Soluzione:**

```bash
pandoc input.md -o output.html
```

## Esercizio 2: Conversione da Markdown a PDF

**Richiesta**: Converti il file
 "input.md" in un documento PDF chiamato "output.pdf".


**Soluzione**:	

```bash
pandoc input.md -o output.pdf
```

## Esercizio 3: Aggiungi un Titolo

**Richiesta**: Aggiungi un titolo "Il Mio Documento" al documento Markdown.

**Soluzione**:

```bash
---
title: Il Mio Documento
---
```

## Esercizio 4: Personalizza un Titolo

**Richiesta**: Personalizza il titolo in grassetto e rosso.

**Soluzione**:

```bash
# **Il Mio Documento**
```

## Esercizio 5: Crea una Lista Puntata

**Richiesta**: Crea una lista puntata di tre elementi nel tuo documento.

**Soluzione**:

```bash
- Elemento 1
- Elemento 2
- Elemento 3
```

## Esercizio 6: Crea una Lista Numerata

**Richiesta**: Crea una lista numerata di tre elementi nel tuo documento.

**Soluzione**:

```bash
1. Elemento 1
2. Elemento 2
3. Elemento 3
```

## Esercizio 7: Inserisci un Collegamento

Richiesta: Inserisci un collegamento ipertestuale a Google nel tuo documento.

**Soluzione**:

```bash
[Google](https://www.google.com)
```

## Esercizio 8: Cita una Fonte

**Richiesta**: Aggiungi una citazione nel tuo documento.

**Soluzione**:

Aggiungi una citazione nel documento

```bash
Come sostenuto da [@barbon2020evaluating].
```

Prepare un file .bib contentente i metadati della citazione 

```bash
@inproceedings{barbon2020evaluating,
  title={Evaluating trace encoding methods in process mining},
  author={Barbon Junior, Sylvio and Ceravolo, Paolo and Damiani, Ernesto and Marques Tavares, Gabriel},
  booktitle={International Symposium: From Data to Models and Back},
  year={2020},
}
```

Esegui Pandoc passando i parametri opportuni

```bash
pandoc --citeproc --bibliography=ref.bib -s input.md -o output.pdf
```


## Esercizio 9: Applica un Foglio di Stile CSS

**Richiesta**: Applica uno stile CSS personalizzato al tuo documento HTML.

**Soluzione**:

```bash
pandoc -s input.md -o output.html --css style.css
```

## Esercizio 10: Genera un TOC

**Richiesta**: Genera un indice automatico delle sezioni nel tuo documento. Produci come output un file PDF.

**Soluzione**:

```bash
pandoc input.md -o output.pdf --toc
```

## Esercizio 11: Modifica il Layout

**Richiesta**: Personalizza il layout del tuo documento PDF, ad esempio aggiungendo un'intestazione e un piè di pagina.

**Soluzione**:

```bash
---
header-includes:
    - \usepackage{fancyhdr}
    - \pagestyle{fancy}
    - \lhead{Editoria Digitale}
    - \rhead{@UNIMI}
    - \lfoot{Tutti i diritti riservati}
    - \rfoot{!!}
---
```

## Esercizio 12: Converti in un Documento Word

**Richiesta**: Converti il documento Markdown in un file Word.

**Soluzione**:

```bash
pandoc input.md -o output.docx
```

## Esercizio 13: Utilizza Filtri Personalizzati

**Richiesta**: Applica un filtro personalizzato per manipolare il contenuto del documento durante la conversione.

**Soluzione**:

Assicurati che Python sia installato

Assicurati che ``pandocfilters`` sia installato

```bash
pip install pandocfilters
```

Definisci lo script del filtro 

```bash
import pandocfilters as pf
import datetime

def replace_date(key, value, format, meta):
	if key == "Header" and value[0] == 4:
		text = pf.stringify(value[2])
		current_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Get the current date in the desired format
		updated_text = text.replace("#### Aggiornato il", "#### Aggiornato il " + current_date)
		return pf.Header(value[0], [value[1], value[2], pf.Str(updated_text)])

if __name__ == "__main__":
	pf.toJSONFilter(replace_date)
```

Esegui il filtro attraverso l'opportuno comando Pandoc

```bash
pandoc input.md -o output.pdf --filter ./data_repalce.py
```

## Esercizio 14: Crea una Presentazione

**Richiesta**: Converti il documento Markdown in una presentazione usando un formato come Beamer.

**Soluzione**:

```bash
pandoc input.md -t beamer -o output.pdf
```

## Esercizio 15: Specifica Metadati da un File

**Richiesta**: Specifica i metadati da un file YAML esterno.

**Soluzione**:

```bash
---
title: "Il Mio Documento"
author: "Nome Autore"
date: "2023-11-02"
---
```

## Esercizio 16: Gestisci Riferimenti Bibliografici

**Richiesta**: Gestisci le citazioni e i riferimenti bibliografici nel tuo documento utilizzando un file CSL e una bibliografia.

**Soluzione**:

```bash
---
bibliography: ref.bib
csl: IEEE.csl
---
```

## Esercizio 17: Aggiungi una Nota a Piè di Pagina

**Richiesta**: Aggiungi una nota a piè di pagina al tuo documento.

**Soluzione**:

```bash
This is some text[^1].

[^1]: This is a footnote.
```

## Esercizio 18: Applica un Layout Personalizzato

**Richiesta**: Applica un layout personalizzato con colonne e blocchi laterali.

**Soluzione**:

```bash
---
geometry: margin=1in
---

# Colonna Principale

Testo principale del documento.

::: {.colonna-laterale}
Contenuto della colonna laterale.
:::

```