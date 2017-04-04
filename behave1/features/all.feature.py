Feature: test jysk

Scenario: scenario1

Given open "https://jysk.ua/"
Then do search by "RYSLINGE"
Then check that 8 results are returned
Then click first element
Then check name of element
Then check description of element
Then check amount of feedbacks at the bottom
Then click on feedbacks tab
Then click on leaving of feedback button
Then set feedback star
Then define "Subject"
Then define "bla bla bla"
Then define "Iryna"
Then define "Che"
Then define "iryna.pavelchak@gmail.com"
Then define "Subject"
Then click on sending feedback button
Then check if validation failed
Then close browser

