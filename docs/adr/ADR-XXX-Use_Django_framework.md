# ADR-nnn: Use Django framework

>|              |                                                                                                                                                                                    |
>| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>| Date         | `01/04/2025` _when the decision was last updated_                                                                                                                                  |
>| Status       | `Proposed`                        |
>| Deciders     | `Team` |
>| Significance | `Structure` |
>| Owners       | @matmoore |
---

- [ADR-nnn: Any Decision Record Template](#adr-nnn-any-decision-record-template)
  - [Context](#context)
  - [Decision](#decision)
    - [Assumptions](#assumptions)
    - [Drivers](#drivers)
    - [Options](#options)
    - [Outcome](#outcome)
    - [Rationale](#rationale)
  - [Consequences](#consequences)
  - [Compliance](#compliance)
  - [Notes](#notes)
  - [Actions](#actions)
  - [Tags](#tags)

## Context

Deciding initial technologies for the service. We are working under the assumption we will be working in Python but need to decide on a framework.

[Reasons for adopting a framework are outlined in the quality framework.](https://github.com/NHSDigital/software-engineering-quality-framework/blob/6d5453d3ee0f9c7af1a4b48d2ec8cb72d9826460/practices/structured-code.md?plain=1#L24). Our app is not trivial enough to build without a framework, and we are assuming it will be fairly typical for a web application running
in the cloud: a stateless service that renders HTML from tempalates, an ORM that connects to a Postgres database, etc.

We are initially intending to productionise the [manage screening events prototype](https://github.com/NHSDigital/manage-screening-events-prototype). We are anticipating building an additional gateway service that would be deployed inside trusts' networks, which this app would communicate with via a queue or API (to be decided later).


## Decision



### Drivers

- Convention over configuration: the framework should provide reasonable, secure defaults, and be familiar enough for new team members joining the team
- Easy to get started with
- Easy to extend while maintaining separation of concerns
- Limited boilerplate

### Options

We are consider the two most common frameworks in Python: Django and Flask. Both are stable, established frameworks, with large open source communities, and both are already in use across the NHS estate.

### Outcome

TBD.

This decision will be relatively hard to move away from once we start building out the app, which is why we've spiked out two options to compare side by side.

### Rationale

Provide a rationale for the decision that is based on weighing the options to ensure that the same questions are not going to be asked again and again unless the decision needs to be superseded.

For non-trivial decisions a comparison table can be useful for the reviewer. Decision criteria down one side, options across the top. You'll likely find decision criteria come from the Drivers section above. Effort can be an important driving factor.  You may have an intuitive feel for this, but reviewers will not. T-shirt sizing the effort for each option may help communicate.

## Consequences

Engineers on the team will need to learn Django. Some suggested learning resources:
- [Django documentation and first steps guide](https://docs.djangoproject.com/en/5.1/)
- Two scoops of Django 3.x by Daniel and Audrey Greenfield
- [Django Girls Tutorial](http://tutorial.djangogirls.org/en/index.html)
- [Django for Beginners](https://learndjango.com/courses/django-for-beginners/) / [Django for Professionals](https://learndjango.com/courses/django-for-professionals/)

[We should expect a new feature release of django roughly every eight months, and regular patch releases](https://docs.djangoproject.com/en/dev/internals/release-process/).

If we decide to build an API in the same service, we should look at [Django Rest Framework](https://www.django-rest-framework.org/)

## Compliance

N/A. We do not need measure anything specifically for this decision.

## Actions

- Run through [Django deployment checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)

## Tags

`#frameworks` `#libraries`
