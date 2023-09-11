---
description: "KI kann verwendet werden, um die sprachliche Korrektur von Studierenden\
  \ zu unterst\xFCtzen. Dies kann in Form von automatischen Korrekturen oder als Feedback\
  \ f\xFCr Studierende erfolgen."
id: sprachlichekorrektur-deeplwrite
image: "anwendungsf\xE4lle/images/decide.svg"
tags:
- sprachlichekorrektur
- studierende
title: Sprachliche Korrektur mit DeepL Write
type: usecase
---


# Sprachliche Korrektur mit DeepL Write


## Beschreibung

DeepL Write ist ein KI-basierter Schreibassistent, der Texte hinsichtlich Grammatik, Rechtschreibung und Stil optimiert. 

Studierende können mithilfe von DeepL Write ihre wissenschaftlichen Arbeiten sprachlich verfeinern, wodurch Grammatik, Rechtschreibung und Stil auf hohem Niveau sichergestellt werden können. 

Der zu bearbeitende Text kann einfach in das dafür vorgesehene Textfenster eingefügt werden; das Tool erkennt und korrigiert Fehler automatisch, wobei Verbesserungsvorschläge im rechten Textfenster grün markiert werden. 

**Bitte beachte die geltenden Richtlinien deiner Bildungseinrichtung zur Verwendung von KI-Tools! Gegebenenfalls musst du die Verwendung von KBW zur sprachlichen Korrektur in deiner schriftlichen Arbeit deklarieren (z.B. explizit in der Methodik erwähnen oder durch einen pauschalen Hinweis andeuten).**


---


## Beispiel

???+ info "Bemerkung"

    DeepL Write befindet sich im August 2023 noch in der Beta-Phase, was sich auf die Performance auswirken kann.


In diesem Beispiel wurde links ein Text eingefügt. DeepL Write zeigt rechts den korrigierten Text an, bei dem die geänderten Teile grün markiert sind. 

Im rechten Feld kann der Text weiter bearbeitet werden. Zum Beispiel kann ein Wort angeklickt werden, um eine alternative Bezeichnung auszuwählen. Hier können auch ganze Sätze umformuliert werden, indem oben im Drop-Down-Menü die Option "Ganzer Satz" ausgewählt wird.

Das folgende Beispiel zeigt, dass DeepL Write einzelne Fehler korrigiert und die Punktuation verbessert hatte. Ausserdem wurde eine formalere Schreibweise erreicht.

![alt text](../anwendungsfälle/images/deeplwrite-sprachlichekorrektur/deeplwrite-1.png)


**Tipp:** 

- Versuche längere Texte abschnittsweise einzufügen. Bei der kostenlosen Version von DeepL Write ist die Zeichenlimite auf 2000 Zeichen gesetzt (Stand August 2023).  
  
- Es ist auch möglich, den Stil zu wählen (Einfach, Geschäftlich, Akademisch, Technisch), aber dies scheint zur Zeit noch fehlerbehaftet zu sein (Stand August 2023).

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
- condition: contains
  property: id
  value: fehlende-transparenz
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

---


## Quellen


