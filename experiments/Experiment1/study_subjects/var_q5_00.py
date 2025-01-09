if __name__ == "__main__":

    ## Programming Quantum Computers
    ##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
    ##   O'Reilly Media
    ##
    ## More samples like this can be found at http://oreilly-qc.github.io
    ##
    ## A complete notebook of all Chapter 5 samples (including this one) can be found at
    ##  https://github.com/oreilly-qc/oreilly-qc.github.io/tree/master/samples/Qiskit

    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
    import math
    ## Uncomment the next line to see diagrams when running in a notebook
    #%matplotlib inline

    ## Example 5-5: Quantum conditional phase flip

    ## Note that this looks different from the gates in the book, because
    ## we're building the operations from Toffoli gates

    # Set up the program
    a = QuantumRegister(3, name='a')
    b = QuantumRegister(2, name='b')
    qc = QuantumCircuit(a, b)

    def main():
        ## initialization
        qc.h(a[0])
        qc.h(a[1])
        qc.x(b[0])
        qc.h(b[1])
        qc.barrier()

        ## Increment
        add_int(a, -3)
        qc.barrier()
        qc.x(b[1])
        multi_cz([a[2], b[0], b[1]])
        qc.x(b[1])
        qc.barrier()
        add_int(a, 3)

    ###############################################
    ## Some utility functions

    def add_squared_qint(qdest, rhs, condition_qubits=None):
        if condition_qubits is None:
            condition_qubits = []
        for bit in range(len(rhs)):
            slideMask = list(set(condition_qubits + [rhs[bit]]))
            add_qint(qdest, rhs, slideMask, bit);

    def add_qint(qdest, rhs, condition_qubits=None, shiftRHS=0):
        if condition_qubits is None:
            condition_qubits = []
        for bit in range(len(rhs)):
            add_int(qdest, 1 << bit, list(set([rhs[bit]] + condition_qubits)), shiftRHS)

    def add_int(qdest, rhs, condition_qubits=None, shiftRHS=0):
        if condition_qubits is None:
            condition_qubits = []
        reverse_to_subtract = False
        if rhs == 0:
            return
        elif rhs < 0:
            rhs = -rhs
            reverse_to_subtract = True
        rhs <<= shiftRHS
        ops = []
        add_val = int(rhs)
        condition_mask = (1 << len(qdest)) - 1

        add_val_mask = 1
        while add_val_mask <= add_val:
            cmask = condition_mask & ~(add_val_mask - 1)
            if add_val_mask & add_val:
                add_shift_mask = 1 << (len(qdest) - 1)
                while add_shift_mask >= add_val_mask:
                    cmask &= ~add_shift_mask
                    ops.append((add_shift_mask, cmask))
                    add_shift_mask >>= 1
            condition_mask &= ~add_val_mask
            add_val_mask <<= 1
        if reverse_to_subtract:
            ops.reverse()
        for inst in ops:
            op_qubits = [x for x in condition_qubits]
            mask = 1
            for i in range(len(qdest)):
                if inst[1] & (1 << i):
                    op_qubits.append(qdest[i])
            for i in range(len(qdest)):
                if inst[0] & (1 << i):
                    op_qubits.append(qdest[i])
            multi_cx(op_qubits)

    def multi_cz(qubits):
        ## This will perform a CCCCCZ on as many qubits as we want,
        ## as long as we have enough scratch qubits
        multi_cx(qubits, do_cz=True)

    def multi_cx(qubits, do_cz=False):
        ## This will perform a CCCCCX with as many conditions as we want,
        ## as long as we have enough scratch qubits
        ## The last qubit in the list is the target.
        target = qubits[-1]
        conds = qubits[:-1]
        scratch_index = 0
        ops = []
        while len(conds) > 2:
            new_conds = []
            for i in range(len(conds)//2):
                ops.append((conds[i * 2], conds[i * 2 + 1], scratch[scratch_index]))
                new_conds.append(scratch[scratch_index])
                scratch_index += 1
            if len(conds) & 1:
                new_conds.append(conds[-1])
            conds = new_conds
        for op in ops:
            qc.ccx(op[0], op[1], op[2])
        if do_cz:
            qc.h(target)
        if len(conds) == 0:
            qc.x(target)
        elif len(conds) == 1:
            qc.cx(conds[0], target)
        else:
            qc.ccx(conds[0], conds[1], target)
        if do_cz:
            qc.h(target)
        ops.reverse()
        for op in ops:
            qc.ccx(op[0], op[1], op[2])

    main()

    ## That's the program. Everything below runs and draws it.

    backend = BasicAer.get_backend('statevector_simulator')
    job = execute(qc, backend)
    result = job.result()

    outputstate = result.get_statevector(qc, decimals=3)
    for i,amp in enumerate(outputstate):
        if abs(amp) > 0.000001:
            print('|{}> {}'.format(i, amp))
    qc.draw()        # draw the circuit

# program circuit
## Example 5-5: Quantum conditional phase flip

number_of_qubits = 5
input_space = "zero"

def run(qc):
    import numpy as np
    qc.h( [0, 1] )
    qc.x(3)
    qc.h(4)
    qc.x(1)
    qc.cx(1, 2)
    qc.x(0)
    qc.cx(0, 1)
    qc.mcx( [0, 1], 2)
    qc.x(4)
    qc.mcp( np.pi, [0, 1, 2], 3 )
    qc.mcp( np.pi, [0, 1, 2], 4 )
    qc.x(4)
    qc.mcx( [0, 1], 2 )
    qc.cx(0, 1)
    qc.x(0)
    qc.cx(1, 2)
    qc.x(1)
    qc.measure([0,1,2,3,4], [0,1,2,3,4])
