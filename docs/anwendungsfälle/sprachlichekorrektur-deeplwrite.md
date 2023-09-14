---
description: "DeepL Write ist ein KI-Schreibassistent, der Studierende bei der sprachlichen Korrektur ihrer Texte unterst\xFCtzt."
id: sprachlichekorrektur-deeplwrite
image: "anwendungsf\xE4lle/images/decide.svg"
tags:
- sprachlichekorrektur
- studierende
title: Sprachliche Korrektur mit DeepL Write
type: usecase
---


# Sprachliche Korrektur mit DeepL Write
DeepL Write ist ein KI-Schreibassistent, der Studierende bei der sprachlichen Korrektur ihrer Texte unterstützt.

## Beschreibung

DeepL Write ist ein KI-basierter Schreibassistent, der Texte hinsichtlich Grammatik, Rechtschreibung und Stil optimiert. Studierende können mithilfe von DeepL Write ihre wissenschaftlichen Arbeiten sprachlich verfeinern, wodurch Grammatik, Rechtschreibung und Stil auf hohem Niveau sichergestellt werden können. 

Der zu überarbeitende Text kann einfach in das dafür vorgesehene Textfenster eingefügt werden; das Tool erkennt und korrigiert Fehler automatisch, wobei Verbesserungsvorschläge im rechten Textfenster grün markiert werden.

**Bitte beachte die geltenden Richtlinien deiner Bildungseinrichtung zur Verwendung von KI-Tools! Gegebenenfalls musst du die Verwendung von KI-basierten Werkzeugen zur sprachlichen Korrektur in deiner schriftlichen Arbeit deklarieren (z.B. explizit in der Methodik erwähnen oder durch einen pauschalen Hinweis andeuten).**


---


## Beispiel

In diesem Beispiel wurde links Text eingefügt. Rechts zeigt DeepL Write den korrigierten Text an, bei dem die geänderten Teile grün markiert sind.

Im rechten Feld kann der Text weiter bearbeitet werden. Zum Beispiel kann ein Wort angeklickt werden, um eine alternative Bezeichnung auszuwählen. Hier können auch ganze Sätze umformuliert werden, indem oben im Dropdown-Menü die Option "Ganzer Satz" ausgewählt wird.

Das folgende Beispiel zeigt, dass DeepL Write einzelne Fehler korrigiert und die Punktuation verbessert hatte. Ausserdem wurde eine formalere Schreibweise erreicht:

![alt text](../anwendungsfälle/images/deeplwrite-sprachlichekorrektur/deeplwrite-1.png)


???+ info "Bemerkung"

    DeepL Write befindet sich im August 2023 noch in der Beta-Phase, was sich auf die Performance auswirken kann.

    Es ist auch möglich, einen Stil zu wählen (Einfach, Geschäftlich, Akademisch, Technisch), aber dies scheint derzeit noch fehlerbehaftet zu sein (Stand August 2023).


!!! Tip  "Tipp"

    Versuche längere Texte abschnittsweise einzufügen. Bei der kostenlosen Version von DeepL Write ist die Zeichenlimite auf 2000 Zeichen gesetzt (Stand August 2023).  
      
    

---


## Tools 

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: deepl-write
```


---


## Risiken


```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: geschuetzte-daten
- condition: equals
  property: id
  value: plagiate
```


---


## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: equals
  property: id
  value: kompetenzerwerb-durch-ki
- condition: equals
  property: id
  value: kompetenzfoerderung
- condition: equals
  property: id
  value: sprachliche-barrieren-aufloesen
```


---


## Links

- DeepL Write App: https://www.deepl.com/write
- DeepL Write Beschreibung: https://support.deepl.com/hc/de/articles/6318834492700-DeepL-Write 

