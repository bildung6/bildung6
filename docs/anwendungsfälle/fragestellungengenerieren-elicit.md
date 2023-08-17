---
description: "KI kann bei der Erstellung von Fragestellungen helfen, indem sie Vorschl\xE4\
  ge f\xFCr relevante und interessante Fragestellungen generiert."
id: fragestellungengenerieren-elicit
image: "anwendungsf\xE4lle/images/researching.svg"
tags:
- fragestellungen
- studierende
title: Fragestellungen generieren Elicit
type: usecase
---


# Fragestellungen generieren mit Elicit

Elicit kann dazu genutzt werden, um Denkanstösse bei der Formulierung der Fragestellung zu gewinnen.



## Beschreibung
Die Hauptfunktionalitäten dieses Research Assistenten zielen vor allem auf die Unterstützung bei der *Literaturrecherche* ab (Stand August 2023) (1). Zur Formulierung deiner Fragestellung kannst du diese Hauptfunktionen nutzen, um Literaturen zu identifizieren, aus der du deine eigene Fragestellung ableiten kannst.

Zudem gibt es einzelne Funktionalitäten oder *Research Task*, wie z.B. *Brainstorm Research Question*. Mit dem *Brainstorming* kannst du mehrere Vorschläge generieren lassen.

---

## Anwendungsbeispiele

### Mit *Brainstorm Research Question* Fragestellungen generieren

???+ info "Bemerkung"

    Wie sich hier erkennen lässt, generiert Elicit mit *Brainstorm Research Question* auch Vorschläge für spezifischeren Subtopics an.
    
    Bedenke hierbei, dass es an dir liegt die Relevanz dieser Vorschläge zu überprüfen.


Mit dem Elicit-Task *Brainstorm Research Question* kannst du Vorschläge zu Fragestellungen einholen.
Dabei kannst du deine Fragestellung als Ausgangspunkt verwenden oder auch nur einzelne Themenfelder angeben.

Im folgenden Beispiel werden die Begriffe "Medical Informatics" und "Care at Home" kombiniert, um Vorschläge für Fragestellungen zu generieren.

**Schritt 1: Auf den Task "Brainstorm Research Question" zugreifen ** 

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_1.png){: style="width:700px"}


**Schritt 2: Zwei Themenfelder angeben ** 

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_2.png){: style="width:700px"}

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_3.png){: style="width:700px"}


**Schritt 3: Weitere Vorschläge generieren ** 

Du kannst die für dich relevanten Fragestellungen markieren, um so weitere Vorschläge zu generieren.

Nutze hierbei die Buttons *Show more like starred* und *Clear unstarred*.

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_4.png){: style="width:500px"}


![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_5.png){: style="width:500px"}


![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_6.png){: style="width:500px"}


**Schritt 3: Auswahl eines Vorschlages ** 

Hast du dich für eine Fragestellung entschieden, kannst du diese Verwenden um mögliche Literaturen zu identifizieren.
Dazu *kopiere* die Fragestellung und *paste* sie in die Hauptfunktionalität rein.


![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_7b.png){: style="width:700px"}


Stelle dir nun eine Auswahl an Literaturen zusammen, die du Lesen willst um deine eigene Fragestellung zu formulieren.
Die Einarbeit in dein Thema ermöglicht dir herauszufinden, welche Implikationen sich aus den publizierten Forschungsresultate ergeben.


![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_8.png)


**Tipps:**

Es lässt sich auch direkt das Suchfeld der Hauptfunktionalität nutzen um Fragestellungen zu *brainstormen*:

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_9a.png){: style="width:500px"}

![alt text](../anwendungsfälle/images/elicit-brainstorm/elicit-brainstorm_9b.png){: style="width:500px"}

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

Bias


```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: abhängikeit
- condition: contains
  property: id
  value: bias-diskriminierung
- condition: contains
  property: id
  value: faehigkeit-komplexe-aufgaben-loesen-nimmt-ab
- condition: contains
  property: id
  value: gesellschaftlicher-bias
- condition: contains
  property: id
  value: kompetenzverlust
- condition: contains
  property: id
  value: nachvollziebarkeit
- condition: contains
  property: id
  value: verlust-kreativität
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kreative-anstoesse
```

---

## Links

Entwicklerseite:
- https://elicit.org/ 

Jan Hendrik Kirchner erklärt, wie er Elicit zur schnellen Erstellung von Forschungsvorschlägen nutzte.
- https://youtu.be/YO9UiBWx6jw

---

## Quellenverzeichnis
1.	FAQ | Elicit [Internet]. [zitiert 14. August 2023]. Verfügbar unter: https://elicit.org/faq

