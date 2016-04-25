<!-- .slide: data-state="section-break" id="governance" -->
# OpenStack Governance Projects


<!-- .slide: data-state="normal" id="openstack-mission" -->
## OpenStack's Mission Statement

<img data-src="images/openstack-logo-plain.png" width="50%" style="float: left; margin-right: 8px" />

<div class="call-to-action">
    "Produce the ubiquitous Open Source Cloud Computing platform
    that will meet the needs of public and private clouds
    regardless of size, by being simple to implement and massively scalable”.
</div>

https://governance.openstack.org/reference/new-projects-requirements.html


<!-- .slide: data-background="images/open_sign_background.jpg" data-background-size="100%" id="governance-four-opens" data-menu-title="The Four Opens" -->
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
## Open Source

<img data-src="images/use_open_source.jpg" style="float: left; height: 70%; margin-right: 80px"/>

<ul style="display: inline">
    <li>No "Open Core" (Feature Limits/Enterprise Edition)</li>
    <li>No Feature Limits, Performance Limits, Enterprise Edition</li>
    <li>Apache v2.0 strongly recommended</li>
    <li>No dependencies on components which effectively impacts redistribution or deployment</li>
</ul>

<aside class="notes">
We are committed to creating truly open source software that is usable and
scalable. Truly open source software is not feature or performance limited and
is not crippled. There will be no “Enterprise Edition”.
</aside>

Note:
* talk about proprietary openstack drivers depending on proprietary components


<!-- .slide: data-state="normal" id="governance-open-design" -->
## Open Design

<p style="text-align: center">
<img data-src="images/open_design.jpg" style="width: 50%"/>
</p>

*   Public Design Decisions
*   Public Road Map
*   Public Requirements and specifications
*   Communication through public mailing lists

Note:
We are committed to an open design process. Every six months the development
community holds a design summit to gather requirements and write specifications
for the upcoming release. The design summits, which are open to the public,
include users, developers, and upstream projects. We gather requirements and
produce an approved roadmap used to guide development for the next six months.

The community controls the design process. You can help make this software meet
your needs.


<!-- .slide: data-state="normal" id="governance-open-development" -->
## Open Development

<p style="text-align: center">
<img data-src="images/development.jpg" style="height: 40%"/>
</p>

*   Open Code Review on review.OpenStack.org
*   Open group of core approvers
*   Cooperation over Competition
*   Open to Code and Code pattern reuse

<aside class="notes">
We maintain a publicly available source code repository through the entire
development process. We do public code reviews. We have public roadmaps. This
makes participation simpler, allows users to follow the development process and
participate in QA at an early stage.

The project uses public code reviews on the OpenStack infrastructure
The project has core reviewers and adopts a test-driven gate in the OpenStack infrastructure for changes
The project provides liaisons that serve as contacts for the work of cross-project teams in OpenStack
Where it makes sense, the project cooperates with existing projects rather than gratuitously competing or reinventing the wheel
Where appropriate, the project adopts technology and patterns used by existing OpenStack projects
</aside>


<!-- .slide: data-state="normal" id="governance-open-testing" -->
## Open Development Testing

<img data-src="images/jenkins_checks.png" style="float: left; height: 70%; margin-right: 80px"/>

<ul style="display: inline">
    <li>Enforces passing of tests prior merging
    <li>Enforces coding style
    <li>Follows Common Testing Requirements
</ul>


<!-- .slide: data-state="normal" id="governance-open-community" -->
## Open Community

<p style="text-align: center">
<img data-src="images/fishbowl_jump.jpg" style="height: 40%"/>
</p>

*   Healthy, vibrant community acting in Lazy consensus model
*   Processes are documented, open and transparent
*   Contributor chosen technical lead
*   Meetings are held & recorded in public IRC

Note:
One of our core goals is to maintain a healthy, vibrant developer and user
community. Most decisions are made using a lazy consensus model. All processes
are documented, open and transparent.

The technical governance of the project is a community meritocracy with
contributors electing technical leads and members of the Technical Committee.

All project meetings are held in public IRC channels and recorded. Additional
technical communication is through public mailing lists and is archived.
