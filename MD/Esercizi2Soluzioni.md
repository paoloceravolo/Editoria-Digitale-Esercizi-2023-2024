# Esercizi avanzati di Pandoc con Soluzioni

Benvenuto a questi esercizi di Pandoc. Scopriremo come utilizzare Pandoc per svolgere diverse trasformazioni sui documenti. Prima di svolgere gli esercizi, assicurati di avere Pandoc installato sul tuo sistema.

## Esercizio 1: Usare i filtri

**Richiesta:** Esegui un semplice script per personalizzare la trasformazione eseguita da Pandoc.

**Soluzione:**

Un filtro in Pandoc è un programma esterno che può essere utilizzato per modificare o trasformare il contenuto del documento durante la conversione. Può essere scritto in qualsiasi linguaggio di programmazione che supporti l'input e l'output da riga di comando.

Ecco un semplice esempio di filtro Pandoc scritto in Python. In questo esempio, creeremo un filtro per sostituire tutte le istanze della parola "Gatto" con "Cane" in un documento di testo 

```bash
#!/usr/bin/env python
import panflute as pf

def replace_text(elem, doc):
    if isinstance(elem, pf.Str) and elem.text == "the editor":
        elem.text = "Markdown"

if __name__ == "__main__":
    pf.toJSONFilter(replace_text)

```
Salviamo il file come ``replace.py``

Attirbuiamo al file i permessi di esecuzione

```
chmod +x replace.py
```

Eseguiamo il comando seguente per applicare il filtro:

```bash
pandoc input.md --filter ./replace.py -o output.pdf
```


Per poterlo eseguire è nceessario aver installato Python e 
