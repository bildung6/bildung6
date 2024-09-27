---
id: podcast
description: "KI für Podcasts einsetzen."
image: "anwendungsfälle/images/podcast.svg" 
tags:
- lehrende
title: Podcast
type: usecase
---


## Beschreibung

Podcasts sind digitale Audio- oder Videoaufnahmen, die über das Internet bereitgestellt werden. Nutzer:innen können sie jederzeit und überall streamen oder herunterladen. Die Formate variieren stark, von Interviews und Diskussionen bis hin zu erzählerischen Inhalten oder Vorträgen. Sie bieten eine flexible Möglichkeit, Inhalte zu vermitteln und sind aufgrund ihrer einfachen Zugänglichkeit und Vielfalt äusserst beliebt.

### Warum Podcasts in der Lehre?

Podcasts bieten Lehrenden eine innovative Methode, Lerninhalte zu vermitteln. Sie ermöglichen es, Lehrinhalte in einem Format anzubieten, das für manche Studierende ansprechender ist als traditionelle Textdokumente oder Skripte. Studierende können Podcasts unterwegs hören, beispielsweise während sie pendeln oder Sport treiben, und so Lehrmaterialien in ihren Alltag integrieren. Dadurch kann Lernen flexibler und individueller gestaltet werden.

### Podcast als weit verbreitetes Medium

Podcasts haben in den letzten Jahren an Popularität gewonnen. Sie werden mittlerweile in vielen Bereichen des Alltags genutzt, von Bildung über Unterhaltung bis hin zu Nachrichten. Diese breite Verbreitung macht sie zu einem attraktiven Medium auch für die Lehre.

### Automatisierung und KI-Unterstützung

Mit KI-Tools kann die Produktion von Podcasts stark vereinfacht werden. Beispielsweise können automatisierte Videos und reine Audio-Podcasts erstellt werden, ohne dass umfangreiche technische Vorkenntnisse nötig sind. Zudem gibt es mittlerweile fortschrittliche Möglichkeiten der synthetischen Stimmgenerierung, die es ermöglicht, Inhalte in verschiedenen Stimmen oder Sprachen zu produzieren – sogar ohne direkte menschliche Aufzeichnung.


---


## Tools für diesen Anwendungsfall

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: podcast-murf
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
```


---

## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT-4o (Ver. 27.09.2024) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---