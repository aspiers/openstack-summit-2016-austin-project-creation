<!-- .slide: data-state="section-break" id="maintenance" data-timing="20" -->
# Life after creating your project

Note:
A lot of the stuff in this section are general best practice
principles for any project not just OpenStack projects, so
I'll try to focus on the specific differences in the OpenStack
ecosystem.


<!-- .slide: data-state="normal" id="thumb-up" data-timing="20" -->
## Code review

<div style="height: 80%; float: left">
<img alt="thumbs up"
         data-src="images/thumbs-up.jpg" />
</div>
<figure class="fragment" style="float: right; width: 50%">
    <img alt="thumb down"
         data-src="images/thumb-down.jpg" />
     <figcaption>
         <a href="https://commons.wikimedia.org/wiki/File:Disapprove.jpg">
             &copy; hobvias sudoneighm CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- This guy is a standard reviewer who likes your code. It's easy to be this guy.
- If you don't like someone's code, you have to tread more carefully.


<!-- .slide: data-state="normal" id="constructive-collaboration" data-timing="60" -->
## Constructive collaboration

<figure class="full-slide">
    <img alt="donut burger"
         data-src="images/donut-burger.jpg" />
     <figcaption>
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


<!-- .slide: data-state="normal" id="core-reviewers" data-timing="60" -->
## Core reviewers

<figure class="full-slide">
    <img alt="two thumbs up"
         data-src="images/two-thumbs-up.jpg" />
     <figcaption>
         <a href="https://commons.wikimedia.org/wiki/File:Young_Somali_man_2.jpg">
             &copy; Entressen kirjasto CC-BY-SA 2.0
         </a>
     </figcaption>
</figure>

Note:
- When you have created a project, you are responsible for deciding
  not only what gets merged, but also who else will be in the core
  reviewer's team.


<!-- .slide: data-state="normal" id="other-votes" data-timing="60" -->
## Other review mechanisms

*   -2: core veto (try to avoid!)
*   +1 workflow
*   -1 workflow
*   0

<p style="margin-top: 2em">
    Reference: [Core Reviewer's Guide](http://docs.openstack.org/infra/manual/core.html)
</p>

<p style="margin-top: 2em">
    https://github.com/openstack/gerrit-dash-creator
</p>

Note:
0 can be a valid vote sometimes, when you are indifferent.


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

<div style="height: auto; float: right; margin-left: 80px">
<img data-src="images/balloon_release.jpg" />
</div>

<ul style="display: inline">
    <li>[SemVer](http://semver.org/) recommended
    <li>Decide a release model
        <ul>
            <li> `release:cycle-with-intermediary` (5.0.0.0b1, 5.0.0.0rc2)
            <li> `release:cycle-with-milestones` (X.Y.Z)
            <li> `release:independent`
        </ul>
    <li>Build / publish tarballs
    <li>Track Release Notes ([`reno`](http://docs.openstack.org/developer/reno/design.html))
    <li>Integrate translations from https://translate.openstack.org/
    <li>http://docs.openstack.org/project-team-guide/release-management.html
</ul>

Note:


<!-- .slide: data-state="section-break" id="reactive-support" data-timing="10" -->
# Reactive support

Note:
- providing decent reactive support can mean the difference between
  life and death of the project


<!-- .slide: data-state="normal" id="bugs" data-timing="20" -->
## Bug / issue tracking

<figure class="full-slide">
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
## Mailing list support

```
To: <openstack-dev@lists.openstack.org>
Subject: [openstack-dev] [neutron] [L3] Wrong fail over of HA-Router
```

<p style="margin-top: 2em" />

* https://wiki.openstack.org/wiki/Mailing_Lists
* http://lists.openstack.org/

Note:
- as with bugs, make sure mails don't get ignored
- encourage people to use `[tags]` for easier filtering


<!-- .slide: data-state="normal" id="IRC-channel" data-timing="60" -->
## `#openstack-foo`

- important to set up project channel on FreeNode if there is
  no existing channel suitable for reuse
- register with `chanserv` and set a helpful topic


<!-- .slide: data-state="normal" id="IRC-support" data-timing="20" -->
## IRC support

<figure class="full-slide">
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
