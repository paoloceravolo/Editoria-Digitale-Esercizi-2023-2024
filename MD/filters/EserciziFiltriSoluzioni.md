# Esercizi avanzati di Pandoc con Soluzioni

Benvenuto a questi esercizi di Pandoc. Scopriremo come utilizzare Pandoc per svolgere diverse trasformazioni sui documenti. Prima di svolgere gli esercizi, assicurati di avere Pandoc installato sul tuo sistema.

## Esercizio 1: Usare i filtri

**Richiesta:** Esegui un semplice script per personalizzare la trasformazione eseguita da Pandoc.

**Soluzione:**

Un filtro in Pandoc è un programma esterno che può essere utilizzato per modificare o trasformare il contenuto del documento durante la conversione. Può essere scritto in qualsiasi linguaggio di programmazione che supporti l'input e l'output da riga di comando.

Ecco un semplice esempio di filtro Pandoc scritto in Python. In questo esempio, creeremo un filtro per sostituire tutte le istanze della parola "Gatto" con "Cane" in un documento di testo 

```bash
#!/usr/bin/env python3

from panflute import *

def action(elem, doc):
    if isinstance(elem, Header):
        elem.level = 1

def main(doc=None):
    return run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()
```
Salviamo il file come ``ToLevel1.py``

Attirbuiamo al file i permessi di esecuzione

```
chmod +x ToLevel1.py
```

Eseguiamo il comando seguente per applicare il filtro:

```bash
pandoc input.md --filter ./ToLevel1.py -o output.pdf
```

Per poterlo eseguire è nceessario aver installato Python e la libreria panflute

```bash
pip install panflute
```

Per indicare al OS quale istallazioen di Python eseguire è necessario indicarlo nell'intestazione con ``#!/usr/bin/env python3`` 