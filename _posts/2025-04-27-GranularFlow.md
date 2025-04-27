---
layout: post
title: "Friction in granular flows --- My understanding of the mu(I) rheology"
date: 2025-04-27
categories: [Simulation, Physics, Terramechanics]
tags: [technical ramblings]
enable_math: true
---

# Introduction
Here I try to lay out my thoughts on the $$\mu(I)$$ rheology introduced by Jop et al. {% cite jop2006constitutiveNature %}. That paper provides a lot of great insights into how granular material flows. Here I just try to write down something that I can come back to anytime and understand the intuition behind this constitutive relation.

# The mu(I) rheology
Jop et al. {% cite jop2006constitutiveNature %} introduce a constitutive relation for granular materials where, given the amount of confinement stress (local pressure, $$p$$), one could determine the magnitude of the shear stress (actually, the scalar equivalent of the deviatoric stress tensor, $$\overline{\tau}$$). This does sound familiar --- in rigid body contact, given the normal force and a friction coefficient, one can determine the tangential friction force.

In rigid body dynamics, the friction coefficient takes the value of static friction, $$\mu_s$$, when the tangential velocity is zero (no slip), and a kinetic friction coefficient, $$\mu_k < \mu_s$$, when the tangential velocity is non-zero (slipping). Jop et al. argued that things work a bit differently for granular materials.

For granular materials, the macroscopic friction coefficient $$\mu = \overline{\tau}/p$$ is actually a function primarily of this dimensionless number $$I$$, called the ``Inertial Number'', so $$\mu = \mu(I)$$. Also, weirdly, in granular flow, this $$\mu(I)$$ increases when flow occurs and is actually often more than the static friction $$\mu_s$$ that determined the onset of flow! This means that as the granular material shears faster and faster (this is determined by the shear rate magnitude, $$\dot{\overline{\gamma}}^{p}$$), the friction coefficient increases. The exact rate at which it increases is determined by a material constant $$I_0$$. In fact, this is how the plot typically looks for the relation between $$\mu$$ and $$I$$ (screenshotted from {% cite jop2006constitutiveNature %}):

<figure id="fig-muI" style="text-align: center;">
  <img src="/assets/img/mu(I).png" alt="mu(I) relation" style="width:90%;">
  <figcaption>
    Figure 1: The relation between the friction coefficient \(\mu\) and the inertial number \(I\) for a granular material.
  </figcaption>
</figure>

# What is the inertial number and what does it signify?
The inertial number $$I$$ is defined as:

$$
I = \dot{\overline{\gamma}}^{p} \frac{\sqrt{d^2 \rho_s}}{\sqrt{p}} = \dot{\overline{\gamma}}^{p} \frac{d \sqrt{\rho_s}}{\sqrt{p}}
$$

where $$\dot{\overline{\gamma}}^{p}$$ is the magnitude of the plastic shear rate, $$d$$ is the grain diameter, $$\rho_s$$ is the solid grain mass density, and $$p$$ is the local pressure.

On a closer look, we can see that the inertial number is essentially proportional to a ratio of two time scales. Consider the term $$\sqrt{p/\rho_s}$$; this has units of velocity. Then consider the term $$d / \sqrt{p/\rho_s}$$; this has units of time. This can be thought of as a microscopic time scale $$\tau_{\text{micro}}$$ --- it represents the time taken for a grain to move roughly its own diameter $$d$$ under the influence of the confining pressure, or more accurately, the characteristic time for local grain rearrangements or inertial response to contact forces. If the grains were very ``light'' (less dense, lower $$\rho_s$$), they would respond more quickly given a pressure, leading to a low $$\tau_{\text{micro}}$$.

The remaining term is the macroscopic plastic shear rate $$\dot{\overline{\gamma}}^{p}$$. Inverting this, we again get a term with units of time: $$\tau_{\text{macro}} = 1/\dot{\overline{\gamma}}^{p}$$. This is the macroscopic timescale over which the bulk material is being plastically deformed. When this is small (i.e., high shear rate), flow behavior is dominated by the shear rate, and inertial effects become significant compared to the time grains have to rearrange.

Combining these two time scales, we get the inertial number as proportional to the ratio of these two time scales ($$I = \tau_{\text{micro}} / \tau_{\text{macro}}$$):

$$
I = \frac{\tau_{\text{micro}}}{\tau_{\text{macro}}}
$$

When the inertial number is small ($$I \ll 1$$), then $$\tau_{\text{macro}} \gg \tau_{\text{micro}}$$. In this case, the macroscopic shear rate is low, and the bulk deformation is very slow compared to the time needed for local grain rearrangements. Grains have time to settle into stable contacts, and the flow is quasi-static. On the other hand, when the inertial number is large ($$I \gtrsim 10^{-3}$$), then $$\tau_{\text{macro}}$$ is comparable to or smaller than $$\tau_{\text{micro}}$$. In this case, bulk deformation is happening too quickly for grains to fully relax into stable configurations and we have ``dense inertial flow''.

# Connecting I and mu
The relation plotted in figure 1 is typically modelled by an equation of the form:
$$
\mu(I) = \mu_s + \frac{\mu_2 - \mu_s}{I_0/I + 1}
$$

where $$\mu_s$$ is the static friction coefficient that determines the onset of flow, and $$\mu_2$$ is the limiting friction coefficient that can be attained at high $$I$$. $$I_0$$ is a material constant that determines the rate of transition between these two friction coefficients as $$I$$ increases.

Now, if $$I \to 0$$, then the denominator becomes large, the fraction goes to zero, and $$\mu \to \mu_s$$. This means that in the quasi-static limit, there is little to no plastic flow, and the onset of plastic flow is determined by the static friction coefficient. However, once plastic flow starts ($$I > 0$$), unlike with frictional contact in rigid body dynamics, the friction coefficient increases with increasing shear rate (relative to pressure). But why does this happen? Don't know, need to read more.... stay tuned.

## References
{% bibliography --cited %}

<script src="https://giscus.app/client.js"
        data-repo="Huzaifg/Huzaifg.github.io"
        data-repo-id="R_kgDOLWzbwg"
        data-category="Q&A"
        data-category-id="DIC_kwDOLWzbws4CfyO_"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="dark"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>





