---
description: "Elicit kann bei der Literaturrecherche behilflich sein, indem es relevante Artikel und Studien identifiziert und zur Auswahl stellt."
id: literaturrecherche-elicit
image: "anwendungsfälle/images/choose_editedinsgtar.svg"
tags:
- literaturrecherche
- studierende
title: Literaturrecherche mit Elicit
type: usecase
---


# Literaturrecherche mit Elicit
Elicit kann bei der Literaturrecherche behilflich sein, indem es relevante Artikel und Studien identifiziert und zur Auswahl stellt.

## Beschreibung

Elicit, entwickelt von Ought, ist ein KI-gestütztes Tool, das speziell für die Literaturrecherche konzipiert wurde. Es hilft dabei, sogenannte "Seed-Artikel" zu finden und gezielt nach Schlüsselwörtern und Themen zu suchen.

Elicit nutzt Sprachmodelle, um Forschungsvorgänge wie die Literaturübersicht zu automatisieren. Es kann relevante Artikel auch ohne exakte Schlüsselwortübereinstimmung finden.

Diese werden in einer Tabelle angezeigt, welche zusätzliche Filter- oder Suchfunktionen bietet und somit die Verwaltung erleichtert.

Zudem bietet das Tool Zusammenfassungen an, welche die Kernaussagen und wichtigen Informationen aus den Texten aufbereiten. Dies bedeutet, dass du anhand einer Fragestellung gezielt relevante Artikel suchen lassen kannst.

Die Basisfunktionen, wie die Recherche nach Artikeln und deren Zusammenfassung, sind kostenlos. Mit einem kostenpflichtigen Konto stehen jedoch erweiterte Funktionen zur Verfügung.

Für weitere Informationen siehe bitte: https://support.elicit.com/

---



---

## Tools 

```yaml
condition: or
entityType: tool
rules:
- condition: equals
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
```


---


## Links

Elicit:

- Elict App: https://elicit.org/
- Weitere Informationen: https://support.elicit.com/

Jan Hendrik Kirchner erklärt, wie er Elicit zur schnellen Erstellung von Forschungsvorschlägen nutzte:

- https://youtu.be/YO9UiBWx6jw


