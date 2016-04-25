<!-- .slide: style="background-image: url(images/egg_packaging.jpg); background-size: cover;" id="rpm-packaging" data-timing="30" -->
<h1 style="color: black; bottom: 0">RPM Packaging for OpenStack</h1>

<img data-src="images/OpenStack_logo.png" width="20%" style="position: absolute; left: 0; top: 480px" align="center"/>


<!-- .slide: data-state="normal" id="rpm-packaging-overview" data-timing="80" -->
## RPM Packaging

<img data-src="images/rpm_packaging.png" style="float: left; height: 70%; margin-right: 80px" data-timing="80"/>

<ul style="display: inline">
    <li>Started at Vancouver Summit (May 2015)
    <li>Crafting project scope and team took considerable time
    <li>Governance approval for Big Tent (July 2015)

    <li>Kickoff directly under OpenStack governance with core devs from Mirantis, Red Hat and SUSE
</ul>

Note:
Finding the right granularity in the scope was difficult (open for all packaging variants or not)


<!-- .slide: data-state="normal" id="rpm-packaging-why" data-timing="60" -->
## Benefits of being a Big Tent Project

<p style="text-align: center">
<img data-src="images/packagingcontributions.png" style="height: 30%"/>
</p>

*   Creates a point of contact for other OpenStack teams
*   Allows cross-project dependencies
*   Governance principles give you guidance and structure
*   Moves "downstream" to "upstream"


<!-- .slide: data-state="normal" id="rpm-packaging-lessons" data-timing="60" -->
## RPM Packaging: It's about Tooling

<p style="text-align: center">
<img data-src="images/differentwheels.png" style="height: 20%"/>
</p>

*   Creating a new project is complex
    *   Creation of tooling and project structure
*   ** Lesson learned:** Big Tent principles gives you guidance and structure
    *   Weekly public IRC meetings
    *   Technical Lead with plan for next release
    *   Follow lazy consensus model
    *   CI Checks and gating
