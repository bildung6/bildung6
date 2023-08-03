---
description: "KI kann bei der Erstellung von Code helfen, indem sie Vorschl\xE4ge\
  \ und Beispiele liefert."
id: codeerstellen
image: "anwendungsf\xE4lle/images/usecase.svg"
tags:
- codeerstellen
- studierende
title: Code erstellen
type: usecase
---


# Code erstellen

## Beschreibung

KI kann bei der Erstellung von Code helfen, indem sie Vorschläge und Beispiele liefert.

## AnwenderInnen

```yaml
condition: or
entityType: user
rules:
- condition: contains
  property: id
  value: studierende
```



## Tools

```yaml
condition: or
entityType: tool
rules:
- condition: contains
  property: id
  value: composeai
- condition: contains
  property: id
  value: tabnine
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

[chance=kreative-anstoesse]
