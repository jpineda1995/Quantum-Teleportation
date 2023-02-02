# Quantum-Teleportation

A brief introduction to quantum teleportation using the Qiskit package, and computation of the Average Fidelity of states. 

Quantum teleportation is the transference of information from remote stations, proposed by Charles Bennett and his team, in the article "Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels", published in 1993. 

To exemplify the standard protocol of teleportation, we commonly say that Alice wishes to send a message to Bob. In order to accomplish this, at first they get two carriers of information and entangle them. One of the entangled parties goes to Alice and the other to Bob's station. Then, Alice prepares the message on an extra carrier of information and proceeds with the Bell State Measurement (BSM) on her two parties. The BSM is a joint measurement on two qubits. Now, Alice needs to measure her two parties separately, getting as possible results: 00, 01, 10, 11. Finally, Alice communicates the information of her measurements to the Bob station and he proceeds to apply corrective operations on his side in order to recover the input state on his carrier. 

In addition, the Average Fidelity (AF) is commonly used as the test Value of the efficiency of the process of teleportation, given the presence of possible noise affection or defects of the device that could produce changes in the system, sending a message with errors. In addition, the AF is a quantifier of the amount of entanglement between the Alice and Bob parties, which defines the classical limit, it means no entanglement. If some entanglement exists, then, the average fidelity will increase, reaching its maximum value at 1, which means maximal entanglement. Some examples of bipartite maximally entangled channels are the Bell states.

Here, the carrier of information is referred to as the physical system that is able to codify the information. Currently, there exist various implementations of quantum processors such as Superconducting Qubits, Nuclear Magnetic Resonance, Ion Traps, Optical Cavity Quantum Electrodynamics, and Optical Photon quantum processors, among many others.

# Code Explanation

We have used the mathematical representation of the Bloch Sphere (BS) in order to prepare the input state on Alice's side. The BS is a very useful tool for the visualization of a two-level pure quantum state. For this, we set the input angles, teleport the state, measure the fidelity of states, and save it. We produce small rotations of these angles in order to accomplish a whole map of the sphere at the end of the process. Finally, the average is taken.
