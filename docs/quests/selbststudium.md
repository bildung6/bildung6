---
title: Selbststudium
type: "quest"
image: quests/images/selbststudium.svg
description: Wie kann KI im Selbstudium eingesetzt werden?
disabled: False
---

In dieser Quest geht es darum, wie künstliche Intelligenz (KI) im Selbststudium eingesetzt werden kann.

###	Einen Lernplan generieren

Nutze KI, um schnell einen Vorschlag für einen individuellen Lernplan zu erstellen.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: lernplangenerieren
```


###	Wissen vertiefen

Nutze KI, um neues Wissen zu erwerben oder vorhandenes Wissen zu vertiefen.


```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: wissenvertiefen
```


### Wissen überprüfen

Nutze KI, um das Gelernte zu überprüfen, indem du es anwendest.

```yaml
condition: or
entityType: usecase
rules:
- condition: equals
  property: id
  value: fragengenerieren
```



