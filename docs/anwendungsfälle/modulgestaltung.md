---
description: "KI kann bei der Gestaltung von Modulen helfen, indem sie Vorschl\xE4\
  ge f\xFCr Struktur, Inhalte und Aktivit\xE4ten macht."
id: modulgestaltung
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- modulgestaltung
- lehrende
title: Modul-Gestaltung
type: usecase
---


# Modul-Gestaltung

## Beschreibung

KI kann bei der Gestaltung von Modulen helfen, indem sie Vorschläge für Struktur, Inhalte und Aktivitäten macht.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: lehrende
```



## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: cogram
- condition: contains
  property: id
  value: composeai
```



## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: kompetenzverlust
- condition: contains
  property: id
  value: monopolbildung
```



## Chance

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: kreative-anstoesse
```

