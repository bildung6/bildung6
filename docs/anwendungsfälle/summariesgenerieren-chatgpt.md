---
description: "Nutze ChatGPT um die Inhalte deines Berichts zusammenzufassen."
id: summariesgenerieren-chatgpt
image: "anwendungsf\xE4lle/images/chatbot.svg"
tags:
- studierende
title: Summaries generieren mit ChatGPT
type: usecase
---


# Summaries generieren mit ChatGPT
Nutze ChatGPT um die Inhalte deines Berichts zusammenzufassen.


## Beschreibung

Bei wissenschaftlichen Tätigkeiten, sei es bei der Recherche oder beim Verfassen von Semesterarbeiten, kann das Generieren von Zusammenfassungen mit ChatGPT eine Zeitersparnis bedeuten. 

Bei der Erstellung von Abschnitten oder Kapiteln könnten die generierten Zusammenfassungen dazu verwendet werden, den roten Faden im Text zu behalten und die Struktur des Berichts sinnvoll aufzubauen. Ein weiterer Anwendungsfall liegt in der Erstellung von Abstracts. Die generierten Zusammenfassungen können als Grundlage dienen, um prägnante und aussagekräftige Abstracts für einen Bericht zu formulieren.


**Es ist wichtig, die generierten Texte kritisch auf fehlerhafte Informationen zu überprüfen. Insbesondere bei Zitaten, Verweisen und Paraphrasen sind die geltenden Zitierregeln genau zu beachten, um Quellen korrekt anzugeben und Plagiate zu vermeiden.**


---


## Beispiele

Die folgenden Beispiele zeigen, wie Zusammenfassungen von Texten mit ChatGPT-3.5 erstellt werden können. Im ersten Beispiel wird ein kurzer Text zusammengefasst. Im zweiten Beispiel wird ein längerer Text abschnittsweise übertragen, um anschliessend eine Zusammenfassung zu generieren. Diese Vorgehensweise war notwendig, da ChatGPT eine Zeichenbegrenzung hat (Stand August 2023) und längere Texte ggf. in "Chunks" übertragen werden müssen (1).



### Kurzer Text zusammenfassen
Für das Zusammenfassen von Texten kann **"tldr"** (too long; didn't read) im Prompt verwendet werden. 





<table >
  <tr>
    <th>Beispiel</th>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input:</i></td>
      </p>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <strong>tldr, antworte auf Deutsch:</strong>
        <br>
        <br>
        """Die Rolle von Zwiebeln und Pastinaken in der Landwirtschaft der Sowjetunion
        <br>
        <br>
        Die Landwirtschaft spielte eine zentrale Rolle in der Sowjetunion, sowohl als wirtschaftlicher Motor als auch als Instrument der politischen Ideologie. Zwei bescheidene..."""
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      In der Sowjetunion spielten Zwiebeln und Pastinaken eine bedeutende Rolle in der Landwirtschaft. Diese bescheidenen Gemüsesorten trugen zur Ernährung der Bevölkerung bei und hatten kulturelle Bedeutung. In einer Zeit wirtschaftlicher Instabilität nach der Gründung der Sowjetunion wurden sie aufgrund ihrer einfachen Anbauweise, Lagerfähigkeit und vielseitigen Verwendung geschätzt. Die robusten Pastinaken gediehen in kälteren Klimazonen gut und lieferten einen süßen, erdigen Geschmack für Suppen und Eintöpfe. Die sowjetische Regierung förderte die Landwirtschaft als Teil der nationalen Stärke und des sozialistischen Fortschritts. Obwohl Zwiebeln und Pastinaken nie den Hauptanteil der Landwirtschaft ausmachten, blieben sie wichtige Nahrungsquellen und kulturelle Symbole. In späteren Jahren führten jedoch Probleme der zentralisierten Planwirtschaft und Nahrungsmittelknappheit zu verstärkten Bemühungen, die Produktion zu diversifizieren. Mit politischen und wirtschaftlichen Reformen brach schließlich die Sowjetunion zusammen, doch Zwiebeln und Pastinaken bleiben als Teil des landwirtschaftlichen Erbes und der kulinarischen Geschichte erhalten.
    </td>
  </tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT ein Summary generieren. Nutze diesen <a href="https://chat.openai.com/share/f5dde4ca-fd39-475e-a6a7-e0999af19a0a"> Link,</a>um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a></i>
    </td>
  </tr>
</table>


???+ info "Bemerkung"
    
    Der hier übermittelte fiktive Artikel wurde mit ChatGPT-3.5 erstellt und beschreibt die Rolle von Zwiebeln und Pastinaken in der Landwirtschaft der Sowjetunion. Aus Platz- und Darstellungsgründen wird der Text hier nicht in voller Länge wiedergegeben. Er kann jedoch über die unten stehenden Links zum Chatverlauf eingesehen werden.


!!! Tip  "Tipp"

    Nutze den *Regenerate*-Button in ChatGPT, um weitere Antworten zu generieren. 
    




### Langer Text schrittweise einfügen und zusammenfassen

Dieses Beispiel simuliert, wie ChatGPT-3.5 verwendet werden kann, um eine Zusammenfassung einer bestehenden Arbeit (z.B. deiner Seminararbeit) zu erstellen.

Um das bestehende Eingabe-Limit (Stand August 2023) von ChatGPT-3.5 zu umgehen, wurde ein Text in mehrere Teile zerlegt und mit spezifischen Prompts an den Chatbot übergeben. 

Hierfür wurde der ***ChatGPT PROMPTs Splitter*** von Jose Diaz (https://chatgpt-prompt-splitter.jjdiaz.dev/) verwendet, mit dem längere Texte **einfach und mit passenden Prompt-Anweisungen aufgeteilt werden können.**


<table >
  <tr>
    <th>Beispiel</th>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input 1:</i></td>
      </p>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
      <strong>Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part 1/2 received" and wait for the next part.</strong>
      <br>
      <strong>[START PART 1/2]</strong>
      <br>
      Introduction There are numerous surveys available to usability practitioners to aid them in assessing the usability of a product or service. Many of these surveys are ...
      <br>
      <strong>[END PART 1/2]</strong>
      <br>
      <strong>Remember not answering yet. Just acknowledge you received this part with the message "Part 1/2 received" and wait for the next part.</strong>
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output 1:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      Part 1/2 received. I'll be waiting for the next part of your text.
    </td>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input 2:</i></td>
      </p>
      </td>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <strong>[START PART 2/2]</strong>
        <br>
        er, if an item is not considered to be concrete singular, then multiple item questionnaires should be utilized. Because different parts of an interface may be judged differently...
        <br>
        <strong>[END PART 2/2]</strong>
        <br>
        <strong>ALL PARTS SENT. Now you can continue processing the request.</strong>
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output 2:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      Part 2/2 received. Thank you for providing the complete text. If you have any questions or if there's anything specific you'd like to discuss or inquire about regarding this text, feel free to let me know!
    </td>
  </tr>
   <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <i>Input 3:</i></td>
      </p>
      </td>
  </tr>
  <tr>
    <td bgcolor="5D6CC0">
      <p style="color:white">
        <strong>Schreibe ein Abstract in der Form, wie es in wissenschaftlichen Arbeiten üblich ist.  Antworte in 5-10 Sätzen auf Deutsch. Und füge die Keywords in einem separaten Abschnitt hinzu.</strong>
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output 3:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      Abstract:
      <br>
      Diese Studie untersucht die Verwendung einer zusätzlichen Adjektivbewertungsskala in Verbindung mit dem System Usability Scale (SUS) zur Bewertung der Benutzerfreundlichkeit von Produkten und Dienstleistungen. Die SUS ist eine bewährte Methode zur Bewertung der Benutzerfreundlichkeit, jedoch bleibt die Bedeutung einzelner SUS-Scores oft unklar. Die Hinzufügung einer Adjektivskala ermöglicht eine subjektive Bewertung der SUS-Ergebnisse. Die Studie zeigt eine hohe Korrelation zwischen der Adjektivbewertung und den SUS-Scores. Die Verwendung der Skala allein wird jedoch aufgrund der Unsicherheiten über die Konnotation von Bewertungen und der begrenzten Aussagekraft nicht empfohlen. Es wird diskutiert, wie eine Letter-Grade-Skala als zusätzliche Bewertungsmethode genutzt werden könnte, um die Interpretation von SUS-Scores zu erleichtern.
      <br>
      <br>
      Keywords: System Usability Scale (SUS), Benutzerfreundlichkeit, Adjektivbewertung, Letter-Grade-Skala, Usability-Bewertung.
    </td>
  </tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT ein Summary generieren. Nutze diesen <a href="https://chat.openai.com/share/b25813cc-89a4-4a26-92f3-d9791429330a"> Link,</a>um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a></i>
    </td>
  </tr>
</table>


???+ info "Bemerkung"
    
    Der in diesem Beispiel verwendete Text stammt aus dem Paper *Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale* von Bangor et al. aus dem Jahr 2009. Diese Untersuchung ergab, dass die System Usability Scale (SUS) um eine weitere Skala erweitert werden könnte (2). Aus Platz- und Darstellungsgründen wird der Text hier nicht vollständig wiedergegeben. Er kann jedoch über den unten stehenden Link zum Chatverlauf eingesehen werden. In den Prompts wurde der gesamte Text ohne Abstract und Keywords übertragen.



Hier zum Vergleich das Original des Abstracts des übermittelten Papers *Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale* von Bangor et al.:

<p style="padding: 20px; border: 1px solid #d9d9e3; background: white">
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
- condition: equals
  property: id
  value: halluzinationen
- condition: equals
  property: id
  value: nachvollziehbarkeit
- condition: equals
  property: id
  value: geschuetzte-daten
- condition: equals
  property: id
  value: plagiate
```

---

## Chancen

```yaml
condition: or
entityType: chance
rules:
- condition: contains
  property: id
  value: sprachliche-barrieren-aufloesen
- condition: contains
  property: id
  value: zweitmeinung
```


---


## Links

ChatGPT PROMPTs Splitter von Jose Diaz:

- ChatGPT PROMPTs Splitter App: https://chatgpt-prompt-splitter.jjdiaz.dev/
- App-Beschreibung: https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270


Folgende Quellen wurden herangezogen, um die hier verwendeten Prompts zu erstellen:

- https://platform.openai.com/docs/guides/gpt-best-practices
- https://chatgpt-prompt-splitter.jjdiaz.dev/



Chatverlauf zur Erstellung des fiktiven Artikels:

- Beispiel 1 (Kurzer Artikel über Zwiebeln und Pastinaken in der Sovietunion): 
https://chat.openai.com/share/19a1b905-ea5a-4091-bac7-55e8d053b11c


---


## Quellen

1.	Diaz J. Break the Limits: Send Large Text Blocks to ChatGPT with Ease [Internet]. Medium. 2023 [zitiert 22. August 2023]. Verfügbar unter: https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270

2.	Bangor A, Kortum P, Miller J. Determining what individual SUS scores mean: adding an adjective rating scale. J Usability Stud. 1. Mai 2009;4(3):114–23. 
