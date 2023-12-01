---
description: "ChatGPT nutzen, um Fragen für Studierende und Lernende zu erstellen."
id: fragengenerieren-chatgpt
image: "anwendungsfälle/images/chatbot.svg"
tags:
- studierende
- lehrende
- fragen
title: Fragen generieren mit ChatGPT
type: usecase
---


# Fragen generieren mit ChatGPT

Mit ChatGPT können schnell Vorschläge für Prüfungen oder ein Quiz erstellt werden.


## Beschreibung

Anwender:innen können ChatGPT als unterstützendes Tool nutzen, um auf effiziente Weise Vorschläge für Prüfungs- und Quizfragen zu generieren, indem sie durch das Chat-Interface spezifische Frageformate und Themenbereiche vorgeben. Der Prozess der Erstellung von Fragen kann dadurch erleichtert und beschleunigt werden.



## Beispiele

In diesem Abschnitt werden Beispiele vorgestellt, wie ChatGPT verwendet werden kann, um mit Hilfe spezifischer Prompts zielgerichtete Fragen für Prüfungen und Quizze zu generieren. Die Eingabe klarer, themenspezifischer Anweisungen oder Schlüsselwörter in die Chat-Benutzeroberfläche kann helfen, nuancierte und relevante Fragen zu generieren.


### Eine Multiple-Choice-Frage generieren

Hier wird ChatGPT-3.5 aufgefordert, eine Multiple-Choice-Frage zu einem Themenfeld zu generieren. Zusätzlich wurde der Chatbot angewiesen, richtige und falsche Antworten mit Emojis (✅ , ❌) zu kennzeichnen.
Durch die Aufforderung, die *Rolle einer Hochschuldozentin* zu übernehmen, sollte die Komplexität der Frage bestimmt werden.


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
        Nimm die Rolle einer Hochschuldozentin ein und erstelle 1 Prüfungsfrage zum Thema "Data Cleaning in Machine Learning" für meine Studierenden. Erstelle jeweils eine Multiple-Choice-Frage mit 4 Antworten, von denen mindestens eine richtig ist und markiere die richtigen Antworten direkt mit einem ✅ -Emoji, und baue mindestens eine  falsche Antwort und markiere die Falschen mit einem ❌-Emoji.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      Selbstverständlich, hier ist eine Prüfungsfrage zum Thema "Data Cleaning in Machine Learning":
      <br>
      <br>
      Frage: Welche der folgenden Maßnahmen sind Teil des Data Cleaning-Prozesses in Machine Learning?
      <br>
      <br>
      A) ✅ Entfernen von Duplikaten in den Datensätzen.<br>
      B) ✅ Füllen von fehlenden Werten in den Daten aus.<br>
      C) ❌ Zufälliges Hinzufügen von neuen Datenpunkten.<br>
      D) ✅ Konvertieren von kategorialen Variablen in numerische Formate.
      <br>
      <br>
      Antworten:<br>
      A) ✅ Entfernen von Duplikaten in den Datensätzen.<br>
      Richtig! Das Entfernen von Duplikaten ist ein wichtiger Schritt im Data Cleaning-Prozess, da doppelte Datensätze die Modellleistung beeinträchtigen können.<br><br>
      B) ✅ Füllen von fehlenden Werten in den Daten aus.<br>
      Richtig! Das Füllen von fehlenden Werten ist entscheidend, um sicherzustellen, dass das Modell ordnungsgemäß funktioniert, da viele Algorithmen nicht mit fehlenden Daten umgehen können.<br><br>
      C) ❌ Zufälliges Hinzufügen von neuen Datenpunkten.<br>
      Falsch. Das zufällige Hinzufügen von neuen Datenpunkten ist normalerweise keine gängige Data Cleaning-Maßnahme und kann die Qualität der Daten verschlechtern.<br><br>
      D) ✅ Konvertieren von kategorialen Variablen in numerische Formate.<br>
      Richtig! Die Umwandlung von kategorialen Variablen in numerische Formate, wie One-Hot-Encoding, ist wichtig, um sie für Machine Learning-Algorithmen zugänglich zu machen.<br><br>
    </td>
  </tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT eine Multiple-Choice-Frage generieren. Nutze diesen <a href="https://chat.openai.com/share/2e2c4856-570e-4b28-92e1-9240b532a8b9"> Link,</a>um den Chatverlauf (ChatGPT-3.5) zu diesem Beispiel anzuschauen.</a></i>
    </td>
  </tr>
</table>



### Generierung von Fragen auf der Grundlage eines Syllabus

In diesem Beispiel wurde zu Beginn ein (fiktiver) Syllabus übermittelt, um Prüfungsfragen zu generieren. Aus Platzgründen ist nicht der gesamte Chatverlauf (ChatGPT-4.0) ersichtlich, dieser enthielt jedoch weitere Aufforderungen (Prompts), um *anspruchsvollere Fragen* zu generieren und *verschiedene Frageformate* zu verwenden. Der vollständige Chatverlauf kann <a href="https://chat.openai.com/share/fb152bf4-78a3-45cb-a131-96f8a28f1f5a">hier </a>eingesehen werden.


<table >
  <tr>
    <th>Beispiel Chatverlauf</th>
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
        Nimm die Rolle eines Fragen-Generators ein und halte dich an die folgende Instruktion.
        <br>
        <br>
        ###Instruktion:###
        <br>
        <br>
        Schritt 1:<br>
        Ich gebe dir einen Syllabus für einen Hochschulkurs, du merkst dir den Inhalt und wartest auf meine weitere Anfrage.
        <br>
        <br>
        Schritt 2:<br>
        Ich werde dich dann bitten, Prüfungsfragen zu generieren, die auf dem Syllabus basieren.
        <br>
        <br>
        ###Syllabus:###<br>
        Modul: Grundlagen der Hämatologie
        <br>
        <br>
        Voraussetzungen: Grundkenntnisse in Biologie und Chemie
        Zielgruppe: Studierende der Medizin, Biologie, Biochemie oder verwandter Studiengänge.
        <br>
        <br>
        Lernziele:
        <br>
        Verstehen der grundlegenden physiologischen und pathophysiologischen Prozesse des hämatologischen Systems.
        Kenntnisse über Blutkrankheiten, Diagnosemethoden und Therapieansätze.
        Fähigkeit, hämatologische Labortests durchzuführen und zu interpretieren.
        <br>
        <br>
        Inhalt:
        <br>
        Woche 1-2: Einführung in die Hämatologie<br>
          •	Definition und Bedeutung der Hämatologie<br>
          •	Blutzellen und ihre Funktionen<br>
          •	Blutbildung (Hämatopoese)<br>
        <br>
        ...<br>
        ...
        <br>
        <br>
        Woche 13-14: Spezielle Themen und Fallstudien<br>
          •	Hämophilie und andere erbliche Blutkrankheiten<br>
          •	Seltene hämatologische Erkrankungen<br>
          •	Aktuelle Forschung und zukünftige Perspektiven in der Hämatologie<br>
        <br>
        ...
        <br>
        <br>
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      Ich habe den Syllabus zum Modul "Grundlagen der Hämatologie" berücksichtigt. Was möchtest du als Nächstes tun?
    </td>
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
        Erstelle  zur Woche 13-14, zwei Multiple-Choice-Prüfungsfrage für Studierende mit 4 Antworten, von denen mindestens eine richtig ist und markiere die richtigen Antworten direkt mit einem ✅ -Emoji, und baue mindestens eine  falsche Antwort und markiere die Falschen mit einem ❌-Emoji.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      <h4>Frage 1: Spezielle Themen und Fallstudien in der Hämatologie</h4>
      Welche der folgenden Aussagen über Hämophilie ist korrekt?
      <br>
      <br>
      A) Hämophilie ist eine ererbte Erkrankung, die hauptsächlich die Blutgerinnung beeinflusst und bei der Betroffenen unkontrollierte Blutungen erleiden können. ✅
      <br>
      <br>
      B) Hämophilie kann durch eine Übertragung von Viren erworben werden. ❌
      <br>
      <br>
      C) Hämophilie betrifft in erster Linie Frauen und wird von Müttern auf Töchter übertragen. ❌
      <br>
      <br>
      D) Hämophilie verursacht eine übermäßige Thrombozytenproduktion. ❌
      <br>
      <br>
      <h4>Frage 2: Spezielle Themen und Fallstudien in der Hämatologie</h4>
      Welches der folgenden Szenarien beschreibt am besten eine seltene hämatologische Erkrankung namens Paroxysmale Nächtliche Hämoglobinurie (PNH)?
      <br>
      <br>
      A) Ein Zustand, bei dem Betroffene während des Schlafes unerklärliche Episoden von Muskelschwäche erleben. ❌
      <br>
      <br>
      B) Eine Erkrankung, bei der es zu einer vermehrten Zerstörung von roten Blutzellen (Hämolyse), Blutgerinnseln und beeinträchtigter Knochenmarksfunktion kommt. ✅
      <br>
      <br>
      C) Eine Erkrankung, bei der das Blut während der Nacht stark eindickt, was zu einer vermehrten Thrombozytenbildung führt. ❌
      <br>
      <br>
      D) Ein Zustand, bei dem Patienten nachts an unkontrollierbaren Blutungen leiden, ohne dass eine offensichtliche Ursache vorliegt. ❌
      <br>
      <br>     
      ....
    </td>
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
        Nun auf dem Niveau eines Medizinstudiums
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      <h4>Frage 1: Hämophilie</h4>
      Die Behandlung von Hämophilie A könnte einen Ansatz mit welchem der folgenden Wirkstoffe umfassen, um das Fehlen des Faktors VIII zu adressieren?
      <br>
      <br>
      A) Desmopressin (DDAVP) ✅
      <br>
      <br>
      B) Warfarin ❌
      <br>
      <br>
      C) Heparin ❌
      <br>
      <br>
      D) Clopidogrel ❌
      <br>
      <br>
      <h4>Frage 2: Paroxysmale Nächtliche Hämoglobinurie (PNH)</h4>
      Welcher Mechanismus ist hauptsächlich für die intravaskuläre Hämolyse bei Paroxysmaler Nächtlicher Hämoglobinurie (PNH) verantwortlich?
      <br>
      <br>
      A) Fehlen von CD55 und CD59 auf der Oberfläche der roten Blutzellen, was zu einer erhöhten Anfälligkeit für den Angriff durch den Komplementkomplex führt. ✅
      <br>
      <br>
      B) Überproduktion von Hämoglobin, das die roten Blutzellen belastet und zu deren Zerstörung führt. ❌
      <br>
      <br>
      C) Mangel an Vitamin B12, der eine ineffiziente Bildung roter Blutzellen verursacht. ❌
      <br>
      <br>
      D) Autoantikörper, die gezielt rote Blutzellen angreifen und zerstören. ❌
      <br>
      <br>
      ...
    </td>
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
        Erstelle mir nun 3 weitere Prüfungsfragen, versuche jede in einem anderen Format zu generieren.
      </p>
    </td>
  </tr>
  <tr>
    <td bgcolor="white"><i>Output:</i></td>
  </tr>
  <tr>
    <td bgcolor="white">
      <h4>Frage 3: Richtig/Falsch-Format</h4>
      Aussage: Hämophilie B ist durch einen Mangel des Gerinnungsfaktors IX gekennzeichnet.
      <br>
      <br>
      Richtig ✅<br>
      Falsch ❌
      <br>
      <br>
      <h4>Frage 4: Lückentext-Format</h4>
      Vervollständigen Sie den folgenden Satz mit dem korrekten Begriff:
      <br>
      <br>
      "Die ________ ist ein Prozess, bei dem Blutzellen aus multipotenten hämatopoetischen Stammzellen im Knochenmark gebildet werden."
      <br>
      <br>
      Antwort: Hämatopoese ✅
      <br>
      <br>
      <h4>Frage 5: Kurzantwort-Format</h4>
      Beschreiben Sie kurz den Mechanismus, wie eine V617F-Mutation im JAK2-Gen mit der Pathophysiologie von Myeloproliferativen Neoplasien (MPN) in Verbindung steht.
      <br>
      <br>
      Antwort:<br>
      Eine akzeptable Antwort könnte folgendermaßen aussehen:<br>
      Die V617F-Mutation im JAK2-Gen resultiert in einer konstitutiven Aktivierung des JAK-STAT-Signalwegs. Dies führt zu einer unkontrollierten Proliferation der myeloiden Zelllinie, welche typisch für MPNs ist. Die ständige Aktivierung dieses Signalwegs trotz des Fehlens von Wachstumsfaktoren fördert das übermäßige Wachstum und die Akkumulation von Blutzellen im Knochenmark und führt zu einer Vielzahl von Symptomen und Komplikationen, die mit MPNs in Zusammenhang stehen.
      <br>
      <br>
      ...
    </td>
  </tr>
  <tr>
    <td  bgcolor="f1f1f1"><i>Chatverlauf: Mit ChatGPT meherere Prüfungsfragen generieren. Nutze diesen <a href="https://chat.openai.com/share/e5984f79-63cf-434e-97fa-4360288efad0"> Link,</a>um den Chatverlauf (ChatGPT-4.0) zu diesem Beispiel anzuschauen.</a></i>
    </td>
  </tr>
</table>



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

## Über diesen Beitrag

Beim Verfassen dieses Beitrags haben die Autor:innen ChatGPT-3.5/-4.0 (Ver. 13.10.2023) und DeepL Write (Ver. 13.10.2023) verwendet, um die sprachliche Darstellung ihrer Gedanken zu verbessern. Die volle Verantwortung für den Inhalt liegt bei den Autor:innen. 


---


## Links

OpenAI, ChatGPT-Entwicklerseite:

- https://openai.com/


OpenAI Blog "Teaching with AI":

- https://openai.com/blog/teaching-with-ai


Chatverläufe: Mit ChatGPT Fragen für ein Quiz oder eine Prüfung generieren:

- https://chat.openai.com/share/2e2c4856-570e-4b28-92e1-9240b532a8b9
- https://chat.openai.com/share/e5984f79-63cf-434e-97fa-4360288efad0


