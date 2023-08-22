---
description: "Nutze ChatGPT um die Inhalte deines Berichts zusammenzufassen."
id: summariesgenerieren-chatgpt
image: "anwendungsf\xE4lle/images/chatbot.svg"
tags:
- summariesgenerieren
- studierende
title: Summaries generieren mit ChatGPT
type: usecase
---


# Summaries generieren mit ChatGPT

## Beschreibung

Bei wissenschaftlichen Tätigkeiten, sei es bei der Recherche oder dem Verfassen von Semesterarbeiten, kann das Generieren von Zusammenfassungen durch ChatGPT eine Zeitersparnis bedeuten. Bei der Erstellung von Abschnitten oder Kapiteln können die generierten Zusammenfassungen dazu verwendet werden, den roten Faden im Text zu behalten und die Struktur des Berichts sinnvoll aufzubauen.

Ein weiterer Anwendungsfall liegt in der Erstellung von Abstracts. Die generierten Zusammenfassungen können als Grundlage dienen, um prägnante und aussagekräftige Abstracts für eine Berichte zu formulieren.

Die folgenden Beispiele zeigen, wie ChatGPT-3.5 verwendet werden kann, um Zusammenfassungen von Texten zu generieren.

Beispiel 1 zeigt die Zusammenfassung eines kurzen Textes. 

Da bei ChatGPT die Zeichenbeschränkung beachtet werden muss, ist es ratsam, längere Texte abschnittsweise (in Chunks) zu übergeben (1). Im zweiten Beispiel wird daher ein Text, dessen Länge das Zeichenlimit überschreitet, Schritt für Schritt übertragen, um anschliessend eine Zusammenfassung zu generieren.

**Es ist wichtig, die generierten Texte kritisch zu überprüfen, um etwaige fehlerhafte Informationen zu erkennen. Besonders im Hinblick auf Zitate und Referenzen sollten die geltenden Zitierregeln sorgfältig beachtet werden, um die Quellen korrekt anzugeben und Plagiate zu vermeiden.**


---


## Beispiele

???+ info "Bemerkung"
    
    Bedenke, dass es in deiner Verantwortung liegt, die Relevanz der Quellen und die Richtigkeit der generierten Zusammenfassungen zu überprüfen. Als in der Forschung tätige Person musst du auch in der Lage sein, den Inhalt der gesichteten Literatur zu verstehen und zu interpretieren.

---


### Beispiel 1: Kurzer Text Zusammenfassen

Der hier genutzte fiktive Artikel wurde mit ChatGPT-3.5 erstellt und beschreibt die Rolle von Zwiebeln und Pastinaken in der Landwirtschaft der Sowjetunion. Aus Platz- und Darstellungsgründen wird der Text hier nicht in voller Länge wiedergegeben. Er kann jedoch über den unten stehenden Link zum Chatverlauf eingesehen werden.

Für das Zusammenfassen von Texten kann "tldr" (too long; didn't read) im Prompt verwendet werden. Der eingefügte Text enthält ca. 650 Wörter bzw. 5000 Zeichen.


**Input**

<p style="padding: 20px; border: 1px solid #d9d9e3; background: white">

<mark>tldr, antworte auf Deutsch:</mark>
<br>
<br>
"Die Rolle von Zwiebeln und Pastinaken in der Landwirtschaft der Sowjetunion
<br>
<br>
Die Landwirtschaft spielte eine zentrale Rolle in der Sowjetunion, sowohl als wirtschaftlicher Motor als auch als Instrument der politischen Ideologie. Zwei bescheidene Gemüsesorten, Zwiebeln und Pastinaken, mögen auf den ersten Blick als unscheinbar erscheinen, doch sie hatten einen bemerkenswerten Einfluss auf die Landwirtschaft und die Gesellschaft des Landes. In diesem Artikel werden wir die Bedeutung von Zwiebeln und Pastinaken in der Landwirtschaft der Sowjetunion genauer betrachten.
<br>
<br>
In den frühen Jahren nach der Gründung der Sowjetunion im Jahr 1922....""
</p>


**Output**

<p style="padding: 20px; border: 1px solid #d9d9e3; background: rgba(247,247,248)">
In der Sowjetunion spielten Zwiebeln und Pastinaken eine bedeutende Rolle in der Landwirtschaft. Diese bescheidenen Gemüsesorten trugen zur Ernährung der Bevölkerung bei und hatten kulturelle Bedeutung. In einer Zeit wirtschaftlicher Instabilität nach der Gründung der Sowjetunion wurden sie aufgrund ihrer einfachen Anbauweise, Lagerfähigkeit und vielseitigen Verwendung geschätzt. Die robusten Pastinaken gediehen in kälteren Klimazonen gut und lieferten einen süßen, erdigen Geschmack für Suppen und Eintöpfe. Die sowjetische Regierung förderte die Landwirtschaft als Teil der nationalen Stärke und des sozialistischen Fortschritts. Obwohl Zwiebeln und Pastinaken nie den Hauptanteil der Landwirtschaft ausmachten, blieben sie wichtige Nahrungsquellen und kulturelle Symbole. In späteren Jahren führten jedoch Probleme der zentralisierten Planwirtschaft und Nahrungsmittelknappheit zu verstärkten Bemühungen, die Produktion zu diversifizieren. Mit politischen und wirtschaftlichen Reformen brach schließlich die Sowjetunion zusammen, doch Zwiebeln und Pastinaken bleiben als Teil des landwirtschaftlichen Erbes und der kulinarischen Geschichte erhalten.
</p>

*Um den Chatverlauf einzusehen oder den Chat fortzusetzen (erfordert einen OpenAI-Account), benutze diesen Link:  https://chat.openai.com/share/f5dde4ca-fd39-475e-a6a7-e0999af19a0a*


---


### Beispiel 2: Langer Text in mehreren Schritten einfügen und zusammenfassen

Dieses Beispiel simuliert, wie ChatGPT-3.5 verwendet werden könnte, um eine Zusammenfassung einer bestehenden Arbeit (z.B. deiner Seminararbeit) zu erstellen.

Um das bestehende Eingabe-Limit (Stand August 2023) von ChatGPT-3.5 zu umgehen, wurde der Text in mehrere Teile zerlegt und mit spezifischen Prompts an den Chatbot übergeben. Hierfür wurde der ***ChatGPT PROMPTs Splitter*** von Jose Diaz (https://chatgpt-prompt-splitter.jjdiaz.dev/) verwendet, mit dem längere Texte einfach und mit passenden Prompt-Anweisungen aufgeteilt werden können.

Der in diesem Beispiel verwendete Text stammt aus der Arbeit *Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale* von Bangor et al. aus dem Jahr 2009. Diese Untersuchung ergab, dass die SUS um eine weitere Skala erweitert werden könnte (2). Aus Platz- und Darstellungsgründen wird der Text hier nicht vollständig wiedergegeben. Er kann jedoch über den unten stehenden Link zum Chatverlauf eingesehen werden. In den Prompts wurde der gesamte Text ohne Abstract und Keywords übertragen.

Der nachfolgende Dialog umfasst grob diese Schritte:

1. Kopiere den Text aus dem Dokument
2. Teile den Text in mehrere Chunks auf (Nutze ein Textdokument oder verwende ein Werkzeug wie den ***ChatGPT PROMPTs Splitter***)
3. Übergebe den Text Schrittweise mit den dazugehörigen Prompts (Anweisungen)
4. Lass ChatGPT eine Zusammenfassung generieren

<br>

**Input 1: Erster Chunk**

<p style="padding: 20px; border: 1px solid #d9d9e3; background: white">
<mark>Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part 1/2 received" and wait for the next part.</mark>
<br>
<mark>[START PART 1/2]</mark> 
<br>
Introduction There are numerous surveys available to usability practitioners to aid them in assessing the usability of a product or service. Many of these surveys are used to evaluate specific types of interfaces, while others can be used to evaluate a wider range of interface types. The System Usability Scale (SUS) (Brooke, 1996) is one of the surveys that can be used to assess the usability of a variety of products or services. There are several...
<br>
<mark>[END PART 1/2]</mark> 
<br>
<mark>Remember not answering yet. Just acknowledge you received this part with the message "Part 1/2 received" and wait for the next part.</mark>
</p>

**Ouptut 1**
<p style="padding: 20px; border: 1px solid #d9d9e3; background: rgba(247,247,248)">
Part 1/2 received. I'll be waiting for the next part of your text.
</p>

<br>

**Input 2: Letzter Chunk**
<p style="padding: 20px; border: 1px solid #d9d9e3; background: white">
<mark>[START PART 2/2]</mark>
<br>
er, if an item is not considered to be concrete singular, then multiple item questionnaires should be utilized. Because different parts of an interface may be judged differently (e.g., the main navigation vs. the help system), we believe that the items tested as part of usability assessments are not necessarily singular. Because we assume that the interfaces are not always singular, as defined by Rossiter (2002), the non-singular nature of the item makes using only a single item questionnaire alone inadvisable. Another note of caution regarding...
<br>
<mark>[END PART 2/2]</mark> 
<br>
<mark>ALL PARTS SENT. Now you can continue processing the request.</mark> 
</p>


**Output 2**

<p style="padding: 20px; border: 1px solid #d9d9e3; background: rgba(247,247,248)">
Part 2/2 received. Thank you for providing the complete text. If you have any questions or if there's anything specific you'd like to discuss or inquire about regarding this text, feel free to let me know!
</p>

<br>

**Input 3: Generiere ein Abstract**
<p style="padding: 20px; border: 1px solid #d9d9e3; background: white">
<mark>Schreibe ein Abstract in der Form, wie es in wissenschaftlichen Arbeiten üblich ist.  Antworte in 5-10 Sätzen auf Deutsch. Und füge die Keywords in einem separaten Abschnitt hinzu.</mark> 
</p>

**Output 3**

<p style="padding: 20px; border: 1px solid #d9d9e3; background: rgba(247,247,248)">
Abstract:
<br>
Diese Studie untersucht die Verwendung einer zusätzlichen Adjektivbewertungsskala in Verbindung mit dem System Usability Scale (SUS) zur Bewertung der Benutzerfreundlichkeit von Produkten und Dienstleistungen. Die SUS ist eine bewährte Methode zur Bewertung der Benutzerfreundlichkeit, jedoch bleibt die Bedeutung einzelner SUS-Scores oft unklar. Die Hinzufügung einer Adjektivskala ermöglicht eine subjektive Bewertung der SUS-Ergebnisse. Die Studie zeigt eine hohe Korrelation zwischen der Adjektivbewertung und den SUS-Scores. Die Verwendung der Skala allein wird jedoch aufgrund der Unsicherheiten über die Konnotation von Bewertungen und der begrenzten Aussagekraft nicht empfohlen. Es wird diskutiert, wie eine Letter-Grade-Skala als zusätzliche Bewertungsmethode genutzt werden könnte, um die Interpretation von SUS-Scores zu erleichtern.
<br>
<br>
Keywords: System Usability Scale (SUS), Benutzerfreundlichkeit, Adjektivbewertung, Letter-Grade-Skala, Usability-Bewertung.
</p>


*Um den Chatverlauf einzusehen oder den Chat fortzusetzen (erfordert einen OpenAI-Account), benutze diesen Link: https://chat.openai.com/share/b25813cc-89a4-4a26-92f3-d9791429330a*


---


Zum Vergleich mit **dem Original** ist hier der Text aus dem Abstract des ausgewählten Papers *Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale* von Bangor et al.:

<p style="padding: 20px; border: 1px solid #d9d9e3; background: rgba(200, 247, 197)">
Abstract:
<br>
The System Usability Scale (SUS) is an inexpensive, yet effective tool for assessing the usability of a product, including Web sites, cell phones, interactive voice response systems, TV applications, and more. It provides an easy-tounderstand score from 0 (negative) to 100 (positive). While a 100-point scale is intuitive in many respects and allows for relative judgments, information describing how the numeric score translates into an absolute judgment of usability is not known. To help answer that question, a seven-point adjective-anchored Likert scale was added as an eleventh question to nearly 1,000 SUS surveys. Results show that the Likert scale scores correlate extremely well with the SUS scores (r=0.822). The addition of the adjective rating scale to the SUS may help practitioners interpret individual SUS scores and aid in explaining the results to non-human factors professionals. 
<br>
<br>
Keywords: System Usability Scale, SUS, Surveys, User Satisfaction, Usability

</p>




---


## Tools 

```yaml
condition: or
entityType: tool
rules:
- condition: equals
  property: id
  value: chatgpt
```

---

## Risiken

```yaml
condition: or
entityType: risk
rules:
- condition: contains
  property: id
  value: halluzinationen
- condition: contains
  property: id
  value: nachvollziehbarkeit
- condition: contains
  property: id
  value: geschuetzte-daten
- condition: contains
  property: id
  value: bias-diskriminierung
- condition: contains
  property: id
  value: gesellschaftlicher-bias
- condition: contains
  property: id
  value: kompetenzverlust
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: effizienzsteigerung
- condition: contains
  property: id
  value: sprachliche-barrieren-aufloesen
```

---

## Links

ChatGPT PROMPTs Splitter von Jose Diaz:

- ChatGPT PROMPTs Splitter App: https://chatgpt-prompt-splitter.jjdiaz.dev/
- Beschreibung: https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270

Chatverlauf zum erstellen fiktiver Artikel:

- Beispiel 1 (Kurzer Artikel über Ziebeln und Pastinaken in der Sovietunion): 
https://chat.openai.com/share/19a1b905-ea5a-4091-bac7-55e8d053b11c

---

## Quellen

1.	Diaz J. Break the Limits: Send Large Text Blocks to ChatGPT with Ease [Internet]. Medium. 2023 [zitiert 22. August 2023]. Verfügbar unter: https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270

2.	Bangor A, Kortum P, Miller J. Determining what individual SUS scores mean: adding an adjective rating scale. J Usability Stud. 1. Mai 2009;4(3):114–23. 