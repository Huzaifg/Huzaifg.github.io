---
layout: page
title: simulations
permalink: /simulations/
nav: true
nav_order: 1
---
Here are some cool simulations from Chrono::CRM, the solver that I develop as part of my PhD. You will find similar images in some of my papers. Here I just accumulate all the images that I thought make me look cool 😎

### Polaris RZR
Simulating a Polaris RZR with rigid and deformable tires on rigid and deformable terrain. Project Chrono simulates vehicle dynamics, Chrono::FEA (ANCF) simulates the tires and Chrono::CRM simulates the terrain (my main contribution). The coloring below the wheel is ground pressure. Cool to see that deformable tires produce lesser ground pressure than rigid tires on deformable terrain.

<a href="{{ 'assets/img/simulations/resized/defTire_demo.png' | relative_url }}" data-lightbox="simulations" data-title="Deformable Tire Simulation">
    <img src="{{ 'assets/img/simulations/resized/defTire_demo.png' | relative_url }}" alt="Deformable Tire Simulation" style="max-width:100%; margin-bottom: 2em;">
</a>

### Bulldozing Simulation
Simulating a John Deere Gator but with a catch. We added a blade to the front so that it can level soil. We then trained a control policy to control the blade to effectively level a hump of soil. The training data came from Chrono::CRM (my main contribution). Work was done in collaboration with my lab collegues Harry Zhang and Ganesh Arivoli. Look at it go!  

<a href="{{ 'assets/img/simulations/resized/bulldozing_3image.png' | relative_url }}" data-lightbox="simulations" data-title="Bulldozing Simulation">
    <img src="{{ 'assets/img/simulations/resized/bulldozing_3image.png' | relative_url }}" alt="Bulldozing Simulation" style="max-width:100%; margin-bottom: 2em;">
</a>

### VIPER
NASA's VIPER rover going for a spin on the moon. Project Chrono simulates the rover dynamics and Chrono::CRM simulates the lunar terrain.

<a href="{{ 'assets/img/simulations/resized/viper_performance.png' | relative_url }}" data-lightbox="simulations" data-title="Viper Performance Analysis">
    <img src="{{ 'assets/img/simulations/resized/viper_performance.png' | relative_url }}" alt="Viper Performance Analysis" style="max-width:100%; margin-bottom: 2em;">
</a>


### MGRU3 Single Wheel
Simulating a single wheel of the MGRU3 rover. Project Chrono simulates the wheel dynamics and Chrono::CRM simulates the terrain. The treads look cool!

<a href="{{ 'assets/img/simulations/resized/mgru3_treads.png' | relative_url }}" data-lightbox="simulations" data-title="MGRU3 Treads Simulation">
    <img src="{{ 'assets/img/simulations/resized/mgru3_treads.png' | relative_url }}" alt="MGRU3 Treads Simulation" style="max-width:100%; margin-bottom: 2em;">
</a> 

### Tracked Vehicle
Simulating a tracked vehicle with track shoes and a rigid chassis. Project Chrono simulates the vehicle dynamics and Chrono::CRM simulates the terrain. Terrain has RMS noise added to it to simulate real terrain.

<a href="{{ 'assets/img/simulations/resized/tracked_performance.png' | relative_url }}" data-lightbox="simulations" data-title="Tracked Vehicle Performance">
    <img src="{{ 'assets/img/simulations/resized/tracked_performance.png' | relative_url }}" alt="Tracked Vehicle Performance" style="max-width:100%; margin-bottom: 2em;">
</a>

### RASSOR
Simulating NASA's solution to extraterrestrial mining, the [Regolith Advanced Surface Systems Operations Robot (RASSOR) Excavator](https://technology.nasa.gov/patent/KSC-TOPS-7). Here you can see it use its counter-rotating drums to dig up Chrono::CRM simulated lunar terrain. How cool!

<a href="{{ 'assets/img/simulations/resized/rassor_performance.png' | relative_url }}" data-lightbox="simulations" data-title="RASSOR Performance Analysis">
    <img src="{{ 'assets/img/simulations/resized/rassor_performance.png' | relative_url }}" alt="RASSOR Performance Analysis" style="max-width:100%; margin-bottom: 2em;">
</a>

### RASSOR Drum Granular Material Collection
The drum of the RASSOR excavator is used to collect granular material from the lunar surface. Here you can see the drum collecting granular material from the lunar surface. The drum is a rigid body with prescribed motion simulated with Project Chrono whereas the granular material is simulated with Chrono::CRM.

<a href="{{ 'assets/img/simulations/resized/rassor_collection_0475.png' | relative_url }}" data-lightbox="simulations" data-title="RASSOR Collection Simulation">
    <img src="{{ 'assets/img/simulations/resized/rassor_collection_0475.png' | relative_url }}" alt="RASSOR Collection Simulation" style="max-width:100%; margin-bottom: 2em;">
</a>


### Flexible Beam
A flexible beam coming in the way of a granular material dam break! The color represents particle velocity. The beam is a flexible cable that is simulated with Chrono::FEA (ANCF) whereas the granular material is simulated with Chrono::CRM.

<a href="{{ 'assets/img/simulations/resized/flex_cable_performance_zoom.png' | relative_url }}" data-lightbox="simulations" data-title="Flexible Cable Simulation">
    <img src="{{ 'assets/img/simulations/resized/flex_cable_performance_zoom.png' | relative_url }}" alt="Flexible Cable Simulation" style="max-width:100%; margin-bottom: 2em;">
</a>
