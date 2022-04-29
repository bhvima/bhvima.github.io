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

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="361px" height="150px" viewBox="-0.5 -0.5 361 95" style="background-color: rgb(255, 255, 255); display: block; margin: auto;"><defs/><g><ellipse cx="180" cy="30" rx="180" ry="30" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-dasharray="3 3" pointer-events="all"/><path d="M 39 73 L 39 29.37" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 39 24.12 L 42.5 31.12 L 39 29.37 L 35.5 31.12 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 110 83 L 110 39.37" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 110 34.12 L 113.5 41.12 L 110 39.37 L 106.5 41.12 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 180.5 46 L 180.5 36 L 180.5 79.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 180.5 84.88 L 177 77.88 L 180.5 79.63 L 184 77.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 250 43 L 250 33 L 250 76.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 250 81.88 L 246.5 74.88 L 250 76.63 L 253.5 74.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 320 74 L 320 30.37" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 320 25.12 L 323.5 32.12 L 320 30.37 L 316.5 32.12 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/></g></svg>

In the discrete one dimensional Ising Model, to define a particular spin configuration we need to first specify how many particles are in our system. The spin configuration \\(\uparrow\uparrow\downarrow\downarrow\uparrow\\) above consists of 5 particles. Another thing to note is that the models will use periodic boundary conditions which idicates the last particle is connected to the first one.

## Energy

Given a configuration of spins we can define the energy using what is referred to as an Ising Hamiltonian:

$$H = -J\sum_{\left<ij\right>} \sigma_i\sigma_j + \mu\sum_i\sigma_i$$


where, \\(\sigma_i=1\\) if the \\(i^{th}\\) spin is up and \\(\sigma_i=-1\\) if it is down, and the brackets \\(\<ij\>\\) indicate a sum over spins that are connected, J is a constant that determines the energy scale, and \\(\mu\\) is a constant that determines the chemical potential.

For example, the Ising Hamiltonian for the spin configuration \\(\uparrow\uparrow\downarrow\downarrow\uparrow\\) is:

$$H = -J(1 + -1 + 1 + -1 + 1) + \mu(1 + 1 + -1 + -1 + 1) $$

## Probability

$$P(\alpha) = e^{-E(\alpha)/T}$$

defines the probability of observing a particular configuration of spins, \\(\alpha\\). Where \\(E(\alpha)\\) is the energy of a particular spin configuration, and T is the temperature in Kelvin. The probability of observing the configuration decays exponentially with increasing energy of \\(\alpha\\).

## Expectation Value

In a dynamical, fluctuating system the spin configuration changes. The average energy of the system can be obtained by adding up the value of an individual configuration multiplied by it's respective probability. 

$$\left<E\right> = \sum_\alpha E(\alpha)P(\alpha)$$

Meaning to obtain the average value (expectation value) computationally, one must compute both the energy and it's probability over all possible configurations. For a given number of spins (particles) the number of possible configurations increases exponentially.