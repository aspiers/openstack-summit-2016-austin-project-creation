<!-- .slide: style="background-image: url(images/egg_packaging.jpg); background-size: cover;" id="rpm-packaging" -->
<h1 style="color: black; bottom: 0">RPM Packaging for OpenStack</h1>

<img data-src="images/OpenStack_logo.png" width="20%" style="position: absolute; left: 0; top: 480px" align="center"/>


<!-- .slide: data-state="normal" id="rpm-packaging-overview" -->
## RPM Packaging

<img data-src="images/rpm_packaging.png" style="float: left; height: 70%; margin-right: 80px"/>

<ul style="display: inline">
    <li>Idea started at Vancouver Summit (May 2015)
    <li>Discussion about scope and team creation took considerable time
    <li>Governance/TC approval for Big Tent (July 2015)

    <li>Kickoff directly from a green field with core from Mirantis, SUSE and Red Hat
</ul>

Note:
Finding the right granularity in the scope was difficult (open for all packaging variants or not)
Start directly as a greenfield activity due to

<!-- .slide: data-state="normal" id="rpm-packaging-why" -->
## Benefits of Big Tent

*   Defined an "upstream" point of contact for other OpenStack teams
*   Enable cross-project dependencies
*   "Upstream" visibility and collaboration instead of downstream efforts
*   Focus set on Cooperation not competition


<!-- .slide: data-state="normal" id="rpm-packaging-lessons" -->
## RPM Packaging: Lessons Learned

<p style="text-align: center">
<img data-src="images/differentwheels.png" style="height: 20%"/>
</p>

*   Starting a new effort can be overwhelming
    *   Don't decide everything at the beginning
    *   Focus on getting started and iterate quickly
*   Open Design principles gives you guidance and structure
    *   It's a feature, not an obstacle
*   Being a new project, lazy consensus approach wasn't established
*   Foster code-driven technical discussion

Note:
Many differences in downstream packaging was overwhelming to resolve
and discussions dragged a long with no actions being implemented. Situation
improved after we started to tackle each problem at a time
