<!-- .slide: data-state="section-break" id="maintenance" data-timing="10" -->
# Life after creating your project

Note:
A lot of the stuff in this section are general best practice
principles for any project not just OpenStack projects, so
I'll try to focus on the specific differences in the OpenStack
ecosystem.


<!-- .slide: data-state="normal" id="code-review" data-timing="60" -->
## Code review

*   +1 / -1: "normal" reviews
*   +2: core review approval
*   -2: core veto (try to avoid!)
*   +1 workflow
*   -1 workflow
*   0

*   [Core Reviewer's Guide](http://docs.openstack.org/infra/manual/core.html)

Note:
- Everyone knows about +1 / -1, but when you have created a project,
  you are responsible for deciding not only what gets merged, but
  also who else will be in the core reviewer's team.


<!-- .slide: data-state="normal" id="constructive-collaboration" data-timing="60" -->
## Constructive collaboration

<figure style="position: absolute; top: 14%; left: 11%; display: table;">
    <img alt="donut burger" style="width: 80%; margin: 0"
         data-src="images/donut-burger.jpg" />
     <figcaption style="text-align: right; font-size: 0.5em;">
         <a href="https://commons.wikimedia.org/wiki/File:Donut_burger.jpg">
             &copy; Phil Denton CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- Firstly be responsive! otherwise project will fail.
- "Criticism sandwich" is potentially flawed but still has some value.
- Be positive, welcoming, and open-minded
- Aim to leave contributor wanting to come back


<!-- .slide: data-state="normal" id="CI" data-timing="20" -->
## CI

<img alt="CI status graphs"
     style="height: 80%"
     data-src="images/CI-stats.png" />

Note:

Noone wants to be in hall of shame!  So ensure CI stays healthy and
visible; this will breed confidence in your project.  Always look for
opportunities to improve it.  Passing is not enough - also need good
code coverage!


<!-- .slide: data-state="normal" id="release-management" -->
## [Release Management](http://docs.openstack.org/project-team-guide/release-management.html)

*   Release models
    *    Common cycle with development milestones
    *    Common cycle with intermediary releases
    *    Independent release model

*   Typical Development Cycle Schedule
*   Managing Release Notes

*   Generate a release artifact
*   Publish a release artifact
*   Import/Export translation strings
*   Tools and approaches vary by language, please choose which language is relevant to you.

*   Building tarballs


<!-- .slide: data-state="section-break" id="reactive-support" data-timing="10" -->
# Reactive support

Note:
- providing decent reactive support can mean the difference between
  life and death of the project


<!-- .slide: data-state="normal" id="bugs" data-timing="20" -->
## Bug / issue tracking

<figure>
    <img alt="A metallic shield bug"
         data-src="images/bug.jpg" />
     <figcaption>
         <a href="https://commons.wikimedia.org/wiki/File:Metallic_shield_bug444.jpg">
             &copy; Benjamint444 CC-BY-SA 3.0
         </a>
     </figcaption>
</figure>

Note:
- triage quickly
- ensure it's always clear what state each issue is in
    - if noone's working on it, that's OK as long as it's clear


<!-- .slide: data-state="normal" id="ML-support" data-timing="20" -->
# Mailing list support

- TODO: insert image here
- usually reuse `openstack-dev@openstack.org`

Note:
- as with bugs, make sure mails don't get ignored
- encourage people to use `[tags]` for easier filtering


<!-- .slide: data-state="normal" id="IRC-channel" data-timing="60" -->
# `#openstack-foo`

- TODO: insert image here
- TODO: show example of setup?

Note:
- important to set up project channel on FreeNode if there is
  no existing channel suitable for reuse
- register with `chanserv` and set a helpful topic


<!-- .slide: data-state="normal" id="IRC-support" data-timing="20" -->
# IRC

<figure>
    <img alt="a tumbleweed"
         data-src="images/Tumbleweed_rolling.jpg" />
     <figcaption>
         <a href="https://commons.wikimedia.org/wiki/File:Tumbleweed_rolling.jpg">
             &copy; Jez Arnold CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- channel is pointless if noone uses it
- idle on channel, make sure questions are going answered


<!-- .slide: data-state="normal" id="IRC-bot" data-timing="20" -->
# IRC bot

<figure>
    <img alt="a bot"
         data-src="images/bot.jpg" />
     <figcaption>
         <a href="">
             &copy;  CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- One way to avoid embarrassment of total silence is to install a
  bot - may seem like cheating, but actually delivers value!


<!-- .slide: data-state="normal" id="IRC-bot-output" data-timing="30" -->
# Sample IRC bot output

```
TODO: example bot output here
```


<!-- .slide: data-state="normal" id="IRC-bot-setup" data-timing="60" -->
# Setting up an IRC bot

```
TODO: show example bot config code
```

- TODO: link to docs


<!-- .slide: data-state="section-break" id="proactive-support" data-timing="10" -->
# Proactive support

Note:
- reactive support is a good start, but for a project to really
  flourish, it needs a more proactive approach


<!-- .slide: data-state="normal" id="IRC-meetings" data-timing="60" -->
## `#openstack-meeting`

- TODO: insert snippet of start of IRC meeting here

Note:
- links to wiki and eavesdrop
- meetings must be scheduled in one of the existing meeting channels
  in order to minimise clashes with other meetings


<!-- .slide: data-state="normal" id="physical-meetings" data-timing="30" -->
## Physical meetings

<figure>
    <img alt="a meeting"
         data-src="images/meeting.jpg" />
     <figcaption>
         <a href="">
             &copy;  CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- personal relationships matter!
- form relationships at summits, mid-cycles, and other meetups


<!-- .slide: data-state="normal" id="proactive-communication" data-timing="60" -->
## Proactive communication

* Interaction with other projects
* Releases
* Blogging

Note:
- The Cross-project Working Group is available to help with
  topics which span multiple projects.
- Make sure your blog is aggregated to planet.openstack.org!


<!-- .slide: data-state="normal" id="documentation" data-timing="60" -->
## Documentation


<!-- .slide: data-state="normal" id="mentoring" data-timing="30" -->
# Mentoring and guiding new contributors

<figure>
    <img alt="mentoring"
         data-src="images/mentoring.jpg" />
     <figcaption>
         <a href="">
             &copy;  CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- Mentoring is perhaps the hardest thing to find time for,
  but one of the most rewarding and productive.
- Pair programming can be very effective.
- More likely to result in participation "stickiness"


<!-- .slide: data-state="normal" id="training" data-timing="60" -->
# Training, screencasts etc.

<figure>
    <img alt="training"
         data-src="images/training.jpg" />
     <figcaption>
         <a href="">
             &copy;  CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- Ultimately your project is for the end users!
  So help them understand and benefit from your project.


<!-- .slide: data-state="normal" id="feedback" data-timing="60" -->
# Gather feedback

<figure>
    <img alt="gathering feedback"
         data-src="images/feedback.jpg" />
     <figcaption>
         <a href="">
             &copy;  CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- submit user stories / specs and ask for reviews
