<!-- .slide: data-state="section-break" id="governance" -->
# OpenStack Governance


<!-- .slide: data-state="normal" id="call-to-action" data-menu-title="Call to action" data-background-transition="zoom" data-background-size="100%" data-background-image="images/OSCloudBlue.png"-->
# OpenStack's Mission Statement

<div class="call-to-action">
    <h3 class="inside">
    The OpenStack mission is “to produce the ubiquitous Open Source Cloud Computing platform
    that will meet the needs of public and private clouds regardless of size, by being simple
    to implement and massively scalable”.
    </h3>

    <h5 class="outside">
        OpenStack is <a href="http://docs.openstack.org/project-team-guide/open-source.html" target="_blank">open source</a>,
        <a href="http://docs.openstack.org/project-team-guide/open-design.html" target="_blank">openly designed</a>,
        <a href="http://docs.openstack.org/project-team-guide/open-development.html" target="_blank">openly developed</a> by an
        <a href="http://docs.openstack.org/project-team-guide/open-community.html" target="_blank">open community</a>.
    </h5>
</div>


<!-- .slide: data-background="images/open_sign_background.jpg" data-background-size="100%" id="governance-four-opens" -->
<!-- <h1 style="color: white">The Four Opens</h1> -->

<div style="color: white; font-size: 80pt; font-weight: bold; text-transform: uppercase">
<div>
        <div class="fragment" style="float: left; align: top left">Source</div>
        <div class="fragment" style="float: right; align: top right">Design</div>
    </div>
    <div style="padding: 8pt">&nbsp;</div>
    <div>
        <p class="fragment" style="position: absolute; bottom: 0">Development</p>
        <p class="fragment" style="position: absolute; bottom: 124pt; right: 0">Community</p>
    </div>
        <div style="padding: 8pt">&nbsp;</div>

</div>


<!-- .slide: data-state="normal" id="governance-open-source" -->
# Open Source

<img data-src="images/use_open_source.jpg" style="float: left; height: 70%; margin margin-right: 80px"/>
<p>
    <ul style="display: inline">
        <li>No "Open Core"</li>
        <li>No Feature Limits, Performance Limits, Enterprise Edition</li>
    </ul>
</p>

<aside class="notes">
We are committed to creating truly open source software that is usable and
scalable. Truly open source software is not feature or performance limited and
is not crippled. There will be no “Enterprise Edition”.
</aside>


<!-- .slide: data-state="normal" id="governance-open-source-licensing" -->
# Open Source Licensing

<img data-src="images/asf_logo.png" width="60%" style="float: left; margin-right: 80px" />
<p>
<h2>Apache License 2.0</h2>
<ul>
    <li>OSI approved
    <li>GPLv3 compatible
    <li>DFSG compatible
</ul>
</p>


<!-- .slide: data-state="normal" id="governance-open-design" -->
# Open Design

*   Public Design summit
*   Public Road Map
*   Public Requirements and specifications

Note:
We are committed to an open design process. Every six months the development
community holds a design summit to gather requirements and write specifications
for the upcoming release. The design summits, which are open to the public,
include users, developers, and upstream projects. We gather requirements and
produce an approved roadmap used to guide development for the next six months.

The community controls the design process. You can help make this software meet
your needs.


<!-- .slide: data-state="normal" id="governance-open-development" -->
# Open Development

*   Public Source
*   Public reviews
*   Public Test results

Note:
We maintain a publicly available source code repository through the entire
development process. We do public code reviews. We have public roadmaps. This
makes participation simpler, allows users to follow the development process and
participate in QA at an early stage.


<!-- .slide: data-state="normal" id="automatedtesting" -->
## [Automated Testing (QA and CI)](http://docs.openstack.org/project-team-guide/testing.html)

*   Required
    *   Unit tests
    *   Functional tests
    *   Integration tests
    *   Style checks


<!-- .slide: data-state="normal" id="governance-open-community" -->
# Open Community

<img data-src="images/fishbowl_jump.jpg" style="height: 40%; text" align="center"/>

*   Lazy consensus model
*   All processes being documented, open and transparent
*   Meritocracy with technical leads
*   Meetings are held in public IRC channels, recorded, communication through public mailing lists

Note:
One of our core goals is to maintain a healthy, vibrant developer and user
community. Most decisions are made using a lazy consensus model. All processes
are documented, open and transparent.

The technical governance of the project is a community meritocracy with
contributors electing technical leads and members of the Technical Committee.

All project meetings are held in public IRC channels and recorded. Additional
technical communication is through public mailing lists and is archived.


<!-- .slide: data-state="normal" id="governance-dependencies" -->
## Dependencies and Optional Modules

When utilizing third party modules or libraries which are not Apache 2.0
licensed, contributors need to understand how the interaction between the
modules will work and the compatibility of the licenses involved. If there are
doubts or concerns, it is recommended to raise the issue in the Technical
Committee Meeting to discuss with the Technical Committee how to proceed. In
general, err on the side of caution here.

Note:
- talk about proprietary cinder storage drivers
