---
layout: post
title: Pushing the Boundaries
usemathjax: true
---

Solving a seemingly exponentially hard problem in polynomial time 

# Problem

The Ising Model is used to represent the interaction of atomic "spins" of electrons in a metal. The spin is like an angular momentum which exerts force to charged particles. In the Ising Model, the particles can be in only one of two states (up or down). We will consider a simple case where there is only a line of particles in one dimension.
Our goal is to observe how different spin configurations change different aspects of the system.

## Spin Configuration

In the discrete one dimensional Ising Model, to define a particular spin configuration we need to first specify how many particles are in our system. For example, a spin configuration with 5 particles would look like &#8593; &#8595; &#8595; &#8593; &#8595;. There are evidently 2<sup>5</sup> possible spin configurations for a 5 particle system. Another thing to note is that the models will use periodic boundary conditions. Instead of thinking the particles being arranged in a line, imagine them arranged in a circle. This allows the last particle to affect the first particle as well. 

## Energy

Given a configuration of spins we can define the energy using what is referred to as an Ising Hamiltonian:

$$H = -\frac{J}{k}\sum_{<ij>} s_is_j + \tfrac{\mu}{k}\sum_i s_i$$

where, \\(s_i=1\\) if the \\(i^{th}\\) spin is up and \\(s_i=-1\\) if it is down, and the brackets \\(<ij>\\) indicate a sum over spins that are connected, and J is a constant that determines the energy scale. The energy here has been divided by the Boltzmann constant to yield units of temperature.
