---
description: "Elicit kann bei der Erstellung von Fragestellungen helfen, indem es Vorschl\xE4\
  ge generiert."
id: fragestellungengenerieren-elicit
image: "anwendungsf\xE4lle/images/researching.svg"
tags:
- fragestellungen
- studierende
title: Fragestellungen generieren mit Elicit
type: usecase
---


# Fragestellungen generieren mit Elicit

Elicit kann bei der Erstellung von Fragestellungen helfen, indem es Vorschläge generiert.


## Beschreibung
Die Hauptfunktionalitäten dieses Research Assistenten zielen vor allem auf die Unterstützung bei der *Literaturrecherche* ab (Stand August 2023) (1). Zur Formulierung deiner Fragestellung kannst du diese Hauptfunktionen nutzen, um Fachpublikationen zu identifizieren, aus der du deine eigene Fragestellung ableiten kannst. Oder du nutzt das Tool um zu prüfen, ob es bereits Publikationen gibt, die deine Forschungsfrage adressieren oder gar beantworten.

Zudem bietet das Tool einzelne Funktionalitäten oder *Research Task*, wie z.B. *Brainstorm Research Question*. Mit dem *Brainstorming* kannst du mehrere Vorschläge generieren lassen.


---


## Beispiel

Dieses Beispiel zeigt, wie mit Elicit mehrere Fragestellungen generiert werden können.

### Mit "Brainstorm Research Question" Fragestellungen generieren

Mit dem Elicit-Task *Brainstorm Research Question* kannst du Vorschläge zu Fragestellungen einholen.
Dabei kannst du deine Fragestellung als Ausgangspunkt verwenden oder auch nur einzelne Themenfelder angeben.

Im folgenden Beispiel werden die Begriffe "Medical Informatics" und "Care at Home" kombiniert, um Vorschläge für Fragestellungen zu generieren.

???+ info "Bemerkung"

    Wie sich hier erkennen lässt, generiert Elicit mit *Brainstorm Research Question* auch Vorschläge für spezifischeren Subtopics an.
    
    Bedenke hierbei, dass es an dir liegt die Relevanz dieser Vorschläge zu überprüfen.



| Beispiel: Step-by-Step zur Fragestellung                                              |
| :------------------------------------------------------------------------------------ |
| **1. Auf den Task "Brainstorm Research Question" zugreifen**                          | 
| ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_1.png)      |
| **2. Themenfelder angeben**<br>Gib eine Fragestellung, Keywords oder Themenfelder ein.| 
| ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_3.png)      |
| **3. Weitere Vorschläge generieren**<br> Du kannst die relevanten Fragestellungen markieren, um so weitere Vorschläge zu generieren. <br> Nutze hierbei die Buttons *Show more like starred* und *Clear unstarred.*|
| ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_4.png) |
| **4. Auswahl eines Vorschlages**<br>Wenn du dich für eine Fragestellung entschieden hast, kannst du diese verwenden, um mögliche Literatur zu identifizieren. Kopiere dazu die Fragestellung und füge sie in die Hauptfunktionalität ein.| 
| ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_7b.png){: style="width:700px"} |
| **5. Passende Literaturen auswählen** <br>Stelle dir nun eine Auswahl an Literaturen zusammen, die du lesen willst, um deine eigene Fragestellung zu formulieren. Die Einarbeit in dein Thema ermöglicht dir herauszufinden, welche Implikationen sich aus den publizierten Forschungsresultate ergeben.|
| ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_8.png)      | 


!!! Tip  "Tipp"

    Es lässt sich auch direkt das Suchfeld der Hauptfunktionalität nutzen, um Fragestellungen zu *brainstormen*:

    ![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_9a.png){: style="width:500px"}


---


## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: elicit
```


---


## Risiken


```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: bias-diskriminierung
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: nachvollziehbarkeit
```


---


## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kompetenzerwerb-durch-ki
- condition: contains
  property: id
  value: zweitmeinung
```


---


## Links

Elicit:

- Elict App: https://elicit.org/
- Elicit FAQ: https://elicit.org/faq
- Entwicklerseiter: https://ought.org/elicit
- Youtube Channel: https://www.youtube.com/@Oughtinc

Jan Hendrik Kirchner erklärt, wie er Elicit zur schnellen Erstellung von Forschungsvorschlägen nutzte.

- https://youtu.be/YO9UiBWx6jw


---


## Quellen

1.	FAQ | Elicit [Internet]. [zitiert 14. August 2023]. Verfügbar unter: https://elicit.org/faq

