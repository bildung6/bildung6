---
id: ideengenerieren
description: "KI kann bei der Ideenfindung helfen, indem sie Vorschläge generiert."
image: "anwendungsfälle/images/lightbulb_idee.svg" 
tags:
- ideen
- studierende
title: Ideen generieren
type: usecase
---



# Ideen generieren

Die Ideenfindung ist ein entscheidender Faktor für die Steigerung von Innovationen, sei es in Industrieprojekten oder bei wissenschaftlichen Arbeiten. Besonders in den explorativen Phasen sind neue Perspektiven und alternative Ideen von grossem Wert. An dieser Stelle könnten KI-gestützte Assistenten eine erhebliche Unterstützung bieten, da sie effizienteres und kreativeres Arbeiten ermöglichen. Dies wäre besonders vorteilhaft, wenn kein Team zur Verfügung steht, um unterschiedliche Perspektiven einzubringen.

## Beschreibung

Künstliche Intelligenz (KI) hat das Potenzial, die Kreativität und Innovationskraft von Menschen erheblich zu fördern, indem Aufgaben an die KI delegiert werden können. **Eine Kombination aus menschlichem Know-how und KI-Anwendungen erweist sich dabei als der effektivste Ansatz** (1).

V. Bilgram et al. zeigen, wie KI insbesondere in den frühen Phasen von Innovationsprozessen wie Exploration und Ideenfindung neue Perspektiven eröffnen und die Vielfalt sowie Anzahl von Ideen steigern kann. 

Ein konkretes Beispiel ist die Anwendung von KI bei Projektmanagementaufgaben. In ihren Projekten erprobten Bilgram und Laarmann vier praktische Anwendungen von generativer KI: Erstens, die Durchführung einer PESTEL-Analyse im Automobilmarkt, um externe Einflussfaktoren effizient zu erfassen. Zweitens, die Erstellung von Nutzerreisen und Personas, um die Bedürfnisse und Herausforderungen der Kunden besser zu verstehen. Drittens, die Unterstützung bei der Ideengenerierung, um innovative, auf Kundenbedürfnisse zugeschnittene Produkte und Dienstleistungen zu entwickeln. Schliesslich nutzten sie die KI, um einfache digitale Prototypen zu erstellen, die auch Nicht-Technikern ermöglichen, funktionale Modelle umzusetzen. Diese Anwendungen zeigen, wie KI den Innovationsprozess beschleunigen und vereinfachen kann, wobei die Ergebnisse stark von den Fähigkeiten der Anwender abhängen, was die zentrale Rolle des Menschen im Umgang mit KI unterstreicht (1,2). 

---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: pestel-chatgpt
- condition: contains
  property: id
  value: sixthinkinghats-chatgpt
```

---

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: geschuetzte-daten
- condition: contains
  property: id
  value: bias-diskriminierung
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: entlastung-durch-automatisierung
- condition: contains
  property: id
  value: zweitmeinung
```



---


## Quellen

1.  Koivisto M, Grassini S. Best humans still outperform artificial intelligence in a creative divergent thinking task. Sci Rep. 14. September 2023;13(1):13601. 
2.  Bilgram V, Laarmann F. Accelerating Innovation With Generative AI: AI-Augmented Digital Prototyping and Innovation Methods. IEEE Eng Manag Rev. 2023;51(2):18–25. 