#!/usr/bin/env python
# coding: utf-8
# In[1]:
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import math

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer, Aer,IBMQ
from qiskit.visualization import plot_bloch_vector
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.extensions import Initialize
from qiskit.quantum_info import state_fidelity
from qiskit.quantum_info import partial_trace
# In[2]:
from qiskit.quantum_info import Statevector
zero = Statevector.from_label('0')
one = Statevector.from_label('1')
# In[3]:
#all possible states of initialization
sf=0
avef=0

ntheta=60
nphi=60

nalpha = 6

dalpha=pi/nalpha
dtheta=pi/(ntheta)
dphi=2*pi/(nphi)

for ialpha in range(0,nalpha):
    alpha=dalpha*ialpha
    avef=0
    for iphi in range(0,nphi):
        phi=dphi*iphi
        
        for itheta in range(0,ntheta):
            theta=dtheta*itheta

            qrA = QuantumRegister(1)
            qrB = QuantumRegister(2)
            qrC = QuantumRegister(1)
            cr1 = ClassicalRegister(1)
            cr2 = ClassicalRegister(1)
            mycircuit = QuantumCircuit(qrA, qrB, qrC, cr1, cr2)
                #bcomputation and initial state
            b = np.exp(1j * phi) * np.sin(theta/2)
            a = np.cos(theta/2)
            sv = a * zero + b * one
                #extra qubit rotation
                #initialize qubit
            init_gate = Initialize(sv.data)
            init_gate.label = "init"
            mycircuit.append(init_gate, [0])
            mycircuit.barrier()
                #entanglement between alice2 and bob qubits
            mycircuit.h(qrB[0])
            mycircuit.cx(qrB[0], qrB[1])
            mycircuit.barrier()
                #NOISE
            mycircuit.h(qrC[0])
            mycircuit.crx(alpha,qrC[0], qrA[0])
            mycircuit.barrier()
                #Bell Measurement between qubits alice1 and alice2
            mycircuit.cx(qrA[0], qrB[0])
            mycircuit.h(qrA[0])
            mycircuit.barrier()
                #NOISE
            #mycircuit.h(qrC[0])
            #mycircuit.crx(alpha,qrC[0], qrA[0])
            #mycircuit.barrier()
                ###measure of alice's qubits
            mycircuit.measure([qrA[0],qrB[0]], [0,1])
            mycircuit.barrier()
                #NOISE
            #mycircuit.h(qrC[0])
            #mycircuit.crx(alpha,qrC[0], qrA[0])
            #mycircuit.barrier()
                ###recovering bob state
            mycircuit.z(qrB[1]).c_if(cr1, 1)
            mycircuit.x(qrB[1]).c_if(cr2, 1)
                #bob state 
            backend = BasicAer.get_backend('statevector_simulator')
            out_vector = execute(mycircuit, backend).result().get_statevector()
                #bob partial trace and fidelity
            new = partial_trace(out_vector, [0,1,3])
            sf = state_fidelity(sv, new)
            avef = avef + sf*sin(theta/2)

    avet = avef/(4*pi)*dtheta*dphi
       #Average fidelity / amount of noise
    print(alpha, avet)