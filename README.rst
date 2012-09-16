=========
Accordion
=========

PennApps 2012-Fall Project
(Sadly we were unable to make the PennApps submission deadline.  However we will continue to work on this project.)

Collaborators:
  - Dylan Lukes
  - Siyu Song
  - Enchi Jiang (Derek)

Note: this document is in reStructuredText, not Markdown.

Introduction
---------------------
Accordion is the instrument for aggregating storage.

Accordion provides a unified interface for users to easily manage multiple cloud storage accounts from different services. Accordion is extensible: anyone can write a plugin for any cloud storage service to work with Accordion. Ideally, users should only have to deal with Accordion and leave it to deal with all other cloud services. For now we are only working on a web app, but later we will add desktop and mobile apps.

This repository hosts the server side of Accordion.  The web app is hosted in: https://github.com/faily/accordionwebapp

Derek is maintaining the "master" branch.  Dylan Lukes is maintaining the "future" branch, which aims to clean up existing code base. 


Environment Variables3
---------------------

The following should be set:

- ACCORDION_MONGO_URI: The URL for the MongoDB database to be used.
- DROPBOX_APP_KEY
- DROPBOX_APP_SECRET
