---
title: Wissenschaftliches Arbeiten
type: "quest"
image: quests/images/wissenschaftlich.svg
description: Welche KI-Tools unterstützen mich beim wissenschaftlichen Arbeiten? 
---


In diesem Quest geht es darum, wie KI zur Unterstützung beim wissenschaftlichen Arbeiten eingesetzt werden kann. 

###	Fragestellung generieren
1.	Ein Tool nutzen mit mind. 3 verschiedenen Prompts, um Ideen zu generieren
2.	Feedback zur Fragestellung einholen (Prompt vorgeben, darf adaptiert werden)
3.	Tool: ChatGPT oder ähnliches, Elicit

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: sprachlichekorrektur
```


###	Journalistischer Artikel

1.	Feedback einholen und optimieren
2.	Tool: ChatGPT oder ähnliches

### Präsentation üben

1.	Powerpoint Speaker Coach 

```yaml
condition: or
entityType: usecase
rules:
- condition: contains
  property: id
  value: powerpoint
```


### Literaturrecherche

1.	Nutzen von Elicit, um Informationen zum Background zusammenzustellen inkl. Entsprechender Referenzen

### Summary erstellen

1.	Studierenden erstellen Zusammenfassung und lassen durch ChatGPT optimieren
2.	Offen lassen: Studis können die eigene Version nutzen oder die optimierte

### Sprachliche Korrektur etc. nach Bedarf

1.	In der Methodik die Nutzung beschreiben
2.	Tools: DeepL Write




